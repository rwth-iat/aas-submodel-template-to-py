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


class MaterialComposition(aas.Submodel):

    class BatteryChemistry(aas.SubmodelElementCollection):

        class ShortName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ShortName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"short name"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#shortName"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ClearName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ClearName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"clear name"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#clearName"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"BatteryChemistry",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery chemistry"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryChemistry"
                ),
            }

        def __init__(
            self,
            shortName: Union[str, ShortName],
            clearName: Union[str, ClearName],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if shortName is not None and not isinstance(shortName, aas.SubmodelElement):
                shortName = self.ShortName(shortName)

            # Build a submodel element if a raw value was passed in the argument

            if clearName is not None and not isinstance(clearName, aas.SubmodelElement):
                clearName = self.ClearName(clearName)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(shortName, clearName)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class BatteryMaterials(GeneratedSubmodelElementList):

        class Batterymaterials_item(aas.SubmodelElementCollection):

            class BatteryMaterialLocation(aas.SubmodelElementCollection):

                class ComponentName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ComponentName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"component name"}),
                            "semantic_id": global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentName"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ComponentId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ComponentId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"component ID"}),
                            "semantic_id": global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentId"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"BatteryMaterialLocation",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery material location"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialLocation"
                        ),
                    }

                def __init__(
                    self,
                    componentName: Optional[Union[str, ComponentName]] = None,
                    componentId: Optional[Union[str, ComponentId]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    if sum(arg is not None for arg in (componentName, componentId)) > 1:
                        raise ValueError(
                            "Only one of componentName, componentId may be given (SMT/EitherOr 'BatteryMaterialLocationComponent')"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if componentName is not None and not isinstance(componentName, aas.SubmodelElement):
                        componentName = self.ComponentName(componentName)

                    # Build a submodel element if a raw value was passed in the argument

                    if componentId is not None and not isinstance(componentId, aas.SubmodelElement):
                        componentId = self.ComponentId(componentId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(componentName, componentId)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class BatteryMaterialIdentifier(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BatteryMaterialIdentifier",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery material identifier"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialIdentifier"
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"https://www.cas.org/cas-data/cas-registry"),
                            global_ref(r"urn:irdi:0173-1#02-ABH034#003"),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BatteryMaterialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BatteryMaterialName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery material name"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialName"
                        ),
                        "supplemental_semantic_id": (global_ref(r"urn:irdi:0173-1#02-AAN920#003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BatteryMaterialMass(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BatteryMaterialMass",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery material mass"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialMass"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IsCriticalRawMaterial(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsCriticalRawMaterial",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"is critical raw material"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#isCriticalRawMaterial"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery material"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#BatteryMaterial"
                    ),
                }

            def __init__(
                self,
                batteryMaterialLocation: BatteryMaterialLocation,
                batteryMaterialIdentifier: Union[str, BatteryMaterialIdentifier],
                batteryMaterialName: Union[str, BatteryMaterialName],
                isCriticalRawMaterial: Union[bool, IsCriticalRawMaterial],
                batteryMaterialMass: Optional[Union[xsd.Float, BatteryMaterialMass]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if batteryMaterialIdentifier is not None and not isinstance(
                    batteryMaterialIdentifier, aas.SubmodelElement
                ):
                    batteryMaterialIdentifier = self.BatteryMaterialIdentifier(batteryMaterialIdentifier)

                # Build a submodel element if a raw value was passed in the argument

                if batteryMaterialName is not None and not isinstance(batteryMaterialName, aas.SubmodelElement):
                    batteryMaterialName = self.BatteryMaterialName(batteryMaterialName)

                # Build a submodel element if a raw value was passed in the argument

                if batteryMaterialMass is not None and not isinstance(batteryMaterialMass, aas.SubmodelElement):
                    batteryMaterialMass = self.BatteryMaterialMass(batteryMaterialMass)

                # Build a submodel element if a raw value was passed in the argument

                if isCriticalRawMaterial is not None and not isinstance(isCriticalRawMaterial, aas.SubmodelElement):
                    isCriticalRawMaterial = self.IsCriticalRawMaterial(isCriticalRawMaterial)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    batteryMaterialLocation,
                    batteryMaterialIdentifier,
                    batteryMaterialName,
                    batteryMaterialMass,
                    isCriticalRawMaterial,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"BatteryMaterials",
                "type_value_list_element": aas.SubmodelElementCollection,
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery materials"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterials"
                ),
            }

        def __init__(
            self, batterymaterials_items: Iterable[Batterymaterials_item], **kwargs: Unpack[SubmodelElementListMetadata]
        ):

            # A str would be split into its characters
            if isinstance(batterymaterials_items, str):
                raise TypeError("batterymaterials_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(batterymaterials_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class HazardousSubstances(GeneratedSubmodelElementList):

        class Hazardoussubstances_item(aas.SubmodelElementCollection):

            class HazardousSubstanceClass(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"HazardousSubstanceClass",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substance class"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceClass"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HazardousSubstanceName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"HazardousSubstanceName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substance name"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HazardousSubstanceConcentration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"HazardousSubstanceConcentration",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substance concentration"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceConcentration"
                        ),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HazardousSubstanceImpact(GeneratedSubmodelElementList):

                class Hazardoussubstanceimpact_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"impact"}),
                            "semantic_id": global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#Impact"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"HazardousSubstanceImpact",
                        "type_value_list_element": aas.Property,
                        "value_type_list_element": str,
                        "order_relevant": False,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substance impact"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceImpact"
                        ),
                    }

                def __init__(
                    self,
                    hazardoussubstanceimpact_items: Optional[
                        Iterable[Union[str, Hazardoussubstanceimpact_item]]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(hazardoussubstanceimpact_items, str):
                        raise TypeError("hazardoussubstanceimpact_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if hazardoussubstanceimpact_items:
                        hazardoussubstanceimpact_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Hazardoussubstanceimpact_item(i)
                            for i in hazardoussubstanceimpact_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        hazardoussubstanceimpact_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class HazardousSubstanceLocation(aas.SubmodelElementCollection):

                class ComponentName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ComponentName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"component name"}),
                            "semantic_id": global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentName"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ComponentId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ComponentId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"component ID"}),
                            "semantic_id": global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentId"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"HazardousSubstanceLocation",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substance location"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceLocation"
                        ),
                    }

                def __init__(
                    self,
                    componentName: Optional[Union[str, ComponentName]] = None,
                    componentId: Optional[Union[str, ComponentId]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    if sum(arg is not None for arg in (componentName, componentId)) > 1:
                        raise ValueError(
                            "Only one of componentName, componentId may be given (SMT/EitherOr 'HazardousSubstanceLocationComponent')"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if componentName is not None and not isinstance(componentName, aas.SubmodelElement):
                        componentName = self.ComponentName(componentName)

                    # Build a submodel element if a raw value was passed in the argument

                    if componentId is not None and not isinstance(componentId, aas.SubmodelElement):
                        componentId = self.ComponentId(componentId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(componentName, componentId)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class HazardousSubstanceIdentifier(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"HazardousSubstanceIdentifier",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substance identifier"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceIdentifier"
                        ),
                        "supplemental_semantic_id": (global_ref(r"https://www.cas.org/cas-data/cas-registry"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substance"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#HazardousSubstance"
                    ),
                }

            def __init__(
                self,
                hazardousSubstanceName: Union[str, HazardousSubstanceName],
                hazardousSubstanceIdentifier: Union[str, HazardousSubstanceIdentifier],
                hazardousSubstanceClass: Optional[Union[str, HazardousSubstanceClass]] = None,
                hazardousSubstanceConcentration: Optional[Union[float, HazardousSubstanceConcentration]] = None,
                hazardousSubstanceImpact: Optional[
                    Union[
                        Iterable[Union[str, HazardousSubstanceImpact.Hazardoussubstanceimpact_item]],
                        HazardousSubstanceImpact,
                    ]
                ] = None,
                hazardousSubstanceLocation: Optional[HazardousSubstanceLocation] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if hazardousSubstanceClass is not None and not isinstance(hazardousSubstanceClass, aas.SubmodelElement):
                    hazardousSubstanceClass = self.HazardousSubstanceClass(hazardousSubstanceClass)

                # Build a submodel element if a raw value was passed in the argument

                if hazardousSubstanceName is not None and not isinstance(hazardousSubstanceName, aas.SubmodelElement):
                    hazardousSubstanceName = self.HazardousSubstanceName(hazardousSubstanceName)

                # Build a submodel element if a raw value was passed in the argument

                if hazardousSubstanceConcentration is not None and not isinstance(
                    hazardousSubstanceConcentration, aas.SubmodelElement
                ):
                    hazardousSubstanceConcentration = self.HazardousSubstanceConcentration(
                        hazardousSubstanceConcentration
                    )

                # A str would be split into its characters
                if isinstance(hazardousSubstanceImpact, str):
                    raise TypeError("hazardousSubstanceImpact takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if hazardousSubstanceImpact is not None and not isinstance(
                    hazardousSubstanceImpact, aas.SubmodelElement
                ):
                    hazardousSubstanceImpact = self.HazardousSubstanceImpact(hazardousSubstanceImpact)

                # Build a submodel element if a raw value was passed in the argument

                if hazardousSubstanceIdentifier is not None and not isinstance(
                    hazardousSubstanceIdentifier, aas.SubmodelElement
                ):
                    hazardousSubstanceIdentifier = self.HazardousSubstanceIdentifier(hazardousSubstanceIdentifier)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    hazardousSubstanceClass,
                    hazardousSubstanceName,
                    hazardousSubstanceConcentration,
                    hazardousSubstanceImpact,
                    hazardousSubstanceLocation,
                    hazardousSubstanceIdentifier,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"HazardousSubstances",
                "type_value_list_element": aas.SubmodelElementCollection,
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hazardous substances"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstances"
                ),
            }

        def __init__(
            self,
            hazardoussubstances_items: Optional[Iterable[Hazardoussubstances_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(hazardoussubstances_items, str):
                raise TypeError("hazardoussubstances_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(hazardoussubstances_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"MaterialComposition",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"material composition"}),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": "Mandatory data: Battery chemistry; critical raw materials; materials used in the cathode, anode, and \nelectrolyte; hazardous substances; impact of substances on the environment and on human health or \nsafety."
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02035-6",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(
                r"urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.0#MaterialComposition"
            ),
        }

    def __init__(
        self,
        id_: str,
        batteryChemistry: BatteryChemistry,
        batteryMaterials: Union[Iterable[BatteryMaterials.Batterymaterials_item], BatteryMaterials],
        hazardousSubstances: Union[Iterable[HazardousSubstances.Hazardoussubstances_item], HazardousSubstances],
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(batteryMaterials, str):
            raise TypeError("batteryMaterials takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if batteryMaterials is not None and not isinstance(batteryMaterials, aas.SubmodelElement):
            batteryMaterials = self.BatteryMaterials(batteryMaterials)

        # A str would be split into its characters
        if isinstance(hazardousSubstances, str):
            raise TypeError("hazardousSubstances takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if hazardousSubstances is not None and not isinstance(hazardousSubstances, aas.SubmodelElement):
            hazardousSubstances = self.HazardousSubstances(hazardousSubstances)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(batteryChemistry, batteryMaterials, hazardousSubstances)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
