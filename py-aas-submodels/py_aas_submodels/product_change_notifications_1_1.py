from typing import Any, Iterable, Optional, Tuple, TypedDict, Union, Unpack, cast
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


class BasicEventElementMetadata(TypedDict, total=False):
    """Metadata of aas.BasicEventElement, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    observed: aas.ModelReference[Union["aas.AssetAdministrationShell", aas.Submodel, aas.SubmodelElement]]
    direction: aas.Direction
    state: aas.StateOfEvent
    message_topic: Optional[str]
    message_broker: Optional[
        aas.ModelReference[Union[aas.Submodel, aas.SubmodelElementList, aas.SubmodelElementCollection, aas.Entity]]
    ]
    last_update: Optional[xsd.DateTime]
    min_interval: Optional[xsd.Duration]
    max_interval: Optional[xsd.Duration]
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


class ProductChangeNotifications(aas.Submodel):

    class PcnEventsOutgoing(aas.BasicEventElement):

        @staticmethod
        def template_defaults() -> BasicEventElementMetadata:
            return {
                "id_short": r"PcnEventsOutgoing",
                "observed": aas.ModelReference(
                    key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"www.example.com/ids/sm/3212_3160_4022_4516"),),
                    type_=aas.Submodel,
                    referred_semantic_id=None,
                ),
                "direction": aas.Direction.INPUT,
                "state": aas.StateOfEvent.OFF,
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Note: Industrial users will subscribe to this event by different implementation technologies."
                    }
                ),
                "semantic_id": global_ref(
                    r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/EventsOutgoing/1/0"
                ),
            }

        def __init__(self, **kwargs: Unpack[BasicEventElementMetadata]):

            super().__init__(**(self.template_defaults() | kwargs))

    class Records(GeneratedSubmodelElementList):

        class Records_item(aas.SubmodelElementCollection):

            class Manufacturer(aas.SubmodelElementCollection):

                class ManufacturerName(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {"id_short": r"ManufacturerName", "semantic_id": global_ref(r"0173-1#02-AAO677#004")}

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PhysicalAddress__0__(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"PhysicalAddress__0__",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Note: This set of information is defined by SMT drop-in "Contact Information" in (current) version 1.0, given by the SMT for Contact and Address Information V1.0. The ECLASS IRDI reserved for the SMC was added as supplementalSemanticId.  Note: Use this set of information, until version 1.1 of the SMT drop-in "Contact Information" is published. Note: The idShort shall go without the index "__0__".'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation"
                            ),
                            "supplemental_semantic_id": (
                                global_ref(r"https://admin-shell.io/smt-dropin/smt-dropin-use/1/0"),
                                global_ref(r"0173-1#02-ABG791#003/0173-1#01-ADR442#008"),
                            ),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class PhysicalAddress__1__(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"PhysicalAddress__1__",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Note: this set of information is defined by SMT drop-in "Contact Information" in upcoming version 1.1, given by the SMT for Contact and Address Information V1.1. The ECLASS IRDI reserved for the SMC was added as supplementalSemanticId.  Note: Use this set of information, if version 1.1 of the SMT drop-in "Contact Information" is published. Note: The idShort shall go without the index "__1__".'
                                }
                            ),
                            "semantic_id": global_ref(r"0112/2///61360_7#AAS034"),
                            "supplemental_semantic_id": (
                                global_ref(r"https://admin-shell.io/smt-dropin/smt-dropin-use/1/0"),
                                global_ref(r"0173-1#02-ABG791#003/0173-1#01-ADR442#008"),
                            ),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Manufacturer",
                        "semantic_id": global_ref(r"0173-1#02-ABI295#003/0173-1#01-AHE584#003"),
                    }

                def __init__(
                    self,
                    manufacturerName: Union[aas.MultiLanguageTextType, ManufacturerName],
                    physicalAddress__0__: PhysicalAddress__0__,
                    physicalAddress__1__: PhysicalAddress__1__,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                        manufacturerName = self.ManufacturerName(manufacturerName)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        manufacturerName, physicalAddress__0__, physicalAddress__1__
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ManufacturerChangeID(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManufacturerChangeID",
                        "value_type": str,
                        "semantic_id": global_ref(r"0173-1#02-ABG772#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PcnType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PcnType",
                        "value_type": str,
                        "value_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#07-ABU000#003"),),
                            type_=aas.Submodel,
                            referred_semantic_id=None,
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Following the VDMA 24903, this mandatory global flag distincts between a PCN and PDN. Use either value PCN or PDN with valueId 0173-1#07-ABU000#003 (PCN) or 0173-1#07-ABU001#003 (PDN). Note: According this global flag, the PCN milestone (173-1#07-ABU000#003) communicates the effective date of the PCN and the EOP milestone (EOP milestone (0173-1#07-ABU003#003) communicates the end of production date for the PDN in the life-cycle data."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/PcnType/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LifeCycleData(GeneratedSubmodelElementList):

                class Lifecycledata_item(aas.SubmodelElementCollection):

                    class MilestoneClassification(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"MilestoneClassification",
                                "value_type": str,
                                "value_id": aas.ModelReference(
                                    key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#07-ABU002#003"),),
                                    type_=aas.Submodel,
                                    referred_semantic_id=None,
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: defined point in time with a specific meaning for life-cycle management (IEC 62890:2020). Note: Set value and valueId with one of these: SOP (0173-1#07-ABT998#003),  NRND (0173-1#07-ABT999#003),  PCN (0173-1#07-ABU000#003),  EOS (0173-1#07-ABU002#003),  EOP (0173-1#07-ABU003#003),  LTD (0173-1#07-ABU004#003),  EOSR (0173-1#07-ABU087#003) Note: The PDN milestone is not to be used for this classification. Instead, the global flag PcnType is set with value=PCN and valueId=0173-1#07-ABU000#003."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABG773#002"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DateOfValidity(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DateOfValidity",
                                "value_type": xsd.DateTime,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: Date is in UTC (coordinated universal time). Typically, time is given, as well."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABF815#002"),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/LifeCycleData/Milestone/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        milestoneClassification: Union[str, MilestoneClassification],
                        dateOfValidity: Union[xsd.DateTime, DateOfValidity],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if milestoneClassification is not None and not isinstance(
                            milestoneClassification, aas.SubmodelElement
                        ):
                            milestoneClassification = self.MilestoneClassification(milestoneClassification)

                        # Build a submodel element if a raw value was passed in the argument

                        if dateOfValidity is not None and not isinstance(dateOfValidity, aas.SubmodelElement):
                            dateOfValidity = self.DateOfValidity(dateOfValidity)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(milestoneClassification, dateOfValidity)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"LifeCycleData",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/LifeCycleData/Milestone/1/0"
                        ),
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/LifeCycleData/List/1/0"
                        ),
                    }

                def __init__(
                    self,
                    lifecycledata_items: Optional[Iterable[Lifecycledata_item]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(lifecycledata_items, str):
                        raise TypeError("lifecycledata_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(lifecycledata_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ReasonsOfChange(GeneratedSubmodelElementList):

                class Reasonsofchange_item(aas.SubmodelElementCollection):

                    class ReasonClassificationSystem(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ReasonClassificationSystem",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r'Note: Examples for common names for classification systems are "VDMA24903" or "ECLASS".'
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABF813#002"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VersionOfClassificationSystem(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"VersionOfClassificationSystem",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Common version identifier of the used classification system, in order to distinguish different version of the property dictionary.  Note: Casing is to be ignored.",
                                        r"de": r"Note: 4 digit year of publication date of classifcation standard can serve as version.",
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAR710#002"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ReasonId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ReasonId",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: Ideally, the Property/valueId is used to reference the IRI/ IRDI of the reason id given by ECLASS."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABG774#002"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "semantic_id": global_ref(r"0173-1#02-ABI296#002/0173-1#01-AHE585#002"),
                        }

                    def __init__(
                        self,
                        reasonClassificationSystem: Union[str, ReasonClassificationSystem],
                        reasonId: Union[str, ReasonId],
                        versionOfClassificationSystem: Optional[Union[str, VersionOfClassificationSystem]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if reasonClassificationSystem is not None and not isinstance(
                            reasonClassificationSystem, aas.SubmodelElement
                        ):
                            reasonClassificationSystem = self.ReasonClassificationSystem(reasonClassificationSystem)

                        # Build a submodel element if a raw value was passed in the argument

                        if versionOfClassificationSystem is not None and not isinstance(
                            versionOfClassificationSystem, aas.SubmodelElement
                        ):
                            versionOfClassificationSystem = self.VersionOfClassificationSystem(
                                versionOfClassificationSystem
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if reasonId is not None and not isinstance(reasonId, aas.SubmodelElement):
                            reasonId = self.ReasonId(reasonId)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            reasonClassificationSystem, versionOfClassificationSystem, reasonId
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"ReasonsOfChange",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABI296#002/0173-1#01-AHE585#002"),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Multiple classification systems might be used. Constraint: At least one reason according VDM24903 shall be given."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI296#002"),
                    }

                def __init__(
                    self,
                    reasonsofchange_items: Iterable[Reasonsofchange_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(reasonsofchange_items, str):
                        raise TypeError("reasonsofchange_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(reasonsofchange_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ItemCategories(GeneratedSubmodelElementList):

                class Itemcategories_item(aas.SubmodelElementCollection):

                    class ItemClassificationSystem(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ItemClassificationSystem",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r'Note: Examples for common names for classification systems are "VDMA24903".'
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/ItemCategory/ItemClassificationSystem/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VersionOfClassificationSystem(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"VersionOfClassificationSystem",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Common version identifier of the used classification system, in order to distinguish different version of the property dictionary.  Note: Casing is to be ignored.",
                                        r"de": r"Note: 4 digit year of publication data of classifcation standard can serve as version.",
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAR710#002"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ItemCategory(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ItemCategory",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: Ideally, the Property/valueId is used to reference the IRI/ IRDI of the reason id given by ECLASS."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/ItemCategory/ItemCategory/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/ItemCategory/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        itemClassificationSystem: Union[str, ItemClassificationSystem],
                        itemCategory: Union[str, ItemCategory],
                        versionOfClassificationSystem: Optional[Union[str, VersionOfClassificationSystem]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if itemClassificationSystem is not None and not isinstance(
                            itemClassificationSystem, aas.SubmodelElement
                        ):
                            itemClassificationSystem = self.ItemClassificationSystem(itemClassificationSystem)

                        # Build a submodel element if a raw value was passed in the argument

                        if versionOfClassificationSystem is not None and not isinstance(
                            versionOfClassificationSystem, aas.SubmodelElement
                        ):
                            versionOfClassificationSystem = self.VersionOfClassificationSystem(
                                versionOfClassificationSystem
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if itemCategory is not None and not isinstance(itemCategory, aas.SubmodelElement):
                            itemCategory = self.ItemCategory(itemCategory)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            itemClassificationSystem, versionOfClassificationSystem, itemCategory
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"ItemCategories",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/ItemCategory/1/0"
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Multiple classification systems might be used. Constraint: At least one item category according VDM24903 shall be given."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/ItemCategory/List/1/0"
                        ),
                    }

                def __init__(
                    self,
                    itemcategories_items: Iterable[Itemcategories_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(itemcategories_items, str):
                        raise TypeError("itemcategories_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(itemcategories_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class AffectedPartNumbers(GeneratedSubmodelElementList):

                class Affectedpartnumbers_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": "Note: This Property codes only part number (\"12345\"), a set of part numbers (\"12345;23456;34567\"), a range of part numbers(\"10000-19999\"). For each of these, wildcards like asterix (\"1*8\", all numbers starting with '1' and ending with '8') or question mark (\"1?3?8\", all 5 digit numbers starting with '1' and ending with '8' and middle as '5') are allowed."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/AffectedPartNumber/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"AffectedPartNumbers",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/AffectedPartNumber/1/0"
                        ),
                        "value_type_list_element": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Constraint: Affected part numbers shall only be listed, if not the full range of part numbers produced for this item (product family and designation) is affected. Note: Multiple single part numbers with wildcards or ranges of part numbers are listed."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/AffectedPartNumber/List/1/0"
                        ),
                    }

                def __init__(
                    self,
                    affectedpartnumbers_items: Optional[Iterable[Union[str, Affectedpartnumbers_item]]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(affectedpartnumbers_items, str):
                        raise TypeError("affectedpartnumbers_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if affectedpartnumbers_items:
                        affectedpartnumbers_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Affectedpartnumbers_item(i)
                            for i in affectedpartnumbers_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        affectedpartnumbers_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class PcnReasonComment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"PcnReasonComment",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: May be substituted by PcnChangeInformation"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABF814#002"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PcnChangeInformation(aas.SubmodelElementCollection):

                class ChangeTitle(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ChangeTitle",
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/PcnChangeInformation/ChangeTitle/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ChangeDetail(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ChangeDetail",
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/PcnChangeInformation/ChangeDetail/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"PcnChangeInformation",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/PcnChangeInformation/1/0"
                        ),
                    }

                def __init__(
                    self,
                    changeTitle: Union[aas.MultiLanguageTextType, ChangeTitle],
                    changeDetail: Union[aas.MultiLanguageTextType, ChangeDetail],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if changeTitle is not None and not isinstance(changeTitle, aas.SubmodelElement):
                        changeTitle = self.ChangeTitle(changeTitle)

                    # Build a submodel element if a raw value was passed in the argument

                    if changeDetail is not None and not isinstance(changeDetail, aas.SubmodelElement):
                        changeDetail = self.ChangeDetail(changeDetail)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(changeTitle, changeDetail)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class AdditionalInformation(GeneratedSubmodelElementList):

                class Additionalinformation_item(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Note: This File element can be used to attach the conventional "product change information" already provided by many suppliers or e.g. some detail geometry information.'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/AdditionalInformation/AdditionalInformation/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/octet-stream",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"AdditionalInformation",
                        "type_value_list_element": aas.File,
                        "semantic_id_list_element": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/AdditionalInformation/AdditionalInformation/1/0"
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'Note: Suppliers are encouraged to add the conventional "product change information" documents and further details, e.g. photo-based or geometric change information to the PCN record.'
                            }
                        ),
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/AdditionalInformation/List/1/0"
                        ),
                    }

                def __init__(
                    self,
                    additionalinformation_items: Optional[Iterable[Additionalinformation_item]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(additionalinformation_items, str):
                        raise TypeError("additionalinformation_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        additionalinformation_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class DateOfRecord(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfRecord",
                        "value_type": xsd.DateTime,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Date is in UTC (coordinated universal time). Typically, time is given, as well."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABF816#003"),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ItemOfChange(aas.SubmodelElementCollection):

                class ManufacturerProductFamily(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ManufacturerProductFamily",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: mandatory property according to EU Machine Directive 2006/42/EC."}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAU731#003"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ManufacturerProductDesignation(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ManufacturerProductDesignation",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: mandatory property according to EU Machine Directive 2006/42/EC."}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAW338#002"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class OrderCodeOfManufacturer(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"OrderCodeOfManufacturer",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: Optional, as it might not exist for long term used items."}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAO227#004"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ManufacturerAssetID(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ManufacturerAssetID",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: This can be used to easily retrieve further information on the described item, such as full technical data, documentation, MCAD or ECAD models."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABG775#002"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProductClassifications(GeneratedSubmodelElementList):

                    class Productclassifications_item(aas.SubmodelElementCollection):

                        class ClassificationSystem(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ClassificationSystem",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"0173-1#02-AAR709#002"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class VersionOfClassificationSystem(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"VersionOfClassificationSystem",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r'Common version identifier of the used classification system, in order to distinguish different version of the property dictionary.  Note: Casing is to be ignored. Note: the SMT "Technical Data" refers to this as: [IRI] https://admin-shell.io/ZVEI/TechnicalData/ClassificationSystemVersion/1/1'
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAR710#002"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ProductClassId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ProductClassId",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r'Note: Ideally, the Property/valueId is used to reference the IRI/ IRDI of the product class. Note: the SMT "Technical Data" refers to this as: [IRI] https://admin-shell.io/ZVEI/TechnicalData/ProductClassId/1/1'
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABG776#002"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "semantic_id": global_ref(r"0173-1#02-ABI298#002/0173-1#01-AHE587#002"),
                            }

                        def __init__(
                            self,
                            classificationSystem: Union[str, ClassificationSystem],
                            productClassId: Union[str, ProductClassId],
                            versionOfClassificationSystem: Optional[Union[str, VersionOfClassificationSystem]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if classificationSystem is not None and not isinstance(
                                classificationSystem, aas.SubmodelElement
                            ):
                                classificationSystem = self.ClassificationSystem(classificationSystem)

                            # Build a submodel element if a raw value was passed in the argument

                            if versionOfClassificationSystem is not None and not isinstance(
                                versionOfClassificationSystem, aas.SubmodelElement
                            ):
                                versionOfClassificationSystem = self.VersionOfClassificationSystem(
                                    versionOfClassificationSystem
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if productClassId is not None and not isinstance(productClassId, aas.SubmodelElement):
                                productClassId = self.ProductClassId(productClassId)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                classificationSystem, versionOfClassificationSystem, productClassId
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ProductClassifications",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id_list_element": global_ref(r"0173-1#02-ABI298#002/0173-1#01-AHE587#002"),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: It is encouraged to provide the actual product classficiation, e.g. by ECLASS, in order to ease the identification of relevant items by the industrial user."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABI298#002"),
                        }

                    def __init__(
                        self,
                        productclassifications_items: Optional[Iterable[Productclassifications_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(productclassifications_items, str):
                            raise TypeError("productclassifications_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            productclassifications_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class HardwareVersion(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"HardwareVersion",
                            "value_type": str,
                            "semantic_id": global_ref(r"0173-1#02-AAN270#003"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class RemainingAmountAvailable(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"RemainingAmountAvailable",
                            "value_type": xsd.PositiveInteger,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: This is an indicative figure; the manufacturer/ supplier may use a heuristical model to distribute available stock to a forecasted number of industrial users. Useful for industrial users to assess individual need of products against assumed availability."
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-BAF551#004"),
                        }

                    def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TechnicalData_Changes(GeneratedSubmodelElementList):

                    class Technicaldata_changes_item(aas.SubmodelElementCollection):

                        class Arbitrary(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Arbitrary",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": "Note: An arbitrary Property, MLP, Range-element can be placed in this structure with arbitrary semanticId. It is marked by the supplementalSemanticId for 'new value'."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                                    "supplemental_semantic_id": (
                                        global_ref(
                                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/TechnicalData_Changes/NewValue/1/0"
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class OriginOfChange(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": r"OriginOfChange",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Note: The set of technical data in the definition refers to the Submodel for technical data in the AAS."
                                        }
                                    ),
                                    "semantic_id": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                                value=r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/TechnicalData_Changes/OriginOfChange/1/0",
                                            ),
                                        ),
                                        type_=aas.ConceptDescription,
                                        referred_semantic_id=None,
                                    ),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ReasonId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ReasonId",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Note: Ideally, the Property/valueId is used to reference the IRI/ IRDI of the reason id given by ECLASS."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABG774#002"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: This SMC can be added to annotate changes in DataElements of existing Submodels (e.g. for technical data) and to provide more specific information to reason and items of a VDMA 24903 change."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/TechnicalData_Changes/Change/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            arbitrary: Optional[Union[str, Arbitrary]] = None,
                            originOfChange: Optional[Union[aas.Reference, OriginOfChange]] = None,
                            reasonId: Optional[Union[str, ReasonId]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if arbitrary is not None and not isinstance(arbitrary, aas.SubmodelElement):
                                arbitrary = self.Arbitrary(arbitrary)

                            # Build a submodel element if a raw value was passed in the argument

                            if originOfChange is not None and not isinstance(originOfChange, aas.SubmodelElement):
                                originOfChange = self.OriginOfChange(originOfChange)

                            # Build a submodel element if a raw value was passed in the argument

                            if reasonId is not None and not isinstance(reasonId, aas.SubmodelElement):
                                reasonId = self.ReasonId(reasonId)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(arbitrary, originOfChange, reasonId)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"TechnicalData_Changes",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id_list_element": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/TechnicalData_Changes/Change/1/0"
                            ),
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/TechnicalData_Changes/List/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        technicaldata_changes_items: Optional[Iterable[Technicaldata_changes_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(technicaldata_changes_items, str):
                            raise TypeError("technicaldata_changes_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            technicaldata_changes_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class TechnicalData_CurrentState(aas.SubmodelElementCollection):

                    class Arbitrary(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Arbitrary",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: Each DataElement represents a change of a technical data element. DataElements such as Property, MultiLanguageProperty and Range are applicable. To bring about the information, both idShort and semanticId can be set to the resepctive {arbitrary} attribute of the corresponding  technical data element."
                                    }
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"TechnicalData_CurrentState",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: For the recommended items, the technical data elements are individually grouped in fit, form, function, other. As different alternatives might engange different groupings, the respective technical data elements of the item of change are not grouped, at all. Note: If possible, technical data elements in the recommended items should find its counterparts here (that is: DataElement with identical semanticId)."
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/TechnicalData_CurrentState/List/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(
                        self,
                        arbitrary: Optional[Iterable[Union[str, Arbitrary]]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(arbitrary, str):
                            raise TypeError("arbitrary takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if arbitrary:
                            arbitrary = [
                                i if isinstance(i, aas.SubmodelElement) else self.Arbitrary(i) for i in arbitrary
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(arbitrary)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ItemOfChange",
                        "semantic_id": global_ref(r"0173-1#02-ABI297#003/0173-1#01-AHE586#003"),
                    }

                def __init__(
                    self,
                    manufacturerProductFamily: Union[aas.MultiLanguageTextType, ManufacturerProductFamily],
                    manufacturerProductDesignation: Union[aas.MultiLanguageTextType, ManufacturerProductDesignation],
                    orderCodeOfManufacturer: Optional[Union[aas.MultiLanguageTextType, OrderCodeOfManufacturer]] = None,
                    manufacturerAssetID: Optional[Union[aas.Reference, ManufacturerAssetID]] = None,
                    productClassifications: Optional[
                        Union[Iterable[ProductClassifications.Productclassifications_item], ProductClassifications]
                    ] = None,
                    hardwareVersion: Optional[Union[str, HardwareVersion]] = None,
                    remainingAmountAvailable: Optional[Union[xsd.PositiveInteger, RemainingAmountAvailable]] = None,
                    technicalData_Changes: Optional[
                        Union[Iterable[TechnicalData_Changes.Technicaldata_changes_item], TechnicalData_Changes]
                    ] = None,
                    technicalData_CurrentState: Optional[TechnicalData_CurrentState] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if manufacturerProductFamily is not None and not isinstance(
                        manufacturerProductFamily, aas.SubmodelElement
                    ):
                        manufacturerProductFamily = self.ManufacturerProductFamily(manufacturerProductFamily)

                    # Build a submodel element if a raw value was passed in the argument

                    if manufacturerProductDesignation is not None and not isinstance(
                        manufacturerProductDesignation, aas.SubmodelElement
                    ):
                        manufacturerProductDesignation = self.ManufacturerProductDesignation(
                            manufacturerProductDesignation
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if orderCodeOfManufacturer is not None and not isinstance(
                        orderCodeOfManufacturer, aas.SubmodelElement
                    ):
                        orderCodeOfManufacturer = self.OrderCodeOfManufacturer(orderCodeOfManufacturer)

                    # Build a submodel element if a raw value was passed in the argument

                    if manufacturerAssetID is not None and not isinstance(manufacturerAssetID, aas.SubmodelElement):
                        manufacturerAssetID = self.ManufacturerAssetID(manufacturerAssetID)

                    # A str would be split into its characters
                    if isinstance(productClassifications, str):
                        raise TypeError("productClassifications takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if productClassifications is not None and not isinstance(
                        productClassifications, aas.SubmodelElement
                    ):
                        productClassifications = self.ProductClassifications(productClassifications)

                    # Build a submodel element if a raw value was passed in the argument

                    if hardwareVersion is not None and not isinstance(hardwareVersion, aas.SubmodelElement):
                        hardwareVersion = self.HardwareVersion(hardwareVersion)

                    # Build a submodel element if a raw value was passed in the argument

                    if remainingAmountAvailable is not None and not isinstance(
                        remainingAmountAvailable, aas.SubmodelElement
                    ):
                        remainingAmountAvailable = self.RemainingAmountAvailable(remainingAmountAvailable)

                    # A str would be split into its characters
                    if isinstance(technicalData_Changes, str):
                        raise TypeError("technicalData_Changes takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if technicalData_Changes is not None and not isinstance(technicalData_Changes, aas.SubmodelElement):
                        technicalData_Changes = self.TechnicalData_Changes(technicalData_Changes)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        manufacturerProductFamily,
                        manufacturerProductDesignation,
                        orderCodeOfManufacturer,
                        manufacturerAssetID,
                        productClassifications,
                        hardwareVersion,
                        remainingAmountAvailable,
                        technicalData_Changes,
                        technicalData_CurrentState,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class RecommendedItems(GeneratedSubmodelElementList):

                class Recommendeditems_item(aas.SubmodelElementCollection):

                    class ManufacturerProductFamily(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"ManufacturerProductFamily",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: mandatory property according to EU Machine Directive 2006/42/EC."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAU731#003"),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ManufacturerProductDesignation(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"ManufacturerProductDesignation",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: mandatory property according to EU Machine Directive 2006/42/EC."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAW338#002"),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class OrderCodeOfManufacturer(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"OrderCodeOfManufacturer",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Note: Mandatory, as required to order."}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAO227#004"),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ProductClassifications(GeneratedSubmodelElementList):

                        class Productclassifications_item(aas.SubmodelElementCollection):

                            class ClassificationSystem(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"ClassificationSystem",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"0173-1#02-AAR709#002"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class VersionOfClassificationSystem(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"VersionOfClassificationSystem",
                                        "value_type": str,
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r'Common version identifier of the used classification system, in order to distinguish different version of the property dictionary.  Note: Casing is to be ignored. Note: the SMT "Technical Data" refers to this as: [IRI] https://admin-shell.io/ZVEI/TechnicalData/ClassificationSystemVersion/1/1'
                                            }
                                        ),
                                        "semantic_id": global_ref(r"0173-1#02-AAR710#002"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class ProductClassId(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"ProductClassId",
                                        "value_type": str,
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r'Note: Ideally, the Property/valueId is used to reference the IRI/ IRDI of the product class. Note: the SMT "Technical Data" refers to this as: [IRI] https://admin-shell.io/ZVEI/TechnicalData/ProductClassId/1/1'
                                            }
                                        ),
                                        "semantic_id": global_ref(r"0173-1#02-ABG776#002"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": None,
                                    "semantic_id": global_ref(r"0173-1#02-ABI298#002/0173-1#01-AHE587#002"),
                                }

                            def __init__(
                                self,
                                classificationSystem: Union[str, ClassificationSystem],
                                versionOfClassificationSystem: Union[str, VersionOfClassificationSystem],
                                productClassId: Union[str, ProductClassId],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if classificationSystem is not None and not isinstance(
                                    classificationSystem, aas.SubmodelElement
                                ):
                                    classificationSystem = self.ClassificationSystem(classificationSystem)

                                # Build a submodel element if a raw value was passed in the argument

                                if versionOfClassificationSystem is not None and not isinstance(
                                    versionOfClassificationSystem, aas.SubmodelElement
                                ):
                                    versionOfClassificationSystem = self.VersionOfClassificationSystem(
                                        versionOfClassificationSystem
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if productClassId is not None and not isinstance(productClassId, aas.SubmodelElement):
                                    productClassId = self.ProductClassId(productClassId)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    classificationSystem, versionOfClassificationSystem, productClassId
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"ProductClassifications",
                                "type_value_list_element": aas.SubmodelElementCollection,
                                "semantic_id_list_element": global_ref(r"0173-1#02-ABI298#002/0173-1#01-AHE587#002"),
                                "semantic_id": global_ref(r"0173-1#02-ABI298#002"),
                            }

                        def __init__(
                            self,
                            productclassifications_items: Optional[Iterable[Productclassifications_item]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(productclassifications_items, str):
                                raise TypeError("productclassifications_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                productclassifications_items, number_repeated=False
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class TechnicalData_Fit(aas.SubmodelElementCollection):

                        class TargetEstimate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TargetEstimate",
                                    "value_type": xsd.Float,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Note: It is the suppliers role to assess the provided technical data elements of the recommended item with respect to the actual item of change. A percentage is given between 0% (totally not suitable at all) and 100% (equal performance to the actual item of change)."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABG777#003"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Arbitrary(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Arbitrary",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Arbitrary Property, MLP or Range elements with specific semanticIds might be added."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"TechnicalData_Fit",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: it is recommended that the selected property types for the recommended items are matching to the provided properties if the item of change to allow a one-by-one comparison of items. Note: the manufacturers are recommended to select only those property types, which support a meaningful comparison of the recommendation with the item of change. To many property types are considered to increase the signal/ noise ratio of information."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABI299#003/0173-1#01-AHE588#003"),
                            }

                        def __init__(
                            self,
                            arbitrary: Union[str, Arbitrary],
                            targetEstimate: Optional[Union[xsd.Float, TargetEstimate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if targetEstimate is not None and not isinstance(targetEstimate, aas.SubmodelElement):
                                targetEstimate = self.TargetEstimate(targetEstimate)

                            # Build a submodel element if a raw value was passed in the argument

                            if arbitrary is not None and not isinstance(arbitrary, aas.SubmodelElement):
                                arbitrary = self.Arbitrary(arbitrary)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(targetEstimate, arbitrary)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class TechnicalData_Form(aas.SubmodelElementCollection):

                        class TargetEstimate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TargetEstimate",
                                    "value_type": xsd.Float,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Note: It is the suppliers role to assess the provided technical data elements of the recommended item with respect to the actual item of change. A percentage is given between 0% (totally not suitable at all) and 100% (equal performance to the actual item of change)."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABG777#003"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Arbitrary(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Arbitrary",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Arbitrary Property, MLP or Range elements with specific semanticIds might be added."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"TechnicalData_Form",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: it is recommended that the selected property types for the recommended items are matching to the provided properties if the item of change to allow a one-by-one comparison of items. Note: the manufacturers are recommended to select only those property types, which support a meaningful comparison of the recommendation with the item of change. To many property types are considered to increase the signal/ noise ratio of information."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABI300#003/0173-1#01-AHE589#003"),
                            }

                        def __init__(
                            self,
                            arbitrary: Union[str, Arbitrary],
                            targetEstimate: Optional[Union[xsd.Float, TargetEstimate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if targetEstimate is not None and not isinstance(targetEstimate, aas.SubmodelElement):
                                targetEstimate = self.TargetEstimate(targetEstimate)

                            # Build a submodel element if a raw value was passed in the argument

                            if arbitrary is not None and not isinstance(arbitrary, aas.SubmodelElement):
                                arbitrary = self.Arbitrary(arbitrary)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(targetEstimate, arbitrary)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class TechnicalData_Function(aas.SubmodelElementCollection):

                        class TargetEstimate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TargetEstimate",
                                    "value_type": xsd.Float,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Note: It is the suppliers role to assess the provided technical data elements of the recommended item with respect to the actual item of change. A percentage is given between 0% (totally not suitable at all) and 100% (equal performance to the actual item of change)."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABG777#003"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Arbitrary(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Arbitrary",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Arbitrary Property, MLP or Range elements with specific semanticIds might be added."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"TechnicalData_Function",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: it is recommended that the selected property types for the recommended items are matching to the provided properties if the item of change to allow a one-by-one comparison of items. Note: the manufacturers are recommended to select only those property types, which support a meaningful comparison of the recommendation with the item of change. To many property types are considered to increase the signal/ noise ratio of information."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABI301#003/0173-1#01-AHE590#003"),
                            }

                        def __init__(
                            self,
                            arbitrary: Union[str, Arbitrary],
                            targetEstimate: Optional[Union[xsd.Float, TargetEstimate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if targetEstimate is not None and not isinstance(targetEstimate, aas.SubmodelElement):
                                targetEstimate = self.TargetEstimate(targetEstimate)

                            # Build a submodel element if a raw value was passed in the argument

                            if arbitrary is not None and not isinstance(arbitrary, aas.SubmodelElement):
                                arbitrary = self.Arbitrary(arbitrary)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(targetEstimate, arbitrary)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class TechnicalData_Other(aas.SubmodelElementCollection):

                        class TargetEstimate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TargetEstimate",
                                    "value_type": xsd.Float,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Note: It is the suppliers role to assess the provided technical data elements of the recommended item with respect to the actual item of change. A percentage is given between 0% (totally not suitable at all) and 100% (equal performance to the actual item of change)."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABG777#003"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Arbitrary(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Arbitrary",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Arbitrary Property, MLP or Range elements with specific semanticIds might be added."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"TechnicalData_Other",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Note: the manufacturers are recommended to select only those property types, which support a meaningful comparison of the recommendation with the item of change. To many property types are considered to increase the signal/ noise ratio of information. Note: the SMC TechnicalData_Other is supposed to comprise meaningful property instances, which do not fit into the categorries fit, form, function."
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABI302#003/0173-1#01-AHE591#003"),
                            }

                        def __init__(
                            self,
                            arbitrary: Union[str, Arbitrary],
                            targetEstimate: Optional[Union[xsd.Float, TargetEstimate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if targetEstimate is not None and not isinstance(targetEstimate, aas.SubmodelElement):
                                targetEstimate = self.TargetEstimate(targetEstimate)

                            # Build a submodel element if a raw value was passed in the argument

                            if arbitrary is not None and not isinstance(arbitrary, aas.SubmodelElement):
                                arbitrary = self.Arbitrary(arbitrary)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(targetEstimate, arbitrary)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class IncotermCode(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"IncotermCode",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Note: see https://en.wikipedia.org/wiki/Incoterms"}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAO280#004"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DeliveryTimeClassOtherRegion(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DeliveryTimeClassOtherRegion",
                                "value_type": xsd.Int,
                                "semantic_id": global_ref(r"0173-1#02-ABG779#003"),
                            }

                        def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DeliveryTimeClassSameRegion(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DeliveryTimeClassSameRegion",
                                "value_type": xsd.Int,
                                "semantic_id": global_ref(r"0173-1#02-ABG778#003"),
                            }

                        def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ConformityDeclarations(aas.SubmodelElementCollection):

                        class Arbitrary(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Arbitrary",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Arbitrary SubmodelElements with specific semanticIds might be added."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"ConformityDeclarations",
                                "semantic_id": global_ref(r"0173-1#02-ABI303#003/0173-1#01-AHE592#003"),
                            }

                        def __init__(
                            self, arbitrary: Union[str, Arbitrary], **kwargs: Unpack[SubmodelElementCollectionMetadata]
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if arbitrary is not None and not isinstance(arbitrary, aas.SubmodelElement):
                                arbitrary = self.Arbitrary(arbitrary)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(arbitrary)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "semantic_id": global_ref(
                                r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/RecommendedItem/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        manufacturerProductFamily: Union[aas.MultiLanguageTextType, ManufacturerProductFamily],
                        manufacturerProductDesignation: Union[
                            aas.MultiLanguageTextType, ManufacturerProductDesignation
                        ],
                        orderCodeOfManufacturer: Union[aas.MultiLanguageTextType, OrderCodeOfManufacturer],
                        productClassifications: Optional[
                            Union[Iterable[ProductClassifications.Productclassifications_item], ProductClassifications]
                        ] = None,
                        technicalData_Fit: Optional[TechnicalData_Fit] = None,
                        technicalData_Form: Optional[TechnicalData_Form] = None,
                        technicalData_Function: Optional[TechnicalData_Function] = None,
                        technicalData_Other: Optional[TechnicalData_Other] = None,
                        incotermCode: Optional[Union[str, IncotermCode]] = None,
                        deliveryTimeClassOtherRegion: Optional[Union[xsd.Int, DeliveryTimeClassOtherRegion]] = None,
                        deliveryTimeClassSameRegion: Optional[Union[xsd.Int, DeliveryTimeClassSameRegion]] = None,
                        conformityDeclarations: Optional[ConformityDeclarations] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if manufacturerProductFamily is not None and not isinstance(
                            manufacturerProductFamily, aas.SubmodelElement
                        ):
                            manufacturerProductFamily = self.ManufacturerProductFamily(manufacturerProductFamily)

                        # Build a submodel element if a raw value was passed in the argument

                        if manufacturerProductDesignation is not None and not isinstance(
                            manufacturerProductDesignation, aas.SubmodelElement
                        ):
                            manufacturerProductDesignation = self.ManufacturerProductDesignation(
                                manufacturerProductDesignation
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if orderCodeOfManufacturer is not None and not isinstance(
                            orderCodeOfManufacturer, aas.SubmodelElement
                        ):
                            orderCodeOfManufacturer = self.OrderCodeOfManufacturer(orderCodeOfManufacturer)

                        # A str would be split into its characters
                        if isinstance(productClassifications, str):
                            raise TypeError("productClassifications takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if productClassifications is not None and not isinstance(
                            productClassifications, aas.SubmodelElement
                        ):
                            productClassifications = self.ProductClassifications(productClassifications)

                        # Build a submodel element if a raw value was passed in the argument

                        if incotermCode is not None and not isinstance(incotermCode, aas.SubmodelElement):
                            incotermCode = self.IncotermCode(incotermCode)

                        # Build a submodel element if a raw value was passed in the argument

                        if deliveryTimeClassOtherRegion is not None and not isinstance(
                            deliveryTimeClassOtherRegion, aas.SubmodelElement
                        ):
                            deliveryTimeClassOtherRegion = self.DeliveryTimeClassOtherRegion(
                                deliveryTimeClassOtherRegion
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if deliveryTimeClassSameRegion is not None and not isinstance(
                            deliveryTimeClassSameRegion, aas.SubmodelElement
                        ):
                            deliveryTimeClassSameRegion = self.DeliveryTimeClassSameRegion(deliveryTimeClassSameRegion)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            manufacturerProductFamily,
                            manufacturerProductDesignation,
                            orderCodeOfManufacturer,
                            productClassifications,
                            technicalData_Fit,
                            technicalData_Form,
                            technicalData_Function,
                            technicalData_Other,
                            incotermCode,
                            deliveryTimeClassOtherRegion,
                            deliveryTimeClassSameRegion,
                            conformityDeclarations,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"RecommendedItems",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/RecommendedItem/1/0"
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The supplier is encoraged to provide recommended items."}
                        ),
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/RecommendedItem/List/1/0"
                        ),
                    }

                def __init__(
                    self,
                    recommendeditems_items: Optional[Iterable[Recommendeditems_item]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(recommendeditems_items, str):
                        raise TypeError("recommendeditems_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        recommendeditems_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {"id_short": None, "semantic_id": global_ref(r"0173-1#02-ABI294#003/0173-1#01-AHE583#003")}

            def __init__(
                self,
                manufacturer: Manufacturer,
                pcnType: Union[str, PcnType],
                reasonsOfChange: Union[Iterable[ReasonsOfChange.Reasonsofchange_item], ReasonsOfChange],
                itemCategories: Union[Iterable[ItemCategories.Itemcategories_item], ItemCategories],
                pcnChangeInformation: PcnChangeInformation,
                dateOfRecord: Union[xsd.DateTime, DateOfRecord],
                itemOfChange: ItemOfChange,
                manufacturerChangeID: Optional[Union[str, ManufacturerChangeID]] = None,
                lifeCycleData: Optional[Union[Iterable[LifeCycleData.Lifecycledata_item], LifeCycleData]] = None,
                affectedPartNumbers: Optional[
                    Union[Iterable[Union[str, AffectedPartNumbers.Affectedpartnumbers_item]], AffectedPartNumbers]
                ] = None,
                pcnReasonComment: Optional[Union[aas.MultiLanguageTextType, PcnReasonComment]] = None,
                additionalInformation: Optional[
                    Union[Iterable[AdditionalInformation.Additionalinformation_item], AdditionalInformation]
                ] = None,
                recommendedItems: Optional[
                    Union[Iterable[RecommendedItems.Recommendeditems_item], RecommendedItems]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if manufacturerChangeID is not None and not isinstance(manufacturerChangeID, aas.SubmodelElement):
                    manufacturerChangeID = self.ManufacturerChangeID(manufacturerChangeID)

                # Build a submodel element if a raw value was passed in the argument

                if pcnType is not None and not isinstance(pcnType, aas.SubmodelElement):
                    pcnType = self.PcnType(pcnType)

                # A str would be split into its characters
                if isinstance(lifeCycleData, str):
                    raise TypeError("lifeCycleData takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if lifeCycleData is not None and not isinstance(lifeCycleData, aas.SubmodelElement):
                    lifeCycleData = self.LifeCycleData(lifeCycleData)

                # A str would be split into its characters
                if isinstance(reasonsOfChange, str):
                    raise TypeError("reasonsOfChange takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if reasonsOfChange is not None and not isinstance(reasonsOfChange, aas.SubmodelElement):
                    reasonsOfChange = self.ReasonsOfChange(reasonsOfChange)

                # A str would be split into its characters
                if isinstance(itemCategories, str):
                    raise TypeError("itemCategories takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if itemCategories is not None and not isinstance(itemCategories, aas.SubmodelElement):
                    itemCategories = self.ItemCategories(itemCategories)

                # A str would be split into its characters
                if isinstance(affectedPartNumbers, str):
                    raise TypeError("affectedPartNumbers takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if affectedPartNumbers is not None and not isinstance(affectedPartNumbers, aas.SubmodelElement):
                    affectedPartNumbers = self.AffectedPartNumbers(affectedPartNumbers)

                # Build a submodel element if a raw value was passed in the argument

                if pcnReasonComment is not None and not isinstance(pcnReasonComment, aas.SubmodelElement):
                    pcnReasonComment = self.PcnReasonComment(pcnReasonComment)

                # A str would be split into its characters
                if isinstance(additionalInformation, str):
                    raise TypeError("additionalInformation takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if additionalInformation is not None and not isinstance(additionalInformation, aas.SubmodelElement):
                    additionalInformation = self.AdditionalInformation(additionalInformation)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfRecord is not None and not isinstance(dateOfRecord, aas.SubmodelElement):
                    dateOfRecord = self.DateOfRecord(dateOfRecord)

                # A str would be split into its characters
                if isinstance(recommendedItems, str):
                    raise TypeError("recommendedItems takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if recommendedItems is not None and not isinstance(recommendedItems, aas.SubmodelElement):
                    recommendedItems = self.RecommendedItems(recommendedItems)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    manufacturer,
                    manufacturerChangeID,
                    pcnType,
                    lifeCycleData,
                    reasonsOfChange,
                    itemCategories,
                    affectedPartNumbers,
                    pcnReasonComment,
                    pcnChangeInformation,
                    additionalInformation,
                    dateOfRecord,
                    itemOfChange,
                    recommendedItems,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"Records",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#02-ABI294#003/0173-1#01-AHE583#003"),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Note: Newer records shall be added by adding a new highest index to the list."}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABI294#003"),
            }

        def __init__(
            self, records_items: Optional[Iterable[Records_item]] = None, **kwargs: Unpack[SubmodelElementListMetadata]
        ):

            # A str would be split into its characters
            if isinstance(records_items, str):
                raise TypeError("records_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(records_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ProductChangeNotifications",
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta_02036",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"0173-1#01-AHE582#003"),
        }

    def __init__(
        self,
        id_: str,
        pcnEventsOutgoing: Optional[PcnEventsOutgoing] = None,
        records: Optional[Union[Iterable[Records.Records_item], Records]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(records, str):
            raise TypeError("records takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if records is not None and not isinstance(records, aas.SubmodelElement):
            records = self.Records(records)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(pcnEventsOutgoing, records)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
