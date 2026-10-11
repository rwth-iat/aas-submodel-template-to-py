from typing import Any, ForwardRef, Iterable, Optional, Tuple, TypedDict, Union, Unpack
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


def global_ref(value: str) -> aas.ExternalReference:
    """External reference to the global identifier `value`, e.g. a semantic ID"""
    return aas.ExternalReference((aas.Key(aas.KeyTypes.GLOBAL_REFERENCE, value),))


def collect_submodel_elements(*elements: Any, number_repeated: bool = True) -> list[aas.SubmodelElement]:
    """Collect the submodel elements passed to an init in one list: single elements, unless None,
    and the elements of iterables, whose idShorts get an index if `number_repeated` (e.g. Keyword00)"""
    collected = []
    for element in elements:
        if element is None:
            continue
        elif isinstance(element, aas.SubmodelElement):
            collected.append(element)
        elif isinstance(element, Iterable):
            for n, item in enumerate(element):
                if number_repeated:
                    # Number with two digits at least, as the placeholders {00} and __00__ of templates
                    item.id_short = f"{item.id_short}{n:02d}"
                collected.append(item)
        else:
            raise TypeError(f"Expected a submodel element or an iterable of them, got {element.__class__}")
    return collected


class GeneratedSubmodelElementList(aas.SubmodelElementList):
    """SubmodelElementList, whose items may be instances of subclasses of type_value_list_element,
    such as the generated classes of its items"""

    def _check_constraints(self, new, existing) -> None:
        # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
        # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
        saved_id_short = new.id_short
        new.id_short = None

        # We relax constraint AASd-108 here: It is allowed to add subclasses of the specified in type_value_list_element
        if not isinstance(new, self.type_value_list_element):
            raise aas.AASConstraintViolation(
                108,
                "All first level elements must be of the type specified in "
                f"type_value_list_element={self.type_value_list_element.__name__}, "
                f"got {new!r}",
            )

        if (
            self.semantic_id_list_element is not None
            and new.semantic_id is not None
            and new.semantic_id != self.semantic_id_list_element
        ):
            # Constraint AASd-115 specifies that if the semantic_id of an item is not specified
            # but semantic_id_list_element is, the semantic_id of the new is assumed to be identical.
            # Not really a constraint...
            # TODO: maybe set the semantic_id of new to semantic_id_list_element if it is None
            raise aas.AASConstraintViolation(
                107,
                f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                "is specified all first level children must have the same "
                f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
            )

        # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
        # is either Property or Range. Thus, `new` must have the value_type property.
        # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
        if (
            self.type_value_list_element in (aas.Property, aas.Range)
            and new.value_type is not self.value_type_list_element
        ):  # type: ignore
            raise aas.AASConstraintViolation(
                109,
                "All first level elements must have the value_type "  # type: ignore
                "specified by value_type_list_element="
                f"{self.value_type_list_element.__name__}, got "  # type: ignore
                f"{new!r} with value_type={new.value_type.__name__}",
            )  # type: ignore

        # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
        # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
        if new.semantic_id is not None and self.semantic_id_list_element is None:
            for item in existing:
                if item.semantic_id is not None and new.semantic_id != item.semantic_id:
                    raise aas.AASConstraintViolation(
                        114,
                        f"Element to be added {new!r} has semantic_id "
                        f"{new.semantic_id!r}, while already contained element "
                        f"{item!r} has semantic_id {item.semantic_id!r}, which "
                        "aren't equal.",
                    )

        # Re-assign id_short
        new.id_short = saved_id_short


class MultiLanguagePropertyMetadata(TypedDict, total=False):
    """Metadata of aas.MultiLanguageProperty, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_id: Optional[aas.Reference]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class PropertyMetadata(TypedDict, total=False):
    """Metadata of aas.Property, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_type: aas.DataTypeDefXsd
    value_id: Optional[aas.Reference]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class RangeMetadata(TypedDict, total=False):
    """Metadata of aas.Range, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_type: aas.DataTypeDefXsd
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class ReferenceElementMetadata(TypedDict, total=False):
    """Metadata of aas.ReferenceElement, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelElementCollectionMetadata(TypedDict, total=False):
    """Metadata of aas.SubmodelElementCollection, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelElementListMetadata(TypedDict, total=False):
    """Metadata of aas.SubmodelElementList, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    type_value_list_element: type[aas.SubmodelElement]
    semantic_id_list_element: Optional[aas.Reference]
    value_type_list_element: Optional[aas.DataTypeDefXsd]
    order_relevant: bool
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelMetadata(TypedDict, total=False):
    """Metadata of aas.Submodel, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    administration: Optional[aas.AdministrativeInformation]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    kind: aas.ModellingKind
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class EnergyFlexibilityDataModel(aas.Submodel):

    class FlexibleLoadMeasuresPackage(aas.SubmodelElementCollection):

        class Metadata(aas.SubmodelElementCollection):

            class InstanceId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"instanceId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Instance ID"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The ID of a Flexibility Space or Flexible-Load Measure Package for unique identification"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Comment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"comment",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Comment"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Free text to comment the EFDM object."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/comment"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EfdmVersion(aas.SubmodelElementCollection):

                class VersionNumber(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"versionNumber",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Version Number"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"the EFDM version (e.g. 0.3)"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/versionNumber"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SchemaLink(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"schemaLink",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Schema Link"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"hyperlink to the corresponding scheme"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/schemaLink"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"efdmVersion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"EFDM Version"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Specification of the EFDM version and hyperlink to the corresponding scheme."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/efdmVersion"
                        ),
                    }

                def __init__(
                    self,
                    versionNumber: Union[str, VersionNumber],
                    schemaLink: Union[str, SchemaLink],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if versionNumber is not None and not isinstance(versionNumber, aas.SubmodelElement):
                        versionNumber = self.VersionNumber(versionNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if schemaLink is not None and not isinstance(schemaLink, aas.SubmodelElement):
                        schemaLink = self.SchemaLink(schemaLink)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(versionNumber, schemaLink)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Origin(aas.SubmodelElementCollection):

                class OriginId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"originId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the creating service and point in time of creation"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"timestamp of the creating service"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"origin",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the creating service and point in time of creation. By means of the automated filling in of the Element, conclusions about the origin and an allocation to executing agencies are made possible. In the case of communication with external services, this Element is replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/origin"),
                    }

                def __init__(
                    self,
                    originId: Union[str, OriginId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if originId is not None and not isinstance(originId, aas.SubmodelElement):
                        originId = self.OriginId(originId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(originId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Modification(aas.SubmodelElementCollection):

                class ModificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"modificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the service instance that last processed this object "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Its value should be provided by service provider, who creates SMC flexibilitySpace of the EFDM instance"
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"modification",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the service instance that last processed this object and point in time of last processing. In the case of communication with external services, this Element can be replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modification"
                        ),
                    }

                def __init__(
                    self,
                    modificationId: Union[str, ModificationId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if modificationId is not None and not isinstance(modificationId, aas.SubmodelElement):
                        modificationId = self.ModificationId(modificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(modificationId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"metadata",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Metadata"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The metadata provides essential information for tracking and tracing of the model instances."
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/metadata",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(
                self,
                instanceId: Union[str, InstanceId],
                efdmVersion: EfdmVersion,
                origin: Origin,
                modification: Modification,
                comment: Optional[Union[aas.LangStringSet, Comment]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if instanceId is not None and not isinstance(instanceId, aas.SubmodelElement):
                    instanceId = self.InstanceId(instanceId)

                # Build a submodel element if a raw value was passed in the argument

                if comment is not None and not isinstance(comment, aas.SubmodelElement):
                    comment = self.Comment(comment)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    instanceId, comment, efdmVersion, origin, modification
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FlexibleLoadMeasures(GeneratedSubmodelElementList):

            class Flexibleloadmeasures_item(aas.SubmodelElementCollection):

                class FlexibleLoadMeasureId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"flexibleLoadMeasureId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Measure ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of the load measure for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Status(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"status",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Status"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"enum: draft, toExecute, inExecution, executed, partiallyExecuted, failed, canceled. The status of a Flexible-Load Measure indicates its current progress within the process of providing energy flexiblity. The goal is to enable clear tracking of each measure across defined phases."
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/status",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class FlexibleLoadId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"flexibleLoadId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of the Flexible Load to which the Flexible-Load Measure is directed."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Reward(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"reward",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reward"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Total revenue received by a company for executing the Flexible-Load Measure."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/reward"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LoadChangeProfiles(GeneratedSubmodelElementList):

                    class Loadchangeprofiles_item(aas.SubmodelElementCollection):

                        class Power(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"power",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Positive power states mean that the Flexible-Load Measure requests an increase in power consumption from the Flexible Load. Negative power states require a decrease in power consumption. Interpolation between Power States is linear; a step change in power can be mapped by specifying two equal timestamps with different power values."
                                        }
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-AAZ820#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Timestamp(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"timestamp",
                                    "value_type": xsd.DateTime,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"timestamp of a power state"}
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Load Change Profile"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Load profile that represents the power reduction or increase of the Flexible Load. "
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerState"
                                ),
                            }

                        def __init__(
                            self,
                            power: Union[xsd.Float, Power],
                            timestamp: Union[xsd.DateTime, Timestamp],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if power is not None and not isinstance(power, aas.SubmodelElement):
                                power = self.Power(power)

                            # Build a submodel element if a raw value was passed in the argument

                            if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                                timestamp = self.Timestamp(timestamp)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(power, timestamp)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"loadChangeProfiles",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Load Change Profiles"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"loadChangeProfiles may contain multiple loadChangeProfile. "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/loadChangeProfiles"
                            ),
                        }

                    def __init__(
                        self,
                        loadchangeprofiles_items: Iterable[Loadchangeprofiles_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(loadchangeprofiles_items, str):
                            raise TypeError("loadchangeprofiles_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            loadchangeprofiles_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Measure"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Each flexibleLoadMeasure describes a specific load change profile of a dedicated Flexible Load within an Flexibility Space. In addition, the revenue resulting from the execution of the flexibleLoadMeasure is specified in this class."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoad"
                        ),
                    }

                def __init__(
                    self,
                    flexibleLoadMeasureId: Union[str, FlexibleLoadMeasureId],
                    status: Union[str, Status],
                    flexibleLoadId: Union[str, FlexibleLoadId],
                    loadChangeProfiles: Union[Iterable[LoadChangeProfiles.Loadchangeprofiles_item], LoadChangeProfiles],
                    reward: Optional[Union[str, Reward]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if flexibleLoadMeasureId is not None and not isinstance(flexibleLoadMeasureId, aas.SubmodelElement):
                        flexibleLoadMeasureId = self.FlexibleLoadMeasureId(flexibleLoadMeasureId)

                    # Build a submodel element if a raw value was passed in the argument

                    if status is not None and not isinstance(status, aas.SubmodelElement):
                        status = self.Status(status)

                    # Build a submodel element if a raw value was passed in the argument

                    if flexibleLoadId is not None and not isinstance(flexibleLoadId, aas.SubmodelElement):
                        flexibleLoadId = self.FlexibleLoadId(flexibleLoadId)

                    # Build a submodel element if a raw value was passed in the argument

                    if reward is not None and not isinstance(reward, aas.SubmodelElement):
                        reward = self.Reward(reward)

                    # A str would be split into its characters
                    if isinstance(loadChangeProfiles, str):
                        raise TypeError("loadChangeProfiles takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if loadChangeProfiles is not None and not isinstance(loadChangeProfiles, aas.SubmodelElement):
                        loadChangeProfiles = self.LoadChangeProfiles(loadChangeProfiles)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        flexibleLoadMeasureId, status, flexibleLoadId, reward, loadChangeProfiles
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"flexibleLoadMeasures",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Measures"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"flexibleLoadMeasuresmay contain multiple flexibleLoadMeasure. "}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoadMeasures"
                    ),
                }

            def __init__(
                self,
                flexibleloadmeasures_items: Iterable[Flexibleloadmeasures_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(flexibleloadmeasures_items, str):
                    raise TypeError("flexibleloadmeasures_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    flexibleloadmeasures_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"flexibleLoadMeasuresPackage",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Measures Package"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The flexibleLoadMeasuresPackage contains one or more Flexible-Load Measures that describe a specific change in the performance of a dedicated Flexible Load"
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoadMeasuresPackage"
                ),
            }

        def __init__(
            self,
            metadata: Metadata,
            flexibleLoadMeasures: Union[Iterable[FlexibleLoadMeasures.Flexibleloadmeasures_item], FlexibleLoadMeasures],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(flexibleLoadMeasures, str):
                raise TypeError("flexibleLoadMeasures takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if flexibleLoadMeasures is not None and not isinstance(flexibleLoadMeasures, aas.SubmodelElement):
                flexibleLoadMeasures = self.FlexibleLoadMeasures(flexibleLoadMeasures)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(metadata, flexibleLoadMeasures)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FlexibilitySpace_operationalPotential(aas.SubmodelElementCollection):

        class Metadata(aas.SubmodelElementCollection):

            class InstanceId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"instanceId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Instance ID"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The ID of a Flexibility Space or Flexible-Load Measure Package for unique identification"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Comment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"comment",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Comment"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Free text to comment the EFDM object."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/comment"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EfdmVersion(aas.SubmodelElementCollection):

                class VersionNumber(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"versionNumber",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Version Number"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"the EFDM version (e.g. 0.3)"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/versionNumber"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SchemaLink(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"schemaLink",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Schema Link"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"hyperlink to the corresponding scheme"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/schemaLink"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"efdmVersion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"EFDM Version"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Specification of the EFDM version and hyperlink to the corresponding scheme."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/efdmVersion"
                        ),
                    }

                def __init__(
                    self,
                    versionNumber: Union[str, VersionNumber],
                    schemaLink: Union[str, SchemaLink],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if versionNumber is not None and not isinstance(versionNumber, aas.SubmodelElement):
                        versionNumber = self.VersionNumber(versionNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if schemaLink is not None and not isinstance(schemaLink, aas.SubmodelElement):
                        schemaLink = self.SchemaLink(schemaLink)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(versionNumber, schemaLink)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Origin(aas.SubmodelElementCollection):

                class OriginId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"originId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the creating service and point in time of creation"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"timestamp of the creating service"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"origin",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the creating service and point in time of creation. By means of the automated filling in of the Element, conclusions about the origin and an allocation to executing agencies are made possible. In the case of communication with external services, this Element is replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/origin"),
                    }

                def __init__(
                    self,
                    originId: Union[str, OriginId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if originId is not None and not isinstance(originId, aas.SubmodelElement):
                        originId = self.OriginId(originId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(originId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Modification(aas.SubmodelElementCollection):

                class ModificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"modificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the service instance that last processed this object "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"timestamp of of last processing"}),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"modification",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the service instance that last processed this object and point in time of last processing. In the case of communication with external services, this Element can be replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modification"
                        ),
                    }

                def __init__(
                    self,
                    modificationId: Union[str, ModificationId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if modificationId is not None and not isinstance(modificationId, aas.SubmodelElement):
                        modificationId = self.ModificationId(modificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(modificationId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"metadata",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Metadata"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The metadata provides essential information for tracking and tracing of the model instances."
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/metadata",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(
                self,
                instanceId: Union[str, InstanceId],
                efdmVersion: EfdmVersion,
                origin: Origin,
                modification: Modification,
                comment: Optional[Union[aas.LangStringSet, Comment]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if instanceId is not None and not isinstance(instanceId, aas.SubmodelElement):
                    instanceId = self.InstanceId(instanceId)

                # Build a submodel element if a raw value was passed in the argument

                if comment is not None and not isinstance(comment, aas.SubmodelElement):
                    comment = self.Comment(comment)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    instanceId, comment, efdmVersion, origin, modification
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class UtilizationContext(aas.SubmodelElementCollection):

            class Status(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"status",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Status"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"enum: draft, available, offered, reserved, measuresRequest, finalized. The status of a Flexibility Space describes its current condition within the overall process of applying energy-flexible measures. The objctive is to make the progession and individual phases of each Flexibility Space transparently traceable."
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/status",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ModellingScope(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"modellingScope",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modelling Scope"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"enum: generalTechnicalPotential, operationalPotential, applicationTailoredPotential. The modelling scope places individual EFDM instances and their key figures into context. generalTechnicalPotential: The modelling of flexibility includes universally valid technical characteristics and restrictions; the model does not contain operational strategies, production plans, or other plant-specific limitations. The energy flexibility potential is not directly implementable. operationalPotential: Flexibility is fully considered within the production environment; the model describes the maximum feasible potential, independent of the specific use case. applicationTailoredPotential: The model describes a potential tailored to a specific application (e.g. energy market may allow only Flexible Load with 15-min holding durations); storage and dependencies may need to be transformed to be represented as Flexible Load."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modellingScope"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Trading(aas.SubmodelElementCollection):

                class ExternallyTradeable(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"externallyTradeable",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Externally Tradeable"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r" Indicates whether the Flexibility Space is intended to participate in external energy markets (true) or is to be used exclusively for internal optimization purposes (false)."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/externallyTradeable"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AutoTradeable(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"autoTradeable",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Auto Tradeable"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r" Specifies whether the trading process can be executed automatically (true) or if additional manual preparations or reviews and verification procedures are required (false)."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/autoTradeable"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"trading",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Trading"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The Trading of a Flexibility Space comprises configurable properties that determine its feasibility and operational implementation"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/trading"
                        ),
                    }

                def __init__(
                    self,
                    externallyTradeable: Union[str, ExternallyTradeable],
                    autoTradeable: Union[str, AutoTradeable],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if externallyTradeable is not None and not isinstance(externallyTradeable, aas.SubmodelElement):
                        externallyTradeable = self.ExternallyTradeable(externallyTradeable)

                    # Build a submodel element if a raw value was passed in the argument

                    if autoTradeable is not None and not isinstance(autoTradeable, aas.SubmodelElement):
                        autoTradeable = self.AutoTradeable(autoTradeable)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(externallyTradeable, autoTradeable)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"utilizationContext",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Utilization Context"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Containing metainformation, describing the model status and scope"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/utilizationContext"
                    ),
                }

            def __init__(
                self,
                status: Union[str, Status],
                modellingScope: Union[str, ModellingScope],
                trading: Trading,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if status is not None and not isinstance(status, aas.SubmodelElement):
                    status = self.Status(status)

                # Build a submodel element if a raw value was passed in the argument

                if modellingScope is not None and not isinstance(modellingScope, aas.SubmodelElement):
                    modellingScope = self.ModellingScope(modellingScope)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(status, modellingScope, trading)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FlexibleLoads(GeneratedSubmodelElementList):

            class Flexibleloads_item(aas.SubmodelElementCollection):

                class FlexibleLoadId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"flexibleLoadId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of a Flexible Load for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services. String Format: UUID"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReactionDuration(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"reactionDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reaction Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Time (seconds) required by a technical system between the receipt of a call-up and the initiation of a Flexible-Load Measure within the enterprise. The call must be issued with at least this lead time before the Flexible-Load Measure starts."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAV535#002"),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class Validity(aas.SubmodelElementCollection):

                    class From(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"from",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"From"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"from time. If this period is not specified, continuous availability of the Flexible Load  is assumed. "
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABF198#001"),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Until(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"until",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Until"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"until time. If this period is not specified, continuous availability of the Flexible Load  is assumed. "
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABF198#001"),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TemporalType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"temporalType",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Temporal Type"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"enum: start, total, end. The temporalType start specifies that the start of each Flexible-Load Measure belonging to this Flexible Load must lie within the Validity Period. end specifies that the end of each Flexible-Load Measure belonging to this Flexible Load must lie within the Validity Period. total specifies that the total duration of each Flexible-Load Measure belonging to this Flexible Load must lie within the Validity Period."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/temporalType"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"validity",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Validity"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Subset of the company-internal planning horizon in which the Flexible Load is available. The beginning and end of this validity period are specified with the attributes from and until. If this period is not specified, continuous availability of the Flexible Load is assumed. "
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/validity"
                            ),
                        }

                    def __init__(
                        self,
                        from_: Optional[Union[xsd.DateTime, From]] = None,
                        until: Optional[Union[xsd.DateTime, Until]] = None,
                        temporalType: Optional[Union[str, TemporalType]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if from_ is not None and not isinstance(from_, aas.SubmodelElement):
                            from_ = self.From(from_)

                        # Build a submodel element if a raw value was passed in the argument

                        if until is not None and not isinstance(until, aas.SubmodelElement):
                            until = self.Until(until)

                        # Build a submodel element if a raw value was passed in the argument

                        if temporalType is not None and not isinstance(temporalType, aas.SubmodelElement):
                            temporalType = self.TemporalType(temporalType)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(from_, until, temporalType)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class PowerStates(GeneratedSubmodelElementList):

                    class Powerstates_item(aas.SubmodelElementCollection):

                        class Power(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"power",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"A positive sign means that the Flexible Load can increase its power consumption. Negative Power States represent a possible decrease in power consumption. Uncertainty can be represented by specifying a range."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAZ820#001"),
                                }

                            def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class Duration(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"duration",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Duration"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"The time period during which the Flexible Load can run in its corresponding Power States. Uncertainty can be represented by specifying a range."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAQ203#001"),
                                }

                            def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class ReferencePoint(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"referencePoint",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reference Point"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"the scheduled baseline load"}
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAZ820#001"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class DurationType(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"durationType",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Duration Type"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"enum: deliveryDuration, holdingDuration. Duration either corresponds to the time of a constant Power State (holdingDuration) OR a constant Power State WITH initial power modulation (deliveryDuration)."
                                        }
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/durationType",
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power State"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"A power state with which the Flexible Load can run during the corresponding holding periods. "
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerState",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(
                            self,
                            power: Union[Tuple[xsd.Float, xsd.Float], Power],
                            duration: Optional[Union[Tuple[xsd.Float, xsd.Float], Duration]] = None,
                            referencePoint: Optional[Union[xsd.Float, ReferencePoint]] = None,
                            durationType: Optional[Union[str, DurationType]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if power is not None and not isinstance(power, aas.SubmodelElement):
                                power = self.Power(min=power[0], max=power[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if duration is not None and not isinstance(duration, aas.SubmodelElement):
                                duration = self.Duration(min=duration[0], max=duration[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if referencePoint is not None and not isinstance(referencePoint, aas.SubmodelElement):
                                referencePoint = self.ReferencePoint(referencePoint)

                            # Build a submodel element if a raw value was passed in the argument

                            if durationType is not None and not isinstance(durationType, aas.SubmodelElement):
                                durationType = self.DurationType(durationType)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                power, duration, referencePoint, durationType
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"powerStates",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power States"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"a set of Power States with which the Flexible Load can run during each of the (number of changes + 1) holding periods. "
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerStates",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(
                        self,
                        powerstates_items: Iterable[Powerstates_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(powerstates_items, str):
                            raise TypeError("powerstates_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(powerstates_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class UsageNumber(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"usageNumber",
                            "value_type": xsd.PositiveInteger,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Usage Number"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The permitted number of activations of the Flexible Load within the Validity Period. A specified minimum value of the range defines a required number of activations; a specified maximum value sets an upper limit on activation frequency."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/usageNumber"
                            ),
                        }

                    def __init__(
                        self, min: xsd.PositiveInteger, max: xsd.PositiveInteger, **kwargs: Unpack[RangeMetadata]
                    ):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class ModulationNumber(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"modulationNumber",
                            "value_type": xsd.NonNegativeInteger,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modulation Number"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The maximum number of Power State changes (modulations) allowed within one use of a Flexible Load. The two modulations corresponding to the initial activation and the final deactivation are not counted."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modulationNumber"
                            ),
                        }

                    def __init__(
                        self, min: xsd.NonNegativeInteger, max: xsd.NonNegativeInteger, **kwargs: Unpack[RangeMetadata]
                    ):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class PowerGradients(aas.SubmodelElementCollection):

                    class ActivationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"activationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Activation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Actication Gradient specifies the power gradient applicable during the initial activation of the Flexibl Load."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class ModulationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"modulationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modulation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Modulation Gradient specifies the power gradient during transitions between Power States."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class DeactivationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"deactivationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Deactivation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Deactivation Gradient specifies the power gradient during the final deactivation phase"
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"powerGradients",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power Gradients"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The absolute value of the power gradient of a Flexible Load indicates how fast the power can be increased or decreased."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerGradients"
                            ),
                        }

                    def __init__(
                        self,
                        activationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], ActivationGradient]] = None,
                        modulationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], ModulationGradient]] = None,
                        deactivationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], DeactivationGradient]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if activationGradient is not None and not isinstance(activationGradient, aas.SubmodelElement):
                            activationGradient = self.ActivationGradient(
                                min=activationGradient[0], max=activationGradient[1]
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if modulationGradient is not None and not isinstance(modulationGradient, aas.SubmodelElement):
                            modulationGradient = self.ModulationGradient(
                                min=modulationGradient[0], max=modulationGradient[1]
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if deactivationGradient is not None and not isinstance(
                            deactivationGradient, aas.SubmodelElement
                        ):
                            deactivationGradient = self.DeactivationGradient(
                                min=deactivationGradient[0], max=deactivationGradient[1]
                            )

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            activationGradient, modulationGradient, deactivationGradient
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class RegenerationDuration(aas.Property):

                    ALLOWED_RANGE = (xsd.from_xsd(r"0.0", xsd.Float), None)

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"regenerationDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Regeneration Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The required regeneration time during which no other measure of the same Flexible Load may be activated following the deactivation of a previous measure. This time constraint applies only if an actual deactivation occurs. If another measure follows without interruption, no deactivation takes place between them; this does not constitute a violation of the defined regerneration period."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAV535#002"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and (
                            value < self.ALLOWED_RANGE[0]
                            or self.ALLOWED_RANGE[1] is not None
                            and value > self.ALLOWED_RANGE[1]
                        ):
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class FlexibleLoadCosts(aas.SubmodelElementCollection):

                    class VariableCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"variableCost",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Variable costs refer to the total amount of energy converted. "}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerEnergyConverted"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CostPerUsage(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"costPerUsage",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Cost Per Usage"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Usage costs are incurred per use of a Flexible-Load."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerUsage"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FixedCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"fixedCost",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fixed Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Fixed costs incurred during the Validity Period regardless of the call of a Flexible Load (example: standby costs of a power generation plant)."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/fixedCost"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"flexibleLoadCosts",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Costs"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The costs associated with the use of the Flexible Load, excluding electricity costs. The Costs of a Flexible Load consist of variable cost, usage cost and fixed cost."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoadCosts"
                            ),
                        }

                    def __init__(
                        self,
                        variableCost: Optional[Union[xsd.Float, VariableCost]] = None,
                        costPerUsage: Optional[Union[xsd.Float, CostPerUsage]] = None,
                        fixedCost: Optional[Union[xsd.Float, FixedCost]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if variableCost is not None and not isinstance(variableCost, aas.SubmodelElement):
                            variableCost = self.VariableCost(variableCost)

                        # Build a submodel element if a raw value was passed in the argument

                        if costPerUsage is not None and not isinstance(costPerUsage, aas.SubmodelElement):
                            costPerUsage = self.CostPerUsage(costPerUsage)

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedCost is not None and not isinstance(fixedCost, aas.SubmodelElement):
                            fixedCost = self.FixedCost(fixedCost)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(variableCost, costPerUsage, fixedCost)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class OrderConfirmationDeadline(aas.SubmodelElementCollection):

                    class OrderConfirmationDeadlineAbsolute(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"orderConfirmationDeadlineAbsolute",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Order Confirmation Deadline Absolute"}
                                ),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"absolute deadline"}),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class OrderConfirmationDeadlineRelative(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"orderConfirmationDeadlineRelative",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Order Confirmation Deadline Relative"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"relative to the start time of the Flexible-Load Measure (e.g. 100 seconds before the start of a FLM)"
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-AAQ203#001"),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"orderConfirmationDeadline",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Order Confirmation Deadline"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Latest possible time by which confirmation of an accepted offer of the Flexible Load must have been received. By this time, the flexibility provider needs to know whether the Flexible Load must be held ready. After the Booking Confirmation Deadline is exceeded, the Flexible Load offer is removed from the market. The Order Confirmation Deadline can be specified EITHER absolutely with a fixed time OR relative to the start time of the Flexible-Load Measure (e.g. 100 seconds before the start of a FLM). If no value is specified, constant availability for offering is assumed until the latest possible start time within the Validity Period minus the Reaction Duration."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/orderConfirmationDeadline"
                            ),
                        }

                    def __init__(
                        self,
                        orderConfirmationDeadlineAbsolute: Optional[
                            Union[xsd.DateTime, OrderConfirmationDeadlineAbsolute]
                        ] = None,
                        orderConfirmationDeadlineRelative: Optional[
                            Union[str, OrderConfirmationDeadlineRelative]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if orderConfirmationDeadlineAbsolute is not None and not isinstance(
                            orderConfirmationDeadlineAbsolute, aas.SubmodelElement
                        ):
                            orderConfirmationDeadlineAbsolute = self.OrderConfirmationDeadlineAbsolute(
                                orderConfirmationDeadlineAbsolute
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if orderConfirmationDeadlineRelative is not None and not isinstance(
                            orderConfirmationDeadlineRelative, aas.SubmodelElement
                        ):
                            orderConfirmationDeadlineRelative = self.OrderConfirmationDeadlineRelative(
                                orderConfirmationDeadlineRelative
                            )

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            orderConfirmationDeadlineAbsolute, orderConfirmationDeadlineRelative
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Prices(aas.SubmodelElementCollection):

                    class VariablePrice(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"variablePrice",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Price"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Variable price refer to the total amount of energy converted. "}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PricePerEnergyConverted"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class PricePerUsage(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"pricePerUsage",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Price Per Usage"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Usage price are incurred per use of a Flexible-Load."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PricePerUsage"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FixedPrice(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"fixedPrice",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fixed Price"}),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Fixed price"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/fixedPrice"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"prices",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Prices"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Prices to be realized on the market as a minimum for offering the Flexible Load. The Prices of a Flexible Load are composed of a variable price, a usage price and a fixed price analogous to the Costs. Prices are only needed if the Flexible Load is to be actively offered on the market."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/prices"
                            ),
                        }

                    def __init__(
                        self,
                        variablePrice: Optional[Union[str, VariablePrice]] = None,
                        pricePerUsage: Optional[Union[str, PricePerUsage]] = None,
                        fixedPrice: Optional[Union[str, FixedPrice]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if variablePrice is not None and not isinstance(variablePrice, aas.SubmodelElement):
                            variablePrice = self.VariablePrice(variablePrice)

                        # Build a submodel element if a raw value was passed in the argument

                        if pricePerUsage is not None and not isinstance(pricePerUsage, aas.SubmodelElement):
                            pricePerUsage = self.PricePerUsage(pricePerUsage)

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedPrice is not None and not isinstance(fixedPrice, aas.SubmodelElement):
                            fixedPrice = self.FixedPrice(fixedPrice)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(variablePrice, pricePerUsage, fixedPrice)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Location(aas.SubmodelElementCollection):

                    class MeterLocation(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"meterLocation",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Meter Location"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The unambiguous allocation is made by means of the meter point designation known in the energy industry / in market communication. In Germany, it corresponds to a 33-digit alphanumeric code number."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/MeterPointDesignation"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VoltageLevel(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"voltageLevel",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Voltage Level"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The specification of the Grid Voltage Level to which the Flexible Load is connected. The voltage level at the grid connection point is to be used, independent of deviating voltage levels in any company grid."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/GridVoltageLevel"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"location",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Location"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Meter point designation for the geographical and power grid topological location of a Flexible Load. "
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/location"
                            ),
                        }

                    def __init__(
                        self,
                        meterLocation: Optional[Union[str, MeterLocation]] = None,
                        voltageLevel: Optional[Union[str, VoltageLevel]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if meterLocation is not None and not isinstance(meterLocation, aas.SubmodelElement):
                            meterLocation = self.MeterLocation(meterLocation)

                        # Build a submodel element if a raw value was passed in the argument

                        if voltageLevel is not None and not isinstance(voltageLevel, aas.SubmodelElement):
                            voltageLevel = self.VoltageLevel(voltageLevel)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(meterLocation, voltageLevel)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r" Each flexibleLoad describes the energy flexibility of a technical system (i.e. controllable unit) or a combination of systems (i.e. an ensemble of controllable units) that can adjust its power consumption or generation in response to external conditions or requirements. It focuses on the limitations and possibilities (degrees of freedom) of changing power outputs of a technical system."
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoad",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    flexibleLoadId: Union[str, FlexibleLoadId],
                    powerStates: Union[Iterable[PowerStates.Powerstates_item], PowerStates],
                    reactionDuration: Optional[Union[Tuple[xsd.Float, xsd.Float], ReactionDuration]] = None,
                    validity: Optional[Validity] = None,
                    usageNumber: Optional[Union[Tuple[xsd.PositiveInteger, xsd.PositiveInteger], UsageNumber]] = None,
                    modulationNumber: Optional[
                        Union[Tuple[xsd.NonNegativeInteger, xsd.NonNegativeInteger], ModulationNumber]
                    ] = None,
                    powerGradients: Optional[PowerGradients] = None,
                    regenerationDuration: Optional[Union[xsd.Float, RegenerationDuration]] = None,
                    flexibleLoadCosts: Optional[FlexibleLoadCosts] = None,
                    orderConfirmationDeadline: Optional[OrderConfirmationDeadline] = None,
                    prices: Optional[Prices] = None,
                    location: Optional[Location] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if flexibleLoadId is not None and not isinstance(flexibleLoadId, aas.SubmodelElement):
                        flexibleLoadId = self.FlexibleLoadId(flexibleLoadId)

                    # Build a submodel element if a raw value was passed in the argument

                    if reactionDuration is not None and not isinstance(reactionDuration, aas.SubmodelElement):
                        reactionDuration = self.ReactionDuration(min=reactionDuration[0], max=reactionDuration[1])

                    # A str would be split into its characters
                    if isinstance(powerStates, str):
                        raise TypeError("powerStates takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if powerStates is not None and not isinstance(powerStates, aas.SubmodelElement):
                        powerStates = self.PowerStates(powerStates)

                    # Build a submodel element if a raw value was passed in the argument

                    if usageNumber is not None and not isinstance(usageNumber, aas.SubmodelElement):
                        usageNumber = self.UsageNumber(min=usageNumber[0], max=usageNumber[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if modulationNumber is not None and not isinstance(modulationNumber, aas.SubmodelElement):
                        modulationNumber = self.ModulationNumber(min=modulationNumber[0], max=modulationNumber[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if regenerationDuration is not None and not isinstance(regenerationDuration, aas.SubmodelElement):
                        regenerationDuration = self.RegenerationDuration(regenerationDuration)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        flexibleLoadId,
                        reactionDuration,
                        validity,
                        powerStates,
                        usageNumber,
                        modulationNumber,
                        powerGradients,
                        regenerationDuration,
                        flexibleLoadCosts,
                        orderConfirmationDeadline,
                        prices,
                        location,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"flexibleLoads",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Loads"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"flexibleLoads may contain multiple flexibleLoad."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoads"
                    ),
                }

            def __init__(
                self, flexibleloads_items: Iterable[Flexibleloads_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(flexibleloads_items, str):
                    raise TypeError("flexibleloads_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(flexibleloads_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Storages(GeneratedSubmodelElementList):

            class Storages_item(aas.SubmodelElementCollection):

                class StorageId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"storageId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of a storage for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StorageCosts(aas.SubmodelElementCollection):

                    class VariableCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"variableCost",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Variable costs refer to the total amount of energy converted."}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerEnergyConverted",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CostPerUsage(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"costPerUsage",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Cost Per Usage"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Usage costs arise per use of a storage tank."}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerUsage",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FixedCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"fixedCost",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fixed Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Fixed costs arise from keeping a storage facility on standby."}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/fixedCost",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"storageCosts",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage Costs"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The costs associated with the use of the energy storage. The Costs of a storage facility consist of variable cost, usage cost and fixed cost. Variable costs refer to the total amount of energy converted. Usage costs arise per use of a storage tank. Fixed costs arise from keeping a storage facility on standby."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storageCosts"
                            ),
                        }

                    def __init__(
                        self,
                        variableCost: Optional[Union[str, VariableCost]] = None,
                        costPerUsage: Optional[Union[str, CostPerUsage]] = None,
                        fixedCost: Optional[Union[str, FixedCost]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if variableCost is not None and not isinstance(variableCost, aas.SubmodelElement):
                            variableCost = self.VariableCost(variableCost)

                        # Build a submodel element if a raw value was passed in the argument

                        if costPerUsage is not None and not isinstance(costPerUsage, aas.SubmodelElement):
                            costPerUsage = self.CostPerUsage(costPerUsage)

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedCost is not None and not isinstance(fixedCost, aas.SubmodelElement):
                            fixedCost = self.FixedCost(fixedCost)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(variableCost, costPerUsage, fixedCost)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class UsableCapacity(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"usableCapacity",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Usable Capacity"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Lower and upper limit of the storage energy content. These limits must never be exceeded or fallen short of. Depending on the choice of reference point, it is also possible to specify negative storage capacities, e.g. if it needs to be possible to either exceed or fall below storage limits."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class InitialEnergyContent(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"initialEnergyContent",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Initial Energy Content"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Energy content of the storage at the start time of the Validity Period of the associated Flexible Load (Suppliers). If the storage is connected to several Flexible Loads, the Initial Energy Content refers to the earliest start time of the Validity Periods of all Flexible Loads. If the initial energy content cannot be quantified exactly, the predicted range can be specified via min and max."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class TargetEnergyContent(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"targetEnergyContent",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Target Energy Content"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Energy content that the storage must have at the end time of the Validity Period of the associated Flexible Loads (Suppliers). If the storage is connected to several Flexible Loads, the Target Energy Content refers to the latest end time of the Validity Periods of all Flexible Loads. If the target energy content is flexible, the desired target range is specified can be specified via min and max."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class EnergyLoss(aas.Property):

                    ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.UnsignedShort), xsd.from_xsd(r"100", xsd.UnsignedShort))

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"energyLoss",
                            "value_type": xsd.UnsignedShort,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Energy Loss"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Proportion of the energy content that is continuously lost, e.g. through exchange with the environment. The percentage refers to the actual energy content and not to the storage capacity."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/EnergyContentLossPerHour"
                            ),
                        }

                    def __init__(self, value: xsd.UnsignedShort, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and (
                            value < self.ALLOWED_RANGE[0]
                            or self.ALLOWED_RANGE[1] is not None
                            and value > self.ALLOWED_RANGE[1]
                        ):
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Suppliers(GeneratedSubmodelElementList):

                    class Suppliers_item(aas.SubmodelElementCollection):

                        class FlexibleLoadId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"flexibleLoadId",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load ID"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"This ID identifies the Flexible Load supplying the storage. The ID of a Flexible Load for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ConversionEfficiency(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"conversionEfficiency",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Conversion Efficiency"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Energy conversion efficiency of the suppiler"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/EnergyConversionEfficiency"
                                    ),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Supplier"}),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Indicating a single supply"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/supplier"
                                ),
                            }

                        def __init__(
                            self,
                            flexibleLoadId: Union[str, FlexibleLoadId],
                            conversionEfficiency: Optional[Union[xsd.Float, ConversionEfficiency]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if flexibleLoadId is not None and not isinstance(flexibleLoadId, aas.SubmodelElement):
                                flexibleLoadId = self.FlexibleLoadId(flexibleLoadId)

                            # Build a submodel element if a raw value was passed in the argument

                            if conversionEfficiency is not None and not isinstance(
                                conversionEfficiency, aas.SubmodelElement
                            ):
                                conversionEfficiency = self.ConversionEfficiency(conversionEfficiency)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(flexibleLoadId, conversionEfficiency)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"suppliers",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Suppliers"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"One or more Flexible Loads supplying the storage. The Flexible Loads must be defined in the same Flexibility Space. The conversion efficiency is specified for each supply system."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/suppliers"
                            ),
                        }

                    def __init__(
                        self, suppliers_items: Iterable[Suppliers_item], **kwargs: Unpack[SubmodelElementListMetadata]
                    ):

                        # A str would be split into its characters
                        if isinstance(suppliers_items, str):
                            raise TypeError("suppliers_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(suppliers_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Drains(GeneratedSubmodelElementList):

                    class Drains_item(aas.SubmodelElementCollection):

                        class Power(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"power",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power"}),
                                    "description": aas.MultiLanguageTextType(dict_={r"en": r"power drained"}),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-AAZ820#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Timestamp(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"timestamp",
                                    "value_type": xsd.DateTime,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"timestamp of power drain"}
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Drain"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Indicating a single non-influenceable energy demand"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/drain"
                                ),
                            }

                        def __init__(
                            self,
                            power: Optional[Union[str, Power]] = None,
                            timestamp: Optional[Union[xsd.DateTime, Timestamp]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if power is not None and not isinstance(power, aas.SubmodelElement):
                                power = self.Power(power)

                            # Build a submodel element if a raw value was passed in the argument

                            if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                                timestamp = self.Timestamp(timestamp)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(power, timestamp)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"drains",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Drains"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Non-influenceable energy demands in the form of a load profile that must be met. The interpolation between the Power States is linear."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/drains"
                            ),
                        }

                    def __init__(
                        self, drains_items: Iterable[Drains_item], **kwargs: Unpack[SubmodelElementListMetadata]
                    ):

                        # A str would be split into its characters
                        if isinstance(drains_items, str):
                            raise TypeError("drains_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(drains_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A storage represents a technical system or a combination of systems that has the potential to store energy"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storage",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    storageId: Union[str, StorageId],
                    usableCapacity: Union[Tuple[xsd.Float, xsd.Float], UsableCapacity],
                    initialEnergyContent: Union[Tuple[xsd.Float, xsd.Float], InitialEnergyContent],
                    storageCosts: Optional[StorageCosts] = None,
                    targetEnergyContent: Optional[Union[Tuple[xsd.Float, xsd.Float], TargetEnergyContent]] = None,
                    energyLoss: Optional[Union[xsd.UnsignedShort, EnergyLoss]] = None,
                    suppliers: Optional[Union[Iterable[Suppliers.Suppliers_item], Suppliers]] = None,
                    drains: Optional[Union[Iterable[Drains.Drains_item], Drains]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if storageId is not None and not isinstance(storageId, aas.SubmodelElement):
                        storageId = self.StorageId(storageId)

                    # Build a submodel element if a raw value was passed in the argument

                    if usableCapacity is not None and not isinstance(usableCapacity, aas.SubmodelElement):
                        usableCapacity = self.UsableCapacity(min=usableCapacity[0], max=usableCapacity[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if initialEnergyContent is not None and not isinstance(initialEnergyContent, aas.SubmodelElement):
                        initialEnergyContent = self.InitialEnergyContent(
                            min=initialEnergyContent[0], max=initialEnergyContent[1]
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if targetEnergyContent is not None and not isinstance(targetEnergyContent, aas.SubmodelElement):
                        targetEnergyContent = self.TargetEnergyContent(
                            min=targetEnergyContent[0], max=targetEnergyContent[1]
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if energyLoss is not None and not isinstance(energyLoss, aas.SubmodelElement):
                        energyLoss = self.EnergyLoss(energyLoss)

                    # A str would be split into its characters
                    if isinstance(suppliers, str):
                        raise TypeError("suppliers takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if suppliers is not None and not isinstance(suppliers, aas.SubmodelElement):
                        suppliers = self.Suppliers(suppliers)

                    # A str would be split into its characters
                    if isinstance(drains, str):
                        raise TypeError("drains takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if drains is not None and not isinstance(drains, aas.SubmodelElement):
                        drains = self.Drains(drains)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        storageId,
                        storageCosts,
                        usableCapacity,
                        initialEnergyContent,
                        targetEnergyContent,
                        energyLoss,
                        suppliers,
                        drains,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"storages",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storages"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Storages may contain multiple storages, each of which represents a technical system or a combination of systems that has the potential to store energy"
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storages",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(self, storages_items: Iterable[Storages_item], **kwargs: Unpack[SubmodelElementListMetadata]):

                # A str would be split into its characters
                if isinstance(storages_items, str):
                    raise TypeError("storages_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(storages_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Dependencies(GeneratedSubmodelElementList):

            class Dependencies_item(aas.SubmodelElementCollection):

                class DependencyId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"dependencyId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependency ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The ID of a dependency for unique identification. "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ApplicabilityDuration(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"applicabilityDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Applicability Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The time period following the activation of theTriggering Flexible-Load during which the Target Flexible-Load must be activated at least once (Logical Type: implies) or must not be activated at all (Logical Type: excludes). The values specified for min and max define the Applicability duration relative to: "
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAQ203#001"),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class ApplicabilityConditions(GeneratedSubmodelElementList):

                    class Applicabilityconditions_item(aas.SubmodelElementCollection):

                        class Comparator(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"comparator",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Comparator"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"enum: equals, less, lessEqual, greater, greaterEqual."}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/comparator"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FormulaRight(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"formulaRight",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Formula Right"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"The Target Flexible-Load metrics are incorporated on the right side."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/formulaRight"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FormulaLeft(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"formulaLeft",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Formula Left"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"The Triggering Flexible-Load metrics are incorporated on the left side of the formula."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/formulaLeft"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Applicability Condition"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Indicating a single condition"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/applicabilityCondition"
                                ),
                            }

                        def __init__(
                            self,
                            comparator: Optional[Union[str, Comparator]] = None,
                            formulaRight: Optional[Union[str, FormulaRight]] = None,
                            formulaLeft: Optional[Union[str, FormulaLeft]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if comparator is not None and not isinstance(comparator, aas.SubmodelElement):
                                comparator = self.Comparator(comparator)

                            # Build a submodel element if a raw value was passed in the argument

                            if formulaRight is not None and not isinstance(formulaRight, aas.SubmodelElement):
                                formulaRight = self.FormulaRight(formulaRight)

                            # Build a submodel element if a raw value was passed in the argument

                            if formulaLeft is not None and not isinstance(formulaLeft, aas.SubmodelElement):
                                formulaLeft = self.FormulaLeft(formulaLeft)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                comparator, formulaRight, formulaLeft
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"applicabilityConditions",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Applicability Conditions"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Additional conditions that must be met for the dependency to be considered fulfilled. In other words, an activation of the Triggering Flexible-Load implies or excludes a corresponding activation of the Target Flexible-Load in a configuration (measure), so that the applicability conditions are fulfilled. The Triggering Flexible-Load metrics are incorporated on the left side of the formula. The Target Flexible-Load metrics are incorporated on the right side."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/applicabilityConditions"
                            ),
                        }

                    def __init__(
                        self,
                        applicabilityconditions_items: Iterable[Applicabilityconditions_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(applicabilityconditions_items, str):
                            raise TypeError("applicabilityconditions_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            applicabilityconditions_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class TriggeringFlexibleLoad(aas.SubmodelElementCollection):

                    class TemporalType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"temporalType",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Temporal Type"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r'enum: start, total, end. The temporalType start specifies that with the activation of a Flexible-Load Measure belonging to this Flexible Load, the dependency Applicability Duration" of the Target Flexible-Load begins.  end specifies that at the deactivation end of a Flexible-Load Measure belonging to this Flexible Load, the dependency Appicability Duration of the "Target Flexible-Load begins.  total specifies that during a Flexible-Load Measure belonging to this Flexible Load, the dependency Applicability Duration of the Target Flexible-Load is valid.'
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/temporalType",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TriggeringFlexibleLoadId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"triggeringFlexibleLoadId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Triggering Flexible Load ID"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The ID of the Flexible Load that is affected by the Triggering Flexible-Load. The Flexible Load must be defined in the same Flexibility Space, and is referenced by its ID."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"triggeringFlexibleLoad",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Triggering Flexible Load"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The Flexible Load that triggers the dependency. The Flexible Load must be defined in the same Flexibility Space, and is referenced by its ID. In addition, one time parameter (start, total or end) of the Triggering Flexible-Load affected by the dependency is to be indicated."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/triggeringFlexibleLoad"
                            ),
                        }

                    def __init__(
                        self,
                        temporalType: Union[str, TemporalType],
                        triggeringFlexibleLoadId: Union[str, TriggeringFlexibleLoadId],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if temporalType is not None and not isinstance(temporalType, aas.SubmodelElement):
                            temporalType = self.TemporalType(temporalType)

                        # Build a submodel element if a raw value was passed in the argument

                        if triggeringFlexibleLoadId is not None and not isinstance(
                            triggeringFlexibleLoadId, aas.SubmodelElement
                        ):
                            triggeringFlexibleLoadId = self.TriggeringFlexibleLoadId(triggeringFlexibleLoadId)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(temporalType, triggeringFlexibleLoadId)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class TargetFlexibleLoad(aas.SubmodelElementCollection):

                    class TemporalType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"temporalType",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Temporal Type"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"enum: start, total, end. The temporalType start specifies that the start of a Flexible-Load Measure of the Target Flexible-Load is affected by the dependency Applicability Duration. end specifies that the deactivation end of a Flexible-Load Measure of the Target Flexible-Load is affected by the dependency Applicability Duration. total specifies that the Flexible-Load Measure of the Target Flexible-Load is affected by the dependency Applicability Duration starting at activation until the end of deactivation"
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/temporalType",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TargetFlexibleLoadId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"targetFlexibleLoadId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Target Flexible Load ID"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"UUID of the Flexible Load that is affected by the Triggering Flexible-Load. The Flexible Load must be defined in the same Flexibility Space, and is referenced by its ID."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"targetFlexibleLoad",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Target Flexible Load"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"target flexible load"}),
                        }

                    def __init__(
                        self,
                        temporalType: Union[str, TemporalType],
                        targetFlexibleLoadId: Union[str, TargetFlexibleLoadId],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if temporalType is not None and not isinstance(temporalType, aas.SubmodelElement):
                            temporalType = self.TemporalType(temporalType)

                        # Build a submodel element if a raw value was passed in the argument

                        if targetFlexibleLoadId is not None and not isinstance(
                            targetFlexibleLoadId, aas.SubmodelElement
                        ):
                            targetFlexibleLoadId = self.TargetFlexibleLoadId(targetFlexibleLoadId)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(temporalType, targetFlexibleLoadId)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class LogicalType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"logicalType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Logical Type"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"enum: implies, excludes. Specifies whether a use of the Triggering Flexible-Load requires (implies) or prevents (excludes) the activation of the Target Flexible-Load within the Applicability Duration."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/logicalType"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependency"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Each dependency can be used to describe a restriction or dependency for the interaction of several Flexible Loads within an Flexibility Space. This allows the permissible operating options of an overall system to be mapped in greater detail so that Flexible-Load Measures do not have a negative impact on the system, the production processes or the product quality."
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/dependency",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    dependencyId: Union[str, DependencyId],
                    triggeringFlexibleLoad: TriggeringFlexibleLoad,
                    targetFlexibleLoad: TargetFlexibleLoad,
                    logicalType: Union[str, LogicalType],
                    applicabilityDuration: Optional[Union[Tuple[xsd.Float, xsd.Float], ApplicabilityDuration]] = None,
                    applicabilityConditions: Optional[
                        Union[Iterable[ApplicabilityConditions.Applicabilityconditions_item], ApplicabilityConditions]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if dependencyId is not None and not isinstance(dependencyId, aas.SubmodelElement):
                        dependencyId = self.DependencyId(dependencyId)

                    # Build a submodel element if a raw value was passed in the argument

                    if applicabilityDuration is not None and not isinstance(applicabilityDuration, aas.SubmodelElement):
                        applicabilityDuration = self.ApplicabilityDuration(
                            min=applicabilityDuration[0], max=applicabilityDuration[1]
                        )

                    # A str would be split into its characters
                    if isinstance(applicabilityConditions, str):
                        raise TypeError("applicabilityConditions takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if applicabilityConditions is not None and not isinstance(
                        applicabilityConditions, aas.SubmodelElement
                    ):
                        applicabilityConditions = self.ApplicabilityConditions(applicabilityConditions)

                    # Build a submodel element if a raw value was passed in the argument

                    if logicalType is not None and not isinstance(logicalType, aas.SubmodelElement):
                        logicalType = self.LogicalType(logicalType)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        dependencyId,
                        applicabilityDuration,
                        applicabilityConditions,
                        triggeringFlexibleLoad,
                        targetFlexibleLoad,
                        logicalType,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"dependencies",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependencies"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"dependenciesmay contain multiple dependencies, each of which can be used to describe a restriction or dependency for the interaction of several Flexible Loads within an Flexibility Space. This allows the permissible operating options of an overall system to be mapped in greater detail so that Flexible-Load Measures do not have a negative impact on the system, the production processes or the product quality."
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/dependencies",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(
                self, dependencies_items: Iterable[Dependencies_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(dependencies_items, str):
                    raise TypeError("dependencies_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(dependencies_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"flexibilitySpace_operationalPotential",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexibility Space Operational Potential"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"This SMC describes the degrees of freedom of an energy-flexible system within its actual operational environment. It includes all relevant conditions, resources, and constraints of the production context, enabling a realistic representation of the maximum feasible flexibility potential, regardless of a specific application."
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibilitySpace_operationalPotential"
                ),
            }

        def __init__(
            self,
            metadata: Metadata,
            utilizationContext: UtilizationContext,
            flexibleLoads: Union[Iterable[FlexibleLoads.Flexibleloads_item], FlexibleLoads],
            storages: Optional[Union[Iterable[Storages.Storages_item], Storages]] = None,
            dependencies: Optional[Union[Iterable[Dependencies.Dependencies_item], Dependencies]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(flexibleLoads, str):
                raise TypeError("flexibleLoads takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if flexibleLoads is not None and not isinstance(flexibleLoads, aas.SubmodelElement):
                flexibleLoads = self.FlexibleLoads(flexibleLoads)

            # A str would be split into its characters
            if isinstance(storages, str):
                raise TypeError("storages takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if storages is not None and not isinstance(storages, aas.SubmodelElement):
                storages = self.Storages(storages)

            # A str would be split into its characters
            if isinstance(dependencies, str):
                raise TypeError("dependencies takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if dependencies is not None and not isinstance(dependencies, aas.SubmodelElement):
                dependencies = self.Dependencies(dependencies)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                metadata, utilizationContext, flexibleLoads, storages, dependencies
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FlexibilitySpace_applicationTailoredPotential(aas.SubmodelElementCollection):

        class Metadata(aas.SubmodelElementCollection):

            class InstanceId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"instanceId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Instance ID"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The ID of a Flexibility Space or Flexible-Load Measure Package for unique identification"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Comment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"comment",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Comment"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Free text to comment the EFDM object."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/comment"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EfdmVersion(aas.SubmodelElementCollection):

                class VersionNumber(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"versionNumber",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Version Number"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"the EFDM version (e.g. 0.3)"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/versionNumber"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SchemaLink(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"schemaLink",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Schema Link"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"hyperlink to the corresponding scheme"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/schemaLink"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"efdmVersion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"EFDM Version"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Specification of the EFDM version and hyperlink to the corresponding scheme."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/efdmVersion"
                        ),
                    }

                def __init__(
                    self,
                    versionNumber: Union[str, VersionNumber],
                    schemaLink: Union[str, SchemaLink],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if versionNumber is not None and not isinstance(versionNumber, aas.SubmodelElement):
                        versionNumber = self.VersionNumber(versionNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if schemaLink is not None and not isinstance(schemaLink, aas.SubmodelElement):
                        schemaLink = self.SchemaLink(schemaLink)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(versionNumber, schemaLink)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Origin(aas.SubmodelElementCollection):

                class OriginId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"originId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the creating service and point in time of creation"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"timestamp of the creating service"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"origin",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the creating service and point in time of creation. By means of the automated filling in of the Element, conclusions about the origin and an allocation to executing agencies are made possible. In the case of communication with external services, this Element is replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/origin"),
                    }

                def __init__(
                    self,
                    originId: Union[str, OriginId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if originId is not None and not isinstance(originId, aas.SubmodelElement):
                        originId = self.OriginId(originId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(originId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Modification(aas.SubmodelElementCollection):

                class ModificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"modificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the service instance that last processed this object "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Its value should be provided by service provider, who creates SMC flexibilitySpace of the EFDM instance"
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"modification",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the service instance that last processed this object and point in time of last processing. In the case of communication with external services, this Element can be replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modification"
                        ),
                    }

                def __init__(
                    self,
                    modificationId: Union[str, ModificationId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if modificationId is not None and not isinstance(modificationId, aas.SubmodelElement):
                        modificationId = self.ModificationId(modificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(modificationId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"metadata",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Metadata"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The metadata provides essential information for tracking and tracing of the model instances."
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/metadata",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(
                self,
                instanceId: Union[str, InstanceId],
                efdmVersion: EfdmVersion,
                origin: Origin,
                modification: Modification,
                comment: Optional[Union[aas.LangStringSet, Comment]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if instanceId is not None and not isinstance(instanceId, aas.SubmodelElement):
                    instanceId = self.InstanceId(instanceId)

                # Build a submodel element if a raw value was passed in the argument

                if comment is not None and not isinstance(comment, aas.SubmodelElement):
                    comment = self.Comment(comment)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    instanceId, comment, efdmVersion, origin, modification
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class UtilizationContext(aas.SubmodelElementCollection):

            class Status(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"status",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Status"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"enum: draft, available, offered, reserved, measuresRequest, finalized. The status of a Flexibility Space describes its current condition within the overall process of applying energy-flexible measures. The objctive is to make the progession and individual phases of each Flexibility Space transparently traceable."
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/status",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ModellingScope(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"modellingScope",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modelling Scope"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"enum: generalTechnicalPotential, operationalPotential, applicationTailoredPotential. The modelling scope places individual EFDM instances and their key figures into context. generalTechnicalPotential: The modelling of flexibility includes universally valid technical characteristics and restrictions; the model does not contain operational strategies, production plans, or other plant-specific limitations. The energy flexibility potential is not directly implementable. operationalPotential: Flexibility is fully considered within the production environment; the model describes the maximum feasible potential, independent of the specific use case. applicationTailoredPotential: The model describes a potential tailored to a specific application (e.g. energy market may allow only Flexible Load with 15-min holding durations); storage and dependencies may need to be transformed to be represented as Flexible Load."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modellingScope"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Trading(aas.SubmodelElementCollection):

                class ExternallyTradeable(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"externallyTradeable",
                            "value_type": bool,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Externally Tradeable"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r" Indicates whether the Flexibility Space is intended to participate in external energy markets (true) or is to be used exclusively for internal optimization purposes (false)."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/externallyTradeable"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AutoTradeable(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"autoTradeable",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Auto Tradeable"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r" Specifies whether the trading process can be executed automatically (true) or if additional manual preparations or reviews and verification procedures are required (false)."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/autoTradeable"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"trading",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Trading"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The Trading of a Flexibility Space comprises configurable properties that determine its feasibility and operational implementation"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/trading"
                        ),
                    }

                def __init__(
                    self,
                    externallyTradeable: Union[bool, ExternallyTradeable],
                    autoTradeable: Union[str, AutoTradeable],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if externallyTradeable is not None and not isinstance(externallyTradeable, aas.SubmodelElement):
                        externallyTradeable = self.ExternallyTradeable(externallyTradeable)

                    # Build a submodel element if a raw value was passed in the argument

                    if autoTradeable is not None and not isinstance(autoTradeable, aas.SubmodelElement):
                        autoTradeable = self.AutoTradeable(autoTradeable)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(externallyTradeable, autoTradeable)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"utilizationContext",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Utilization Context"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Containing metainformation, describing the model status and scope"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/utilizationContext"
                    ),
                }

            def __init__(
                self,
                status: Union[str, Status],
                modellingScope: Union[str, ModellingScope],
                trading: Trading,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if status is not None and not isinstance(status, aas.SubmodelElement):
                    status = self.Status(status)

                # Build a submodel element if a raw value was passed in the argument

                if modellingScope is not None and not isinstance(modellingScope, aas.SubmodelElement):
                    modellingScope = self.ModellingScope(modellingScope)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(status, modellingScope, trading)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FlexibleLoads(GeneratedSubmodelElementList):

            class Flexibleloads_item(aas.SubmodelElementCollection):

                class FlexibleLoadId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"flexibleLoadId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of a Flexible Load for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services. String Format: UUID"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReactionDuration(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"reactionDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reaction Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Time (seconds) required by a technical system between the receipt of a call-up and the initiation of a Flexible-Load Measure within the enterprise. The call must be issued with at least this lead time before the Flexible-Load Measure starts."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAV535#002"),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class Validity(aas.SubmodelElementCollection):

                    class From(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"from",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"From"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"from time. If this period is not specified, continuous availability of the Flexible Load  is assumed. "
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABF198#001"),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Until(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"until",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Until"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"until time. If this period is not specified, continuous availability of the Flexible Load  is assumed. "
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABF198#001"),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TemporalType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"temporalType",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Temporal Type"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"enum: start, total, end. The temporalType start specifies that the start of each Flexible-Load Measure belonging to this Flexible Load must lie within the Validity Period. end specifies that the end of each Flexible-Load Measure belonging to this Flexible Load must lie within the Validity Period. total specifies that the total duration of each Flexible-Load Measure belonging to this Flexible Load must lie within the Validity Period."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/temporalType"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"validity",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Validity"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Subset of the company-internal planning horizon in which the Flexible Load is available. The beginning and end of this validity period are specified with the attributes from and until. If this period is not specified, continuous availability of the Flexible Load is assumed. "
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/validity"
                            ),
                        }

                    def __init__(
                        self,
                        from_: Optional[Union[xsd.DateTime, From]] = None,
                        until: Optional[Union[xsd.DateTime, Until]] = None,
                        temporalType: Optional[Union[str, TemporalType]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if from_ is not None and not isinstance(from_, aas.SubmodelElement):
                            from_ = self.From(from_)

                        # Build a submodel element if a raw value was passed in the argument

                        if until is not None and not isinstance(until, aas.SubmodelElement):
                            until = self.Until(until)

                        # Build a submodel element if a raw value was passed in the argument

                        if temporalType is not None and not isinstance(temporalType, aas.SubmodelElement):
                            temporalType = self.TemporalType(temporalType)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(from_, until, temporalType)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class PowerStates(GeneratedSubmodelElementList):

                    class Powerstates_item(aas.SubmodelElementCollection):

                        class Power(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"power",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"A positive sign means that the Flexible Load can increase its power consumption. Negative Power States represent a possible decrease in power consumption. Uncertainty can be represented by specifying a range."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAZ820#001"),
                                }

                            def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class Duration(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"duration",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Duration"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"The time period during which the Flexible Load can run in its corresponding Power States. Uncertainty can be represented by specifying a range."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAQ203#001"),
                                }

                            def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class DurationType(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"durationType",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Duration Type"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"enum: deliveryDuration, holdingDuration. Duration either corresponds to the time of a constant Power State (holdingDuration) OR a constant Power State WITH initial power modulation (deliveryDuration)."
                                        }
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/durationType",
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ReferencePoint(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"referencePoint",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reference Point"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"the scheduled baseline load"}
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAZ820#001"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power State"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"A power state with which the Flexible Load can run during the corresponding holding periods. "
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerState",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(
                            self,
                            power: Union[Tuple[xsd.Float, xsd.Float], Power],
                            duration: Optional[Union[Tuple[xsd.Float, xsd.Float], Duration]] = None,
                            durationType: Optional[Union[str, DurationType]] = None,
                            referencePoint: Optional[Union[xsd.Float, ReferencePoint]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if power is not None and not isinstance(power, aas.SubmodelElement):
                                power = self.Power(min=power[0], max=power[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if duration is not None and not isinstance(duration, aas.SubmodelElement):
                                duration = self.Duration(min=duration[0], max=duration[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if durationType is not None and not isinstance(durationType, aas.SubmodelElement):
                                durationType = self.DurationType(durationType)

                            # Build a submodel element if a raw value was passed in the argument

                            if referencePoint is not None and not isinstance(referencePoint, aas.SubmodelElement):
                                referencePoint = self.ReferencePoint(referencePoint)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                power, duration, durationType, referencePoint
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"powerStates",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power States"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"a set of Power States with which the Flexible Load can run during each of the (number of changes + 1) holding periods. "
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerStates",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(
                        self,
                        powerstates_items: Iterable[Powerstates_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(powerstates_items, str):
                            raise TypeError("powerstates_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(powerstates_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class UsageNumber(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"usageNumber",
                            "value_type": xsd.PositiveInteger,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Usage Number"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The permitted number of activations of the Flexible Load within the Validity Period. A specified minimum value of the range defines a required number of activations; a specified maximum value sets an upper limit on activation frequency."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/usageNumber"
                            ),
                        }

                    def __init__(
                        self, min: xsd.PositiveInteger, max: xsd.PositiveInteger, **kwargs: Unpack[RangeMetadata]
                    ):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class ModulationNumber(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"modulationNumber",
                            "value_type": xsd.NonNegativeInteger,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modulation Number"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The maximum number of Power State changes (modulations) allowed within one use of a Flexible Load. The two modulations corresponding to the initial activation and the final deactivation are not counted."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modulationNumber"
                            ),
                        }

                    def __init__(
                        self, min: xsd.NonNegativeInteger, max: xsd.NonNegativeInteger, **kwargs: Unpack[RangeMetadata]
                    ):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class PowerGradients(aas.SubmodelElementCollection):

                    class ActivationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"activationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Activation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Actication Gradient specifies the power gradient applicable during the initial activation of the Flexibl Load."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class ModulationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"modulationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modulation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Modulation Gradient specifies the power gradient during transitions between Power States."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class DeactivationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"deactivationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Deactivation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Deactivation Gradient specifies the power gradient during the final deactivation phase"
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"powerGradients",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power Gradients"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The absolute value of the power gradient of a Flexible Load indicates how fast the power can be increased or decreased."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerGradients"
                            ),
                        }

                    def __init__(
                        self,
                        activationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], ActivationGradient]] = None,
                        modulationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], ModulationGradient]] = None,
                        deactivationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], DeactivationGradient]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if activationGradient is not None and not isinstance(activationGradient, aas.SubmodelElement):
                            activationGradient = self.ActivationGradient(
                                min=activationGradient[0], max=activationGradient[1]
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if modulationGradient is not None and not isinstance(modulationGradient, aas.SubmodelElement):
                            modulationGradient = self.ModulationGradient(
                                min=modulationGradient[0], max=modulationGradient[1]
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if deactivationGradient is not None and not isinstance(
                            deactivationGradient, aas.SubmodelElement
                        ):
                            deactivationGradient = self.DeactivationGradient(
                                min=deactivationGradient[0], max=deactivationGradient[1]
                            )

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            activationGradient, modulationGradient, deactivationGradient
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class RegenerationDuration(aas.Property):

                    ALLOWED_RANGE = (xsd.from_xsd(r"0.0", xsd.Float), None)

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"regenerationDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Regeneration Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The required regeneration time during which no other measure of the same Flexible Load may be activated following the deactivation of a previous measure. This time constraint applies only if an actual deactivation occurs. If another measure follows without interruption, no deactivation takes place between them; this does not constitute a violation of the defined regerneration period."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAV535#002"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and (
                            value < self.ALLOWED_RANGE[0]
                            or self.ALLOWED_RANGE[1] is not None
                            and value > self.ALLOWED_RANGE[1]
                        ):
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class FlexibleLoadCosts(aas.SubmodelElementCollection):

                    class VariableCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"variableCost",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Variable costs refer to the total amount of energy converted. "}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerEnergyConverted"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CostPerUsage(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"costPerUsage",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Cost Per Usage"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Usage costs are incurred per use of a Flexible-Load."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerUsage"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FixedCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"fixedCost",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fixed Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Fixed costs incurred during the Validity Period regardless of the call of a Flexible Load (example: standby costs of a power generation plant)."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/fixedCost"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"flexibleLoadCosts",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Costs"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The costs associated with the use of the Flexible Load, excluding electricity costs. The Costs of a Flexible Load consist of variable cost, usage cost and fixed cost."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoadCosts"
                            ),
                        }

                    def __init__(
                        self,
                        variableCost: Optional[Union[xsd.Float, VariableCost]] = None,
                        costPerUsage: Optional[Union[xsd.Float, CostPerUsage]] = None,
                        fixedCost: Optional[Union[xsd.Float, FixedCost]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if variableCost is not None and not isinstance(variableCost, aas.SubmodelElement):
                            variableCost = self.VariableCost(variableCost)

                        # Build a submodel element if a raw value was passed in the argument

                        if costPerUsage is not None and not isinstance(costPerUsage, aas.SubmodelElement):
                            costPerUsage = self.CostPerUsage(costPerUsage)

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedCost is not None and not isinstance(fixedCost, aas.SubmodelElement):
                            fixedCost = self.FixedCost(fixedCost)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(variableCost, costPerUsage, fixedCost)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class OrderConfirmationDeadline(aas.SubmodelElementCollection):

                    class OrderConfirmationDeadlineAbsolute(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"orderConfirmationDeadlineAbsolute",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Order Confirmation Deadline Absolute"}
                                ),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"absolute deadline"}),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class OrderConfirmationDeadlineRelative(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"orderConfirmationDeadlineRelative",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Order Confirmation Deadline Relative"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"relative to the start time of the Flexible-Load Measure (e.g. 100 seconds before the start of a FLM)"
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-AAQ203#001"),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"orderConfirmationDeadline",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Order Confirmation Deadline"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Latest possible time by which confirmation of an accepted offer of the Flexible Load must have been received. By this time, the flexibility provider needs to know whether the Flexible Load must be held ready. After the Booking Confirmation Deadline is exceeded, the Flexible Load offer is removed from the market. The Order Confirmation Deadline can be specified EITHER absolutely with a fixed time OR relative to the start time of the Flexible-Load Measure (e.g. 100 seconds before the start of a FLM). If no value is specified, constant availability for offering is assumed until the latest possible start time within the Validity Period minus the Reaction Duration."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/orderConfirmationDeadline"
                            ),
                        }

                    def __init__(
                        self,
                        orderConfirmationDeadlineAbsolute: Optional[
                            Union[xsd.DateTime, OrderConfirmationDeadlineAbsolute]
                        ] = None,
                        orderConfirmationDeadlineRelative: Optional[
                            Union[str, OrderConfirmationDeadlineRelative]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if orderConfirmationDeadlineAbsolute is not None and not isinstance(
                            orderConfirmationDeadlineAbsolute, aas.SubmodelElement
                        ):
                            orderConfirmationDeadlineAbsolute = self.OrderConfirmationDeadlineAbsolute(
                                orderConfirmationDeadlineAbsolute
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if orderConfirmationDeadlineRelative is not None and not isinstance(
                            orderConfirmationDeadlineRelative, aas.SubmodelElement
                        ):
                            orderConfirmationDeadlineRelative = self.OrderConfirmationDeadlineRelative(
                                orderConfirmationDeadlineRelative
                            )

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            orderConfirmationDeadlineAbsolute, orderConfirmationDeadlineRelative
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Prices(aas.SubmodelElementCollection):

                    class VariablePrice(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"variablePrice",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Price"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Variable price refer to the total amount of energy converted. "}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PricePerEnergyConverted"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class PricePerUsage(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"pricePerUsage",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Price Per Usage"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Usage price are incurred per use of a Flexible-Load."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PricePerUsage"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FixedPrice(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"fixedPrice",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fixed Price"}),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Fixed price"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/fixedPrice"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"prices",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Prices"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Prices to be realized on the market as a minimum for offering the Flexible Load. The Prices of a Flexible Load are composed of a variable price, a usage price and a fixed price analogous to the Costs. Prices are only needed if the Flexible Load is to be actively offered on the market."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/prices"
                            ),
                        }

                    def __init__(
                        self,
                        variablePrice: Optional[Union[str, VariablePrice]] = None,
                        pricePerUsage: Optional[Union[str, PricePerUsage]] = None,
                        fixedPrice: Optional[Union[str, FixedPrice]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if variablePrice is not None and not isinstance(variablePrice, aas.SubmodelElement):
                            variablePrice = self.VariablePrice(variablePrice)

                        # Build a submodel element if a raw value was passed in the argument

                        if pricePerUsage is not None and not isinstance(pricePerUsage, aas.SubmodelElement):
                            pricePerUsage = self.PricePerUsage(pricePerUsage)

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedPrice is not None and not isinstance(fixedPrice, aas.SubmodelElement):
                            fixedPrice = self.FixedPrice(fixedPrice)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(variablePrice, pricePerUsage, fixedPrice)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Location(aas.SubmodelElementCollection):

                    class MeterLocation(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"meterLocation",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Meter Location"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The unambiguous allocation is made by means of the meter point designation known in the energy industry / in market communication. In Germany, it corresponds to a 33-digit alphanumeric code number."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/MeterPointDesignation"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VoltageLevel(aas.Property):

                        ALLOWED_RANGE = (xsd.from_xsd(r"0.0", xsd.Float), None)

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"voltageLevel",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Voltage Level"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The specification of the Grid Voltage Level to which the Flexible Load is connected. The voltage level at the grid connection point is to be used, independent of deviating voltage levels in any company grid."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/GridVoltageLevel"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and (
                                value < self.ALLOWED_RANGE[0]
                                or self.ALLOWED_RANGE[1] is not None
                                and value > self.ALLOWED_RANGE[1]
                            ):
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"location",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Location"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Meter point designation for the geographical and power grid topological location of a Flexible Load. "
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/location"
                            ),
                        }

                    def __init__(
                        self,
                        meterLocation: Optional[Union[str, MeterLocation]] = None,
                        voltageLevel: Optional[Union[xsd.Float, VoltageLevel]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if meterLocation is not None and not isinstance(meterLocation, aas.SubmodelElement):
                            meterLocation = self.MeterLocation(meterLocation)

                        # Build a submodel element if a raw value was passed in the argument

                        if voltageLevel is not None and not isinstance(voltageLevel, aas.SubmodelElement):
                            voltageLevel = self.VoltageLevel(voltageLevel)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(meterLocation, voltageLevel)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r" Each flexibleLoad describes the energy flexibility of a technical system (i.e. controllable unit) or a combination of systems (i.e. an ensemble of controllable units) that can adjust its power consumption or generation in response to external conditions or requirements. It focuses on the limitations and possibilities (degrees of freedom) of changing power outputs of a technical system."
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoad",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    flexibleLoadId: Union[str, FlexibleLoadId],
                    powerStates: Union[Iterable[PowerStates.Powerstates_item], PowerStates],
                    reactionDuration: Optional[Union[Tuple[xsd.Float, xsd.Float], ReactionDuration]] = None,
                    validity: Optional[Validity] = None,
                    usageNumber: Optional[Union[Tuple[xsd.PositiveInteger, xsd.PositiveInteger], UsageNumber]] = None,
                    modulationNumber: Optional[
                        Union[Tuple[xsd.NonNegativeInteger, xsd.NonNegativeInteger], ModulationNumber]
                    ] = None,
                    powerGradients: Optional[PowerGradients] = None,
                    regenerationDuration: Optional[Union[xsd.Float, RegenerationDuration]] = None,
                    flexibleLoadCosts: Optional[FlexibleLoadCosts] = None,
                    orderConfirmationDeadline: Optional[OrderConfirmationDeadline] = None,
                    prices: Optional[Prices] = None,
                    location: Optional[Location] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if flexibleLoadId is not None and not isinstance(flexibleLoadId, aas.SubmodelElement):
                        flexibleLoadId = self.FlexibleLoadId(flexibleLoadId)

                    # Build a submodel element if a raw value was passed in the argument

                    if reactionDuration is not None and not isinstance(reactionDuration, aas.SubmodelElement):
                        reactionDuration = self.ReactionDuration(min=reactionDuration[0], max=reactionDuration[1])

                    # A str would be split into its characters
                    if isinstance(powerStates, str):
                        raise TypeError("powerStates takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if powerStates is not None and not isinstance(powerStates, aas.SubmodelElement):
                        powerStates = self.PowerStates(powerStates)

                    # Build a submodel element if a raw value was passed in the argument

                    if usageNumber is not None and not isinstance(usageNumber, aas.SubmodelElement):
                        usageNumber = self.UsageNumber(min=usageNumber[0], max=usageNumber[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if modulationNumber is not None and not isinstance(modulationNumber, aas.SubmodelElement):
                        modulationNumber = self.ModulationNumber(min=modulationNumber[0], max=modulationNumber[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if regenerationDuration is not None and not isinstance(regenerationDuration, aas.SubmodelElement):
                        regenerationDuration = self.RegenerationDuration(regenerationDuration)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        flexibleLoadId,
                        reactionDuration,
                        validity,
                        powerStates,
                        usageNumber,
                        modulationNumber,
                        powerGradients,
                        regenerationDuration,
                        flexibleLoadCosts,
                        orderConfirmationDeadline,
                        prices,
                        location,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"flexibleLoads",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Loads"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"flexibleLoads may contain multiple flexibleLoad."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoads"
                    ),
                }

            def __init__(
                self, flexibleloads_items: Iterable[Flexibleloads_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(flexibleloads_items, str):
                    raise TypeError("flexibleloads_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(flexibleloads_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Storages(GeneratedSubmodelElementList):

            class Storages_item(aas.SubmodelElementCollection):

                class StorageId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"storageId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of a storage for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StorageCosts(aas.SubmodelElementCollection):

                    class VariableCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"variableCost",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Variable costs refer to the total amount of energy converted."}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerEnergyConverted",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CostPerUsage(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"costPerUsage",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Cost Per Usage"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Usage costs arise per use of a storage tank."}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/CostPerUsage",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FixedCost(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"fixedCost",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fixed Cost"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Fixed costs arise from keeping a storage facility on standby."}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/fixedCost",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"storageCosts",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage Costs"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The costs associated with the use of the energy storage. The Costs of a storage facility consist of variable cost, usage cost and fixed cost. Variable costs refer to the total amount of energy converted. Usage costs arise per use of a storage tank. Fixed costs arise from keeping a storage facility on standby."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storageCosts"
                            ),
                        }

                    def __init__(
                        self,
                        variableCost: Optional[Union[str, VariableCost]] = None,
                        costPerUsage: Optional[Union[str, CostPerUsage]] = None,
                        fixedCost: Optional[Union[str, FixedCost]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if variableCost is not None and not isinstance(variableCost, aas.SubmodelElement):
                            variableCost = self.VariableCost(variableCost)

                        # Build a submodel element if a raw value was passed in the argument

                        if costPerUsage is not None and not isinstance(costPerUsage, aas.SubmodelElement):
                            costPerUsage = self.CostPerUsage(costPerUsage)

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedCost is not None and not isinstance(fixedCost, aas.SubmodelElement):
                            fixedCost = self.FixedCost(fixedCost)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(variableCost, costPerUsage, fixedCost)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class UsableCapacity(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"usableCapacity",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Usable Capacity"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Lower and upper limit of the storage energy content. These limits must never be exceeded or fallen short of. Depending on the choice of reference point, it is also possible to specify negative storage capacities, e.g. if it needs to be possible to either exceed or fall below storage limits."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class InitialEnergyContent(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"initialEnergyContent",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Initial Energy Content"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Energy content of the storage at the start time of the Validity Period of the associated Flexible Load (Suppliers). If the storage is connected to several Flexible Loads, the Initial Energy Content refers to the earliest start time of the Validity Periods of all Flexible Loads. If the initial energy content cannot be quantified exactly, the predicted range can be specified via min and max."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class TargetEnergyContent(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"targetEnergyContent",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Target Energy Content"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Energy content that the storage must have at the end time of the Validity Period of the associated Flexible Loads (Suppliers). If the storage is connected to several Flexible Loads, the Target Energy Content refers to the latest end time of the Validity Periods of all Flexible Loads. If the target energy content is flexible, the desired target range is specified can be specified via min and max."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class EnergyLoss(aas.Property):

                    ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.UnsignedShort), xsd.from_xsd(r"100", xsd.UnsignedShort))

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"energyLoss",
                            "value_type": xsd.UnsignedShort,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Energy Loss"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Proportion of the energy content that is continuously lost, e.g. through exchange with the environment. The percentage refers to the actual energy content and not to the storage capacity."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/EnergyContentLossPerHour"
                            ),
                        }

                    def __init__(self, value: xsd.UnsignedShort, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and (
                            value < self.ALLOWED_RANGE[0]
                            or self.ALLOWED_RANGE[1] is not None
                            and value > self.ALLOWED_RANGE[1]
                        ):
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Suppliers(GeneratedSubmodelElementList):

                    class Suppliers_item(aas.SubmodelElementCollection):

                        class FlexibleLoadId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"flexibleLoadId",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load ID"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"This ID identifies the Flexible Load supplying the storage. The ID of a Flexible Load for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ConversionEfficiency(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"conversionEfficiency",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Conversion Efficiency"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Energy conversion efficiency of the suppiler"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/EnergyConversionEfficiency"
                                    ),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Supplier"}),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Indicating a single supply"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/supplier"
                                ),
                            }

                        def __init__(
                            self,
                            flexibleLoadId: Union[str, FlexibleLoadId],
                            conversionEfficiency: Optional[Union[xsd.Float, ConversionEfficiency]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if flexibleLoadId is not None and not isinstance(flexibleLoadId, aas.SubmodelElement):
                                flexibleLoadId = self.FlexibleLoadId(flexibleLoadId)

                            # Build a submodel element if a raw value was passed in the argument

                            if conversionEfficiency is not None and not isinstance(
                                conversionEfficiency, aas.SubmodelElement
                            ):
                                conversionEfficiency = self.ConversionEfficiency(conversionEfficiency)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(flexibleLoadId, conversionEfficiency)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"suppliers",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Suppliers"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"One or more Flexible Loads supplying the storage. The Flexible Loads must be defined in the same Flexibility Space. The conversion efficiency is specified for each supply system."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/suppliers"
                            ),
                        }

                    def __init__(
                        self, suppliers_items: Iterable[Suppliers_item], **kwargs: Unpack[SubmodelElementListMetadata]
                    ):

                        # A str would be split into its characters
                        if isinstance(suppliers_items, str):
                            raise TypeError("suppliers_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(suppliers_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Drains(GeneratedSubmodelElementList):

                    class Drains_item(aas.SubmodelElementCollection):

                        class Power(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"power",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power"}),
                                    "description": aas.MultiLanguageTextType(dict_={r"en": r"power drained"}),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-AAZ820#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Timestamp(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"timestamp",
                                    "value_type": xsd.DateTime,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"timestamp of power drain"}
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Drain"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Indicating a single non-influenceable energy demand"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/drain"
                                ),
                            }

                        def __init__(
                            self,
                            power: Optional[Union[xsd.Float, Power]] = None,
                            timestamp: Optional[Union[xsd.DateTime, Timestamp]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if power is not None and not isinstance(power, aas.SubmodelElement):
                                power = self.Power(power)

                            # Build a submodel element if a raw value was passed in the argument

                            if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                                timestamp = self.Timestamp(timestamp)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(power, timestamp)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"drains",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Drains"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Non-influenceable energy demands in the form of a load profile that must be met. The interpolation between the Power States is linear."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/drains"
                            ),
                        }

                    def __init__(
                        self, drains_items: Iterable[Drains_item], **kwargs: Unpack[SubmodelElementListMetadata]
                    ):

                        # A str would be split into its characters
                        if isinstance(drains_items, str):
                            raise TypeError("drains_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(drains_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A storage represents a technical system or a combination of systems that has the potential to store energy"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storage",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    storageId: Union[str, StorageId],
                    usableCapacity: Union[Tuple[xsd.Float, xsd.Float], UsableCapacity],
                    initialEnergyContent: Union[Tuple[xsd.Float, xsd.Float], InitialEnergyContent],
                    storageCosts: Optional[StorageCosts] = None,
                    targetEnergyContent: Optional[Union[Tuple[xsd.Float, xsd.Float], TargetEnergyContent]] = None,
                    energyLoss: Optional[Union[xsd.UnsignedShort, EnergyLoss]] = None,
                    suppliers: Optional[Union[Iterable[Suppliers.Suppliers_item], Suppliers]] = None,
                    drains: Optional[Union[Iterable[Drains.Drains_item], Drains]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if storageId is not None and not isinstance(storageId, aas.SubmodelElement):
                        storageId = self.StorageId(storageId)

                    # Build a submodel element if a raw value was passed in the argument

                    if usableCapacity is not None and not isinstance(usableCapacity, aas.SubmodelElement):
                        usableCapacity = self.UsableCapacity(min=usableCapacity[0], max=usableCapacity[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if initialEnergyContent is not None and not isinstance(initialEnergyContent, aas.SubmodelElement):
                        initialEnergyContent = self.InitialEnergyContent(
                            min=initialEnergyContent[0], max=initialEnergyContent[1]
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if targetEnergyContent is not None and not isinstance(targetEnergyContent, aas.SubmodelElement):
                        targetEnergyContent = self.TargetEnergyContent(
                            min=targetEnergyContent[0], max=targetEnergyContent[1]
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if energyLoss is not None and not isinstance(energyLoss, aas.SubmodelElement):
                        energyLoss = self.EnergyLoss(energyLoss)

                    # A str would be split into its characters
                    if isinstance(suppliers, str):
                        raise TypeError("suppliers takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if suppliers is not None and not isinstance(suppliers, aas.SubmodelElement):
                        suppliers = self.Suppliers(suppliers)

                    # A str would be split into its characters
                    if isinstance(drains, str):
                        raise TypeError("drains takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if drains is not None and not isinstance(drains, aas.SubmodelElement):
                        drains = self.Drains(drains)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        storageId,
                        storageCosts,
                        usableCapacity,
                        initialEnergyContent,
                        targetEnergyContent,
                        energyLoss,
                        suppliers,
                        drains,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"storages",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storages"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Storages may contain multiple storages, each of which represents a technical system or a combination of systems that has the potential to store energy"
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storages",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(self, storages_items: Iterable[Storages_item], **kwargs: Unpack[SubmodelElementListMetadata]):

                # A str would be split into its characters
                if isinstance(storages_items, str):
                    raise TypeError("storages_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(storages_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Dependencies(GeneratedSubmodelElementList):

            class Dependencies_item(aas.SubmodelElementCollection):

                class DependencyId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"dependencyId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependency ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The ID of a dependency for unique identification. "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ApplicabilityDuration(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"applicabilityDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Applicability Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The time period following the activation of theTriggering Flexible-Load during which the Target Flexible-Load must be activated at least once (Logical Type: implies) or must not be activated at all (Logical Type: excludes). The values specified for min and max define the Applicability duration relative to: "
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAQ203#001"),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class ApplicabilityConditions(GeneratedSubmodelElementList):

                    class Applicabilityconditions_item(aas.SubmodelElementCollection):

                        class Comparator(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"comparator",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Comparator"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"enum: equals, less, lessEqual, greater, greaterEqual."}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/comparator"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FormulaRight(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"formulaRight",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Formula Right"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"The Target Flexible-Load metrics are incorporated on the right side."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/formulaRight"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FormulaLeft(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"formulaLeft",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Formula Left"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"The Triggering Flexible-Load metrics are incorporated on the left side of the formula."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/formulaLeft"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Applicability Condition"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Indicating a single condition"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/applicabilityCondition"
                                ),
                            }

                        def __init__(
                            self,
                            comparator: Optional[Union[str, Comparator]] = None,
                            formulaRight: Optional[Union[str, FormulaRight]] = None,
                            formulaLeft: Optional[Union[str, FormulaLeft]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if comparator is not None and not isinstance(comparator, aas.SubmodelElement):
                                comparator = self.Comparator(comparator)

                            # Build a submodel element if a raw value was passed in the argument

                            if formulaRight is not None and not isinstance(formulaRight, aas.SubmodelElement):
                                formulaRight = self.FormulaRight(formulaRight)

                            # Build a submodel element if a raw value was passed in the argument

                            if formulaLeft is not None and not isinstance(formulaLeft, aas.SubmodelElement):
                                formulaLeft = self.FormulaLeft(formulaLeft)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                comparator, formulaRight, formulaLeft
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"applicabilityConditions",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Applicability Conditions"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Additional conditions that must be met for the dependency to be considered fulfilled. In other words, an activation of the Triggering Flexible-Load implies or excludes a corresponding activation of the Target Flexible-Load in a configuration (measure), so that the applicability conditions are fulfilled. The Triggering Flexible-Load metrics are incorporated on the left side of the formula. The Target Flexible-Load metrics are incorporated on the right side."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/applicabilityConditions"
                            ),
                        }

                    def __init__(
                        self,
                        applicabilityconditions_items: Iterable[Applicabilityconditions_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(applicabilityconditions_items, str):
                            raise TypeError("applicabilityconditions_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            applicabilityconditions_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class TriggeringFlexibleLoad(aas.SubmodelElementCollection):

                    class TemporalType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"temporalType",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Temporal Type"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r'enum: start, total, end. The temporalType start specifies that with the activation of a Flexible-Load Measure belonging to this Flexible Load, the dependency Applicability Duration" of the Target Flexible-Load begins.  end specifies that at the deactivation end of a Flexible-Load Measure belonging to this Flexible Load, the dependency Appicability Duration of the "Target Flexible-Load begins.  total specifies that during a Flexible-Load Measure belonging to this Flexible Load, the dependency Applicability Duration of the Target Flexible-Load is valid.'
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/temporalType",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TriggeringFlexibleLoadId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"triggeringFlexibleLoadId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Triggering Flexible Load ID"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The ID of the Flexible Load that is affected by the Triggering Flexible-Load. The Flexible Load must be defined in the same Flexibility Space, and is referenced by its ID."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"triggeringFlexibleLoad",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Triggering Flexible Load"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The Flexible Load that triggers the dependency. The Flexible Load must be defined in the same Flexibility Space, and is referenced by its ID. In addition, one time parameter (start, total or end) of the Triggering Flexible-Load affected by the dependency is to be indicated."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/triggeringFlexibleLoad"
                            ),
                        }

                    def __init__(
                        self,
                        temporalType: Union[str, TemporalType],
                        triggeringFlexibleLoadId: Union[str, TriggeringFlexibleLoadId],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if temporalType is not None and not isinstance(temporalType, aas.SubmodelElement):
                            temporalType = self.TemporalType(temporalType)

                        # Build a submodel element if a raw value was passed in the argument

                        if triggeringFlexibleLoadId is not None and not isinstance(
                            triggeringFlexibleLoadId, aas.SubmodelElement
                        ):
                            triggeringFlexibleLoadId = self.TriggeringFlexibleLoadId(triggeringFlexibleLoadId)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(temporalType, triggeringFlexibleLoadId)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class TargetFlexibleLoad(aas.SubmodelElementCollection):

                    class TemporalType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"temporalType",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Temporal Type"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"enum: start, total, end. The temporalType start specifies that the start of a Flexible-Load Measure of the Target Flexible-Load is affected by the dependency Applicability Duration. end specifies that the deactivation end of a Flexible-Load Measure of the Target Flexible-Load is affected by the dependency Applicability Duration. total specifies that the Flexible-Load Measure of the Target Flexible-Load is affected by the dependency Applicability Duration starting at activation until the end of deactivation"
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/temporalType",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TargetFlexibleLoadId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"targetFlexibleLoadId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Target Flexible Load ID"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"UUID of the Flexible Load that is affected by the Triggering Flexible-Load. The Flexible Load must be defined in the same Flexibility Space, and is referenced by its ID."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"targetFlexibleLoad",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Target Flexible Load"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"target flexible load"}),
                        }

                    def __init__(
                        self,
                        temporalType: Union[str, TemporalType],
                        targetFlexibleLoadId: Union[str, TargetFlexibleLoadId],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if temporalType is not None and not isinstance(temporalType, aas.SubmodelElement):
                            temporalType = self.TemporalType(temporalType)

                        # Build a submodel element if a raw value was passed in the argument

                        if targetFlexibleLoadId is not None and not isinstance(
                            targetFlexibleLoadId, aas.SubmodelElement
                        ):
                            targetFlexibleLoadId = self.TargetFlexibleLoadId(targetFlexibleLoadId)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(temporalType, targetFlexibleLoadId)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class LogicalType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"logicalType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Logical Type"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"enum: implies, excludes. Specifies whether a use of the Triggering Flexible-Load requires (implies) or prevents (excludes) the activation of the Target Flexible-Load within the Applicability Duration."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/logicalType"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependency"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Each dependency can be used to describe a restriction or dependency for the interaction of several Flexible Loads within an Flexibility Space. This allows the permissible operating options of an overall system to be mapped in greater detail so that Flexible-Load Measures do not have a negative impact on the system, the production processes or the product quality."
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/dependency",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    dependencyId: Union[str, DependencyId],
                    triggeringFlexibleLoad: TriggeringFlexibleLoad,
                    targetFlexibleLoad: TargetFlexibleLoad,
                    logicalType: Union[str, LogicalType],
                    applicabilityDuration: Optional[Union[Tuple[xsd.Float, xsd.Float], ApplicabilityDuration]] = None,
                    applicabilityConditions: Optional[
                        Union[Iterable[ApplicabilityConditions.Applicabilityconditions_item], ApplicabilityConditions]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if dependencyId is not None and not isinstance(dependencyId, aas.SubmodelElement):
                        dependencyId = self.DependencyId(dependencyId)

                    # Build a submodel element if a raw value was passed in the argument

                    if applicabilityDuration is not None and not isinstance(applicabilityDuration, aas.SubmodelElement):
                        applicabilityDuration = self.ApplicabilityDuration(
                            min=applicabilityDuration[0], max=applicabilityDuration[1]
                        )

                    # A str would be split into its characters
                    if isinstance(applicabilityConditions, str):
                        raise TypeError("applicabilityConditions takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if applicabilityConditions is not None and not isinstance(
                        applicabilityConditions, aas.SubmodelElement
                    ):
                        applicabilityConditions = self.ApplicabilityConditions(applicabilityConditions)

                    # Build a submodel element if a raw value was passed in the argument

                    if logicalType is not None and not isinstance(logicalType, aas.SubmodelElement):
                        logicalType = self.LogicalType(logicalType)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        dependencyId,
                        applicabilityDuration,
                        applicabilityConditions,
                        triggeringFlexibleLoad,
                        targetFlexibleLoad,
                        logicalType,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"dependencies",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependencies"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"dependenciesmay contain multiple dependencies, each of which can be used to describe a restriction or dependency for the interaction of several Flexible Loads within an Flexibility Space. This allows the permissible operating options of an overall system to be mapped in greater detail so that Flexible-Load Measures do not have a negative impact on the system, the production processes or the product quality."
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/dependencies",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(
                self, dependencies_items: Iterable[Dependencies_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(dependencies_items, str):
                    raise TypeError("dependencies_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(dependencies_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"flexibilitySpace_applicationTailoredPotential",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Flexibility Space Application Tailored Potential"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"This SMC describes the degrees of freedom of an energy-flexible system tailored to the requirements and restrictions of a specific application or market. Property values are derived from the operational potential but adjusted to meet the defined application conditions, such as market rules, technical standards, or contractual obligations."
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibilitySpace_applicationTailoredPotential"
                ),
            }

        def __init__(
            self,
            metadata: Metadata,
            utilizationContext: UtilizationContext,
            flexibleLoads: Union[Iterable[FlexibleLoads.Flexibleloads_item], FlexibleLoads],
            storages: Optional[Union[Iterable[Storages.Storages_item], Storages]] = None,
            dependencies: Optional[Union[Iterable[Dependencies.Dependencies_item], Dependencies]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(flexibleLoads, str):
                raise TypeError("flexibleLoads takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if flexibleLoads is not None and not isinstance(flexibleLoads, aas.SubmodelElement):
                flexibleLoads = self.FlexibleLoads(flexibleLoads)

            # A str would be split into its characters
            if isinstance(storages, str):
                raise TypeError("storages takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if storages is not None and not isinstance(storages, aas.SubmodelElement):
                storages = self.Storages(storages)

            # A str would be split into its characters
            if isinstance(dependencies, str):
                raise TypeError("dependencies takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if dependencies is not None and not isinstance(dependencies, aas.SubmodelElement):
                dependencies = self.Dependencies(dependencies)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                metadata, utilizationContext, flexibleLoads, storages, dependencies
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FlexibilitySpace_generalTechnicalPotential(aas.SubmodelElementCollection):

        class Metadata(aas.SubmodelElementCollection):

            class InstanceId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"instanceId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Instance ID"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The ID of a Flexibility Space or Flexible-Load Measure Package for unique identification"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Comment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"comment",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Comment"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Free text to comment the EFDM object."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/comment"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EfdmVersion(aas.SubmodelElementCollection):

                class VersionNumber(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"versionNumber",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Version Number"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"the EFDM version (e.g. 0.3)"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/versionNumber"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SchemaLink(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"schemaLink",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Schema Link"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"hyperlink to the corresponding scheme"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/schemaLink"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"efdmVersion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"EFDM Version"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Specification of the EFDM version and hyperlink to the corresponding scheme."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/efdmVersion"
                        ),
                    }

                def __init__(
                    self,
                    versionNumber: Union[str, VersionNumber],
                    schemaLink: Union[str, SchemaLink],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if versionNumber is not None and not isinstance(versionNumber, aas.SubmodelElement):
                        versionNumber = self.VersionNumber(versionNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if schemaLink is not None and not isinstance(schemaLink, aas.SubmodelElement):
                        schemaLink = self.SchemaLink(schemaLink)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(versionNumber, schemaLink)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Origin(aas.SubmodelElementCollection):

                class OriginId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"originId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the creating service and point in time of creation"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"timestamp of the creating service"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"origin",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the creating service and point in time of creation. By means of the automated filling in of the Element, conclusions about the origin and an allocation to executing agencies are made possible. In the case of communication with external services, this Element is replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/origin"),
                    }

                def __init__(
                    self,
                    originId: Union[str, OriginId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if originId is not None and not isinstance(originId, aas.SubmodelElement):
                        originId = self.OriginId(originId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(originId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Modification(aas.SubmodelElementCollection):

                class ModificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"modificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the service instance that last processed this object "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"timestamp of of last processing"}),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"modification",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the service instance that last processed this object and point in time of last processing. In the case of communication with external services, this Element can be replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modification"
                        ),
                    }

                def __init__(
                    self,
                    modificationId: Union[str, ModificationId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if modificationId is not None and not isinstance(modificationId, aas.SubmodelElement):
                        modificationId = self.ModificationId(modificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(modificationId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"metadata",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Metadata"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The metadata provides essential information for tracking and tracing of the model instances."
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/metadata",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(
                self,
                instanceId: Union[str, InstanceId],
                efdmVersion: EfdmVersion,
                origin: Origin,
                modification: Modification,
                comment: Optional[Union[aas.LangStringSet, Comment]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if instanceId is not None and not isinstance(instanceId, aas.SubmodelElement):
                    instanceId = self.InstanceId(instanceId)

                # Build a submodel element if a raw value was passed in the argument

                if comment is not None and not isinstance(comment, aas.SubmodelElement):
                    comment = self.Comment(comment)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    instanceId, comment, efdmVersion, origin, modification
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class UtilizationContext(aas.SubmodelElementCollection):

            class Status(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"status",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Status"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'Status of the model instance in case of generalTechnicalPotential should be "draft"'
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/status",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ModellingScope(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"modellingScope",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modelling Scope"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"generalTechnicalPotential: modelling of flexibility includes universally valid technical characteristics and restrictions. The model does not contain information on operational strategies, production plans, or other limitations arising from the specific use of the plant or system. In this case, the energy flexibility potential is not directly implementable."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modellingScope"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"utilizationContext",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Utilization Context"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Containing metainformation, describing the model status and scope"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/utilizationContext"
                    ),
                }

            def __init__(
                self,
                status: Union[str, Status],
                modellingScope: Union[str, ModellingScope],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if status is not None and not isinstance(status, aas.SubmodelElement):
                    status = self.Status(status)

                # Build a submodel element if a raw value was passed in the argument

                if modellingScope is not None and not isinstance(modellingScope, aas.SubmodelElement):
                    modellingScope = self.ModellingScope(modellingScope)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(status, modellingScope)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FlexibleLoads(GeneratedSubmodelElementList):

            class Flexibleloads_item(aas.SubmodelElementCollection):

                class FlexibleLoadId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"flexibleLoadId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of a Flexible Load for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services. String Format: UUID"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReactionDuration(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"reactionDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reaction Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Time (seconds) required by a technical system between the receipt of a call-up and the initiation of a Flexible-Load Measure within the enterprise. The call must be issued with at least this lead time before the Flexible-Load Measure starts."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAV535#002"),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class RegenerationDuration(aas.Property):

                    ALLOWED_RANGE = (xsd.from_xsd(r"0.0", xsd.Float), None)

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"regenerationDuration",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Regeneration Duration"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The required regeneration time during which no other measure of the same Flexible Load may be activated following the deactivation of a previous measure. This time constraint applies only if an actual deactivation occurs. If another measure follows without interruption, no deactivation takes place between them; this does not constitute a violation of the defined regerneration period."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAV535#002"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and (
                            value < self.ALLOWED_RANGE[0]
                            or self.ALLOWED_RANGE[1] is not None
                            and value > self.ALLOWED_RANGE[1]
                        ):
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PowerGradients(aas.SubmodelElementCollection):

                    class ActivationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"activationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Activation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Actication Gradient specifies the power gradient applicable during the initial activation of the Flexibl Load."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class ModulationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"modulationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modulation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Modulation Gradient specifies the power gradient during transitions between Power States."
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class DeactivationGradient(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"deactivationGradient",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Deactivation Gradient"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Deactivation Gradient specifies the power gradient during the final deactivation phase"
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/PowerGradient",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"powerGradients",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power Gradients"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The absolute value of the power gradient of a Flexible Load indicates how fast the power can be increased or decreased."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerGradients"
                            ),
                        }

                    def __init__(
                        self,
                        activationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], ActivationGradient]] = None,
                        modulationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], ModulationGradient]] = None,
                        deactivationGradient: Optional[Union[Tuple[xsd.Float, xsd.Float], DeactivationGradient]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if activationGradient is not None and not isinstance(activationGradient, aas.SubmodelElement):
                            activationGradient = self.ActivationGradient(
                                min=activationGradient[0], max=activationGradient[1]
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if modulationGradient is not None and not isinstance(modulationGradient, aas.SubmodelElement):
                            modulationGradient = self.ModulationGradient(
                                min=modulationGradient[0], max=modulationGradient[1]
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if deactivationGradient is not None and not isinstance(
                            deactivationGradient, aas.SubmodelElement
                        ):
                            deactivationGradient = self.DeactivationGradient(
                                min=deactivationGradient[0], max=deactivationGradient[1]
                            )

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            activationGradient, modulationGradient, deactivationGradient
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ModulationNumber(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"modulationNumber",
                            "value_type": xsd.NonNegativeInteger,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modulation Number"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The maximum number of Power State changes (modulations) allowed within one use of a Flexible Load. The two modulations corresponding to the initial activation and the final deactivation are not counted."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modulationNumber"
                            ),
                        }

                    def __init__(
                        self, min: xsd.NonNegativeInteger, max: xsd.NonNegativeInteger, **kwargs: Unpack[RangeMetadata]
                    ):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class PowerStates(GeneratedSubmodelElementList):

                    class Powerstates_item(aas.SubmodelElementCollection):

                        class Power(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"power",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"A positive sign means that the Flexible Load can increase its power consumption. Negative Power States represent a possible decrease in power consumption. Uncertainty can be represented by specifying a range."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAZ820#001"),
                                }

                            def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power State"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"A power state with which the Flexible Load can run during the corresponding holding periods. "
                                    }
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerState",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(
                            self,
                            power: Union[Tuple[xsd.Float, xsd.Float], Power],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if power is not None and not isinstance(power, aas.SubmodelElement):
                                power = self.Power(min=power[0], max=power[1])

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(power)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"powerStates",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power States"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"a set of Power States with which the Flexible Load can run during each of the (number of changes + 1) holding periods. "
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerStates",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(
                        self,
                        powerstates_items: Iterable[Powerstates_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(powerstates_items, str):
                            raise TypeError("powerstates_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(powerstates_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r" Each flexibleLoad describes the energy flexibility of a technical system (i.e. controllable unit) or a combination of systems (i.e. an ensemble of controllable units) that can adjust its power consumption or generation in response to external conditions or requirements. It focuses on the limitations and possibilities (degrees of freedom) of changing power outputs of a technical system."
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoad",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    flexibleLoadId: Union[str, FlexibleLoadId],
                    reactionDuration: Union[Tuple[xsd.Float, xsd.Float], ReactionDuration],
                    regenerationDuration: Union[xsd.Float, RegenerationDuration],
                    powerStates: Union[Iterable[PowerStates.Powerstates_item], PowerStates],
                    powerGradients: Optional[PowerGradients] = None,
                    modulationNumber: Optional[
                        Union[Tuple[xsd.NonNegativeInteger, xsd.NonNegativeInteger], ModulationNumber]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if flexibleLoadId is not None and not isinstance(flexibleLoadId, aas.SubmodelElement):
                        flexibleLoadId = self.FlexibleLoadId(flexibleLoadId)

                    # Build a submodel element if a raw value was passed in the argument

                    if reactionDuration is not None and not isinstance(reactionDuration, aas.SubmodelElement):
                        reactionDuration = self.ReactionDuration(min=reactionDuration[0], max=reactionDuration[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if regenerationDuration is not None and not isinstance(regenerationDuration, aas.SubmodelElement):
                        regenerationDuration = self.RegenerationDuration(regenerationDuration)

                    # Build a submodel element if a raw value was passed in the argument

                    if modulationNumber is not None and not isinstance(modulationNumber, aas.SubmodelElement):
                        modulationNumber = self.ModulationNumber(min=modulationNumber[0], max=modulationNumber[1])

                    # A str would be split into its characters
                    if isinstance(powerStates, str):
                        raise TypeError("powerStates takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if powerStates is not None and not isinstance(powerStates, aas.SubmodelElement):
                        powerStates = self.PowerStates(powerStates)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        flexibleLoadId,
                        reactionDuration,
                        regenerationDuration,
                        powerGradients,
                        modulationNumber,
                        powerStates,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"flexibleLoads",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Loads"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"flexibleLoads may contain multiple flexibleLoad."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoads"
                    ),
                }

            def __init__(
                self, flexibleloads_items: Iterable[Flexibleloads_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(flexibleloads_items, str):
                    raise TypeError("flexibleloads_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(flexibleloads_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Storages(GeneratedSubmodelElementList):

            class Storages_item(aas.SubmodelElementCollection):

                class StorageId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"storageId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of a storage for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class UsableCapacity(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"usableCapacity",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Usable Capacity"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Lower and upper limit of the storage energy content. These limits must never be exceeded or fallen short of. Depending on the choice of reference point, it is also possible to specify negative storage capacities, e.g. if it needs to be possible to either exceed or fall below storage limits."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class InitialEnergyContent(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"initialEnergyContent",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Initial Energy Content"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Energy content of the storage at the start time of the Validity Period of the associated Flexible Load (Suppliers). If the storage is connected to several Flexible Loads, the Initial Energy Content refers to the earliest start time of the Validity Periods of all Flexible Loads. If the initial energy content cannot be quantified exactly, the predicted range can be specified via min and max."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/ElectricalEnergyStorageContent"
                            ),
                        }

                    def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class EnergyLoss(aas.Property):

                    ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.UnsignedShort), xsd.from_xsd(r"100", xsd.UnsignedShort))

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"energyLoss",
                            "value_type": xsd.UnsignedShort,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Energy Loss"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Proportion of the energy content that is continuously lost, e.g. through exchange with the environment. The percentage refers to the actual energy content and not to the storage capacity."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/EnergyContentLossPerHour"
                            ),
                        }

                    def __init__(self, value: xsd.UnsignedShort, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and (
                            value < self.ALLOWED_RANGE[0]
                            or self.ALLOWED_RANGE[1] is not None
                            and value > self.ALLOWED_RANGE[1]
                        ):
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Suppliers(GeneratedSubmodelElementList):

                    class Suppliers_item(aas.SubmodelElementCollection):

                        class FlexibleLoadId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"flexibleLoadId",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load ID"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"This ID identifies the Flexible Load supplying the storage. The ID of a Flexible Load for unique identification. The Universally Unique Identifier (UUID) is generated automatically and is used for identification and assignment within an IT system in a company and for further processing by external, market-side services."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ConversionEfficiency(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"conversionEfficiency",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Conversion Efficiency"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Energy conversion efficiency of the suppiler"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/EnergyConversionEfficiency"
                                    ),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Supplier"}),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Indicating a single supply"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/supplier"
                                ),
                            }

                        def __init__(
                            self,
                            flexibleLoadId: Union[str, FlexibleLoadId],
                            conversionEfficiency: Optional[Union[xsd.Float, ConversionEfficiency]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if flexibleLoadId is not None and not isinstance(flexibleLoadId, aas.SubmodelElement):
                                flexibleLoadId = self.FlexibleLoadId(flexibleLoadId)

                            # Build a submodel element if a raw value was passed in the argument

                            if conversionEfficiency is not None and not isinstance(
                                conversionEfficiency, aas.SubmodelElement
                            ):
                                conversionEfficiency = self.ConversionEfficiency(conversionEfficiency)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(flexibleLoadId, conversionEfficiency)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"suppliers",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Suppliers"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"One or more Flexible Loads supplying the storage. The Flexible Loads must be defined in the same Flexibility Space. The conversion efficiency is specified for each supply system."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/suppliers"
                            ),
                        }

                    def __init__(
                        self, suppliers_items: Iterable[Suppliers_item], **kwargs: Unpack[SubmodelElementListMetadata]
                    ):

                        # A str would be split into its characters
                        if isinstance(suppliers_items, str):
                            raise TypeError("suppliers_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(suppliers_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storage"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A storage represents a technical system or a combination of systems that has the potential to store energy"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storage",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(
                    self,
                    storageId: Union[str, StorageId],
                    usableCapacity: Union[Tuple[xsd.Float, xsd.Float], UsableCapacity],
                    initialEnergyContent: Optional[Union[Tuple[xsd.Float, xsd.Float], InitialEnergyContent]] = None,
                    energyLoss: Optional[Union[xsd.UnsignedShort, EnergyLoss]] = None,
                    suppliers: Optional[Union[Iterable[Suppliers.Suppliers_item], Suppliers]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if storageId is not None and not isinstance(storageId, aas.SubmodelElement):
                        storageId = self.StorageId(storageId)

                    # Build a submodel element if a raw value was passed in the argument

                    if usableCapacity is not None and not isinstance(usableCapacity, aas.SubmodelElement):
                        usableCapacity = self.UsableCapacity(min=usableCapacity[0], max=usableCapacity[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if initialEnergyContent is not None and not isinstance(initialEnergyContent, aas.SubmodelElement):
                        initialEnergyContent = self.InitialEnergyContent(
                            min=initialEnergyContent[0], max=initialEnergyContent[1]
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if energyLoss is not None and not isinstance(energyLoss, aas.SubmodelElement):
                        energyLoss = self.EnergyLoss(energyLoss)

                    # A str would be split into its characters
                    if isinstance(suppliers, str):
                        raise TypeError("suppliers takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if suppliers is not None and not isinstance(suppliers, aas.SubmodelElement):
                        suppliers = self.Suppliers(suppliers)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        storageId, usableCapacity, initialEnergyContent, energyLoss, suppliers
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"storages",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Storages"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Storages may contain multiple storages, each of which represents a technical system or a combination of systems that has the potential to store energy"
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/storages",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(self, storages_items: Iterable[Storages_item], **kwargs: Unpack[SubmodelElementListMetadata]):

                # A str would be split into its characters
                if isinstance(storages_items, str):
                    raise TypeError("storages_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(storages_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"flexibilitySpace_generalTechnicalPotential",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Flexibility Space General Technical Potential"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"This SMC describes the degrees of freedom of an energy-flexible system based solely on its general technical characteristics. It focuses on the inherent flexibility potential of the system, independent of any operational strategies, specific conditions, or application-related constraints."
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibilitySpace_generalTechnicalPotential"
                ),
            }

        def __init__(
            self,
            metadata: Metadata,
            utilizationContext: UtilizationContext,
            flexibleLoads: Union[Iterable[FlexibleLoads.Flexibleloads_item], FlexibleLoads],
            storages: Optional[Union[Iterable[Storages.Storages_item], Storages]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(flexibleLoads, str):
                raise TypeError("flexibleLoads takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if flexibleLoads is not None and not isinstance(flexibleLoads, aas.SubmodelElement):
                flexibleLoads = self.FlexibleLoads(flexibleLoads)

            # A str would be split into its characters
            if isinstance(storages, str):
                raise TypeError("storages takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if storages is not None and not isinstance(storages, aas.SubmodelElement):
                storages = self.Storages(storages)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                metadata, utilizationContext, flexibleLoads, storages
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FlexibleLoadMeasureExecutionLog(aas.SubmodelElementCollection):

        class Metadata(aas.SubmodelElementCollection):

            class InstanceId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"instanceId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Instance ID"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The ID of a Flexibility Space or Flexible-Load Measure Package for unique identification"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Comment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"comment",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Comment"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Free text to comment the EFDM object."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/comment"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EfdmVersion(aas.SubmodelElementCollection):

                class VersionNumber(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"versionNumber",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Version Number"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"the EFDM version (e.g. 0.3)"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/versionNumber"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SchemaLink(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"schemaLink",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Schema Link"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"hyperlink to the corresponding scheme"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/schemaLink"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"efdmVersion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"EFDM Version"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Specification of the EFDM version and hyperlink to the corresponding scheme."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/efdmVersion"
                        ),
                    }

                def __init__(
                    self,
                    versionNumber: Union[str, VersionNumber],
                    schemaLink: Union[str, SchemaLink],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if versionNumber is not None and not isinstance(versionNumber, aas.SubmodelElement):
                        versionNumber = self.VersionNumber(versionNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if schemaLink is not None and not isinstance(schemaLink, aas.SubmodelElement):
                        schemaLink = self.SchemaLink(schemaLink)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(versionNumber, schemaLink)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Origin(aas.SubmodelElementCollection):

                class OriginId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"originId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the creating service and point in time of creation"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"timestamp of the creating service"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"origin",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the creating service and point in time of creation. By means of the automated filling in of the Element, conclusions about the origin and an allocation to executing agencies are made possible. In the case of communication with external services, this Element is replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/origin"),
                    }

                def __init__(
                    self,
                    originId: Union[str, OriginId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if originId is not None and not isinstance(originId, aas.SubmodelElement):
                        originId = self.OriginId(originId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(originId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Modification(aas.SubmodelElementCollection):

                class ModificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"modificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"UUID of the service instance that last processed this object "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Timestamp(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"timestamp",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"timestamp of of last processing"}),
                            "semantic_id": aas.ModelReference(
                                key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"),),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"modification",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modification"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Containing UUID of the service instance that last processed this object and point in time of last processing. In the case of communication with external services, this Element can be replaced by an ID that is intended for external communication."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/modification"
                        ),
                    }

                def __init__(
                    self,
                    modificationId: Union[str, ModificationId],
                    timestamp: Union[xsd.DateTime, Timestamp],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if modificationId is not None and not isinstance(modificationId, aas.SubmodelElement):
                        modificationId = self.ModificationId(modificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                        timestamp = self.Timestamp(timestamp)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(modificationId, timestamp)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"metadata",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Metadata"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The metadata provides essential information for tracking and tracing of the model instances."
                        }
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/metadata",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(
                self,
                instanceId: Union[str, InstanceId],
                efdmVersion: EfdmVersion,
                origin: Origin,
                modification: Modification,
                comment: Optional[Union[aas.LangStringSet, Comment]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if instanceId is not None and not isinstance(instanceId, aas.SubmodelElement):
                    instanceId = self.InstanceId(instanceId)

                # Build a submodel element if a raw value was passed in the argument

                if comment is not None and not isinstance(comment, aas.SubmodelElement):
                    comment = self.Comment(comment)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    instanceId, comment, efdmVersion, origin, modification
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ExecutionLogEntries(GeneratedSubmodelElementList):

            class Executionlogentries_item(aas.SubmodelElementCollection):

                class FlexibleLoadMeasureId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"flexibleLoadMeasureId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Measure ID"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The ID of the Flexible-Load Measure for which the log entry is created."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/UUID"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Reward(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"reward",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reward"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Realized revenue from implementing the Flexible-Load Measure. The sign indicates the direction of the cash flow, while the referencePoint specifies whether the value represents a cost saving or the total amount."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/reward"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Exceptions(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"exceptions",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Exceptions"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Error objects that occurred during the execution of the Flexible-Load Measure."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/exceptions"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LoadChangeProfiles(GeneratedSubmodelElementList):

                    class Loadchangeprofiles_item(aas.SubmodelElementCollection):

                        class Power(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"power",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Power"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Positive power states mean that the Flexible-Load Measure requests an increase in power consumption from the Flexible Load. Negative power states require a decrease in power consumption. Interpolation between Power States is linear; a step change in power can be mapped by specifying two equal timestamps with different power values."
                                        }
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-AAZ820#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Timestamp(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"timestamp",
                                    "value_type": xsd.DateTime,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Timestamp"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"timestamp of a power state"}
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABF198#001"
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ReferencePoint(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": r"referencePoint",
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reference Point"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Refers to the associated Flexible-Load Measure as planed value"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/referencePoint"
                                    ),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Load Change Profile"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"A single Load profile that records the actual power reduction or increase of the Flexible load during execution. "
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/powerState"
                                ),
                            }

                        def __init__(
                            self,
                            power: Union[xsd.Float, Power],
                            timestamp: Union[xsd.DateTime, Timestamp],
                            referencePoint: Union[aas.Reference, ReferencePoint],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if power is not None and not isinstance(power, aas.SubmodelElement):
                                power = self.Power(power)

                            # Build a submodel element if a raw value was passed in the argument

                            if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                                timestamp = self.Timestamp(timestamp)

                            # Build a submodel element if a raw value was passed in the argument

                            if referencePoint is not None and not isinstance(referencePoint, aas.SubmodelElement):
                                referencePoint = self.ReferencePoint(referencePoint)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(power, timestamp, referencePoint)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"loadChangeProfiles",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Load Change Profiles"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Load profiles that record the actual power reduction or increase of the Flexible load during execution. The Power values are refer to the same referencePoint as the associated Flexible-Load Measure."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/loadChangeProfiles"
                            ),
                        }

                    def __init__(
                        self,
                        loadchangeprofiles_items: Iterable[Loadchangeprofiles_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(loadchangeprofiles_items, str):
                            raise TypeError("loadchangeprofiles_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            loadchangeprofiles_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Execution Log Entry"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Each executionLogEntry describes an implemented flexibleLoadMeasure."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/executionLogEntry00"
                        ),
                    }

                def __init__(
                    self,
                    flexibleLoadMeasureId: Union[str, FlexibleLoadMeasureId],
                    loadChangeProfiles: Union[Iterable[LoadChangeProfiles.Loadchangeprofiles_item], LoadChangeProfiles],
                    reward: Optional[Union[str, Reward]] = None,
                    exceptions: Optional[Union[str, Exceptions]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if flexibleLoadMeasureId is not None and not isinstance(flexibleLoadMeasureId, aas.SubmodelElement):
                        flexibleLoadMeasureId = self.FlexibleLoadMeasureId(flexibleLoadMeasureId)

                    # Build a submodel element if a raw value was passed in the argument

                    if reward is not None and not isinstance(reward, aas.SubmodelElement):
                        reward = self.Reward(reward)

                    # Build a submodel element if a raw value was passed in the argument

                    if exceptions is not None and not isinstance(exceptions, aas.SubmodelElement):
                        exceptions = self.Exceptions(exceptions)

                    # A str would be split into its characters
                    if isinstance(loadChangeProfiles, str):
                        raise TypeError("loadChangeProfiles takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if loadChangeProfiles is not None and not isinstance(loadChangeProfiles, aas.SubmodelElement):
                        loadChangeProfiles = self.LoadChangeProfiles(loadChangeProfiles)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        flexibleLoadMeasureId, reward, exceptions, loadChangeProfiles
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"executionLogEntries",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Execution Log Entries"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"executionLogEntries contains one or more executionLogEntry, each of which describes an implemented flexibleLoadMeasure."
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/executionLogEntries"
                    ),
                }

            def __init__(
                self,
                executionlogentries_items: Iterable[Executionlogentries_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(executionlogentries_items, str):
                    raise TypeError("executionlogentries_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(executionlogentries_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"flexibleLoadMeasureExecutionLog",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Flexible Load Measure Execution Log"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The flexibleLoadMeasureExecutionLog contains one or more Execution Log-Entry that records an implemented flexible load measure."
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/EnergyFlexibilityDataModel/1/0/flexibleLoadMeasureExecutionLog"
                ),
            }

        def __init__(
            self,
            metadata: Metadata,
            executionLogEntries: Union[Iterable[ExecutionLogEntries.Executionlogentries_item], ExecutionLogEntries],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(executionLogEntries, str):
                raise TypeError("executionLogEntries takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if executionLogEntries is not None and not isinstance(executionLogEntries, aas.SubmodelElement):
                executionLogEntries = self.ExecutionLogEntries(executionLogEntries)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(metadata, executionLogEntries)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"EnergyFlexibilityDataModel",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel Energy Flexibility Data Model (EFDM) provides a unified framework for describing energy flexibility"
                }
            ),
        }

    def __init__(
        self,
        id_: str,
        flexibleLoadMeasuresPackage: Optional[FlexibleLoadMeasuresPackage] = None,
        flexibilitySpace_operationalPotential: Optional[FlexibilitySpace_operationalPotential] = None,
        flexibilitySpace_applicationTailoredPotential: Optional[FlexibilitySpace_applicationTailoredPotential] = None,
        flexibilitySpace_generalTechnicalPotential: Optional[FlexibilitySpace_generalTechnicalPotential] = None,
        flexibleLoadMeasureExecutionLog: Optional[FlexibleLoadMeasureExecutionLog] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            flexibleLoadMeasuresPackage,
            flexibilitySpace_operationalPotential,
            flexibilitySpace_applicationTailoredPotential,
            flexibilitySpace_generalTechnicalPotential,
            flexibleLoadMeasureExecutionLog,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
