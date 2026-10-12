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


class PredictiveMaintenance(aas.Submodel):

    class RemainingUsefulLifePrediction(aas.SubmodelElementCollection):

        class RemainingUsefulLifetime(aas.Entity):

            class IndicationType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IndicationType",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Type of wear-relevant duration, e.g. time, cycles, distance, etc.",
                                r"de": r"Art der verschleißrelevanten Dauer, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/IndicationType/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DurationValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DurationValue",
                        "value_type": float,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Value of duration in the wear relevant unit, e.g. time, operation cycles, distance, etc.",
                                r"de": r"Zahlenwert der Dauer in der verschleißrelevanten Einheit, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/DurationValue/1/0"
                        ),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EngineeringUnit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EngineeringUnit",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Wear relevant physical unit, e.g. time, operation cycles, distance, etc.",
                                r"de": r"Verschleißrelevante physikalische Einheit, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/EngineeringUnit/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StartValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StartValue",
                        "value_type": float,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Starting value from which the duration is measured in the wear-relevant unit, e.g. time, cycles, distance, etc.",
                                r"de": r"Startwert, von dem ab die Dauer gemessen wird in der verschleißrelevanten Einheit, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PredictiveMaintenance/StartValue/1/0"),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StartDateTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StartDateTime",
                        "value_type": xsd.DateTime,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Start date and time from which the duration is measured",
                                r"de": r"Startdatum und -zeit, von der ab die Dauer gemessen wird",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/StartDateTime/1/0"
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Description of the wear duration information",
                                r"de": r"Beschreibung der Angabe zur verschleißrelevanten Dauer",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PredictiveMaintenance/Description/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"RemainingUsefulLifetime",
                    "entity_type": aas.EntityType.CO_MANAGED_ENTITY,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Remaining useful life time, bades on Lifetime model of OPC Foundation (https://reference.opcfoundation.org/DI/v104/docs/10)",
                            r"de": r"Verbleibende Betriebszeit in Anlehnung an Lifetime model der OPC Foundation (https://reference.opcfoundation.org/DI/v104/docs/10)",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLifetime/1/0"
                    ),
                }

            def __init__(
                self,
                indicationType: Union[str, IndicationType],
                durationValue: Union[float, DurationValue],
                engineeringUnit: Union[str, EngineeringUnit],
                startValue: Union[float, StartValue],
                startDateTime: Optional[Union[xsd.DateTime, StartDateTime]] = None,
                description_: Optional[Union[str, Description]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if indicationType is not None and not isinstance(indicationType, aas.SubmodelElement):
                    indicationType = self.IndicationType(indicationType)

                # Build a submodel element if a raw value was passed in the argument

                if durationValue is not None and not isinstance(durationValue, aas.SubmodelElement):
                    durationValue = self.DurationValue(durationValue)

                # Build a submodel element if a raw value was passed in the argument

                if engineeringUnit is not None and not isinstance(engineeringUnit, aas.SubmodelElement):
                    engineeringUnit = self.EngineeringUnit(engineeringUnit)

                # Build a submodel element if a raw value was passed in the argument

                if startValue is not None and not isinstance(startValue, aas.SubmodelElement):
                    startValue = self.StartValue(startValue)

                # Build a submodel element if a raw value was passed in the argument

                if startDateTime is not None and not isinstance(startDateTime, aas.SubmodelElement):
                    startDateTime = self.StartDateTime(startDateTime)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    indicationType, durationValue, engineeringUnit, startValue, startDateTime, description_
                )

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RemainingUsfulLifeDateTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RemainingUsfulLifeDateTime",
                    "value_type": xsd.DateTime,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"mark attributed to an instant by means of a specified timescale, expressed as a date and a time",
                            r"de": r"Markierung, zugeordnet zu einem Moment mittles einer spezifischen Zeitskala, ausgedrückt als Datum und Uhrzeit",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsfulLifeDateTime/1/0"
                    ),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ConfidenceInterval(aas.Range):

            @staticmethod
            def template_defaults() -> RangeMetadata:
                return {
                    "id_short": r"ConfidenceInterval",
                    "value_type": float,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"confidence interval, measured in the unit of the predicted value",
                            r"de": r"Konfidenzintervall in der Einheit des prognositizierten Wertes",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PredictiveMaintenance/ConfidenceInterval/1/0"
                    ),
                }

            def __init__(self, min: float, max: float, **kwargs: Unpack[RangeMetadata]):

                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

        class ListRULBoundaryConditions(GeneratedSubmodelElementList):

            class Listrulboundaryconditions_item(aas.SubmodelElementCollection):

                class ConditionName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ConditionName",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL prediction is valid.",
                                    r"de": r"Bezeichnung des Indikators (Prozesswert, KPI, Materialeigenschaft, Anlageneigenschaft), der eine Randbedingung beschreibt, für die die RUL-Vorhersage gültig ist.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class IsBoundaryConditionUsedInModel(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"IsBoundaryConditionUsedInModel",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"If this boundary condition is used in the model for RUL prediction true, else false",
                                    r"de": r"Wenn diese Randbedingung im Modell für die RUL Prognose verwendet true sonst false",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryConditionUsedInModel/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class BoundaryValueRange(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"BoundaryValueRange",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Value range of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL prediction is valid.",
                                    r"de": r"Wertebereich des Indikators (Prozesswert, KPI, Materialeigenschaft, Anlageneigenschaft), der eine Randbedingung beschreibt, für die die RUL-Vorhersage gültig ist.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class BoundaryEngineeringUnit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"BoundaryEngineeringUnit",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Engineering Unit of the boundary condition indicator",
                                    r"de": r"Physikalische Einheit des Indikators, der die Randbedingung beschreibt",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineeringUnit/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DriftInfoAIModel(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"DriftInfoAIModel",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Drift information of AI model", r"de": r"Drift Information of AI Model"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0"
                            ),
                        }

                    def __init__(self, min: float, max: float, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                class MeanValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MeanValue",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Mean value of the distribution of indicator values",
                                    r"de": r"Mttelwert der Verteilung des Indikators",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Standarddeviation(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Standarddeviation",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Standard deviation of the distribution of indicator values",
                                    r"de": r"Standardabweichung der Verteilung des Indikators",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Skewness(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Skewness",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Skewness of the distribution of indicator values",
                                    r"de": r"Schiefe der Verteilung des Indikators",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class BoundaryDescription(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"BoundaryDescription",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the boundary of a RUL prediction condition",
                                    r"de": r"Beschreibung einer RUL Vorhersage-Randbedingung",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Boundary condition for which remaining useful life has been predicted",
                                r"de": r"Randbedingung unter der die nutzbare Restlebensdauer prognositiziert wurde",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0"
                        ),
                    }

                def __init__(
                    self,
                    conditionName: Union[str, ConditionName],
                    isBoundaryConditionUsedInModel: Union[bool, IsBoundaryConditionUsedInModel],
                    boundaryValueRange: Union[float, BoundaryValueRange],
                    boundaryEngineeringUnit: Union[str, BoundaryEngineeringUnit],
                    driftInfoAIModel: Optional[Union[Tuple[float, float], DriftInfoAIModel]] = None,
                    meanValue: Optional[Union[float, MeanValue]] = None,
                    standarddeviation: Optional[Union[float, Standarddeviation]] = None,
                    skewness: Optional[Union[float, Skewness]] = None,
                    boundaryDescription: Optional[Union[str, BoundaryDescription]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if conditionName is not None and not isinstance(conditionName, aas.SubmodelElement):
                        conditionName = self.ConditionName(conditionName)

                    # Build a submodel element if a raw value was passed in the argument

                    if isBoundaryConditionUsedInModel is not None and not isinstance(
                        isBoundaryConditionUsedInModel, aas.SubmodelElement
                    ):
                        isBoundaryConditionUsedInModel = self.IsBoundaryConditionUsedInModel(
                            isBoundaryConditionUsedInModel
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if boundaryValueRange is not None and not isinstance(boundaryValueRange, aas.SubmodelElement):
                        boundaryValueRange = self.BoundaryValueRange(boundaryValueRange)

                    # Build a submodel element if a raw value was passed in the argument

                    if boundaryEngineeringUnit is not None and not isinstance(
                        boundaryEngineeringUnit, aas.SubmodelElement
                    ):
                        boundaryEngineeringUnit = self.BoundaryEngineeringUnit(boundaryEngineeringUnit)

                    # Build a submodel element if a raw value was passed in the argument

                    if driftInfoAIModel is not None and not isinstance(driftInfoAIModel, aas.SubmodelElement):
                        driftInfoAIModel = self.DriftInfoAIModel(min=driftInfoAIModel[0], max=driftInfoAIModel[1])

                    # Build a submodel element if a raw value was passed in the argument

                    if meanValue is not None and not isinstance(meanValue, aas.SubmodelElement):
                        meanValue = self.MeanValue(meanValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if standarddeviation is not None and not isinstance(standarddeviation, aas.SubmodelElement):
                        standarddeviation = self.Standarddeviation(standarddeviation)

                    # Build a submodel element if a raw value was passed in the argument

                    if skewness is not None and not isinstance(skewness, aas.SubmodelElement):
                        skewness = self.Skewness(skewness)

                    # Build a submodel element if a raw value was passed in the argument

                    if boundaryDescription is not None and not isinstance(boundaryDescription, aas.SubmodelElement):
                        boundaryDescription = self.BoundaryDescription(boundaryDescription)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        conditionName,
                        isBoundaryConditionUsedInModel,
                        boundaryValueRange,
                        boundaryEngineeringUnit,
                        driftInfoAIModel,
                        meanValue,
                        standarddeviation,
                        skewness,
                        boundaryDescription,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"ListRULBoundaryConditions",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of boundary conditions for which remaining useful life has been predicted",
                            r"de": r"Liste der Randbedingungen unter denen die nutzbare Restlebensdauer prognostiziert wurde",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PredictiveMaintenance/ListRULBoundaryConditions/1/0"
                    ),
                }

            def __init__(
                self,
                listrulboundaryconditions_items: Iterable[Listrulboundaryconditions_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(listrulboundaryconditions_items, str):
                    raise TypeError("listrulboundaryconditions_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    listrulboundaryconditions_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class PredictionModelInformation(aas.SubmodelElementCollection):

            class ModelType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ModelType",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Model type as an enumerated value: physical based methods, data-driven methods, hybrid methods",
                                r"de": r"Modeltyp als enumerierter Wert: physical based methods, data-driven methods, hybrid methods",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PredictiveMaintenance/ModelType/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ModelDescription(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ModelDescription",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"More detailed description of the model type used for RUL prediction (optional)",
                                r"de": r"Detailliertere Beschreibung des Modelltyps, der für die RUL Prognose verwendet wird (optional)",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/ModelDescription/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SMAIModelNamePlate(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"SMAIModelNamePlate",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Reference to AIModelNameplate", r"de": r"Referenz auf AIModelNameplate"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/SMAIModelNamePlate/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"PredictionModelInformation",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Information about the model for RUL prediction relevant in the context of predictive maintenance",
                            r"de": r"Informationen über das Modell zur Prognose der RUL im Kontext der vorausschauenden Wartung",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PredictiveMaintenance/PredictionModelInformation/1/0"
                    ),
                }

            def __init__(
                self,
                modelType: Union[str, ModelType],
                modelDescription: Optional[Union[str, ModelDescription]] = None,
                sMAIModelNamePlate: Optional[Union[aas.Reference, SMAIModelNamePlate]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if modelType is not None and not isinstance(modelType, aas.SubmodelElement):
                    modelType = self.ModelType(modelType)

                # Build a submodel element if a raw value was passed in the argument

                if modelDescription is not None and not isinstance(modelDescription, aas.SubmodelElement):
                    modelDescription = self.ModelDescription(modelDescription)

                # Build a submodel element if a raw value was passed in the argument

                if sMAIModelNamePlate is not None and not isinstance(sMAIModelNamePlate, aas.SubmodelElement):
                    sMAIModelNamePlate = self.SMAIModelNamePlate(sMAIModelNamePlate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(modelType, modelDescription, sMAIModelNamePlate)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ListPreAlerts(GeneratedSubmodelElementList):

            class Listprealerts_item(aas.SubmodelElementCollection):

                class PreAlertMessage(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PreAlertMessage",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Message to be displayed when alarm regarding predicted remaining useful life is raised",
                                    r"de": r"Nachricht, die bei Auslösen eines Alarms bezüglich der vorhergesagten verbleibenden Restnutzungsdauer angezeigt wird",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/PreAlertMessage/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PreAlertValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PreAlertValue",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Pre-warning duration in wear relevant unit before remaining useful life is exceeded",
                                    r"de": r"Vorwarndauer in verschleißrelevanter Einheit vor Eintritt der Überschreitung verbleibenden Restnutzungsdauer",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/PredictiveMaintenance/PreAlertValue/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Definition of a pre-alert which should be raised before remaining useful life is exceeded",
                                r"de": r"Definition eiens Voralarms, der vor Erreichen der Restlebensdauer ausgelöst werden sollen",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/PredictiveMaintenance/PreAlerts/1/0"),
                    }

                def __init__(
                    self,
                    preAlertValue: Union[float, PreAlertValue],
                    preAlertMessage: Optional[Union[str, PreAlertMessage]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if preAlertMessage is not None and not isinstance(preAlertMessage, aas.SubmodelElement):
                        preAlertMessage = self.PreAlertMessage(preAlertMessage)

                    # Build a submodel element if a raw value was passed in the argument

                    if preAlertValue is not None and not isinstance(preAlertValue, aas.SubmodelElement):
                        preAlertValue = self.PreAlertValue(preAlertValue)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(preAlertMessage, preAlertValue)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"ListPreAlerts",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List for defining pre-alerts which should be raised before remaining useful life is exceeded",
                            r"de": r"Liste, um Voralarme zu definieren, die vor Erreichen der Restlebensdauer ausgelöst werden sollen",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/PredictiveMaintenance/ListPreAlerts/1/0"),
                }

            def __init__(
                self,
                listprealerts_items: Optional[Iterable[Listprealerts_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(listprealerts_items, str):
                    raise TypeError("listprealerts_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(listprealerts_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class AlertAfterExceedingRemainingUsableLife(aas.SubmodelElementCollection):

            class AlertMessage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AlertMessage",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Message to be displayed when alarm regarding predicted remaining useful life is raised",
                                r"de": r"Nachricht, die bei Auslösen eines Alarms bezüglich der vorhergesagten verbleibenden Restnutzungsdauer angezeigt wird",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/AlertMessage/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaintenanceRequired(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaintenanceRequired",
                        "value_type": bool,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Maintenance required", r"de": r"Wartung erforderlich"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/PredictiveMaintenance/MaintenanceRequired/1/0"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"AlertAfterExceedingRemainingUsableLife",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Alert information which should be triggered or displayed after exceeding remaining useful life",
                            r"de": r"Alarminformationen die ausgelöst oder angezeigt werden sollen, wenn die Restlebensdauer überschritten wird",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/PredictiveMaintenance/AlertAfterExceedingRemainingUsableLife/1/0"
                    ),
                }

            def __init__(
                self,
                maintenanceRequired: Union[bool, MaintenanceRequired],
                alertMessage: Optional[Union[str, AlertMessage]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if alertMessage is not None and not isinstance(alertMessage, aas.SubmodelElement):
                    alertMessage = self.AlertMessage(alertMessage)

                # Build a submodel element if a raw value was passed in the argument

                if maintenanceRequired is not None and not isinstance(maintenanceRequired, aas.SubmodelElement):
                    maintenanceRequired = self.MaintenanceRequired(maintenanceRequired)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(alertMessage, maintenanceRequired)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"RemainingUsefulLifePrediction",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Information about remaining useful life (RUL) prediction in the context of predictive maintenance",
                        r"de": r"Informationen über die Prognose der nutzbaren Restlebensdauer (RUL) im Kontext der vorausschauenden Wartung",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLifePrediction/1/0"
                ),
            }

        def __init__(
            self,
            remainingUsefulLifetime: RemainingUsefulLifetime,
            confidenceInterval: Union[Tuple[float, float], ConfidenceInterval],
            listRULBoundaryConditions: Union[
                Iterable[ListRULBoundaryConditions.Listrulboundaryconditions_item], ListRULBoundaryConditions
            ],
            predictionModelInformation: PredictionModelInformation,
            remainingUsfulLifeDateTime: Optional[Union[xsd.DateTime, RemainingUsfulLifeDateTime]] = None,
            listPreAlerts: Optional[Union[Iterable[ListPreAlerts.Listprealerts_item], ListPreAlerts]] = None,
            alertAfterExceedingRemainingUsableLife: Optional[AlertAfterExceedingRemainingUsableLife] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if remainingUsfulLifeDateTime is not None and not isinstance(
                remainingUsfulLifeDateTime, aas.SubmodelElement
            ):
                remainingUsfulLifeDateTime = self.RemainingUsfulLifeDateTime(remainingUsfulLifeDateTime)

            # Build a submodel element if a raw value was passed in the argument

            if confidenceInterval is not None and not isinstance(confidenceInterval, aas.SubmodelElement):
                confidenceInterval = self.ConfidenceInterval(min=confidenceInterval[0], max=confidenceInterval[1])

            # A str would be split into its characters
            if isinstance(listRULBoundaryConditions, str):
                raise TypeError("listRULBoundaryConditions takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if listRULBoundaryConditions is not None and not isinstance(listRULBoundaryConditions, aas.SubmodelElement):
                listRULBoundaryConditions = self.ListRULBoundaryConditions(listRULBoundaryConditions)

            # A str would be split into its characters
            if isinstance(listPreAlerts, str):
                raise TypeError("listPreAlerts takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if listPreAlerts is not None and not isinstance(listPreAlerts, aas.SubmodelElement):
                listPreAlerts = self.ListPreAlerts(listPreAlerts)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                remainingUsefulLifetime,
                remainingUsfulLifeDateTime,
                confidenceInterval,
                listRULBoundaryConditions,
                predictionModelInformation,
                listPreAlerts,
                alertAfterExceedingRemainingUsableLife,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"PredictiveMaintenance",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel Predictive Maintenance is a collection of properties to provide information for predictive maintenance use cases. It is intended to use this submodel in sub-systems of production lines to describe predictive maintenance relevant topics for the sub-system, as well as to use this submodel in predictive maintenance software applications",
                    r"de": r"Das Teilmodell Predictive Maintenance stellt Informationen für Anwendungsfälle von Predictive Maintenance bereit. Dieses Teilmodell ist für Sub-Systeme von Produktionslinien vorgesehen, um Predictive Maintenance relevante Informationen für das Sub-System zu beschreiben sowie für Software-Anwendungen für vorausschauende Wartung",
                }
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self, id_: str, remainingUsefulLifePrediction: RemainingUsefulLifePrediction, **kwargs: Unpack[SubmodelMetadata]
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(remainingUsefulLifePrediction)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
