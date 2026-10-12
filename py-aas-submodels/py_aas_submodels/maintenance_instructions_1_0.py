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


class MaintenanceInstructions(aas.Submodel):

    class MaintenanceFreeAsset(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"MaintenanceFreeAsset",
                "value_type": bool,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"de": r"Festlegung, ob ein Asset wartungsfrei ist, oder eine Wartung benötigt. Bei einem wartungsfreien Asset Wert =True . Wird eine Wartung benötig Wert = False. Somit kann ausgeschlossen werden, dass ein Hersteller vergessen hat das SM Maintenance zu erstellen und der Anwender hat die Sicherheit, dass das Asset wartungsfrei ist. ",
                        r"en": r"Determines whether an asset is maintenance-free or requires maintenance. If an asset is maintenance-free, value = true. If maintenance is required, value = false. This excludes the possibility that a manufacturer has forgotten to create the SM Maintenance and the user has the certainty that the asset is maintenance-free. ",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/maintenanceinstructions/maintenancefreeasset/1/0"
                ),
            }

        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class MaintenanceInstructionsForSpecificInterval(aas.SubmodelElementCollection):

        class MaintenanceTechnicians(aas.SubmodelElementCollection):

            class NumberOfRequiredTechnicians(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NumberOfRequiredTechnicians",
                        "value_type": xsd.Decimal,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Anzahl der für die Wartung benötigten Techniker",
                                r"en": r"Number of technicians needed for maintenance",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/numberofrequiredtechnicians/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RequiredQualification(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"RequiredQualification",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Anforderung an die Mindestqualifikation der Techniker",
                                r"en": r"Requirement for the minimum qualification of technicians",
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-BAF831#002"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EstimatedTotalWorkingTime(aas.SubmodelElementCollection):

                class ValueTotalEstimatedWorkingTime(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ValueTotalEstimatedWorkingTime",
                            "value_type": xsd.Decimal,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Wert für die Dauer der gesamten Wartung",
                                    r"en": r"Value for the duration of the entire maintenance",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/valuetotalestimatedworkingtime/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class UnitValueTotalEstimatedWorkingTime(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"UnitValueTotalEstimatedWorkingTime",
                            "value_type": str,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Einheit für die Dauer der gesamten Wartung - Beispiel Stunden, Tage, Wochen",
                                    r"en": r"Unit for the duration of the entire maintenance - example hours, days, weeks",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/unitvaluetotalestimatedworkingtime/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"EstimatedTotalWorkingTime",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Sammlung, um den voraussichtlichen Zeitaufwand für die Durchführung der Wartung zu definieren",
                                r"en": r"Collection to define the expected time needed to perform the maintenance",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/estimatedtotalworkingtime/1/0"
                        ),
                    }

                def __init__(
                    self,
                    valueTotalEstimatedWorkingTime: Union[xsd.Decimal, ValueTotalEstimatedWorkingTime],
                    unitValueTotalEstimatedWorkingTime: Union[str, UnitValueTotalEstimatedWorkingTime],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if valueTotalEstimatedWorkingTime is not None and not isinstance(
                        valueTotalEstimatedWorkingTime, aas.SubmodelElement
                    ):
                        valueTotalEstimatedWorkingTime = self.ValueTotalEstimatedWorkingTime(
                            valueTotalEstimatedWorkingTime
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if unitValueTotalEstimatedWorkingTime is not None and not isinstance(
                        unitValueTotalEstimatedWorkingTime, aas.SubmodelElement
                    ):
                        unitValueTotalEstimatedWorkingTime = self.UnitValueTotalEstimatedWorkingTime(
                            unitValueTotalEstimatedWorkingTime
                        )

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        valueTotalEstimatedWorkingTime, unitValueTotalEstimatedWorkingTime
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"MaintenanceTechnicians",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Details zu den für die Wartung benötigten Technikern",
                            r"en": r"Details of the technicians required for maintenance",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/maintenanceinstructions/maintenancetechnicians/1/0"
                    ),
                }

            def __init__(
                self,
                numberOfRequiredTechnicians: Optional[Union[xsd.Decimal, NumberOfRequiredTechnicians]] = None,
                requiredQualification: Optional[
                    Iterable[Union[aas.MultiLanguageTextType, RequiredQualification]]
                ] = None,
                estimatedTotalWorkingTime: Optional[EstimatedTotalWorkingTime] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if numberOfRequiredTechnicians is not None and not isinstance(
                    numberOfRequiredTechnicians, aas.SubmodelElement
                ):
                    numberOfRequiredTechnicians = self.NumberOfRequiredTechnicians(numberOfRequiredTechnicians)

                # A str would be split into its characters
                if isinstance(requiredQualification, str):
                    raise TypeError("requiredQualification takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if requiredQualification:
                    requiredQualification = [
                        i if isinstance(i, aas.SubmodelElement) else self.RequiredQualification(i)
                        for i in requiredQualification
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    numberOfRequiredTechnicians, requiredQualification, estimatedTotalWorkingTime
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ListMaintenanceSteps(aas.SubmodelElementCollection):

            class MaintenanceStep(aas.SubmodelElementCollection):

                class MaintenanceStepID(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaintenanceStepID",
                            "value_type": str,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"ID oder Nummer des Wartungsschritts für eine klare Strukturierung der Wartung",
                                    r"en": r"ID or number of the maintenance step for a clear structuring of the maintenance",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/maintenancestepid/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaintenanceStepName(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"MaintenanceStepName",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Benennung des Wartungsschritt - Beispiel Wartungsstart",
                                    r"en": r"Naming of the maintenance step - example maintenance start",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/maintenancestepname/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalizationDescription(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"LocalizationDescription",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Angabe zur Lokalisierung des Wartungsschritts",
                                    r"en": r"Indication of the localization of the maintenance.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/localizationdescription/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LinkSMMaintenanceComponentModuleMachine(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"LinkSMMaintenanceComponentModuleMachine",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Link zu einem anderen SM Maintenance. Beispiel Link zum SM Maintenance eines Sensors in einer Maschine. Von hier kann somit in eine Wartungsinformation einer unterlagerten Komponente gesprungen werden.",
                                    r"en": r"Link to another SM Maintenance. Example Link to the SM Maintenance of a sensor in a machine. From here, it is possible to jump to the maintenance information of a subordinate component.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/linksmmaintenancecomponentmodulemachine/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LinkAASComponentModuleMachine(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"LinkAASComponentModuleMachine",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Link zu einer unterlagerten AAS. Beispiel Link zur Sensors in einer Maschine. Von hier kann somit zu den Inforamtionen einer unterlagerten Komponente gesprungen werden.",
                                    r"en": r"Link to a subordinate AAS. Example Link to the sensors in a machine. From here you can jump to the information of a subordinate component.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/linkaascomponentmodulemachine/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class InstructionMaintenanceStep(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"InstructionMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Arbeitsanweisung/ Beschreibung eines Wartungsschritts als Alternative zu dem Sprung in eine Wartungsinformation von unterlagerten Komponenten.",
                                    r"en": r"Work instruction/ description of a maintenance step as an alternative to jumping to a maintenance information of subordinate components.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/instructionmaintenancestep/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class RelatedDocumentOrFileMaintenanceStep(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"RelatedDocumentOrFileMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Verknüpfung von unterstützenden Dokumenten die zu diesem Wartungsschritt gehören",
                                    r"en": r"Linking of supporting documents that belong to this maintenance step.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/relateddocumentorfilemaintenancestep/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/pdf",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class SparePartForMaintenanceStep(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"SparePartForMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Link auf ein in diesem Wartungsschritt benötigtes Ersatzteils. Eine Liste aller benötigten Ersatzteile für eine Wartung befindet sich in der SMC SparePartList des SM Maintenance",
                                    r"en": r"Link to a spare part required in this maintenance step. A list of all the spare parts required for maintenance can be found in the SMC SparePartList of the SM Maintenance",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/sparepartformaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class QuantityOfSparePartForMaintenanceStep(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QuantityOfSparePartForMaintenanceStep",
                            "value_type": xsd.Decimal,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Nummer des in diesem Wartungsschritt benötigten Ersatzteils.",
                                    r"en": r"Number of spare part required in this maintenance step.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/quantityofsparepartformaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ConsumablesForMaintenanceStep(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ConsumablesForMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Link auf ein benötigtes Verbrauchsmaterial.",
                                    r"en": r"Link to a required consumable.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/consumablesformaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class QuantityOfConsumablesForMaintenanceStep(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QuantityOfConsumablesForMaintenanceStep",
                            "value_type": xsd.Decimal,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Angabe zur benötigten Menge des unter ConsumablesForMaintenanceStep referenzierten Verbrauchmaterials für diesen Wartungsschritt",
                                    r"en": r"Indication of the required number of consumables referenced under ConsumablesForMaintenanceStep for this maintenance step.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/quantityofconsumablesformaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class UnitForQuantityOfConsumablesForMaintenanceStep(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"UnitForQuantityOfConsumablesForMaintenanceStep",
                            "value_type": str,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Einheit der benötigten Anzahl des unter ConsumablesForMaintenanceStep referenzierten Verbrauchmaterials für diesen Wartungsschritt. Beispiele: Blatt, Gramm, Milliliter",
                                    r"en": r"Unit of the required number of consumables referenced under ConsumablesForMaintenanceStep for this maintenance step. Examples: Sheet, gram, millilitre",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/unitforquantityofconsumablesformaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ToolsForMaintenanceStep(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ToolsForMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Verweis auf ein benötigtes Werkzeug. Eine Liste aller benötigten Ersatzteile für eine Wartung befindet sich in der SMC MaintenanceToolList des SM Maintenance",
                                    r"en": r"Reference to a required tool. A list of all required spare parts for a maintenance can be found in the SMC MaintenanceToolList of the SM Maintenance",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/toolsformaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class QuantityOfToolsForMaintenanceStep(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QuantityOfToolsForMaintenanceStep",
                            "value_type": xsd.Decimal,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Angabe zur benötigten Anzahl des unter ToolsForMaintenanceStep referenzierten Werkzeugs für diesen Wartungsschritt",
                                    r"en": r"Indication of the required number of the tool referenced under ToolsForMaintenanceStep for this maintenance step.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/quantityoftoolsformaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DocumentationSignatureMandatory(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DocumentationSignatureMandatory",
                            "value_type": bool,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Vorgabe, ob dieser Wartungsschritt dokumentiert werden muss. O entspricht keine Dokumentation notwendig, 1 entspricht Dokumentation notwendig",
                                    r"en": r"Specifies whether this maintenance step must be documented. O corresponds to no documentation necessary, 1 corresponds to documentation necessary",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/documentationsignaturemandatory/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EstimatedDurationTimeMaintenanceStep(aas.SubmodelElementCollection):

                    class ValueEstimatedDurationTimeMaintenanceStep(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ValueEstimatedDurationTimeMaintenanceStep",
                                "value_type": xsd.Decimal,
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Angabe der Dauer für diesen Wartungsschritt (Wert)",
                                        r"en": r"Indication of the duration for this maintenance step (value)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/valueestimateddurationtimemaintenancestep/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class UnitEstimatedDurationTimeMaintenanceStep(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"UnitEstimatedDurationTimeMaintenanceStep",
                                "value_type": str,
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Zeiteinheit für den Wert der Dauer für diesen wArtungsschritt - Beispiel Stunden, Tage, Wochen",
                                        r"en": r"Time unit for the value of the duration for this wArting step - example hours, days, weeks",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/unitestimateddurationtimemaintenancestep/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"EstimatedDurationTimeMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"de": r"Estimated duration for this maintenance step"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/estimateddurationtimemaintenancestep/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        valueEstimatedDurationTimeMaintenanceStep: Optional[
                            Union[xsd.Decimal, ValueEstimatedDurationTimeMaintenanceStep]
                        ] = None,
                        unitEstimatedDurationTimeMaintenanceStep: Optional[
                            Union[str, UnitEstimatedDurationTimeMaintenanceStep]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if valueEstimatedDurationTimeMaintenanceStep is not None and not isinstance(
                            valueEstimatedDurationTimeMaintenanceStep, aas.SubmodelElement
                        ):
                            valueEstimatedDurationTimeMaintenanceStep = self.ValueEstimatedDurationTimeMaintenanceStep(
                                valueEstimatedDurationTimeMaintenanceStep
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if unitEstimatedDurationTimeMaintenanceStep is not None and not isinstance(
                            unitEstimatedDurationTimeMaintenanceStep, aas.SubmodelElement
                        ):
                            unitEstimatedDurationTimeMaintenanceStep = self.UnitEstimatedDurationTimeMaintenanceStep(
                                unitEstimatedDurationTimeMaintenanceStep
                            )

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            valueEstimatedDurationTimeMaintenanceStep, unitEstimatedDurationTimeMaintenanceStep
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ConditionForNextMaintenanceStep(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ConditionForNextMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Bedinung für den nächsten Wartungsschritt ",
                                    r"en": r"Condition for the next maintenance step ",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/conditionfornextmaintenancestep/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NextMaintenanceStep(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"NextMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Referenz auf den folgenden Wartungsschritt, wenn die Bedingung erfüllt ist.",
                                    r"en": r"Reference to the following maintenance step if the condition is fulfilled.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/nextmaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ConditionForAlternativeNextStep(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ConditionForAlternativeNextStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Alternativer nächster Schritt, wenn die vorherige Bedingung nicht erfüllt ist. ",
                                    r"en": r"Alternative next step if the previous condition is not fulfilled. ",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/conditionforalternativenextstep/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AlternativeNextMaintenanceStep(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"AlternativeNextMaintenanceStep",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Referenz auf den folgenden Wartungsschritt, wenn die Bedingung nicht erfüllt ist.",
                                    r"en": r"Reference to the following maintenance step if the condition is not fulfilled.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/alternativenextmaintenancestep/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EndOfMaintenance(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EndOfMaintenance",
                            "value_type": bool,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Beendigung der Wartung, wenn dies der letzte Wartungsschritt war. 1 = Ende der Wartung erreicht",
                                    r"en": r"End of maintenance if this was the last maintenance step. 1 = End of maintenance reached",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/endofmaintenance/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MaintenanceStep",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Sammlung aller Details und Informationen zu einem Wartungsschritt ",
                                r"en": r"Collection of all details and information about a maintenance site",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/maintenancestep/1/0"
                        ),
                    }

                def __init__(
                    self,
                    maintenanceStepID: Optional[Union[str, MaintenanceStepID]] = None,
                    maintenanceStepName: Optional[Union[aas.MultiLanguageTextType, MaintenanceStepName]] = None,
                    localizationDescription: Optional[Union[aas.MultiLanguageTextType, LocalizationDescription]] = None,
                    linkSMMaintenanceComponentModuleMachine: Optional[
                        Union[aas.Reference, LinkSMMaintenanceComponentModuleMachine]
                    ] = None,
                    linkAASComponentModuleMachine: Optional[Union[aas.Reference, LinkAASComponentModuleMachine]] = None,
                    instructionMaintenanceStep: Optional[
                        Union[aas.MultiLanguageTextType, InstructionMaintenanceStep]
                    ] = None,
                    relatedDocumentOrFileMaintenanceStep: Optional[
                        Iterable[RelatedDocumentOrFileMaintenanceStep]
                    ] = None,
                    sparePartForMaintenanceStep: Optional[
                        Iterable[Union[aas.Reference, SparePartForMaintenanceStep]]
                    ] = None,
                    quantityOfSparePartForMaintenanceStep: Optional[
                        Union[xsd.Decimal, QuantityOfSparePartForMaintenanceStep]
                    ] = None,
                    consumablesForMaintenanceStep: Optional[
                        Iterable[Union[aas.Reference, ConsumablesForMaintenanceStep]]
                    ] = None,
                    quantityOfConsumablesForMaintenanceStep: Optional[
                        Iterable[Union[xsd.Decimal, QuantityOfConsumablesForMaintenanceStep]]
                    ] = None,
                    unitForQuantityOfConsumablesForMaintenanceStep: Optional[
                        Union[str, UnitForQuantityOfConsumablesForMaintenanceStep]
                    ] = None,
                    toolsForMaintenanceStep: Optional[Iterable[Union[aas.Reference, ToolsForMaintenanceStep]]] = None,
                    quantityOfToolsForMaintenanceStep: Optional[
                        Union[xsd.Decimal, QuantityOfToolsForMaintenanceStep]
                    ] = None,
                    documentationSignatureMandatory: Optional[Union[bool, DocumentationSignatureMandatory]] = None,
                    estimatedDurationTimeMaintenanceStep: Optional[EstimatedDurationTimeMaintenanceStep] = None,
                    conditionForNextMaintenanceStep: Optional[
                        Union[aas.MultiLanguageTextType, ConditionForNextMaintenanceStep]
                    ] = None,
                    nextMaintenanceStep: Optional[Union[aas.Reference, NextMaintenanceStep]] = None,
                    conditionForAlternativeNextStep: Optional[
                        Iterable[Union[aas.MultiLanguageTextType, ConditionForAlternativeNextStep]]
                    ] = None,
                    alternativeNextMaintenanceStep: Optional[
                        Iterable[Union[aas.Reference, AlternativeNextMaintenanceStep]]
                    ] = None,
                    endOfMaintenance: Optional[Union[bool, EndOfMaintenance]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if maintenanceStepID is not None and not isinstance(maintenanceStepID, aas.SubmodelElement):
                        maintenanceStepID = self.MaintenanceStepID(maintenanceStepID)

                    # Build a submodel element if a raw value was passed in the argument

                    if maintenanceStepName is not None and not isinstance(maintenanceStepName, aas.SubmodelElement):
                        maintenanceStepName = self.MaintenanceStepName(maintenanceStepName)

                    # Build a submodel element if a raw value was passed in the argument

                    if localizationDescription is not None and not isinstance(
                        localizationDescription, aas.SubmodelElement
                    ):
                        localizationDescription = self.LocalizationDescription(localizationDescription)

                    # Build a submodel element if a raw value was passed in the argument

                    if linkSMMaintenanceComponentModuleMachine is not None and not isinstance(
                        linkSMMaintenanceComponentModuleMachine, aas.SubmodelElement
                    ):
                        linkSMMaintenanceComponentModuleMachine = self.LinkSMMaintenanceComponentModuleMachine(
                            linkSMMaintenanceComponentModuleMachine
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if linkAASComponentModuleMachine is not None and not isinstance(
                        linkAASComponentModuleMachine, aas.SubmodelElement
                    ):
                        linkAASComponentModuleMachine = self.LinkAASComponentModuleMachine(
                            linkAASComponentModuleMachine
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if instructionMaintenanceStep is not None and not isinstance(
                        instructionMaintenanceStep, aas.SubmodelElement
                    ):
                        instructionMaintenanceStep = self.InstructionMaintenanceStep(instructionMaintenanceStep)

                    # A str would be split into its characters
                    if isinstance(relatedDocumentOrFileMaintenanceStep, str):
                        raise TypeError("relatedDocumentOrFileMaintenanceStep takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(sparePartForMaintenanceStep, str):
                        raise TypeError("sparePartForMaintenanceStep takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if sparePartForMaintenanceStep:
                        sparePartForMaintenanceStep = [
                            i if isinstance(i, aas.SubmodelElement) else self.SparePartForMaintenanceStep(i)
                            for i in sparePartForMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if quantityOfSparePartForMaintenanceStep is not None and not isinstance(
                        quantityOfSparePartForMaintenanceStep, aas.SubmodelElement
                    ):
                        quantityOfSparePartForMaintenanceStep = self.QuantityOfSparePartForMaintenanceStep(
                            quantityOfSparePartForMaintenanceStep
                        )

                    # A str would be split into its characters
                    if isinstance(consumablesForMaintenanceStep, str):
                        raise TypeError("consumablesForMaintenanceStep takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if consumablesForMaintenanceStep:
                        consumablesForMaintenanceStep = [
                            i if isinstance(i, aas.SubmodelElement) else self.ConsumablesForMaintenanceStep(i)
                            for i in consumablesForMaintenanceStep
                        ]

                    # A str would be split into its characters
                    if isinstance(quantityOfConsumablesForMaintenanceStep, str):
                        raise TypeError("quantityOfConsumablesForMaintenanceStep takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if quantityOfConsumablesForMaintenanceStep:
                        quantityOfConsumablesForMaintenanceStep = [
                            i if isinstance(i, aas.SubmodelElement) else self.QuantityOfConsumablesForMaintenanceStep(i)
                            for i in quantityOfConsumablesForMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if unitForQuantityOfConsumablesForMaintenanceStep is not None and not isinstance(
                        unitForQuantityOfConsumablesForMaintenanceStep, aas.SubmodelElement
                    ):
                        unitForQuantityOfConsumablesForMaintenanceStep = (
                            self.UnitForQuantityOfConsumablesForMaintenanceStep(
                                unitForQuantityOfConsumablesForMaintenanceStep
                            )
                        )

                    # A str would be split into its characters
                    if isinstance(toolsForMaintenanceStep, str):
                        raise TypeError("toolsForMaintenanceStep takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if toolsForMaintenanceStep:
                        toolsForMaintenanceStep = [
                            i if isinstance(i, aas.SubmodelElement) else self.ToolsForMaintenanceStep(i)
                            for i in toolsForMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if quantityOfToolsForMaintenanceStep is not None and not isinstance(
                        quantityOfToolsForMaintenanceStep, aas.SubmodelElement
                    ):
                        quantityOfToolsForMaintenanceStep = self.QuantityOfToolsForMaintenanceStep(
                            quantityOfToolsForMaintenanceStep
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if documentationSignatureMandatory is not None and not isinstance(
                        documentationSignatureMandatory, aas.SubmodelElement
                    ):
                        documentationSignatureMandatory = self.DocumentationSignatureMandatory(
                            documentationSignatureMandatory
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if conditionForNextMaintenanceStep is not None and not isinstance(
                        conditionForNextMaintenanceStep, aas.SubmodelElement
                    ):
                        conditionForNextMaintenanceStep = self.ConditionForNextMaintenanceStep(
                            conditionForNextMaintenanceStep
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if nextMaintenanceStep is not None and not isinstance(nextMaintenanceStep, aas.SubmodelElement):
                        nextMaintenanceStep = self.NextMaintenanceStep(nextMaintenanceStep)

                    # A str would be split into its characters
                    if isinstance(conditionForAlternativeNextStep, str):
                        raise TypeError("conditionForAlternativeNextStep takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if conditionForAlternativeNextStep:
                        conditionForAlternativeNextStep = [
                            i if isinstance(i, aas.SubmodelElement) else self.ConditionForAlternativeNextStep(i)
                            for i in conditionForAlternativeNextStep
                        ]

                    # A str would be split into its characters
                    if isinstance(alternativeNextMaintenanceStep, str):
                        raise TypeError("alternativeNextMaintenanceStep takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if alternativeNextMaintenanceStep:
                        alternativeNextMaintenanceStep = [
                            i if isinstance(i, aas.SubmodelElement) else self.AlternativeNextMaintenanceStep(i)
                            for i in alternativeNextMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if endOfMaintenance is not None and not isinstance(endOfMaintenance, aas.SubmodelElement):
                        endOfMaintenance = self.EndOfMaintenance(endOfMaintenance)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        maintenanceStepID,
                        maintenanceStepName,
                        localizationDescription,
                        linkSMMaintenanceComponentModuleMachine,
                        linkAASComponentModuleMachine,
                        instructionMaintenanceStep,
                        relatedDocumentOrFileMaintenanceStep,
                        sparePartForMaintenanceStep,
                        quantityOfSparePartForMaintenanceStep,
                        consumablesForMaintenanceStep,
                        quantityOfConsumablesForMaintenanceStep,
                        unitForQuantityOfConsumablesForMaintenanceStep,
                        toolsForMaintenanceStep,
                        quantityOfToolsForMaintenanceStep,
                        documentationSignatureMandatory,
                        estimatedDurationTimeMaintenanceStep,
                        conditionForNextMaintenanceStep,
                        nextMaintenanceStep,
                        conditionForAlternativeNextStep,
                        alternativeNextMaintenanceStep,
                        endOfMaintenance,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ListMaintenanceSteps",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Auflistung der einzelnen Wartungsschritte inkl. aller benötigten Details je Wartungsschritt",
                            r"en": r"Listing of the individual maintenance steps incl. all required details per maintenance step",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/maintenanceinstructions/listmaintenancesteps/1/0"
                    ),
                }

            def __init__(
                self,
                maintenanceStep: Optional[Iterable[MaintenanceStep]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(maintenanceStep, str):
                    raise TypeError("maintenanceStep takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(maintenanceStep)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MaintenanceInstructionsForSpecificInterval",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"de": r"Wartungsdetails für eine spezifischen Zeitinterval - Beispiel Wartung nach 6 Monaten",
                        r"en": r"Collection that includes all the details of a maintenance interval. ",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/maintenanceinstructions/maintenanceinstructionsforspecificinterval/1/0"
                ),
            }

        def __init__(
            self,
            maintenanceTechnicians: Optional[MaintenanceTechnicians] = None,
            listMaintenanceSteps: Optional[ListMaintenanceSteps] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(maintenanceTechnicians, listMaintenanceSteps)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MaintenanceToolList(GeneratedSubmodelElementList):

        class Maintenancetoollist_item(aas.SubmodelElementCollection):

            class ToolID(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ToolID",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"ID des Werkzeugs",
                                r"en": r"An ID can be assigned to uniquely identify a tool.",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/maintenanceinstructions/toolid/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ToolName(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ToolName",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Ein Name für das Werkzeug kann gespeichert werden, um das Werkzeug für Menschen verständlicher zu machen.",
                                r"en": r"A name for the tool can be stored to make the tool more understandable for humans.",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/maintenanceinstructions/toolname/1/0"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CollectionMaxQuantityOfTool(aas.SubmodelElementCollection):

                class CollectionMaxQuantityOfToolForSpecificInterval(aas.SubmodelElementCollection):

                    class MaxQuantityOfTool(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"MaxQuantityOfTool",
                                "value_type": xsd.Decimal,
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Benötigte Gesamtanzahl des Werkzeugs für einen Wartungsinterval",
                                        r"en": r"Total number of tools required for specific maintenance interval",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/maxquantityoftool/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ReferenceNameOfMaintenance(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"ReferenceNameOfMaintenance",
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Referenz zur ID eines spezifischen Wartungsintervals",
                                        r"en": r"Reference to ID of specific maintenance interval",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmaintenance/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ReferenceToMaintenanceID(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"ReferenceToMaintenanceID",
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Referenz zur ID eines spezifischen Wartungsintervals",
                                        r"en": r"Reference to ID of specific maintenance interval",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmaintenance/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"CollectionMaxQuantityOfToolForSpecificInterval",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Kollektion Benötige Anzahl des Werkzeugs für ein spezifisches Wartungsintervall.",
                                    r"en": r"Collection Total quantity of tools required for one specific maintenance intervals.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/collectionmaxquantityoftoolforspecificinterval/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        maxQuantityOfTool: Optional[Union[xsd.Decimal, MaxQuantityOfTool]] = None,
                        referenceNameOfMaintenance: Optional[Union[aas.Reference, ReferenceNameOfMaintenance]] = None,
                        referenceToMaintenanceID: Optional[Union[aas.Reference, ReferenceToMaintenanceID]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if maxQuantityOfTool is not None and not isinstance(maxQuantityOfTool, aas.SubmodelElement):
                            maxQuantityOfTool = self.MaxQuantityOfTool(maxQuantityOfTool)

                        # Build a submodel element if a raw value was passed in the argument

                        if referenceNameOfMaintenance is not None and not isinstance(
                            referenceNameOfMaintenance, aas.SubmodelElement
                        ):
                            referenceNameOfMaintenance = self.ReferenceNameOfMaintenance(referenceNameOfMaintenance)

                        # Build a submodel element if a raw value was passed in the argument

                        if referenceToMaintenanceID is not None and not isinstance(
                            referenceToMaintenanceID, aas.SubmodelElement
                        ):
                            referenceToMaintenanceID = self.ReferenceToMaintenanceID(referenceToMaintenanceID)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            maxQuantityOfTool, referenceNameOfMaintenance, referenceToMaintenanceID
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"CollectionMaxQuantityOfTool",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Liste der Werkzeuge, die für alle Wartungsintervalle einer Anlage benötigt werden. Die Menge richtet sich nach den verschiedenen Wartungsintervallen. Jede Menge pro Wartungsintervall wird in einer eigenen SMC beschrieben/definiert.",
                                r"en": r"List of tools required for all maintenance intervals of an asset. The quantity is devied by the different maintenance intervals. Each quantity per maintenance interval is described/ defined in an own SMC.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/collectionmaxquantityoftool/1/0"
                        ),
                    }

                def __init__(
                    self,
                    collectionMaxQuantityOfToolForSpecificInterval: Optional[
                        CollectionMaxQuantityOfToolForSpecificInterval
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        collectionMaxQuantityOfToolForSpecificInterval
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class CompanyNameToolSupplier(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"CompanyNameToolSupplier",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"de": r"Name des Werkzeugherstellers", r"en": r"Name of the tool manufacturer"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/companynametoolsupplier/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrderCodeToolOfManufacturer(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrderCodeToolOfManufacturer",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Eine vom Hersteller vergebene eindeutige Kombination aus Zahlen und Buchstaben, die zur Identifizierung des Werkzeugs bei der Bestellung verwendet wird",
                                r"en": r"unique combination of numbers and letters issued by the manufacturer that is used to identify the tool for ordering",
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABA950#008"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO227#004"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ToolDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ToolDescription",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Detaillierte Beschreibung des Werkzeugs",
                                r"en": r"Detailed description of the tool",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/tooldescription/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressOfAdditionalLinkTool(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressOfAdditionalLinkTool",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Web site address where information about the tool is given, e.g. link to shop"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAQ326#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Die Sammlung enthält alle Informationen und Details zu einem Werkzeug, das für die Wartung benötigt wird. Dazu gehören der Name, die Bestellnummer, der Hersteller und eine Beschreibung.",
                            r"en": r"The collection contains all the information and details about a tool needed for maintenance. This includes the name, order number, manufacturer and a description.",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/maintenanceinstructions/maintenancetool/1/0"
                    ),
                }

            def __init__(
                self,
                toolID: Optional[Union[str, ToolID]] = None,
                toolName: Optional[Union[aas.MultiLanguageTextType, ToolName]] = None,
                collectionMaxQuantityOfTool: Optional[CollectionMaxQuantityOfTool] = None,
                companyNameToolSupplier: Optional[Union[aas.MultiLanguageTextType, CompanyNameToolSupplier]] = None,
                orderCodeToolOfManufacturer: Optional[Union[str, OrderCodeToolOfManufacturer]] = None,
                toolDescription: Optional[Iterable[Union[aas.MultiLanguageTextType, ToolDescription]]] = None,
                addressOfAdditionalLinkTool: Optional[Iterable[Union[str, AddressOfAdditionalLinkTool]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if toolID is not None and not isinstance(toolID, aas.SubmodelElement):
                    toolID = self.ToolID(toolID)

                # Build a submodel element if a raw value was passed in the argument

                if toolName is not None and not isinstance(toolName, aas.SubmodelElement):
                    toolName = self.ToolName(toolName)

                # Build a submodel element if a raw value was passed in the argument

                if companyNameToolSupplier is not None and not isinstance(companyNameToolSupplier, aas.SubmodelElement):
                    companyNameToolSupplier = self.CompanyNameToolSupplier(companyNameToolSupplier)

                # Build a submodel element if a raw value was passed in the argument

                if orderCodeToolOfManufacturer is not None and not isinstance(
                    orderCodeToolOfManufacturer, aas.SubmodelElement
                ):
                    orderCodeToolOfManufacturer = self.OrderCodeToolOfManufacturer(orderCodeToolOfManufacturer)

                # A str would be split into its characters
                if isinstance(toolDescription, str):
                    raise TypeError("toolDescription takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if toolDescription:
                    toolDescription = [
                        i if isinstance(i, aas.SubmodelElement) else self.ToolDescription(i) for i in toolDescription
                    ]

                # A str would be split into its characters
                if isinstance(addressOfAdditionalLinkTool, str):
                    raise TypeError("addressOfAdditionalLinkTool takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if addressOfAdditionalLinkTool:
                    addressOfAdditionalLinkTool = [
                        i if isinstance(i, aas.SubmodelElement) else self.AddressOfAdditionalLinkTool(i)
                        for i in addressOfAdditionalLinkTool
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    toolID,
                    toolName,
                    collectionMaxQuantityOfTool,
                    companyNameToolSupplier,
                    orderCodeToolOfManufacturer,
                    toolDescription,
                    addressOfAdditionalLinkTool,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"MaintenanceToolList",
                "type_value_list_element": aas.SubmodelElementCollection,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"de": r"Gesamtliste der benötigten Werkzeuge für alle Wartungsintervalle eines Assets",
                        r"en": r"Total list of tools required for all maintenance intervals of an asset",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/maintenanceinstructions/maintenancetoollist/1/0"
                ),
            }

        def __init__(
            self,
            maintenancetoollist_items: Optional[Iterable[Maintenancetoollist_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(maintenancetoollist_items, str):
                raise TypeError("maintenancetoollist_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(maintenancetoollist_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MaintenanceConsumablesList(GeneratedSubmodelElementList):

        class Maintenanceconsumableslist_item(aas.SubmodelElementCollection):

            class ConsumableID(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ConsumableID",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"An ID can be assigned to uniquely identify a consumable, e.g. the globalAssetId of the tool."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/consumableid/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ConsumableName(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ConsumableName",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A name for the consumable can be stored to name the consumable more understandable for humans."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/consumablename/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CollectionQuantityOfConsumable(aas.SubmodelElementCollection):

                class QuantityOfConsumableForSpecificInterval(aas.SubmodelElementCollection):

                    class QuantityOfConsumable(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"QuantityOfConsumable",
                                "value_type": xsd.Decimal,
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Benötigte Gesamtanzahl des Verbrauchsmaterials für einen Wartungsinterval",
                                        r"en": r"Total number of consumble required for specific maintenance interval",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/quantityofconsumable/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ReferenceNameOfMaintenance(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"ReferenceNameOfMaintenance",
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Referenz zu Namen eines spezifischen Wartungsintervals",
                                        r"en": r"Referenceto name of specific maintenance interval",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmanintainance/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ReferenceToMaintenanceID(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"ReferenceToMaintenanceID",
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"de": r"Referenz zur ID eines spezifischen Wartungsintervals",
                                        r"en": r"Reference to ID of specific maintenance interval",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmaintenance/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"QuantityOfConsumableForSpecificInterval",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Kollektion benötige Anzahl des Verbrauchmaterials für ein spezifisches Wartungsintervall",
                                    r"en": r"Collection total quantity of consumable required for a specific maintenance intervals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/maintenanceinstructions/quantityofconsumableforspecificinterval/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        quantityOfConsumable: Optional[Union[xsd.Decimal, QuantityOfConsumable]] = None,
                        referenceNameOfMaintenance: Optional[Union[aas.Reference, ReferenceNameOfMaintenance]] = None,
                        referenceToMaintenanceID: Optional[Union[aas.Reference, ReferenceToMaintenanceID]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if quantityOfConsumable is not None and not isinstance(
                            quantityOfConsumable, aas.SubmodelElement
                        ):
                            quantityOfConsumable = self.QuantityOfConsumable(quantityOfConsumable)

                        # Build a submodel element if a raw value was passed in the argument

                        if referenceNameOfMaintenance is not None and not isinstance(
                            referenceNameOfMaintenance, aas.SubmodelElement
                        ):
                            referenceNameOfMaintenance = self.ReferenceNameOfMaintenance(referenceNameOfMaintenance)

                        # Build a submodel element if a raw value was passed in the argument

                        if referenceToMaintenanceID is not None and not isinstance(
                            referenceToMaintenanceID, aas.SubmodelElement
                        ):
                            referenceToMaintenanceID = self.ReferenceToMaintenanceID(referenceToMaintenanceID)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            quantityOfConsumable, referenceNameOfMaintenance, referenceToMaintenanceID
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"CollectionQuantityOfConsumable",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Sammelmenge des für die Wartungsintervalle benötigten Verbrauchsmaterials.",
                                r"en": r"Collection quantity of consumable required for maintenance intervals.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/collectionquantityofconsumables/1/0"
                        ),
                    }

                def __init__(
                    self,
                    quantityOfConsumableForSpecificInterval: Optional[QuantityOfConsumableForSpecificInterval] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(quantityOfConsumableForSpecificInterval)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class UnitMaxQuantityOfConsumable(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"UnitMaxQuantityOfConsumable",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Einheit zur benötigten Gesamtmenge des Verbauchsmaterials. Beispiel: Blatt, Milliliter, Gramm, ...",
                                r"en": r"Unit for the total quantity of consumable material required. Example: sheet, millilitre, gram, ...",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/unitmaxquantityofconsumable/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CompanyNameSupplierConsumable(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"CompanyNameSupplierConsumable",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Name des Verbrauchsmaterialherstellers z.B. Max Mustermann GmbH",
                                r"en": r"Name of the consumables manufacturer e.g. Max Mustermann GmbH",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/companynamesupplierconsumable/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrderCodeConsumableOfManufacturer(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrderCodeConsumableOfManufacturer",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"unique combination of numbers and letters issued by the manufacturer that is used to identify the consumable for ordering"
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABA950#008"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO227#004"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ConsumableDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ConsumableDescription",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Beschreibung des Verbauchsmaterials. Beispiel: Reinigungspapier; Farbe blau; Blattgröße 380x 380 mm doppellagig.",
                                r"en": r"Description of the consumables. Example: Cleaning paper; colour blue; sheet size 380x 380 mm double-ply.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/consumabledescription/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DisposalInstructionsForConsumable(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"DisposalInstructionsForConsumable",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Angabe zur fachgerechten Entsorgung des Verbauchsmaterials.",
                                r"en": r"Information on the proper disposal of the consumables.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/disposalinstructionsforconsumable/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressOfAdditionalLinkConsumable(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressOfAdditionalLinkConsumable",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Web site address where information about the consumable is given, e.g. link to shop"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAQ326#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Die Sammlung enthält alle Informationen und Details zu einem Verbrauchsmaterial, das für die Wartung benötigt wird. Dazu gehören die Bezeichnung, die Bestellnummer, der Hersteller und eine Beschreibung.",
                            r"en": r"The collection contains all information and details about a consumable required for maintenance. This includes the designation, order number, manufacturer and a description.",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/maintenanceinstructions/maintenanceconsumable/1/0"
                    ),
                }

            def __init__(
                self,
                consumableID: Optional[Union[str, ConsumableID]] = None,
                consumableName: Optional[Union[aas.MultiLanguageTextType, ConsumableName]] = None,
                collectionQuantityOfConsumable: Optional[CollectionQuantityOfConsumable] = None,
                unitMaxQuantityOfConsumable: Optional[Union[str, UnitMaxQuantityOfConsumable]] = None,
                companyNameSupplierConsumable: Optional[
                    Union[aas.MultiLanguageTextType, CompanyNameSupplierConsumable]
                ] = None,
                orderCodeConsumableOfManufacturer: Optional[Union[str, OrderCodeConsumableOfManufacturer]] = None,
                consumableDescription: Optional[
                    Iterable[Union[aas.MultiLanguageTextType, ConsumableDescription]]
                ] = None,
                disposalInstructionsForConsumable: Optional[
                    Iterable[Union[aas.MultiLanguageTextType, DisposalInstructionsForConsumable]]
                ] = None,
                addressOfAdditionalLinkConsumable: Optional[
                    Iterable[Union[str, AddressOfAdditionalLinkConsumable]]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if consumableID is not None and not isinstance(consumableID, aas.SubmodelElement):
                    consumableID = self.ConsumableID(consumableID)

                # Build a submodel element if a raw value was passed in the argument

                if consumableName is not None and not isinstance(consumableName, aas.SubmodelElement):
                    consumableName = self.ConsumableName(consumableName)

                # Build a submodel element if a raw value was passed in the argument

                if unitMaxQuantityOfConsumable is not None and not isinstance(
                    unitMaxQuantityOfConsumable, aas.SubmodelElement
                ):
                    unitMaxQuantityOfConsumable = self.UnitMaxQuantityOfConsumable(unitMaxQuantityOfConsumable)

                # Build a submodel element if a raw value was passed in the argument

                if companyNameSupplierConsumable is not None and not isinstance(
                    companyNameSupplierConsumable, aas.SubmodelElement
                ):
                    companyNameSupplierConsumable = self.CompanyNameSupplierConsumable(companyNameSupplierConsumable)

                # Build a submodel element if a raw value was passed in the argument

                if orderCodeConsumableOfManufacturer is not None and not isinstance(
                    orderCodeConsumableOfManufacturer, aas.SubmodelElement
                ):
                    orderCodeConsumableOfManufacturer = self.OrderCodeConsumableOfManufacturer(
                        orderCodeConsumableOfManufacturer
                    )

                # A str would be split into its characters
                if isinstance(consumableDescription, str):
                    raise TypeError("consumableDescription takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if consumableDescription:
                    consumableDescription = [
                        i if isinstance(i, aas.SubmodelElement) else self.ConsumableDescription(i)
                        for i in consumableDescription
                    ]

                # A str would be split into its characters
                if isinstance(disposalInstructionsForConsumable, str):
                    raise TypeError("disposalInstructionsForConsumable takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if disposalInstructionsForConsumable:
                    disposalInstructionsForConsumable = [
                        i if isinstance(i, aas.SubmodelElement) else self.DisposalInstructionsForConsumable(i)
                        for i in disposalInstructionsForConsumable
                    ]

                # A str would be split into its characters
                if isinstance(addressOfAdditionalLinkConsumable, str):
                    raise TypeError("addressOfAdditionalLinkConsumable takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if addressOfAdditionalLinkConsumable:
                    addressOfAdditionalLinkConsumable = [
                        i if isinstance(i, aas.SubmodelElement) else self.AddressOfAdditionalLinkConsumable(i)
                        for i in addressOfAdditionalLinkConsumable
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    consumableID,
                    consumableName,
                    collectionQuantityOfConsumable,
                    unitMaxQuantityOfConsumable,
                    companyNameSupplierConsumable,
                    orderCodeConsumableOfManufacturer,
                    consumableDescription,
                    disposalInstructionsForConsumable,
                    addressOfAdditionalLinkConsumable,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"MaintenanceConsumablesList",
                "type_value_list_element": aas.SubmodelElementCollection,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"de": r"Gesamtliste der benötigten Verbrauchsmaterialien für alle Wartungsintervalle",
                        r"en": r"Total list of consumables required for all maintenance intervals of an asset. Each consumable is described/defined in its own SMC’s",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/maintenanceinstructions/maintenanceconsumableslist/1/0"
                ),
            }

        def __init__(
            self,
            maintenanceconsumableslist_items: Optional[Iterable[Maintenanceconsumableslist_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(maintenanceconsumableslist_items, str):
                raise TypeError("maintenanceconsumableslist_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                maintenanceconsumableslist_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MaintenanceSparePartList(GeneratedSubmodelElementList):

        class Maintenancesparepartlist_item(aas.SubmodelElementCollection):

            class SparePartID(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SparePartID",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"An ID can be assigned to uniquely identify a spare part, e.g. the globalAssetId of the spare part."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/sparepartid/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SparePartName(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"SparePartName",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Eine Bezeichnung des Ersatzteils kann gespeichert werden, um das Ersatzteil für den Menschen verständlicher zu benennen.",
                                r"en": r"A designation of the spare part can be stored to name the spare part more understandable for people.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/sparepartname/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CollectionQuantityOfSparePart(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"CollectionQuantityOfSparePart",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Kollektion benötige Anzahl des Ersatzteils für die Wartungsintervalle.",
                                r"en": r"Collection quantity of spare part required for maintenance intervals.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/collectionquantityofsparepart/1/0"
                        ),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class CompanyNameSupplierSparePart(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"CompanyNameSupplierSparePart",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Name des Ersatzteilherstellers z.B. Max Mustermann GmbH",
                                r"en": r"Name of the spare parts manufacturer e.g. Max Mustermann GmbH",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/companynamesuppliersparepart/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrderCodeSparePartOfManufacturer(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrderCodeSparePartOfManufacturer",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"unique combination of numbers and letters issued by the manufacturer that is used to identify the spare part for ordering"
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABA950#008"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SparePartDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"SparePartDescription",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"de": r"Beschreibung des Ersatzteils.", r"en": r"Description of the spare part."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/sparepartdescription/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DisposalInstructionsForSparePart(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"DisposalInstructionsForSparePart",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Angabe zur fachgerechten Entsorgung des Ersatzteils.",
                                r"en": r"Information on the proper disposal of the spare part.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/maintenanceinstructions/disposalinstructionsforsparepart/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressOfAdditionalLinkSparePart(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressOfAdditionalLinkSparePart",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Web site address where information about the consumable is given, e.g. link to shop"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAQ326#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Die Sammlung enthält alle Informationen und Details zu einem Verbrauchsmaterial, das für die Wartung benötigt wird. Dazu gehören die Bezeichnung, die Bestellnummer, der Hersteller und eine Beschreibung.",
                            r"en": r"The collection contains all information and details about a consumable required for maintenance. This includes the designation, order number, manufacturer and a description.",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"htthttps://admin-shell.io/idta/maintenanceinstructions/maintenancesparepart/1/0"
                    ),
                }

            def __init__(
                self,
                sparePartID: Optional[Union[str, SparePartID]] = None,
                sparePartName: Optional[Union[aas.MultiLanguageTextType, SparePartName]] = None,
                collectionQuantityOfSparePart: Optional[CollectionQuantityOfSparePart] = None,
                companyNameSupplierSparePart: Optional[
                    Union[aas.MultiLanguageTextType, CompanyNameSupplierSparePart]
                ] = None,
                orderCodeSparePartOfManufacturer: Optional[Union[str, OrderCodeSparePartOfManufacturer]] = None,
                sparePartDescription: Optional[Iterable[Union[aas.MultiLanguageTextType, SparePartDescription]]] = None,
                disposalInstructionsForSparePart: Optional[
                    Iterable[Union[aas.MultiLanguageTextType, DisposalInstructionsForSparePart]]
                ] = None,
                addressOfAdditionalLinkSparePart: Optional[
                    Iterable[Union[str, AddressOfAdditionalLinkSparePart]]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if sparePartID is not None and not isinstance(sparePartID, aas.SubmodelElement):
                    sparePartID = self.SparePartID(sparePartID)

                # Build a submodel element if a raw value was passed in the argument

                if sparePartName is not None and not isinstance(sparePartName, aas.SubmodelElement):
                    sparePartName = self.SparePartName(sparePartName)

                # Build a submodel element if a raw value was passed in the argument

                if companyNameSupplierSparePart is not None and not isinstance(
                    companyNameSupplierSparePart, aas.SubmodelElement
                ):
                    companyNameSupplierSparePart = self.CompanyNameSupplierSparePart(companyNameSupplierSparePart)

                # Build a submodel element if a raw value was passed in the argument

                if orderCodeSparePartOfManufacturer is not None and not isinstance(
                    orderCodeSparePartOfManufacturer, aas.SubmodelElement
                ):
                    orderCodeSparePartOfManufacturer = self.OrderCodeSparePartOfManufacturer(
                        orderCodeSparePartOfManufacturer
                    )

                # A str would be split into its characters
                if isinstance(sparePartDescription, str):
                    raise TypeError("sparePartDescription takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if sparePartDescription:
                    sparePartDescription = [
                        i if isinstance(i, aas.SubmodelElement) else self.SparePartDescription(i)
                        for i in sparePartDescription
                    ]

                # A str would be split into its characters
                if isinstance(disposalInstructionsForSparePart, str):
                    raise TypeError("disposalInstructionsForSparePart takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if disposalInstructionsForSparePart:
                    disposalInstructionsForSparePart = [
                        i if isinstance(i, aas.SubmodelElement) else self.DisposalInstructionsForSparePart(i)
                        for i in disposalInstructionsForSparePart
                    ]

                # A str would be split into its characters
                if isinstance(addressOfAdditionalLinkSparePart, str):
                    raise TypeError("addressOfAdditionalLinkSparePart takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if addressOfAdditionalLinkSparePart:
                    addressOfAdditionalLinkSparePart = [
                        i if isinstance(i, aas.SubmodelElement) else self.AddressOfAdditionalLinkSparePart(i)
                        for i in addressOfAdditionalLinkSparePart
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    sparePartID,
                    sparePartName,
                    collectionQuantityOfSparePart,
                    companyNameSupplierSparePart,
                    orderCodeSparePartOfManufacturer,
                    sparePartDescription,
                    disposalInstructionsForSparePart,
                    addressOfAdditionalLinkSparePart,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"MaintenanceSparePartList",
                "type_value_list_element": aas.SubmodelElementCollection,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"de": r"Gesamtliste der benötigten Ersatzteile für alle Wartungsintervalle",
                        r"en": r"Total list of required spare parts for all maintenance intervals of an asset. Each spare part is described/ defined in its own SMC.",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/maintenanceinstructions/maintenancesparepartlist/1/0"
                ),
            }

        def __init__(
            self,
            maintenancesparepartlist_items: Optional[Iterable[Maintenancesparepartlist_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(maintenancesparepartlist_items, str):
                raise TypeError("maintenancesparepartlist_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                maintenancesparepartlist_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"MaintenanceInstructions",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"de": r"Submodell zur Übermittlung aller wartungsrelevanten Informatationen",
                    r"en": r"The Submodel defines a set of maintenance instructions and additional details, files or documents related to the maintenance of an asset",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell-io/idta-02018",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/MaintenanceInstructions/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        maintenanceFreeAsset: Union[bool, MaintenanceFreeAsset],
        maintenanceInstructionsForSpecificInterval: Optional[
            Iterable[MaintenanceInstructionsForSpecificInterval]
        ] = None,
        maintenanceToolList: Optional[
            Union[Iterable[MaintenanceToolList.Maintenancetoollist_item], MaintenanceToolList]
        ] = None,
        maintenanceConsumablesList: Optional[
            Union[Iterable[MaintenanceConsumablesList.Maintenanceconsumableslist_item], MaintenanceConsumablesList]
        ] = None,
        maintenanceSparePartList: Optional[
            Union[Iterable[MaintenanceSparePartList.Maintenancesparepartlist_item], MaintenanceSparePartList]
        ] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if maintenanceFreeAsset is not None and not isinstance(maintenanceFreeAsset, aas.SubmodelElement):
            maintenanceFreeAsset = self.MaintenanceFreeAsset(maintenanceFreeAsset)

        # A str would be split into its characters
        if isinstance(maintenanceInstructionsForSpecificInterval, str):
            raise TypeError("maintenanceInstructionsForSpecificInterval takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(maintenanceToolList, str):
            raise TypeError("maintenanceToolList takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if maintenanceToolList is not None and not isinstance(maintenanceToolList, aas.SubmodelElement):
            maintenanceToolList = self.MaintenanceToolList(maintenanceToolList)

        # A str would be split into its characters
        if isinstance(maintenanceConsumablesList, str):
            raise TypeError("maintenanceConsumablesList takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if maintenanceConsumablesList is not None and not isinstance(maintenanceConsumablesList, aas.SubmodelElement):
            maintenanceConsumablesList = self.MaintenanceConsumablesList(maintenanceConsumablesList)

        # A str would be split into its characters
        if isinstance(maintenanceSparePartList, str):
            raise TypeError("maintenanceSparePartList takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if maintenanceSparePartList is not None and not isinstance(maintenanceSparePartList, aas.SubmodelElement):
            maintenanceSparePartList = self.MaintenanceSparePartList(maintenanceSparePartList)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            maintenanceFreeAsset,
            maintenanceInstructionsForSpecificInterval,
            maintenanceToolList,
            maintenanceConsumablesList,
            maintenanceSparePartList,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
