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


class CarbonFootprint(aas.Submodel):

    class ProductCarbonFootprints(GeneratedSubmodelElementList):

        class Productcarbonfootprints_item(aas.SubmodelElementCollection):

            class PcfCalculationMethods(GeneratedSubmodelElementList):

                class Pcfcalculationmethods_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Folgenabschätzungsmethode / Berechnungsmethode",
                                    r"en": r"PCF calculation method",
                                }
                            ),
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"0173-1#02-ABG854#003"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"PcfCalculationMethods",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABG854#003"),
                        "value_type_list_element": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Folgenabschätzungsmethoden", r"en": r"PCF calculation methods"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Normen, Standards, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                                r"en": 'Standards, methods for determining the greenhouse gas emissions of a product.\n\nThis Value List is based on ECLASS 15 with IRDI 0173-1#09-AAO115#003. The full list can be found in Section 2.5 in "Product Carbon Footprint 1.0 (IDTA-02023)".\n',
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CarbonFootprint/PcfCalculationMethods/1/0"
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#pcfCalculationMethods"),
                        ),
                    }

                def __init__(
                    self,
                    pcfcalculationmethods_items: Iterable[Union[str, Pcfcalculationmethods_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(pcfcalculationmethods_items, str):
                        raise TypeError("pcfcalculationmethods_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if pcfcalculationmethods_items:
                        pcfcalculationmethods_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Pcfcalculationmethods_item(i)
                            for i in pcfcalculationmethods_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        pcfcalculationmethods_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class PcfCO2eq(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PcfCO2eq",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"CO2-Äquivalent", r"en": r"PCF co 2 eq"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"DIN DKE Spec 99100 chapter reference: 6.3.2"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABG855#003"),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#pcfCo2eq"),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ReferenceImpactUnitForCalculation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ReferenceImpactUnitForCalculation",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Referenzeinheit für die Berechnung",
                                r"en": r"reference impact unit for calculation",
                            }
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "If a normalized product carbon footprint (PCF) value is provided, the reference value for calculation should be a specific unit such as 'kWh'. \nIf the total PCF value is provided the reference value for calculation should be 'piece'."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABG856#003"),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#referenceImpactUnitForCalculation"
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class QuantityOfMeasureForCalculation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"QuantityOfMeasureForCalculation",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Mengenangabe für die Berechnung",
                                r"en": r"quantity of measure for calculation",
                            }
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "If a normalized product carbon footprint (PCF) value is provided, the quantity of measure for calculation should be 1.\nIf the total PCF value is provided the quantity of measure for calculation should be 1."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABG857#003"),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#quantityOfMeasureForCalculation"
                            ),
                        ),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LifeCyclePhases(GeneratedSubmodelElementList):

                class Lifecyclephases_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Lebenszyklusphase", r"en": r"life cycle phase"}
                            ),
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"0173-1#02-ABG858#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"LifeCyclePhases",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABG858#004"),
                        "value_type_list_element": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Lebenszyklusphasen", r"en": r"life cycle phases"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": 'List of life cycle stages of the product according to the quantification requirements of the standard to which the PCF carbon footprint statement refers.\n\nThe string value in the value list is based on DIN DKE SPEC 99100: "A1 - raw material supply (and upstream production)" (6.3.5 required lify cycle mapping), "A3 - production" (6.3.4 Contribution of main product production/manufacturing lifecycle stage), "A4 - transport to final destination" (6.3.5 Contribution of distribution lifecycle stage), "C3 - recycling, waste treatment" (6.3.6 Contribution of end of life and recycling lifecycle stage)\n\nPlease note that the model should always contain at least one Product Carbon Footprint entry that reflects the total PCF value (including all life cycle phases) of the battery.\n'
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/LifeCyclePhases/1/0"),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#lifeCyclePhases"),
                            global_ref(r"0173-1#02-ABG858#003"),
                        ),
                    }

                def __init__(
                    self,
                    lifecyclephases_items: Iterable[Union[str, Lifecyclephases_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(lifecyclephases_items, str):
                        raise TypeError("lifecyclephases_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if lifecyclephases_items:
                        lifecyclephases_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Lifecyclephases_item(i)
                            for i in lifecyclephases_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(lifecyclephases_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class PerformanceClass(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PerformanceClass",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"performance class"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#performanceClass"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class WebLinkToPublicCarbonFootprintStudy(GeneratedSubmodelElementList):

                class Weblinktopubliccarbonfootprintstudy_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"document identifier"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": "Document identifier of the document (e.g., PDF) that can be found in the HandoverDocumentation Submodel.\n\nDIN DKE Spec 99100 chapter reference: 6.3.8 "
                                }
                            ),
                            "semantic_id": global_ref(
                                r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier"
                            ),
                            "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO099#004"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"WebLinkToPublicCarbonFootprintStudy",
                        "type_value_list_element": aas.Property,
                        "value_type_list_element": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"web link to public carbon footprint study"}
                        ),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#webLinkToPublicCarbonFootprintStudy"
                        ),
                    }

                def __init__(
                    self,
                    weblinktopubliccarbonfootprintstudy_items: Iterable[
                        Union[str, Weblinktopubliccarbonfootprintstudy_item]
                    ],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(weblinktopubliccarbonfootprintstudy_items, str):
                        raise TypeError("weblinktopubliccarbonfootprintstudy_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if weblinktopubliccarbonfootprintstudy_items:
                        weblinktopubliccarbonfootprintstudy_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.Weblinktopubliccarbonfootprintstudy_item(i)
                            )
                            for i in weblinktopubliccarbonfootprintstudy_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        weblinktopubliccarbonfootprintstudy_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Produkt CO2-Fußabdruck", r"en": r"product carbon footprint"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use."
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/1/0"
                    ),
                    "supplemental_semantic_id": (
                        global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#ProductCarbonFootprint"
                        ),
                    ),
                }

            def __init__(
                self,
                pcfCalculationMethods: Union[
                    Iterable[Union[str, PcfCalculationMethods.Pcfcalculationmethods_item]], PcfCalculationMethods
                ],
                pcfCO2eq: Union[xsd.Decimal, PcfCO2eq],
                referenceImpactUnitForCalculation: Union[str, ReferenceImpactUnitForCalculation],
                quantityOfMeasureForCalculation: Union[float, QuantityOfMeasureForCalculation],
                lifeCyclePhases: Union[Iterable[Union[str, LifeCyclePhases.Lifecyclephases_item]], LifeCyclePhases],
                performanceClass: Union[str, PerformanceClass],
                webLinkToPublicCarbonFootprintStudy: Union[
                    Iterable[Union[str, WebLinkToPublicCarbonFootprintStudy.Weblinktopubliccarbonfootprintstudy_item]],
                    WebLinkToPublicCarbonFootprintStudy,
                ],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(pcfCalculationMethods, str):
                    raise TypeError("pcfCalculationMethods takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if pcfCalculationMethods is not None and not isinstance(pcfCalculationMethods, aas.SubmodelElement):
                    pcfCalculationMethods = self.PcfCalculationMethods(pcfCalculationMethods)

                # Build a submodel element if a raw value was passed in the argument

                if pcfCO2eq is not None and not isinstance(pcfCO2eq, aas.SubmodelElement):
                    pcfCO2eq = self.PcfCO2eq(pcfCO2eq)

                # Build a submodel element if a raw value was passed in the argument

                if referenceImpactUnitForCalculation is not None and not isinstance(
                    referenceImpactUnitForCalculation, aas.SubmodelElement
                ):
                    referenceImpactUnitForCalculation = self.ReferenceImpactUnitForCalculation(
                        referenceImpactUnitForCalculation
                    )

                # Build a submodel element if a raw value was passed in the argument

                if quantityOfMeasureForCalculation is not None and not isinstance(
                    quantityOfMeasureForCalculation, aas.SubmodelElement
                ):
                    quantityOfMeasureForCalculation = self.QuantityOfMeasureForCalculation(
                        quantityOfMeasureForCalculation
                    )

                # A str would be split into its characters
                if isinstance(lifeCyclePhases, str):
                    raise TypeError("lifeCyclePhases takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if lifeCyclePhases is not None and not isinstance(lifeCyclePhases, aas.SubmodelElement):
                    lifeCyclePhases = self.LifeCyclePhases(lifeCyclePhases)

                # Build a submodel element if a raw value was passed in the argument

                if performanceClass is not None and not isinstance(performanceClass, aas.SubmodelElement):
                    performanceClass = self.PerformanceClass(performanceClass)

                # A str would be split into its characters
                if isinstance(webLinkToPublicCarbonFootprintStudy, str):
                    raise TypeError("webLinkToPublicCarbonFootprintStudy takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if webLinkToPublicCarbonFootprintStudy is not None and not isinstance(
                    webLinkToPublicCarbonFootprintStudy, aas.SubmodelElement
                ):
                    webLinkToPublicCarbonFootprintStudy = self.WebLinkToPublicCarbonFootprintStudy(
                        webLinkToPublicCarbonFootprintStudy
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    pcfCalculationMethods,
                    pcfCO2eq,
                    referenceImpactUnitForCalculation,
                    quantityOfMeasureForCalculation,
                    lifeCyclePhases,
                    performanceClass,
                    webLinkToPublicCarbonFootprintStudy,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"ProductCarbonFootprints",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(
                    r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/1/0"
                ),
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Produkt CO2-Fußabdruck", r"en": r"product carbon footprints"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprints/1/0"),
                "supplemental_semantic_id": (
                    global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#CarbonFootprintBattery"
                    ),
                ),
            }

        def __init__(
            self,
            productcarbonfootprints_items: Iterable[Productcarbonfootprints_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(productcarbonfootprints_items, str):
                raise TypeError("productcarbonfootprints_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(productcarbonfootprints_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"CarbonFootprint",
            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"C02 Footprint", r"en": r"carbon footprint"}),
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"The Submodel provides the means to access the Carbon Footprint of the asset."}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02023-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/1/0"),
            "supplemental_semantic_id": (
                global_ref(r"urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#CarbonFootprintBattery"),
            ),
        }

    def __init__(
        self,
        id_: str,
        productCarbonFootprints: Union[
            Iterable[ProductCarbonFootprints.Productcarbonfootprints_item], ProductCarbonFootprints
        ],
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(productCarbonFootprints, str):
            raise TypeError("productCarbonFootprints takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if productCarbonFootprints is not None and not isinstance(productCarbonFootprints, aas.SubmodelElement):
            productCarbonFootprints = self.ProductCarbonFootprints(productCarbonFootprints)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(productCarbonFootprints)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
