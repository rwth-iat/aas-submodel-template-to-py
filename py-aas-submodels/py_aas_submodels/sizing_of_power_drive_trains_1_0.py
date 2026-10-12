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


class EntityMetadata(TypedDict, total=False):
    """Metadata of aas.Entity, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    entity_type: Optional[aas.EntityType]
    global_asset_id: Optional[str]
    specific_asset_id: Iterable[aas.SpecificAssetId]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class FileMetadata(TypedDict, total=False):
    """Metadata of aas.File, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


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


class PowerDriveTrainSizing(aas.Submodel):

    class SizingProjectInformation(aas.SubmodelElementCollection):

        class ClientName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ClientName",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/ClientName/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SizingProjectName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SizingProjectName",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectName/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SizingProjectAxisReference(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SizingProjectAxisReference",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectAxisReference/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SizingProjectDescription(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"SizingProjectDescription",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectDescription/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SizingProjectLink(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"SizingProjectLink",
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectLink/1/0"
                    ),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"text/xml", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class SizingToolName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SizingToolName",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingToolName/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DateCreated(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DateCreated",
                    "value_type": xsd.DateTime,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/DateCreated/1/0"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DateChanged(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DateChanged",
                    "value_type": xsd.DateTime,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/DateChanged/1/0"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ContactInformation(aas.SubmodelElementCollection):

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ContactInformation",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation"
                    ),
                }

            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class AmlDriveConfigVersion(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AmlDriveConfigVersion",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmlDriveConfigVersion/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SizingProjectInformation",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Auslegungsprojektinformationen", r"en": r"Sizing project information"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectInformation1/0"
                ),
            }

        def __init__(
            self,
            clientName: Union[str, ClientName],
            sizingProjectName: Union[str, SizingProjectName],
            sizingProjectLink: Iterable[SizingProjectLink],
            sizingToolName: Union[str, SizingToolName],
            dateCreated: Union[xsd.DateTime, DateCreated],
            dateChanged: Union[xsd.DateTime, DateChanged],
            contactInformation: Iterable[ContactInformation],
            sizingProjectAxisReference: Optional[Union[str, SizingProjectAxisReference]] = None,
            sizingProjectDescription: Optional[Union[aas.MultiLanguageTextType, SizingProjectDescription]] = None,
            amlDriveConfigVersion: Optional[Union[str, AmlDriveConfigVersion]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if clientName is not None and not isinstance(clientName, aas.SubmodelElement):
                clientName = self.ClientName(clientName)

            # Build a submodel element if a raw value was passed in the argument

            if sizingProjectName is not None and not isinstance(sizingProjectName, aas.SubmodelElement):
                sizingProjectName = self.SizingProjectName(sizingProjectName)

            # Build a submodel element if a raw value was passed in the argument

            if sizingProjectAxisReference is not None and not isinstance(
                sizingProjectAxisReference, aas.SubmodelElement
            ):
                sizingProjectAxisReference = self.SizingProjectAxisReference(sizingProjectAxisReference)

            # Build a submodel element if a raw value was passed in the argument

            if sizingProjectDescription is not None and not isinstance(sizingProjectDescription, aas.SubmodelElement):
                sizingProjectDescription = self.SizingProjectDescription(sizingProjectDescription)

            # A str would be split into its characters
            if isinstance(sizingProjectLink, str):
                raise TypeError("sizingProjectLink takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if sizingToolName is not None and not isinstance(sizingToolName, aas.SubmodelElement):
                sizingToolName = self.SizingToolName(sizingToolName)

            # Build a submodel element if a raw value was passed in the argument

            if dateCreated is not None and not isinstance(dateCreated, aas.SubmodelElement):
                dateCreated = self.DateCreated(dateCreated)

            # Build a submodel element if a raw value was passed in the argument

            if dateChanged is not None and not isinstance(dateChanged, aas.SubmodelElement):
                dateChanged = self.DateChanged(dateChanged)

            # A str would be split into its characters
            if isinstance(contactInformation, str):
                raise TypeError("contactInformation takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if amlDriveConfigVersion is not None and not isinstance(amlDriveConfigVersion, aas.SubmodelElement):
                amlDriveConfigVersion = self.AmlDriveConfigVersion(amlDriveConfigVersion)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                clientName,
                sizingProjectName,
                sizingProjectAxisReference,
                sizingProjectDescription,
                sizingProjectLink,
                sizingToolName,
                dateCreated,
                dateChanged,
                contactInformation,
                amlDriveConfigVersion,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ApplicationRequirements(aas.SubmodelElementCollection):

        class MotionPattern(aas.SubmodelElementCollection):

            class MotionPatternName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MotionPatternName",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPatternName/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MotionPatternSections(aas.SubmodelElementCollection):

                class RotativeSection(aas.SubmodelElementCollection):

                    class FrictionTorque(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"FrictionTorque",
                                "value_type": xsd.Long,
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionTorque/1/0"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class LeverArmAxialForce(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"LeverArmAxialForce",
                                "value_type": xsd.Long,
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class AxialForce(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"AxialForce",
                                "value_type": xsd.Long,
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/AxialForce/1/0"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class LeverArmRadialForce(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"LeverArmRadialForce",
                                "value_type": xsd.Long,
                                "category": r"CONSTANT",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class RadialForce(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"RadialForce",
                                "value_type": xsd.Long,
                                "category": r"CONSTANT",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/RadialForce/1/0"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class MomentOfInertiaOfLoad(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"MomentOfInertiaOfLoad",
                                "value_type": xsd.Long,
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/MomentOfInertiaOfLoad/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class LoadTorque(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"LoadTorque",
                                "value_type": xsd.Long,
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadTorque/1/0"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class MetadataRotativeMotionFile(aas.SubmodelElementCollection):

                        class Time(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Time",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class AngularPosition(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"AngularPosition",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularPosition/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class AngularVelocity(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"AngularVelocity",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularVelocity/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class AngularAcceleration(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"AngularAcceleration",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularAcceleration/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class AngularJerk(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"AngularJerk",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularJerk/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FrictionTorque(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"FrictionTorque",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionTorque/1/0"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class AxialForce(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"AxialForce",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/AxialForce/1/0"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class RadialForce(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"RadialForce",
                                    "value_type": xsd.Long,
                                    "category": r"CONSTANT",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/RadialForce/1/0"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class LoadTorque(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"LoadTorque",
                                    "value_type": xsd.Long,
                                    "category": r"CONSTANT",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadTorque/1/0"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"MetadataRotativeMotionFile",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/MetadataRotativeMotionFile/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            time: Union[xsd.Long, Time],
                            angularPosition: Union[xsd.Long, AngularPosition],
                            angularVelocity: Union[xsd.Long, AngularVelocity],
                            angularAcceleration: Union[xsd.Long, AngularAcceleration],
                            angularJerk: Optional[Union[xsd.Long, AngularJerk]] = None,
                            frictionTorque: Optional[Union[xsd.Long, FrictionTorque]] = None,
                            axialForce: Optional[Union[xsd.Long, AxialForce]] = None,
                            radialForce: Optional[Union[xsd.Long, RadialForce]] = None,
                            loadTorque: Optional[Union[xsd.Long, LoadTorque]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if time is not None and not isinstance(time, aas.SubmodelElement):
                                time = self.Time(time)

                            # Build a submodel element if a raw value was passed in the argument

                            if angularPosition is not None and not isinstance(angularPosition, aas.SubmodelElement):
                                angularPosition = self.AngularPosition(angularPosition)

                            # Build a submodel element if a raw value was passed in the argument

                            if angularVelocity is not None and not isinstance(angularVelocity, aas.SubmodelElement):
                                angularVelocity = self.AngularVelocity(angularVelocity)

                            # Build a submodel element if a raw value was passed in the argument

                            if angularAcceleration is not None and not isinstance(
                                angularAcceleration, aas.SubmodelElement
                            ):
                                angularAcceleration = self.AngularAcceleration(angularAcceleration)

                            # Build a submodel element if a raw value was passed in the argument

                            if angularJerk is not None and not isinstance(angularJerk, aas.SubmodelElement):
                                angularJerk = self.AngularJerk(angularJerk)

                            # Build a submodel element if a raw value was passed in the argument

                            if frictionTorque is not None and not isinstance(frictionTorque, aas.SubmodelElement):
                                frictionTorque = self.FrictionTorque(frictionTorque)

                            # Build a submodel element if a raw value was passed in the argument

                            if axialForce is not None and not isinstance(axialForce, aas.SubmodelElement):
                                axialForce = self.AxialForce(axialForce)

                            # Build a submodel element if a raw value was passed in the argument

                            if radialForce is not None and not isinstance(radialForce, aas.SubmodelElement):
                                radialForce = self.RadialForce(radialForce)

                            # Build a submodel element if a raw value was passed in the argument

                            if loadTorque is not None and not isinstance(loadTorque, aas.SubmodelElement):
                                loadTorque = self.LoadTorque(loadTorque)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                time,
                                angularPosition,
                                angularVelocity,
                                angularAcceleration,
                                angularJerk,
                                frictionTorque,
                                axialForce,
                                radialForce,
                                loadTorque,
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class MotionSectionFile(aas.File):

                        @staticmethod
                        def template_defaults() -> FileMetadata:
                            return {
                                "id_short": r"MotionSectionFile",
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionSectionFile/1/0"
                                ),
                            }

                        def __init__(
                            self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                        ):

                            super().__init__(
                                value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                            )

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"RotativeSection",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PowerDriveTrainSizing/RotativeMotionPatternSection/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        metadataRotativeMotionFile: MetadataRotativeMotionFile,
                        frictionTorque: Optional[Union[xsd.Long, FrictionTorque]] = None,
                        leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                        axialForce: Optional[Union[xsd.Long, AxialForce]] = None,
                        leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                        radialForce: Optional[Union[xsd.Long, RadialForce]] = None,
                        momentOfInertiaOfLoad: Optional[Union[xsd.Long, MomentOfInertiaOfLoad]] = None,
                        loadTorque: Optional[Union[xsd.Long, LoadTorque]] = None,
                        motionSectionFile: Optional[MotionSectionFile] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if frictionTorque is not None and not isinstance(frictionTorque, aas.SubmodelElement):
                            frictionTorque = self.FrictionTorque(frictionTorque)

                        # Build a submodel element if a raw value was passed in the argument

                        if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                            leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if axialForce is not None and not isinstance(axialForce, aas.SubmodelElement):
                            axialForce = self.AxialForce(axialForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                            leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if radialForce is not None and not isinstance(radialForce, aas.SubmodelElement):
                            radialForce = self.RadialForce(radialForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if momentOfInertiaOfLoad is not None and not isinstance(
                            momentOfInertiaOfLoad, aas.SubmodelElement
                        ):
                            momentOfInertiaOfLoad = self.MomentOfInertiaOfLoad(momentOfInertiaOfLoad)

                        # Build a submodel element if a raw value was passed in the argument

                        if loadTorque is not None and not isinstance(loadTorque, aas.SubmodelElement):
                            loadTorque = self.LoadTorque(loadTorque)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            frictionTorque,
                            leverArmAxialForce,
                            axialForce,
                            leverArmRadialForce,
                            radialForce,
                            momentOfInertiaOfLoad,
                            loadTorque,
                            metadataRotativeMotionFile,
                            motionSectionFile,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class LinearSection(aas.SubmodelElementCollection):

                    class FrictionCoefficient(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"FrictionCoefficient",
                                "value_type": xsd.Long,
                                "category": r"CONSTANT",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FrictionForce(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"FrictionForce",
                                "value_type": xsd.Long,
                                "category": r"CONSTANT",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionForce/1/0"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CompensationForce(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"CompensationForce",
                                "value_type": xsd.Long,
                                "category": r"CONSTANT",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/CompensationForce/1/0"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class LoadMass(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"LoadMass",
                                "value_type": xsd.Long,
                                "category": r"CONSTANT",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadMass/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class LoadSideForce(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"LoadSideForce",
                                "value_type": xsd.Long,
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadSideForce/1/0"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CounterMass(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"CounterMass",
                                "value_type": xsd.Long,
                                "category": r"CONSTANT",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/CounterMass/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class MetadataLinearMotionFile(aas.SubmodelElementCollection):

                        class Time(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Time",
                                    "value_type": xsd.Long,
                                    "category": r"VARIABLE",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Position(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Position",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/Position/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class LinearVelocity(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"LinearVelocity",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearVelocity/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class LinearAcceleration(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"LinearAcceleration",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearAcceleration/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class LinearJerk(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"LinearJerk",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearJerk/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FrictionForce(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"FrictionForce",
                                    "value_type": xsd.Long,
                                    "category": r"CONSTANT",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionForce/1/0"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class LoadSideForce(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"LoadSideForce",
                                    "value_type": xsd.Long,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadSideForce/1/0"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"MetadataLinearMotionFile",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/MetadataLinearMotionFile/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            time: Union[xsd.Long, Time],
                            position: Union[xsd.Long, Position],
                            linearVelocity: Union[xsd.Long, LinearVelocity],
                            linearAcceleration: Union[xsd.Long, LinearAcceleration],
                            linearJerk: Optional[Union[xsd.Long, LinearJerk]] = None,
                            frictionForce: Optional[Union[xsd.Long, FrictionForce]] = None,
                            loadSideForce: Optional[Union[xsd.Long, LoadSideForce]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if time is not None and not isinstance(time, aas.SubmodelElement):
                                time = self.Time(time)

                            # Build a submodel element if a raw value was passed in the argument

                            if position is not None and not isinstance(position, aas.SubmodelElement):
                                position = self.Position(position)

                            # Build a submodel element if a raw value was passed in the argument

                            if linearVelocity is not None and not isinstance(linearVelocity, aas.SubmodelElement):
                                linearVelocity = self.LinearVelocity(linearVelocity)

                            # Build a submodel element if a raw value was passed in the argument

                            if linearAcceleration is not None and not isinstance(
                                linearAcceleration, aas.SubmodelElement
                            ):
                                linearAcceleration = self.LinearAcceleration(linearAcceleration)

                            # Build a submodel element if a raw value was passed in the argument

                            if linearJerk is not None and not isinstance(linearJerk, aas.SubmodelElement):
                                linearJerk = self.LinearJerk(linearJerk)

                            # Build a submodel element if a raw value was passed in the argument

                            if frictionForce is not None and not isinstance(frictionForce, aas.SubmodelElement):
                                frictionForce = self.FrictionForce(frictionForce)

                            # Build a submodel element if a raw value was passed in the argument

                            if loadSideForce is not None and not isinstance(loadSideForce, aas.SubmodelElement):
                                loadSideForce = self.LoadSideForce(loadSideForce)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                time,
                                position,
                                linearVelocity,
                                linearAcceleration,
                                linearJerk,
                                frictionForce,
                                loadSideForce,
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class MotionSectionFile(aas.File):

                        @staticmethod
                        def template_defaults() -> FileMetadata:
                            return {
                                "id_short": r"MotionSectionFile",
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionSectionFile/1/0"
                                ),
                            }

                        def __init__(
                            self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                        ):

                            super().__init__(
                                value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                            )

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"LinearSection",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearMotionPatternSection/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        metadataLinearMotionFile: MetadataLinearMotionFile,
                        frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                        frictionForce: Optional[Union[xsd.Long, FrictionForce]] = None,
                        compensationForce: Optional[Union[xsd.Long, CompensationForce]] = None,
                        loadMass: Optional[Union[xsd.Long, LoadMass]] = None,
                        loadSideForce: Optional[Union[xsd.Long, LoadSideForce]] = None,
                        counterMass: Optional[Union[xsd.Long, CounterMass]] = None,
                        motionSectionFile: Optional[MotionSectionFile] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                            frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                        # Build a submodel element if a raw value was passed in the argument

                        if frictionForce is not None and not isinstance(frictionForce, aas.SubmodelElement):
                            frictionForce = self.FrictionForce(frictionForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if compensationForce is not None and not isinstance(compensationForce, aas.SubmodelElement):
                            compensationForce = self.CompensationForce(compensationForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if loadMass is not None and not isinstance(loadMass, aas.SubmodelElement):
                            loadMass = self.LoadMass(loadMass)

                        # Build a submodel element if a raw value was passed in the argument

                        if loadSideForce is not None and not isinstance(loadSideForce, aas.SubmodelElement):
                            loadSideForce = self.LoadSideForce(loadSideForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if counterMass is not None and not isinstance(counterMass, aas.SubmodelElement):
                            counterMass = self.CounterMass(counterMass)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            frictionCoefficient,
                            frictionForce,
                            compensationForce,
                            loadMass,
                            loadSideForce,
                            counterMass,
                            metadataLinearMotionFile,
                            motionSectionFile,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MotionPatternSections",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPatternSections/1/0"
                        ),
                    }

                def __init__(
                    self,
                    rotativeSection: Optional[Iterable[RotativeSection]] = None,
                    linearSection: Optional[Iterable[LinearSection]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(rotativeSection, str):
                        raise TypeError("rotativeSection takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(linearSection, str):
                        raise TypeError("linearSection takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(rotativeSection, linearSection)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"MotionPattern",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPattern/1/0"),
                }

            def __init__(
                self,
                motionPatternSections: MotionPatternSections,
                motionPatternName: Optional[Union[str, MotionPatternName]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if motionPatternName is not None and not isinstance(motionPatternName, aas.SubmodelElement):
                    motionPatternName = self.MotionPatternName(motionPatternName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(motionPatternName, motionPatternSections)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Environmental(aas.SubmodelElementCollection):

            class InstallationAltitude(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InstallationAltitude",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAZ614#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Atex2Gas(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Atex2Gas",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAR865#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Atex2Dust(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Atex2Dust",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAR866#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AmbientTemperatureController(aas.Range):

                @staticmethod
                def template_defaults() -> RangeMetadata:
                    return {
                        "id_short": r"AmbientTemperatureController",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmbientTemperatureController/1/0"
                        ),
                    }

                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

            class AmbientTemperatureMotor(aas.Range):

                @staticmethod
                def template_defaults() -> RangeMetadata:
                    return {
                        "id_short": r"AmbientTemperatureMotor",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmbientTemperatureMotor/1/0"
                        ),
                    }

                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Environmental",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnvironmentalRequirements/1/0"
                    ),
                }

            def __init__(
                self,
                installationAltitude: Optional[Union[str, InstallationAltitude]] = None,
                atex2Gas: Optional[Union[str, Atex2Gas]] = None,
                atex2Dust: Optional[Union[str, Atex2Dust]] = None,
                ambientTemperatureController: Optional[Union[Tuple[str, str], AmbientTemperatureController]] = None,
                ambientTemperatureMotor: Optional[Union[Tuple[str, str], AmbientTemperatureMotor]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if installationAltitude is not None and not isinstance(installationAltitude, aas.SubmodelElement):
                    installationAltitude = self.InstallationAltitude(installationAltitude)

                # Build a submodel element if a raw value was passed in the argument

                if atex2Gas is not None and not isinstance(atex2Gas, aas.SubmodelElement):
                    atex2Gas = self.Atex2Gas(atex2Gas)

                # Build a submodel element if a raw value was passed in the argument

                if atex2Dust is not None and not isinstance(atex2Dust, aas.SubmodelElement):
                    atex2Dust = self.Atex2Dust(atex2Dust)

                # Build a submodel element if a raw value was passed in the argument

                if ambientTemperatureController is not None and not isinstance(
                    ambientTemperatureController, aas.SubmodelElement
                ):
                    ambientTemperatureController = self.AmbientTemperatureController(
                        min=ambientTemperatureController[0], max=ambientTemperatureController[1]
                    )

                # Build a submodel element if a raw value was passed in the argument

                if ambientTemperatureMotor is not None and not isinstance(ambientTemperatureMotor, aas.SubmodelElement):
                    ambientTemperatureMotor = self.AmbientTemperatureMotor(
                        min=ambientTemperatureMotor[0], max=ambientTemperatureMotor[1]
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    installationAltitude, atex2Gas, atex2Dust, ambientTemperatureController, ambientTemperatureMotor
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class OverallSystemRequirements(aas.SubmodelElementCollection):

            class DcLinkCoupling(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DcLinkCoupling",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/DcLinkCoupling/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BrakePresent(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BrakePresent",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-BAE085#007"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MainsConnection(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MainsConnection",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABF822#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MountingType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MountingType",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAH167#006"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MinSwitchingFrequency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MinSwitchingFrequency",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAN329#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CoolingType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CoolingType",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-BAE122#007"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProtectionType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProtectionType",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-BAG342#007"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CertificateApproval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CertificateApproval",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Zertifikat/Zulassung", r"en": r"Certificate/Approval"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-BAB392#018"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SafetyIntegrityLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SafetyIntegrityLevel",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"safety integrity level (SIL) according to IEC 61508"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABH715#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"OverallSystemRequirements",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PowerDriveTrainSizing/OverallSystemRequirements/1/0"
                    ),
                }

            def __init__(
                self,
                dcLinkCoupling: Optional[Union[str, DcLinkCoupling]] = None,
                brakePresent: Optional[Union[str, BrakePresent]] = None,
                mainsConnection: Optional[Union[str, MainsConnection]] = None,
                mountingType: Optional[Union[str, MountingType]] = None,
                minSwitchingFrequency: Optional[Union[str, MinSwitchingFrequency]] = None,
                coolingType: Optional[Union[str, CoolingType]] = None,
                protectionType: Optional[Union[str, ProtectionType]] = None,
                certificateApproval: Optional[Union[str, CertificateApproval]] = None,
                safetyIntegrityLevel: Optional[Union[str, SafetyIntegrityLevel]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if dcLinkCoupling is not None and not isinstance(dcLinkCoupling, aas.SubmodelElement):
                    dcLinkCoupling = self.DcLinkCoupling(dcLinkCoupling)

                # Build a submodel element if a raw value was passed in the argument

                if brakePresent is not None and not isinstance(brakePresent, aas.SubmodelElement):
                    brakePresent = self.BrakePresent(brakePresent)

                # Build a submodel element if a raw value was passed in the argument

                if mainsConnection is not None and not isinstance(mainsConnection, aas.SubmodelElement):
                    mainsConnection = self.MainsConnection(mainsConnection)

                # Build a submodel element if a raw value was passed in the argument

                if mountingType is not None and not isinstance(mountingType, aas.SubmodelElement):
                    mountingType = self.MountingType(mountingType)

                # Build a submodel element if a raw value was passed in the argument

                if minSwitchingFrequency is not None and not isinstance(minSwitchingFrequency, aas.SubmodelElement):
                    minSwitchingFrequency = self.MinSwitchingFrequency(minSwitchingFrequency)

                # Build a submodel element if a raw value was passed in the argument

                if coolingType is not None and not isinstance(coolingType, aas.SubmodelElement):
                    coolingType = self.CoolingType(coolingType)

                # Build a submodel element if a raw value was passed in the argument

                if protectionType is not None and not isinstance(protectionType, aas.SubmodelElement):
                    protectionType = self.ProtectionType(protectionType)

                # Build a submodel element if a raw value was passed in the argument

                if certificateApproval is not None and not isinstance(certificateApproval, aas.SubmodelElement):
                    certificateApproval = self.CertificateApproval(certificateApproval)

                # Build a submodel element if a raw value was passed in the argument

                if safetyIntegrityLevel is not None and not isinstance(safetyIntegrityLevel, aas.SubmodelElement):
                    safetyIntegrityLevel = self.SafetyIntegrityLevel(safetyIntegrityLevel)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    dcLinkCoupling,
                    brakePresent,
                    mainsConnection,
                    mountingType,
                    minSwitchingFrequency,
                    coolingType,
                    protectionType,
                    certificateApproval,
                    safetyIntegrityLevel,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class UsageProfile(aas.SubmodelElementCollection):

            class CyclesPerMinute(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CyclesPerMinute",
                        "value_type": int,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/CyclesPerMinute/1/0"
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OperatingHoursPerDay(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OperatingHoursPerDay",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/OperatingHoursPerDay/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OperatingDaysPerYear(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OperatingDaysPerYear",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/OperatingDaysPerYear/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"UsageProfile",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/UsageProfile/1/0"),
                }

            def __init__(
                self,
                cyclesPerMinute: Union[int, CyclesPerMinute],
                operatingHoursPerDay: Union[xsd.Long, OperatingHoursPerDay],
                operatingDaysPerYear: Union[xsd.Long, OperatingDaysPerYear],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if cyclesPerMinute is not None and not isinstance(cyclesPerMinute, aas.SubmodelElement):
                    cyclesPerMinute = self.CyclesPerMinute(cyclesPerMinute)

                # Build a submodel element if a raw value was passed in the argument

                if operatingHoursPerDay is not None and not isinstance(operatingHoursPerDay, aas.SubmodelElement):
                    operatingHoursPerDay = self.OperatingHoursPerDay(operatingHoursPerDay)

                # Build a submodel element if a raw value was passed in the argument

                if operatingDaysPerYear is not None and not isinstance(operatingDaysPerYear, aas.SubmodelElement):
                    operatingDaysPerYear = self.OperatingDaysPerYear(operatingDaysPerYear)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    cyclesPerMinute, operatingHoursPerDay, operatingDaysPerYear
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ApplicationRequirements",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Applikationsanforderungen", r"en": r"Application requirements"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/ApplicationRequirements/1/0"
                ),
            }

        def __init__(
            self,
            motionPattern: Optional[MotionPattern] = None,
            environmental: Optional[Environmental] = None,
            overallSystemRequirements: Optional[OverallSystemRequirements] = None,
            usageProfile: Optional[UsageProfile] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                motionPattern, environmental, overallSystemRequirements, usageProfile
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class TransformationMechanism(aas.SubmodelElementCollection):

        class Fan(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"Fan",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Lüfter", r"en": r"Fan"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Fan/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Pump(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"Pump",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Pumpe", r"en": r"Pump"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Pump/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RotraryTable(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StaticEccentricity(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StaticEccentricity",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Exzentrität", r"en": r"Eccentricity"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/StaticEccentricity/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CentroidAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CentroidAngle",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Mittelpunktswinkel", r"en": r"Centroid angle"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CentroidAngle/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"RotraryTable",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Drehtisch", r"en": r"Rotrary table"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/RotraryTable/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                staticEccentricity: Optional[Union[xsd.Long, StaticEccentricity]] = None,
                centroidAngle: Optional[Union[xsd.Long, CentroidAngle]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if staticEccentricity is not None and not isinstance(staticEccentricity, aas.SubmodelElement):
                    staticEccentricity = self.StaticEccentricity(staticEccentricity)

                # Build a submodel element if a raw value was passed in the argument

                if centroidAngle is not None and not isinstance(centroidAngle, aas.SubmodelElement):
                    centroidAngle = self.CentroidAngle(centroidAngle)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    staticEccentricity,
                    centroidAngle,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ChainConveyor(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrictionCoefficient(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrictionCoefficient",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Reibungskoeffizient", r"en": r"Coefficient of friction"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FeedConstant(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FeedConstant",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"ChainConveyor",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Kettenförderer", r"en": r"Chain conveyor"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/ChainConveyor/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                feedConstant: Optional[Union[xsd.Long, FeedConstant]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                    frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                # Build a submodel element if a raw value was passed in the argument

                if feedConstant is not None and not isinstance(feedConstant, aas.SubmodelElement):
                    feedConstant = self.FeedConstant(feedConstant)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    frictionCoefficient,
                    feedConstant,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class BeltConveyor(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrictionCoefficient(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrictionCoefficient",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Reibungskoeffizient", r"en": r"Coefficient of friction"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FeedConstant(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FeedConstant",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"BeltConveyor",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Bandförderer", r"en": r"Belt conveyor"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/BeltConveyor/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                feedConstant: Optional[Union[xsd.Long, FeedConstant]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                    frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                # Build a submodel element if a raw value was passed in the argument

                if feedConstant is not None and not isinstance(feedConstant, aas.SubmodelElement):
                    feedConstant = self.FeedConstant(feedConstant)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    frictionCoefficient,
                    feedConstant,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RollerConveyor(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrictionCoefficient(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrictionCoefficient",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Reibungskoeffizient", r"en": r"Coefficient of friction"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FeedConstant(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FeedConstant",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"RollerConveyor",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Rollenbahn", r"en": r"Roller conveyor"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/RollerConveyor/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                feedConstant: Optional[Union[xsd.Long, FeedConstant]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                    frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                # Build a submodel element if a raw value was passed in the argument

                if feedConstant is not None and not isinstance(feedConstant, aas.SubmodelElement):
                    feedConstant = self.FeedConstant(feedConstant)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    frictionCoefficient,
                    feedConstant,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class BeltDrive(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrictionCoefficient(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrictionCoefficient",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Reibungskoeffizient", r"en": r"Coefficient of friction"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FeedConstant(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FeedConstant",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"BeltDrive",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Riemenantrieb", r"en": r"Belt drive"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/BeltDrive/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                feedConstant: Optional[Union[xsd.Long, FeedConstant]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                    frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                # Build a submodel element if a raw value was passed in the argument

                if feedConstant is not None and not isinstance(feedConstant, aas.SubmodelElement):
                    feedConstant = self.FeedConstant(feedConstant)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    frictionCoefficient,
                    feedConstant,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class TravelingDrive(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrictionCoefficient(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrictionCoefficient",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Reibungskoeffizient", r"en": r"Coefficient of friction"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FeedConstant(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FeedConstant",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"TravelingDrive",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Fahrender Antrieb", r"en": r"Traveling drive"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/TravelingDrive/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                feedConstant: Optional[Union[xsd.Long, FeedConstant]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                    frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                # Build a submodel element if a raw value was passed in the argument

                if feedConstant is not None and not isinstance(feedConstant, aas.SubmodelElement):
                    feedConstant = self.FeedConstant(feedConstant)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    frictionCoefficient,
                    feedConstant,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RackDrive(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrictionCoefficient(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrictionCoefficient",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Reibungskoeffizient", r"en": r"Coefficient of friction"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FeedConstant(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FeedConstant",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DiameterPinion(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DiameterPinion",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Durchmesser Ritzel", r"en": r"Diameter of pinion"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DiameterPinion/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HelixAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"HelixAngle",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Schrägungswinkel der Verzahnung", r"en": r"Helix angle of the toothing"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/HelixAngle/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MovingPart(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MovingPart",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Bewegtes Teil", r"en": r"Moving part"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RackMovingPart/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"RackDrive",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Zahnstangenapplikation", r"en": r"Rack drive"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/RackDrive/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                feedConstant: Optional[Union[xsd.Long, FeedConstant]] = None,
                diameterPinion: Optional[Union[xsd.Long, DiameterPinion]] = None,
                helixAngle: Optional[Union[xsd.Long, HelixAngle]] = None,
                movingPart: Optional[Union[xsd.Long, MovingPart]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                    frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                # Build a submodel element if a raw value was passed in the argument

                if feedConstant is not None and not isinstance(feedConstant, aas.SubmodelElement):
                    feedConstant = self.FeedConstant(feedConstant)

                # Build a submodel element if a raw value was passed in the argument

                if diameterPinion is not None and not isinstance(diameterPinion, aas.SubmodelElement):
                    diameterPinion = self.DiameterPinion(diameterPinion)

                # Build a submodel element if a raw value was passed in the argument

                if helixAngle is not None and not isinstance(helixAngle, aas.SubmodelElement):
                    helixAngle = self.HelixAngle(helixAngle)

                # Build a submodel element if a raw value was passed in the argument

                if movingPart is not None and not isinstance(movingPart, aas.SubmodelElement):
                    movingPart = self.MovingPart(movingPart)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    frictionCoefficient,
                    feedConstant,
                    diameterPinion,
                    helixAngle,
                    movingPart,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class SpindleDrive(aas.Entity):

            class Efficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Efficiency",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InertiaMotorSide(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InertiaMotorSide",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmAxialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmAxialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LeverArmRadialForce(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LeverArmRadialForce",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Hebelarm Axialkraft", r"en": r"Lever arm axial force"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NoLoadTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NoLoadTorque",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Leerlaufdrehmoment", r"en": r"No-load Torque"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InclinationAngle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InclinationAngle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrictionCoefficient(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrictionCoefficient",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Reibungskoeffizient", r"en": r"Coefficient of friction"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FeedConstant(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FeedConstant",
                        "value_type": xsd.Long,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"SpindleDrive",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Spindelantrieb", r"en": r"Spindle drive"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/SpindleDrive/1/0"),
                }

            def __init__(
                self,
                efficiency: Optional[Union[xsd.Long, Efficiency]] = None,
                inertiaMotorSide: Optional[Union[xsd.Long, InertiaMotorSide]] = None,
                leverArmAxialForce: Optional[Union[xsd.Long, LeverArmAxialForce]] = None,
                leverArmRadialForce: Optional[Union[xsd.Long, LeverArmRadialForce]] = None,
                noLoadTorque: Optional[Union[xsd.Long, NoLoadTorque]] = None,
                inclinationAngle: Optional[Union[xsd.Long, InclinationAngle]] = None,
                frictionCoefficient: Optional[Union[xsd.Long, FrictionCoefficient]] = None,
                feedConstant: Optional[Union[xsd.Long, FeedConstant]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if efficiency is not None and not isinstance(efficiency, aas.SubmodelElement):
                    efficiency = self.Efficiency(efficiency)

                # Build a submodel element if a raw value was passed in the argument

                if inertiaMotorSide is not None and not isinstance(inertiaMotorSide, aas.SubmodelElement):
                    inertiaMotorSide = self.InertiaMotorSide(inertiaMotorSide)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmAxialForce is not None and not isinstance(leverArmAxialForce, aas.SubmodelElement):
                    leverArmAxialForce = self.LeverArmAxialForce(leverArmAxialForce)

                # Build a submodel element if a raw value was passed in the argument

                if leverArmRadialForce is not None and not isinstance(leverArmRadialForce, aas.SubmodelElement):
                    leverArmRadialForce = self.LeverArmRadialForce(leverArmRadialForce)

                # Build a submodel element if a raw value was passed in the argument

                if noLoadTorque is not None and not isinstance(noLoadTorque, aas.SubmodelElement):
                    noLoadTorque = self.NoLoadTorque(noLoadTorque)

                # Build a submodel element if a raw value was passed in the argument

                if inclinationAngle is not None and not isinstance(inclinationAngle, aas.SubmodelElement):
                    inclinationAngle = self.InclinationAngle(inclinationAngle)

                # Build a submodel element if a raw value was passed in the argument

                if frictionCoefficient is not None and not isinstance(frictionCoefficient, aas.SubmodelElement):
                    frictionCoefficient = self.FrictionCoefficient(frictionCoefficient)

                # Build a submodel element if a raw value was passed in the argument

                if feedConstant is not None and not isinstance(feedConstant, aas.SubmodelElement):
                    feedConstant = self.FeedConstant(feedConstant)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    efficiency,
                    inertiaMotorSide,
                    leverArmAxialForce,
                    leverArmRadialForce,
                    noLoadTorque,
                    inclinationAngle,
                    frictionCoefficient,
                    feedConstant,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"TransformationMechanism",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Transformationsmechanismen", r"en": r"Transformation mechanism"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"All application mechanisms are listed in the submodel template - note that only one application mechanism can be selected in the design project instance."
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/PowerDriveTrainSizing/TransformationMechanism/1/0"
                ),
            }

        def __init__(
            self,
            fan: Optional[Fan] = None,
            pump: Optional[Pump] = None,
            rotraryTable: Optional[RotraryTable] = None,
            chainConveyor: Optional[ChainConveyor] = None,
            beltConveyor: Optional[BeltConveyor] = None,
            rollerConveyor: Optional[RollerConveyor] = None,
            beltDrive: Optional[BeltDrive] = None,
            travelingDrive: Optional[TravelingDrive] = None,
            rackDrive: Optional[RackDrive] = None,
            spindleDrive: Optional[SpindleDrive] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                fan,
                pump,
                rotraryTable,
                chainConveyor,
                beltConveyor,
                rollerConveyor,
                beltDrive,
                travelingDrive,
                rackDrive,
                spindleDrive,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SizingResult(aas.SubmodelElementCollection):

        class OverallSystem(aas.Entity):

            class ManufacturerName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerName",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO677#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerArticleNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerArticleNumber",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO676#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerProductDesignation(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ManufacturerProductDesignation",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAW338#001"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerOrderCode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerOrderCode",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r" 0173-1#02-AAO227#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ExternalMomentOfInertia(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExternalMomentOfInertia",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/ExternalMomentOfInertia/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InternalMomentOfIntertia(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InternalMomentOfIntertia",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/InternalMomentOfInertia/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MassInertiaRatio(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MassInertiaRatio",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MassInertiaRatio/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DecelerationForEmergencyStop(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DecelerationForEmergencyStop",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/DecelerationForEmergencyStop/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CurrentForEmergencyStop(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CurrentForEmergencyStop",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/CurrentForEmergencyStop/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DisplacementDuringEmergencyStop(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DisplacementDuringEmergencyStop",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/DisplacementDuringEmergencyStop/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EnergyConsumtionPerCycle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EnergyConsumtionPerCycle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"OverallSystem",
                    "entity_type": aas.EntityType.CO_MANAGED_ENTITY,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Gesamtsystem", r"en": r"Overall system"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/OverallSystem/1/0"),
                }

            def __init__(
                self,
                manufacturerName: Optional[Union[str, ManufacturerName]] = None,
                manufacturerArticleNumber: Optional[Union[str, ManufacturerArticleNumber]] = None,
                manufacturerProductDesignation: Optional[
                    Union[aas.MultiLanguageTextType, ManufacturerProductDesignation]
                ] = None,
                manufacturerOrderCode: Optional[Union[str, ManufacturerOrderCode]] = None,
                externalMomentOfInertia: Optional[Union[xsd.Long, ExternalMomentOfInertia]] = None,
                internalMomentOfIntertia: Optional[Union[xsd.Long, InternalMomentOfIntertia]] = None,
                massInertiaRatio: Optional[Union[xsd.Long, MassInertiaRatio]] = None,
                decelerationForEmergencyStop: Optional[Union[xsd.Long, DecelerationForEmergencyStop]] = None,
                currentForEmergencyStop: Optional[Union[xsd.Long, CurrentForEmergencyStop]] = None,
                displacementDuringEmergencyStop: Optional[Union[xsd.Long, DisplacementDuringEmergencyStop]] = None,
                energyConsumtionPerCycle: Optional[Union[xsd.Long, EnergyConsumtionPerCycle]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                    manufacturerName = self.ManufacturerName(manufacturerName)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerArticleNumber is not None and not isinstance(
                    manufacturerArticleNumber, aas.SubmodelElement
                ):
                    manufacturerArticleNumber = self.ManufacturerArticleNumber(manufacturerArticleNumber)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerProductDesignation is not None and not isinstance(
                    manufacturerProductDesignation, aas.SubmodelElement
                ):
                    manufacturerProductDesignation = self.ManufacturerProductDesignation(manufacturerProductDesignation)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerOrderCode is not None and not isinstance(manufacturerOrderCode, aas.SubmodelElement):
                    manufacturerOrderCode = self.ManufacturerOrderCode(manufacturerOrderCode)

                # Build a submodel element if a raw value was passed in the argument

                if externalMomentOfInertia is not None and not isinstance(externalMomentOfInertia, aas.SubmodelElement):
                    externalMomentOfInertia = self.ExternalMomentOfInertia(externalMomentOfInertia)

                # Build a submodel element if a raw value was passed in the argument

                if internalMomentOfIntertia is not None and not isinstance(
                    internalMomentOfIntertia, aas.SubmodelElement
                ):
                    internalMomentOfIntertia = self.InternalMomentOfIntertia(internalMomentOfIntertia)

                # Build a submodel element if a raw value was passed in the argument

                if massInertiaRatio is not None and not isinstance(massInertiaRatio, aas.SubmodelElement):
                    massInertiaRatio = self.MassInertiaRatio(massInertiaRatio)

                # Build a submodel element if a raw value was passed in the argument

                if decelerationForEmergencyStop is not None and not isinstance(
                    decelerationForEmergencyStop, aas.SubmodelElement
                ):
                    decelerationForEmergencyStop = self.DecelerationForEmergencyStop(decelerationForEmergencyStop)

                # Build a submodel element if a raw value was passed in the argument

                if currentForEmergencyStop is not None and not isinstance(currentForEmergencyStop, aas.SubmodelElement):
                    currentForEmergencyStop = self.CurrentForEmergencyStop(currentForEmergencyStop)

                # Build a submodel element if a raw value was passed in the argument

                if displacementDuringEmergencyStop is not None and not isinstance(
                    displacementDuringEmergencyStop, aas.SubmodelElement
                ):
                    displacementDuringEmergencyStop = self.DisplacementDuringEmergencyStop(
                        displacementDuringEmergencyStop
                    )

                # Build a submodel element if a raw value was passed in the argument

                if energyConsumtionPerCycle is not None and not isinstance(
                    energyConsumtionPerCycle, aas.SubmodelElement
                ):
                    energyConsumtionPerCycle = self.EnergyConsumtionPerCycle(energyConsumtionPerCycle)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    manufacturerName,
                    manufacturerArticleNumber,
                    manufacturerProductDesignation,
                    manufacturerOrderCode,
                    externalMomentOfInertia,
                    internalMomentOfIntertia,
                    massInertiaRatio,
                    decelerationForEmergencyStop,
                    currentForEmergencyStop,
                    displacementDuringEmergencyStop,
                    energyConsumtionPerCycle,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class MainComponent(aas.Entity):

            class MainComponentType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MainComponentType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Typ der Hauptkomponente", r"en": r"Main component type"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MainComponentType/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerName",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO677#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerArticleNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerArticleNumber",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO676#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerProductDesignation(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ManufacturerProductDesignation",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAW338#001"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerOrderCode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerOrderCode",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r" 0173-1#02-AAO227#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxCurrentUtilizationPercentage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxCurrentUtilizationPercentage",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxCurrentUtilizationPercentage/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxCurrentUtilization(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxCurrentUtilization",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxCurrentUtilization/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxThermalUtilizationPercentage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxThermalUtilizationPercentage",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxThermalUtilizationPercentage/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxThermalUtilization(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxThermalUtilization",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxThermalUtilization/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AveragePowerLosses(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AveragePowerLosses",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/AveragePowerLosses/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AverageRegenerativePowerDcLink(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AverageRegenerativePowerDcLink",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageRegenerativePowerDcLink/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxRegenerativePowerDcLink(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxRegenerativePowerDcLink",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRegenerativePowerDcLink/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AverageFeedInPowerDcLink(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AverageFeedInPowerDcLink",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageFeedInPowerDcLink/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AverageFeedInPowerMains(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AverageFeedInPowerMains",
                        "value_type": xsd.Long,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageFeedInPowerMains/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxFeedInPowerMains(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxFeedInPowerMains",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxFeedInPowerMains/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContinuousCurrent(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ContinuousCurrent",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/ContinuousCurrent/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RmsOfPower(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RmsOfPower",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/RmsOfPower/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxTorqueUtilizationPercentage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxTorqueUtilizationPercentage",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxTorqueUtilizationPercentage/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxTorqueUtilization(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxTorqueUtilization",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxTorqueUtilization/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxRotationSpeedUtilizationPercentage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxRotationSpeedUtilizationPercentage",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRotationSpeedUtilizationPercentage/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxRotationSpeedUtilization(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxRotationSpeedUtilization",
                        "value_type": xsd.Long,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRotationSpeedUtilization/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EffectiveUtilization(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EffectiveUtilization",
                        "value_type": xsd.Long,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/EffectiveUtilization/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CalculatedServiceLife(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CalculatedServiceLife",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/CalculatedServiceLife/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MassInertiaRatio(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MassInertiaRatio",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/MassInertiaRatio/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FrequencyAtMaxSpeed(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FrequencyAtMaxSpeed",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrequencyAtMaxSpeed/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PowerInRegenerativeOperation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PowerInRegenerativeOperation",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/PowerInRegenerativeOperation/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PowerInMotorOperation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PowerInMotorOperation",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/PowerInMotorOperation/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RmsOfMotorTorque(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RmsOfMotorTorque",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/RmsOfMotorTorque/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EnergyConsumtionPerCycle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EnergyConsumtionPerCycle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"MainComponent",
                    "entity_type": aas.EntityType.CO_MANAGED_ENTITY,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Hauptkomponente", r"en": r"Main component"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/MainComponent/1/0"),
                }

            def __init__(
                self,
                mainComponentType: Iterable[Union[str, MainComponentType]],
                manufacturerName: Union[str, ManufacturerName],
                manufacturerArticleNumber: Union[str, ManufacturerArticleNumber],
                manufacturerOrderCode: Union[str, ManufacturerOrderCode],
                manufacturerProductDesignation: Optional[
                    Union[aas.MultiLanguageTextType, ManufacturerProductDesignation]
                ] = None,
                maxCurrentUtilizationPercentage: Optional[Union[xsd.Long, MaxCurrentUtilizationPercentage]] = None,
                maxCurrentUtilization: Optional[Union[xsd.Long, MaxCurrentUtilization]] = None,
                maxThermalUtilizationPercentage: Optional[Union[xsd.Long, MaxThermalUtilizationPercentage]] = None,
                maxThermalUtilization: Optional[Union[xsd.Long, MaxThermalUtilization]] = None,
                averagePowerLosses: Optional[Union[xsd.Long, AveragePowerLosses]] = None,
                averageRegenerativePowerDcLink: Optional[Union[xsd.Long, AverageRegenerativePowerDcLink]] = None,
                maxRegenerativePowerDcLink: Optional[Union[xsd.Long, MaxRegenerativePowerDcLink]] = None,
                averageFeedInPowerDcLink: Optional[Union[xsd.Long, AverageFeedInPowerDcLink]] = None,
                averageFeedInPowerMains: Optional[Union[xsd.Long, AverageFeedInPowerMains]] = None,
                maxFeedInPowerMains: Optional[Union[xsd.Long, MaxFeedInPowerMains]] = None,
                continuousCurrent: Optional[Union[xsd.Long, ContinuousCurrent]] = None,
                rmsOfPower: Optional[Union[xsd.Long, RmsOfPower]] = None,
                maxTorqueUtilizationPercentage: Optional[Union[xsd.Long, MaxTorqueUtilizationPercentage]] = None,
                maxTorqueUtilization: Optional[Union[xsd.Long, MaxTorqueUtilization]] = None,
                maxRotationSpeedUtilizationPercentage: Optional[
                    Union[xsd.Long, MaxRotationSpeedUtilizationPercentage]
                ] = None,
                maxRotationSpeedUtilization: Optional[Union[xsd.Long, MaxRotationSpeedUtilization]] = None,
                effectiveUtilization: Optional[Union[xsd.Long, EffectiveUtilization]] = None,
                calculatedServiceLife: Optional[Union[xsd.Long, CalculatedServiceLife]] = None,
                massInertiaRatio: Optional[Union[xsd.Long, MassInertiaRatio]] = None,
                frequencyAtMaxSpeed: Optional[Union[xsd.Long, FrequencyAtMaxSpeed]] = None,
                powerInRegenerativeOperation: Optional[Union[xsd.Long, PowerInRegenerativeOperation]] = None,
                powerInMotorOperation: Optional[Union[xsd.Long, PowerInMotorOperation]] = None,
                rmsOfMotorTorque: Optional[Union[xsd.Long, RmsOfMotorTorque]] = None,
                energyConsumtionPerCycle: Optional[Union[xsd.Long, EnergyConsumtionPerCycle]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # A str would be split into its characters
                if isinstance(mainComponentType, str):
                    raise TypeError("mainComponentType takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if mainComponentType:
                    mainComponentType = [
                        i if isinstance(i, aas.SubmodelElement) else self.MainComponentType(i)
                        for i in mainComponentType
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                    manufacturerName = self.ManufacturerName(manufacturerName)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerArticleNumber is not None and not isinstance(
                    manufacturerArticleNumber, aas.SubmodelElement
                ):
                    manufacturerArticleNumber = self.ManufacturerArticleNumber(manufacturerArticleNumber)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerProductDesignation is not None and not isinstance(
                    manufacturerProductDesignation, aas.SubmodelElement
                ):
                    manufacturerProductDesignation = self.ManufacturerProductDesignation(manufacturerProductDesignation)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerOrderCode is not None and not isinstance(manufacturerOrderCode, aas.SubmodelElement):
                    manufacturerOrderCode = self.ManufacturerOrderCode(manufacturerOrderCode)

                # Build a submodel element if a raw value was passed in the argument

                if maxCurrentUtilizationPercentage is not None and not isinstance(
                    maxCurrentUtilizationPercentage, aas.SubmodelElement
                ):
                    maxCurrentUtilizationPercentage = self.MaxCurrentUtilizationPercentage(
                        maxCurrentUtilizationPercentage
                    )

                # Build a submodel element if a raw value was passed in the argument

                if maxCurrentUtilization is not None and not isinstance(maxCurrentUtilization, aas.SubmodelElement):
                    maxCurrentUtilization = self.MaxCurrentUtilization(maxCurrentUtilization)

                # Build a submodel element if a raw value was passed in the argument

                if maxThermalUtilizationPercentage is not None and not isinstance(
                    maxThermalUtilizationPercentage, aas.SubmodelElement
                ):
                    maxThermalUtilizationPercentage = self.MaxThermalUtilizationPercentage(
                        maxThermalUtilizationPercentage
                    )

                # Build a submodel element if a raw value was passed in the argument

                if maxThermalUtilization is not None and not isinstance(maxThermalUtilization, aas.SubmodelElement):
                    maxThermalUtilization = self.MaxThermalUtilization(maxThermalUtilization)

                # Build a submodel element if a raw value was passed in the argument

                if averagePowerLosses is not None and not isinstance(averagePowerLosses, aas.SubmodelElement):
                    averagePowerLosses = self.AveragePowerLosses(averagePowerLosses)

                # Build a submodel element if a raw value was passed in the argument

                if averageRegenerativePowerDcLink is not None and not isinstance(
                    averageRegenerativePowerDcLink, aas.SubmodelElement
                ):
                    averageRegenerativePowerDcLink = self.AverageRegenerativePowerDcLink(averageRegenerativePowerDcLink)

                # Build a submodel element if a raw value was passed in the argument

                if maxRegenerativePowerDcLink is not None and not isinstance(
                    maxRegenerativePowerDcLink, aas.SubmodelElement
                ):
                    maxRegenerativePowerDcLink = self.MaxRegenerativePowerDcLink(maxRegenerativePowerDcLink)

                # Build a submodel element if a raw value was passed in the argument

                if averageFeedInPowerDcLink is not None and not isinstance(
                    averageFeedInPowerDcLink, aas.SubmodelElement
                ):
                    averageFeedInPowerDcLink = self.AverageFeedInPowerDcLink(averageFeedInPowerDcLink)

                # Build a submodel element if a raw value was passed in the argument

                if averageFeedInPowerMains is not None and not isinstance(averageFeedInPowerMains, aas.SubmodelElement):
                    averageFeedInPowerMains = self.AverageFeedInPowerMains(averageFeedInPowerMains)

                # Build a submodel element if a raw value was passed in the argument

                if maxFeedInPowerMains is not None and not isinstance(maxFeedInPowerMains, aas.SubmodelElement):
                    maxFeedInPowerMains = self.MaxFeedInPowerMains(maxFeedInPowerMains)

                # Build a submodel element if a raw value was passed in the argument

                if continuousCurrent is not None and not isinstance(continuousCurrent, aas.SubmodelElement):
                    continuousCurrent = self.ContinuousCurrent(continuousCurrent)

                # Build a submodel element if a raw value was passed in the argument

                if rmsOfPower is not None and not isinstance(rmsOfPower, aas.SubmodelElement):
                    rmsOfPower = self.RmsOfPower(rmsOfPower)

                # Build a submodel element if a raw value was passed in the argument

                if maxTorqueUtilizationPercentage is not None and not isinstance(
                    maxTorqueUtilizationPercentage, aas.SubmodelElement
                ):
                    maxTorqueUtilizationPercentage = self.MaxTorqueUtilizationPercentage(maxTorqueUtilizationPercentage)

                # Build a submodel element if a raw value was passed in the argument

                if maxTorqueUtilization is not None and not isinstance(maxTorqueUtilization, aas.SubmodelElement):
                    maxTorqueUtilization = self.MaxTorqueUtilization(maxTorqueUtilization)

                # Build a submodel element if a raw value was passed in the argument

                if maxRotationSpeedUtilizationPercentage is not None and not isinstance(
                    maxRotationSpeedUtilizationPercentage, aas.SubmodelElement
                ):
                    maxRotationSpeedUtilizationPercentage = self.MaxRotationSpeedUtilizationPercentage(
                        maxRotationSpeedUtilizationPercentage
                    )

                # Build a submodel element if a raw value was passed in the argument

                if maxRotationSpeedUtilization is not None and not isinstance(
                    maxRotationSpeedUtilization, aas.SubmodelElement
                ):
                    maxRotationSpeedUtilization = self.MaxRotationSpeedUtilization(maxRotationSpeedUtilization)

                # Build a submodel element if a raw value was passed in the argument

                if effectiveUtilization is not None and not isinstance(effectiveUtilization, aas.SubmodelElement):
                    effectiveUtilization = self.EffectiveUtilization(effectiveUtilization)

                # Build a submodel element if a raw value was passed in the argument

                if calculatedServiceLife is not None and not isinstance(calculatedServiceLife, aas.SubmodelElement):
                    calculatedServiceLife = self.CalculatedServiceLife(calculatedServiceLife)

                # Build a submodel element if a raw value was passed in the argument

                if massInertiaRatio is not None and not isinstance(massInertiaRatio, aas.SubmodelElement):
                    massInertiaRatio = self.MassInertiaRatio(massInertiaRatio)

                # Build a submodel element if a raw value was passed in the argument

                if frequencyAtMaxSpeed is not None and not isinstance(frequencyAtMaxSpeed, aas.SubmodelElement):
                    frequencyAtMaxSpeed = self.FrequencyAtMaxSpeed(frequencyAtMaxSpeed)

                # Build a submodel element if a raw value was passed in the argument

                if powerInRegenerativeOperation is not None and not isinstance(
                    powerInRegenerativeOperation, aas.SubmodelElement
                ):
                    powerInRegenerativeOperation = self.PowerInRegenerativeOperation(powerInRegenerativeOperation)

                # Build a submodel element if a raw value was passed in the argument

                if powerInMotorOperation is not None and not isinstance(powerInMotorOperation, aas.SubmodelElement):
                    powerInMotorOperation = self.PowerInMotorOperation(powerInMotorOperation)

                # Build a submodel element if a raw value was passed in the argument

                if rmsOfMotorTorque is not None and not isinstance(rmsOfMotorTorque, aas.SubmodelElement):
                    rmsOfMotorTorque = self.RmsOfMotorTorque(rmsOfMotorTorque)

                # Build a submodel element if a raw value was passed in the argument

                if energyConsumtionPerCycle is not None and not isinstance(
                    energyConsumtionPerCycle, aas.SubmodelElement
                ):
                    energyConsumtionPerCycle = self.EnergyConsumtionPerCycle(energyConsumtionPerCycle)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    mainComponentType,
                    manufacturerName,
                    manufacturerArticleNumber,
                    manufacturerProductDesignation,
                    manufacturerOrderCode,
                    maxCurrentUtilizationPercentage,
                    maxCurrentUtilization,
                    maxThermalUtilizationPercentage,
                    maxThermalUtilization,
                    averagePowerLosses,
                    averageRegenerativePowerDcLink,
                    maxRegenerativePowerDcLink,
                    averageFeedInPowerDcLink,
                    averageFeedInPowerMains,
                    maxFeedInPowerMains,
                    continuousCurrent,
                    rmsOfPower,
                    maxTorqueUtilizationPercentage,
                    maxTorqueUtilization,
                    maxRotationSpeedUtilizationPercentage,
                    maxRotationSpeedUtilization,
                    effectiveUtilization,
                    calculatedServiceLife,
                    massInertiaRatio,
                    frequencyAtMaxSpeed,
                    powerInRegenerativeOperation,
                    powerInMotorOperation,
                    rmsOfMotorTorque,
                    energyConsumtionPerCycle,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class OtherComponent(aas.Entity):

            class ManufacturerName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerName",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO677#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerArticleNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerArticleNumber",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO676#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerProductDesignation(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ManufacturerProductDesignation",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAW338#001"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManufacturerOrderCode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerOrderCode",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r" 0173-1#02-AAO227#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class QuantityOfParts(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"QuantityOfParts",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Anzahl Einzelteile", r"en": r"Quantity of parts"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PowerDriveTrainSizing/QuantityOfParts/1/0"
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BulkCount(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BulkCount",
                        "value_type": xsd.UnsignedLong,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0"),
                    }

                def __init__(self, value: xsd.UnsignedLong, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EnergyConsumtionPerCycle(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EnergyConsumtionPerCycle",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"OtherComponent",
                    "entity_type": aas.EntityType.CO_MANAGED_ENTITY,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Komponente", r"en": r"Component"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/OtherComponent/1/0"),
                }

            def __init__(
                self,
                manufacturerName: Optional[Union[str, ManufacturerName]] = None,
                manufacturerArticleNumber: Optional[Union[str, ManufacturerArticleNumber]] = None,
                manufacturerProductDesignation: Optional[
                    Union[aas.MultiLanguageTextType, ManufacturerProductDesignation]
                ] = None,
                manufacturerOrderCode: Optional[Union[str, ManufacturerOrderCode]] = None,
                quantityOfParts: Optional[Union[int, QuantityOfParts]] = None,
                bulkCount: Optional[Union[xsd.UnsignedLong, BulkCount]] = None,
                energyConsumtionPerCycle: Optional[Union[xsd.Long, EnergyConsumtionPerCycle]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                    manufacturerName = self.ManufacturerName(manufacturerName)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerArticleNumber is not None and not isinstance(
                    manufacturerArticleNumber, aas.SubmodelElement
                ):
                    manufacturerArticleNumber = self.ManufacturerArticleNumber(manufacturerArticleNumber)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerProductDesignation is not None and not isinstance(
                    manufacturerProductDesignation, aas.SubmodelElement
                ):
                    manufacturerProductDesignation = self.ManufacturerProductDesignation(manufacturerProductDesignation)

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerOrderCode is not None and not isinstance(manufacturerOrderCode, aas.SubmodelElement):
                    manufacturerOrderCode = self.ManufacturerOrderCode(manufacturerOrderCode)

                # Build a submodel element if a raw value was passed in the argument

                if quantityOfParts is not None and not isinstance(quantityOfParts, aas.SubmodelElement):
                    quantityOfParts = self.QuantityOfParts(quantityOfParts)

                # Build a submodel element if a raw value was passed in the argument

                if bulkCount is not None and not isinstance(bulkCount, aas.SubmodelElement):
                    bulkCount = self.BulkCount(bulkCount)

                # Build a submodel element if a raw value was passed in the argument

                if energyConsumtionPerCycle is not None and not isinstance(
                    energyConsumtionPerCycle, aas.SubmodelElement
                ):
                    energyConsumtionPerCycle = self.EnergyConsumtionPerCycle(energyConsumtionPerCycle)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    manufacturerName,
                    manufacturerArticleNumber,
                    manufacturerProductDesignation,
                    manufacturerOrderCode,
                    quantityOfParts,
                    bulkCount,
                    energyConsumtionPerCycle,
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Messages(aas.SubmodelElementCollection):

            class Message(aas.SubmodelElementCollection):

                class CriticalityOfMessage(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"CriticalityOfMessage",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Kritikalität der Meldung", r"en": r"Criticality of message"}
                            ),
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PowerDriveTrainSizing/CriticalityOfMessage/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MessageText(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"MessageText",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Nachrichtentext", r"en": r"Message text"}
                            ),
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PowerDriveTrainSizing/MessageText/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Message",
                        "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Nachricht", r"en": r"Message"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Message/1/0"),
                    }

                def __init__(
                    self,
                    criticalityOfMessage: Union[str, CriticalityOfMessage],
                    messageText: Union[aas.MultiLanguageTextType, MessageText],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if criticalityOfMessage is not None and not isinstance(criticalityOfMessage, aas.SubmodelElement):
                        criticalityOfMessage = self.CriticalityOfMessage(criticalityOfMessage)

                    # Build a submodel element if a raw value was passed in the argument

                    if messageText is not None and not isinstance(messageText, aas.SubmodelElement):
                        messageText = self.MessageText(messageText)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(criticalityOfMessage, messageText)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Messages",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Nachrichten", r"en": r"Messages"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/Messages/1/0"),
                }

            def __init__(
                self, message: Optional[Iterable[Message]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
            ):

                # A str would be split into its characters
                if isinstance(message, str):
                    raise TypeError("message takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(message)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class TextStatement(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"TextStatement",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Textaussage", r"en": r"Text statement"}),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/TextStatement/1/0"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SizingResult",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Auslegungsergebnisse", r"en": r"Sizing result"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingResult/1/0"),
            }

        def __init__(
            self,
            messages: Messages,
            overallSystem: Optional[OverallSystem] = None,
            mainComponent: Optional[Iterable[MainComponent]] = None,
            otherComponent: Optional[Iterable[OtherComponent]] = None,
            textStatement: Optional[Union[aas.MultiLanguageTextType, TextStatement]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(mainComponent, str):
                raise TypeError("mainComponent takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(otherComponent, str):
                raise TypeError("otherComponent takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if textStatement is not None and not isinstance(textStatement, aas.SubmodelElement):
                textStatement = self.TextStatement(textStatement)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                overallSystem, mainComponent, otherComponent, messages, textStatement
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"PowerDriveTrainSizing",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel containing customer specifications for motion and load profile, limitations and requirements of an industrial motion application."
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/1/0"
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        sizingProjectInformation: SizingProjectInformation,
        applicationRequirements: ApplicationRequirements,
        transformationMechanism: Optional[TransformationMechanism] = None,
        sizingResult: Optional[SizingResult] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            sizingProjectInformation, applicationRequirements, transformationMechanism, sizingResult
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
