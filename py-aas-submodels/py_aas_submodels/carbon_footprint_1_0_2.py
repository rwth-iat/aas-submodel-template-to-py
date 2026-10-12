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
                                    r"en": r"impact assessment method / calculation method",
                                }
                            ),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Standard, method for determining the greenhouse gas emissions of a product.",
                                    r"de": r"Norm, Standard, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                                }
                            ),
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
                            dict_={r"de": r"Folgenabschätzungsmethoden", r"en": r"impact assessment methods"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Normen, Standards, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                                r"en": r"Standards, methods for determining the greenhouse gas emissions of a product.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CarbonFootprint/PcfCalculationMethods/1/0"
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
                            dict_={r"de": r"CO2-Äquivalent", r"en": r"CO2 equivalent"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Sum of all greenhouse gas emissions of a product according to the quantification requirements of the standard."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABG855#003"),
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
                                r"en": r"Reference value for calculation",
                            }
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Quantity unit of the product to which the PCF information on the CO2 footprint refers."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABG856#003"),
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
                                r"en": r"provides the quantity number of pieces or mass or volume to compute the impact of climate change or product carbon footprint."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABG857#003"),
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
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Life cycle stages of the product according to the quantification requirements of the standard to which the PCF carbon footprint statement refers"
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABG858#003"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"LifeCyclePhases",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABG858#003"),
                        "value_type_list_element": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Lebenszyklusphasen", r"en": r"life cycle phases"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List of life cycle stages of the product according to the quantification requirements of the standard to which the PCF carbon footprint statement refers"
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/LifeCyclePhases/1/0"),
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

            class ExplanatoryStatement(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"ExplanatoryStatement",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Erklärung", r"en": r"Explanatory statement"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Explanation required or provided to ensure that a footprint communication can be properly understood by a purchaser, potential purchaser, or user of the product."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CarbonFootprint/ExplanatoryStatement/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class GoodsHandoverAddress(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"GoodsHandoverAddress",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Warenübergabeadresse", r"en": r"goods address hand-over"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Indicates the hand-over address of the goods transport"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"https://admin-shell.io/smt-dropin/smt-dropin-use/1/0"),
                            global_ref(r"0112/2///61360_7#AAS002#001"),
                            global_ref(r"0173-1#02-AAQ837#008"),
                        ),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class PublicationDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PublicationDate",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Veröffentlichungsdatum", r"en": r"Publication date"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "The UTC timestamp on which a Product Carbon Footprint (PCF) - a calculation of a product's total greenhouse gas emissions - was created and published"
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/PublicationDate/1/0"),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ExpirationDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExpirationDate",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Ablaufdatum", r"en": r"Expiration date"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"End date up to which a study or data collection for calculating an ecological footprint is considered current and valid before an update or new calculation is required."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/ExpirationDate/1/0"),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Produkt CO2-Fußabdruck", r"en": r"Product carbon footprint"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use."
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/1/0"
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
                publicationDate: Union[xsd.DateTime, PublicationDate],
                explanatoryStatement: Optional[ExplanatoryStatement] = None,
                goodsHandoverAddress: Optional[GoodsHandoverAddress] = None,
                expirationDate: Optional[Union[xsd.DateTime, ExpirationDate]] = None,
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

                if publicationDate is not None and not isinstance(publicationDate, aas.SubmodelElement):
                    publicationDate = self.PublicationDate(publicationDate)

                # Build a submodel element if a raw value was passed in the argument

                if expirationDate is not None and not isinstance(expirationDate, aas.SubmodelElement):
                    expirationDate = self.ExpirationDate(expirationDate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    pcfCalculationMethods,
                    pcfCO2eq,
                    referenceImpactUnitForCalculation,
                    quantityOfMeasureForCalculation,
                    lifeCyclePhases,
                    explanatoryStatement,
                    goodsHandoverAddress,
                    publicationDate,
                    expirationDate,
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
                    dict_={r"de": r"Produkt CO2-Fußabdruck", r"en": r"Product carbon footprint"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprints/1/0"),
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

    class ProductOrSectorSpecificCarbonFootprints(GeneratedSubmodelElementList):

        class Productorsectorspecificcarbonfootprints_item(aas.SubmodelElementCollection):

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
                                    r"en": r"impact assessment method / calculation method",
                                }
                            ),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Standard, method for determining the greenhouse gas emissions of a product.",
                                    r"de": r"Norm, Standard, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                                }
                            ),
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
                            dict_={r"de": r"Folgenabschätzungsmethoden", r"en": r"impact assessment methods"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Normen, Standards, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                                r"en": r"Standards, methods for determining the greenhouse gas emissions of a product.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CarbonFootprint/PcfCalculationMethods/1/0"
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

            class ProductOrSectorSpecificRule(aas.SubmodelElementCollection):

                class PcfRuleOperator(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PcfRuleOperator",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Herausgeber der PCF Berechnungsmethode",
                                    r"en": r"Operator of the PCF calculation method",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Einrichtung, welche spezifische Anweisungen und Methoden zur Berechnung und Überwachung des CO2-Fußabdrucks eines Produkts oder Sektors definiert und umsetzt.",
                                    r"en": r"Organization that defines and implements specific instructions and methods for calculating and monitoring the carbon footprint of a product or sector.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/Operator/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PcfRuleName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PcfRuleName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Name der PCF Berechnungsmethode",
                                    r"en": r"Name of the PCF calculation method",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Folgenabschätzungsmethode / Berechnungsmethode",
                                    r"en": r"Standard, method for determining the greenhouse gas emissions of a product",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/Name/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PcfRuleVersion(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PcfRuleVersion",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Version der PCF Berechnungsmethode",
                                    r"en": r"Version of the PCF calculation method",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Spezifische Ausgabe oder Revision der Regel, die zur Berechnung des CO2-Fußabdrucks eines Produkts verwendet wird.",
                                    r"en": r"Specific version or revision of the rule used to calculate the carbon footprint of a product.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/Version/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PcfRuleOnlineReference(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"PcfRuleOnlineReference",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Online Referenz zur PCF Berechnungsmethode",
                                    r"en": r"Online reference to the PCF calculation method",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Online-Referenz zur PCF-Berechnungsmethodik, die detaillierte Anweisungen und Richtlinien zur Berechnung des CO2-Fußabdrucks eines Produkts bereitstellt.",
                                    r"en": "Online PCF calculation methodology reference that provides detailed instructions and guidelines for calculating a product's carbon footprint.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/OnlineReference/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/pdf",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProductOrSectorSpecificRule",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Produktspezifische oder sektorspezifische Regel",
                                r"en": r"Product or Sector Specific Rule",
                            }
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Beinhaltet weiterführende Informationen zur produktspezifischen oder sektorspezifischen Regel, welche zur Berechnung des CO2-Fußabdrucks eingesetzt wird. ",
                                r"en": r"Contains further information on the product-specific or sector-specific rule used to calculate the carbon footprint.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/1/0"
                        ),
                    }

                def __init__(
                    self,
                    pcfRuleOperator: Union[str, PcfRuleOperator],
                    pcfRuleName: Union[str, PcfRuleName],
                    pcfRuleVersion: Optional[Union[str, PcfRuleVersion]] = None,
                    pcfRuleOnlineReference: Optional[PcfRuleOnlineReference] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if pcfRuleOperator is not None and not isinstance(pcfRuleOperator, aas.SubmodelElement):
                        pcfRuleOperator = self.PcfRuleOperator(pcfRuleOperator)

                    # Build a submodel element if a raw value was passed in the argument

                    if pcfRuleName is not None and not isinstance(pcfRuleName, aas.SubmodelElement):
                        pcfRuleName = self.PcfRuleName(pcfRuleName)

                    # Build a submodel element if a raw value was passed in the argument

                    if pcfRuleVersion is not None and not isinstance(pcfRuleVersion, aas.SubmodelElement):
                        pcfRuleVersion = self.PcfRuleVersion(pcfRuleVersion)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        pcfRuleOperator, pcfRuleName, pcfRuleVersion, pcfRuleOnlineReference
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ExternalPcfApi(aas.SubmodelElementCollection):

                class PcfApiEndpoint(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PcfApiEndpoint",
                            "value_type": xsd.AnyURI,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Endpunkt", r"en": r"Endpoint"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Spezifische URL oder Adresse, über die Daten zur Berechnung des CO2-Fußabdrucks eines Produkts von externen Quellen abgerufen werden können.",
                                    r"en": r"Specific URL or address that can be used to retrieve data from external sources to calculate the carbon footprint of a product.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CarbonFootprint/ExternalPcfApi/Endpoint/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PcfApiQuery(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PcfApiQuery",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Abfrage", r"en": r"Query"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"de": r"Spezifische Abfrage, über die Daten zur Berechnung des CO2-Fußabdrucks eines Produkts von externen Quellen abgerufen werden können.",
                                    r"en": r"Specific query that can be used to retrieve data from external sources to calculate the carbon footprint of a product.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CarbonFootprint/ExternalPcfApi/Query/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ExternalPcfApi",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Externe API für PCF Informationen",
                                r"en": r"External API for PCF information",
                            }
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Ein externer Dienst, der über eine Schnittstelle Informationen zum CO2-Fußabdruck bereitstellt und den Abruf dieser Daten auf Abruf ermöglicht.",
                                r"en": r"An external service that provides carbon footprint information via an interface, allowing on-demand retrieval of this data when required.",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/ExternalPcfApi/1/0"),
                    }

                def __init__(
                    self,
                    pcfApiEndpoint: Union[xsd.AnyURI, PcfApiEndpoint],
                    pcfApiQuery: Union[str, PcfApiQuery],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if pcfApiEndpoint is not None and not isinstance(pcfApiEndpoint, aas.SubmodelElement):
                        pcfApiEndpoint = self.PcfApiEndpoint(pcfApiEndpoint)

                    # Build a submodel element if a raw value was passed in the argument

                    if pcfApiQuery is not None and not isinstance(pcfApiQuery, aas.SubmodelElement):
                        pcfApiQuery = self.PcfApiQuery(pcfApiQuery)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(pcfApiEndpoint, pcfApiQuery)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class PcfInformation(aas.SubmodelElementCollection):

                class ArbitraryContent(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ArbitraryContent",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Free area for structured collection of specific items of a specific PCF."
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"PcfInformation",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"de": r"Ein Abschnitt, in dem weitere Inhalte entsprechend der Berechnungsmethode zum Product Carbon Footprint aufgeführt werden.",
                                r"en": r"A section in which further content is listed according to the calculation method for the Product Carbon Footprint.",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/PcfInformation/1/0"),
                    }

                def __init__(
                    self,
                    arbitraryContent: Optional[Iterable[Union[str, ArbitraryContent]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(arbitraryContent, str):
                        raise TypeError("arbitraryContent takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryContent:
                        arbitraryContent = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryContent(i)
                            for i in arbitraryContent
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(arbitraryContent)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Product Carbon Footprint, which is determined in accordance with sector or product group-specific rules or guidelines and covers the life cycle or parts of a product life cycle."
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificCarbonFootprint/1/0"
                    ),
                }

            def __init__(
                self,
                pcfCalculationMethods: Union[
                    Iterable[Union[str, PcfCalculationMethods.Pcfcalculationmethods_item]], PcfCalculationMethods
                ],
                productOrSectorSpecificRule: ProductOrSectorSpecificRule,
                pcfInformation: PcfInformation,
                externalPcfApi: Optional[ExternalPcfApi] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(pcfCalculationMethods, str):
                    raise TypeError("pcfCalculationMethods takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if pcfCalculationMethods is not None and not isinstance(pcfCalculationMethods, aas.SubmodelElement):
                    pcfCalculationMethods = self.PcfCalculationMethods(pcfCalculationMethods)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    pcfCalculationMethods, productOrSectorSpecificRule, externalPcfApi, pcfInformation
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"ProductOrSectorSpecificCarbonFootprints",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(
                    r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificCarbonFootprint/1/0"
                ),
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Product Or Sector Specific Carbon Footprints"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Product Carbon Footprints, which is determined in accordance with sector or product group-specific rules or guidelines and covers the life cycle or parts of a product life cycle."
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificCarbonFootprints/1/0"
                ),
            }

        def __init__(
            self,
            productorsectorspecificcarbonfootprints_items: Iterable[Productorsectorspecificcarbonfootprints_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(productorsectorspecificcarbonfootprints_items, str):
                raise TypeError("productorsectorspecificcarbonfootprints_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                productorsectorspecificcarbonfootprints_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"CarbonFootprint",
            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"CO2 Footprint", r"en": r"Carbon Footprint"}),
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"The Submodel provides the means to access the Carbon Footprint of the asset."}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/IDTA02023-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/1/0"),
        }

    def __init__(
        self,
        id_: str,
        productCarbonFootprints: Union[
            Iterable[ProductCarbonFootprints.Productcarbonfootprints_item], ProductCarbonFootprints
        ],
        productOrSectorSpecificCarbonFootprints: Optional[
            Union[
                Iterable[ProductOrSectorSpecificCarbonFootprints.Productorsectorspecificcarbonfootprints_item],
                ProductOrSectorSpecificCarbonFootprints,
            ]
        ] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(productCarbonFootprints, str):
            raise TypeError("productCarbonFootprints takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if productCarbonFootprints is not None and not isinstance(productCarbonFootprints, aas.SubmodelElement):
            productCarbonFootprints = self.ProductCarbonFootprints(productCarbonFootprints)

        # A str would be split into its characters
        if isinstance(productOrSectorSpecificCarbonFootprints, str):
            raise TypeError("productOrSectorSpecificCarbonFootprints takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if productOrSectorSpecificCarbonFootprints is not None and not isinstance(
            productOrSectorSpecificCarbonFootprints, aas.SubmodelElement
        ):
            productOrSectorSpecificCarbonFootprints = self.ProductOrSectorSpecificCarbonFootprints(
                productOrSectorSpecificCarbonFootprints
            )

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            productCarbonFootprints, productOrSectorSpecificCarbonFootprints
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
