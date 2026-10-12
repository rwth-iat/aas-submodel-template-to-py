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


class ProductCondition(aas.Submodel):

    class EnergyThroughput(aas.SubmodelElementCollection):

        class EnergyThroughputValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EnergyThroughputValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"energy throughput value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#energyThroughputValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL850#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"EnergyThroughput",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"energy throughput"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#energyThroughput"
                ),
                "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL850#001"),),
            }

        def __init__(
            self,
            energyThroughputValue: Union[xsd.Float, EnergyThroughputValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if energyThroughputValue is not None and not isinstance(energyThroughputValue, aas.SubmodelElement):
                energyThroughputValue = self.EnergyThroughputValue(energyThroughputValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(energyThroughputValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class CapacityThroughput(aas.SubmodelElementCollection):

        class CapacityThroughputValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CapacityThroughputValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"capacity throughput value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#capacityThroughputValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL849#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"CapacityThroughput",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"capacity throughput"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#capacityThroughput"
                ),
                "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL849#001"),),
            }

        def __init__(
            self,
            capacityThroughputValue: Union[xsd.Float, CapacityThroughputValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if capacityThroughputValue is not None and not isinstance(capacityThroughputValue, aas.SubmodelElement):
                capacityThroughputValue = self.CapacityThroughputValue(capacityThroughputValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(capacityThroughputValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class NumberOfFullCycles(aas.SubmodelElementCollection):

        class NumberOfFullCyclesValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfFullCyclesValue",
                    "value_type": xsd.UnsignedInt,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of full cycles value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#numberOfFullCyclesValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL868#001"),),
                }

            def __init__(self, value: xsd.UnsignedInt, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"NumberOfFullCycles",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of full cycles"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#numberOfFullCycles"
                ),
                "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL868#001"),),
            }

        def __init__(
            self,
            numberOfFullCyclesValue: Union[xsd.UnsignedInt, NumberOfFullCyclesValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if numberOfFullCyclesValue is not None and not isinstance(numberOfFullCyclesValue, aas.SubmodelElement):
                numberOfFullCyclesValue = self.NumberOfFullCyclesValue(numberOfFullCyclesValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(numberOfFullCyclesValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class StateOfCertifiedEnergy(aas.SubmodelElementCollection):

        class StateOfCertifiedEnergyValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"StateOfCertifiedEnergyValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"state of certified energy value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#stateOfCertifiedEnergyValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL847#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"StateOfCertifiedEnergy",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"state of certified energy"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#stateOfCertifiedEnergy"
                ),
                "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL847#001"),),
            }

        def __init__(
            self,
            stateOfCertifiedEnergyValue: Union[xsd.Float, StateOfCertifiedEnergyValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if stateOfCertifiedEnergyValue is not None and not isinstance(
                stateOfCertifiedEnergyValue, aas.SubmodelElement
            ):
                stateOfCertifiedEnergyValue = self.StateOfCertifiedEnergyValue(stateOfCertifiedEnergyValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(stateOfCertifiedEnergyValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class RemainingEnergy(aas.SubmodelElementCollection):

        class RemainingEnergyValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RemainingEnergyValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"remaining energy value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingEnergyValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL870#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"RemainingEnergy",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"remaining energy"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingEnergy"
                ),
                "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL870#001"),),
            }

        def __init__(
            self,
            remainingEnergyValue: Union[xsd.Float, RemainingEnergyValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if remainingEnergyValue is not None and not isinstance(remainingEnergyValue, aas.SubmodelElement):
                remainingEnergyValue = self.RemainingEnergyValue(remainingEnergyValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(remainingEnergyValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class RemainingCapacity(aas.SubmodelElementCollection):

        class RemainingCapacityValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RemainingCapacityValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"remaining capacity value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingCapacityValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL840#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"RemainingCapacity",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"remaining capacity"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingCapacity"
                ),
                "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL840#001"),),
            }

        def __init__(
            self,
            remainingCapacityValue: Union[xsd.Float, RemainingCapacityValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if remainingCapacityValue is not None and not isinstance(remainingCapacityValue, aas.SubmodelElement):
                remainingCapacityValue = self.RemainingCapacityValue(remainingCapacityValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(remainingCapacityValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class NegativeEvents(GeneratedSubmodelElementList):

        class Negativeevents_item(aas.SubmodelElementCollection):

            class NegativeEventValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NegativeEventValue",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"negative event value"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#negativeEventValue"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LastUpdate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LastUpdate",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                        ),
                        "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"negative event"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "The battery passport must contain information and data resulting from its use such as accidents. \n\nDIN DKE Spec 99100 chapter reference: 6.7.8.4"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#NegativeEvent"
                    ),
                }

            def __init__(
                self,
                negativeEventValue: Union[str, NegativeEventValue],
                lastUpdate: Union[xsd.DateTime, LastUpdate],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if negativeEventValue is not None and not isinstance(negativeEventValue, aas.SubmodelElement):
                    negativeEventValue = self.NegativeEventValue(negativeEventValue)

                # Build a submodel element if a raw value was passed in the argument

                if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                    lastUpdate = self.LastUpdate(lastUpdate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(negativeEventValue, lastUpdate)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"NegativeEvents",
                "type_value_list_element": aas.SubmodelElementCollection,
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"negative events"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#negativeEvents"
                ),
            }

        def __init__(
            self,
            negativeevents_items: Optional[Iterable[Negativeevents_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(negativeevents_items, str):
                raise TypeError("negativeevents_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(negativeevents_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class InformationOnAccidents(GeneratedSubmodelElementList):

        class Informationonaccidents_item(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": None,
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"document identifier"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"InformationOnAccidents",
                "type_value_list_element": aas.Property,
                "value_type_list_element": str,
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"information on accidents"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#informationOnAccidents"
                ),
                "supplemental_semantic_id": (
                    global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#DocumentIdentifierSet"),
                    global_ref(r"urn:irdi:0173-1#02-ABL848#001"),
                ),
            }

        def __init__(
            self,
            informationonaccidents_items: Optional[Iterable[Union[str, Informationonaccidents_item]]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(informationonaccidents_items, str):
                raise TypeError("informationonaccidents_items takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if informationonaccidents_items:
                informationonaccidents_items = [
                    i if isinstance(i, aas.SubmodelElement) else self.Informationonaccidents_item(i)
                    for i in informationonaccidents_items
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(informationonaccidents_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class TemperatureInformation(aas.SubmodelElementCollection):

        class TimeExtremeHighTemp(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TimeExtremeHighTemp",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time extreme high temp"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#timeExtremeHighTemp"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL816#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TimeExtremeLowTemp(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TimeExtremeLowTemp",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time extreme low temp"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#timeExtremeLowTemp"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL817#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TimeExtremeHighTempCharging(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TimeExtremeHighTempCharging",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time extreme high temp charging"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#timeExtremeHighTempCharging"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL818#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TimeExtremeLowTempCharging(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TimeExtremeLowTempCharging",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time extreme low temp charging"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#timeExtremeLowTempCharging"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL819#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"TemperatureInformation",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"temperature information"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#temperatureInformation"
                ),
            }

        def __init__(
            self,
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            timeExtremeHighTemp: Optional[Union[xsd.Float, TimeExtremeHighTemp]] = None,
            timeExtremeLowTemp: Optional[Union[xsd.Float, TimeExtremeLowTemp]] = None,
            timeExtremeHighTempCharging: Optional[Union[xsd.Float, TimeExtremeHighTempCharging]] = None,
            timeExtremeLowTempCharging: Optional[Union[xsd.Float, TimeExtremeLowTempCharging]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if timeExtremeHighTemp is not None and not isinstance(timeExtremeHighTemp, aas.SubmodelElement):
                timeExtremeHighTemp = self.TimeExtremeHighTemp(timeExtremeHighTemp)

            # Build a submodel element if a raw value was passed in the argument

            if timeExtremeLowTemp is not None and not isinstance(timeExtremeLowTemp, aas.SubmodelElement):
                timeExtremeLowTemp = self.TimeExtremeLowTemp(timeExtremeLowTemp)

            # Build a submodel element if a raw value was passed in the argument

            if timeExtremeHighTempCharging is not None and not isinstance(
                timeExtremeHighTempCharging, aas.SubmodelElement
            ):
                timeExtremeHighTempCharging = self.TimeExtremeHighTempCharging(timeExtremeHighTempCharging)

            # Build a submodel element if a raw value was passed in the argument

            if timeExtremeLowTempCharging is not None and not isinstance(
                timeExtremeLowTempCharging, aas.SubmodelElement
            ):
                timeExtremeLowTempCharging = self.TimeExtremeLowTempCharging(timeExtremeLowTempCharging)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                timeExtremeHighTemp,
                timeExtremeLowTemp,
                timeExtremeHighTempCharging,
                timeExtremeLowTempCharging,
                lastUpdate,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class RemainingPowerCapability(aas.SubmodelElementCollection):

        class RemainingPowerCapabilityDynamicAt(aas.SubmodelElementCollection):

            class RPCLastUpdated(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RPCLastUpdated",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"RPC last updated"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#rPCLastUpdated"
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AtSoC(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AtSoC",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"at so c"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#atSoC"
                        ),
                        "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL821#001"),),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PowerCapabilityAt(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PowerCapabilityAt",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"power capability at"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#powerCapabilityAt"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"RemainingPowerCapabilityDynamicAt",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"remaining power capability dynamic at"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingPowerCapabilityDynamicAt"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL853#001"),),
                }

            def __init__(
                self,
                rPCLastUpdated: Union[xsd.DateTime, RPCLastUpdated],
                atSoC: Union[xsd.Float, AtSoC],
                powerCapabilityAt: Union[xsd.Float, PowerCapabilityAt],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if rPCLastUpdated is not None and not isinstance(rPCLastUpdated, aas.SubmodelElement):
                    rPCLastUpdated = self.RPCLastUpdated(rPCLastUpdated)

                # Build a submodel element if a raw value was passed in the argument

                if atSoC is not None and not isinstance(atSoC, aas.SubmodelElement):
                    atSoC = self.AtSoC(atSoC)

                # Build a submodel element if a raw value was passed in the argument

                if powerCapabilityAt is not None and not isinstance(powerCapabilityAt, aas.SubmodelElement):
                    powerCapabilityAt = self.PowerCapabilityAt(powerCapabilityAt)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(rPCLastUpdated, atSoC, powerCapabilityAt)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"RemainingPowerCapability",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"remaining power capability"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingPowerCapability"
                ),
                "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL820#001"),),
            }

        def __init__(
            self,
            remainingPowerCapabilityDynamicAt: RemainingPowerCapabilityDynamicAt,
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(remainingPowerCapabilityDynamicAt, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class EvolutionOfSelfDischarge(aas.SubmodelElementCollection):

        class EvolutionOfSelfDischargeValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EvolutionOfSelfDischargeValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"evolution of self discharge value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#evolutionOfSelfDischargeValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL834#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"EvolutionOfSelfDischarge",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"evolution of self discharge"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#evolutionOfSelfDischarge"
                ),
            }

        def __init__(
            self,
            evolutionOfSelfDischargeValue: Union[xsd.Float, EvolutionOfSelfDischargeValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if evolutionOfSelfDischargeValue is not None and not isinstance(
                evolutionOfSelfDischargeValue, aas.SubmodelElement
            ):
                evolutionOfSelfDischargeValue = self.EvolutionOfSelfDischargeValue(evolutionOfSelfDischargeValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(evolutionOfSelfDischargeValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class CurrentSelfDischargingRate(aas.SubmodelElementCollection):

        class CurrentSelfDischargingRateValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CurrentSelfDischargingRateValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"current self discharging rate value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#currentSelfDischargingRateValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL825#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"CurrentSelfDischargingRate",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"current self discharging rate"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#currentSelfDischargingRate"
                ),
            }

        def __init__(
            self,
            currentSelfDischargingRateValue: Union[xsd.Float, CurrentSelfDischargingRateValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if currentSelfDischargingRateValue is not None and not isinstance(
                currentSelfDischargingRateValue, aas.SubmodelElement
            ):
                currentSelfDischargingRateValue = self.CurrentSelfDischargingRateValue(currentSelfDischargingRateValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(currentSelfDischargingRateValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class RemainingRoundTripEnergyEfficiency(aas.SubmodelElementCollection):

        class RemainingRoundTripEnergyEfficiencyValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RemainingRoundTripEnergyEfficiencyValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"remaining round trip energy efficiency value"}
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingRoundTripEnergyEfficiencyValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:iridi:0173-1#02-ABL851#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"RemainingRoundTripEnergyEfficiency",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"remaining round trip energy efficiency"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#remainingRoundTripEnergyEfficiency"
                ),
            }

        def __init__(
            self,
            remainingRoundTripEnergyEfficiencyValue: Union[xsd.Float, RemainingRoundTripEnergyEfficiencyValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if remainingRoundTripEnergyEfficiencyValue is not None and not isinstance(
                remainingRoundTripEnergyEfficiencyValue, aas.SubmodelElement
            ):
                remainingRoundTripEnergyEfficiencyValue = self.RemainingRoundTripEnergyEfficiencyValue(
                    remainingRoundTripEnergyEfficiencyValue
                )

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(remainingRoundTripEnergyEfficiencyValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class StateOfCharge(aas.SubmodelElementCollection):

        class StateOfChargeValue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"StateOfChargeValue",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"state of charge value"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#stateOfChargeValue"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABL821#001"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LastUpdate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LastUpdate",
                    "value_type": xsd.DateTime,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"last update"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#lastUpdate"
                    ),
                    "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-ABG740#003"),),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"StateOfCharge",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"state of charge"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#stateOfCharge"
                ),
            }

        def __init__(
            self,
            stateOfChargeValue: Union[xsd.Float, StateOfChargeValue],
            lastUpdate: Union[xsd.DateTime, LastUpdate],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if stateOfChargeValue is not None and not isinstance(stateOfChargeValue, aas.SubmodelElement):
                stateOfChargeValue = self.StateOfChargeValue(stateOfChargeValue)

            # Build a submodel element if a raw value was passed in the argument

            if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                lastUpdate = self.LastUpdate(lastUpdate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(stateOfChargeValue, lastUpdate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ProductCondition",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"product condition"}),
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"Covers all battery lifetime relevant properties."}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02035-5",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(
                r"urn:samm:io.admin-shell.idta.batterypass.product_condition:1.0.0#ProductCondition"
            ),
        }

    def __init__(
        self,
        id_: str,
        numberOfFullCycles: NumberOfFullCycles,
        informationOnAccidents: Union[
            Iterable[Union[str, InformationOnAccidents.Informationonaccidents_item]], InformationOnAccidents
        ],
        temperatureInformation: TemperatureInformation,
        stateOfCharge: StateOfCharge,
        energyThroughput: Optional[EnergyThroughput] = None,
        capacityThroughput: Optional[CapacityThroughput] = None,
        stateOfCertifiedEnergy: Optional[StateOfCertifiedEnergy] = None,
        remainingEnergy: Optional[RemainingEnergy] = None,
        remainingCapacity: Optional[RemainingCapacity] = None,
        negativeEvents: Optional[Union[Iterable[NegativeEvents.Negativeevents_item], NegativeEvents]] = None,
        remainingPowerCapability: Optional[RemainingPowerCapability] = None,
        evolutionOfSelfDischarge: Optional[EvolutionOfSelfDischarge] = None,
        currentSelfDischargingRate: Optional[CurrentSelfDischargingRate] = None,
        remainingRoundTripEnergyEfficiency: Optional[RemainingRoundTripEnergyEfficiency] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(negativeEvents, str):
            raise TypeError("negativeEvents takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if negativeEvents is not None and not isinstance(negativeEvents, aas.SubmodelElement):
            negativeEvents = self.NegativeEvents(negativeEvents)

        # A str would be split into its characters
        if isinstance(informationOnAccidents, str):
            raise TypeError("informationOnAccidents takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if informationOnAccidents is not None and not isinstance(informationOnAccidents, aas.SubmodelElement):
            informationOnAccidents = self.InformationOnAccidents(informationOnAccidents)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            energyThroughput,
            capacityThroughput,
            numberOfFullCycles,
            stateOfCertifiedEnergy,
            remainingEnergy,
            remainingCapacity,
            negativeEvents,
            informationOnAccidents,
            temperatureInformation,
            remainingPowerCapability,
            evolutionOfSelfDischarge,
            currentSelfDischargingRate,
            remainingRoundTripEnergyEfficiency,
            stateOfCharge,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
