from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class CarbonFootprint(Submodel):

    class ProductCarbonFootprints(SubmodelElementList):

        class Productcarbonfootprints_item(SubmodelElementCollection):

            class PcfCalculationMethods(SubmodelElementList):

                class Pcfcalculationmethods_item(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"pcfcalculationmethods_item",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={
                                r"de": r"Folgenabschätzungsmethode / Berechnungsmethode",
                                r"en": r"impact assessment method / calculation method",
                            }
                        ),
                        category: Union() = r"PARAMETER",
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"en": r"Standard, method for determining the greenhouse gas emissions of a product.",
                                r"de": r"Norm, Standard, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABG854#003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    pcfcalculationmethods_items: Union[str, Pcfcalculationmethods_item],
                    id_short: Union() = r"PcfCalculationMethods",
                    type_value_list_element: SubmodelElement = Property,
                    semantic_id_list_element: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG854#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    value_type_list_element: Optional[DataTypeDefXsd] = str,
                    order_relevant: bool = True,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Folgenabschätzungsmethoden",
                            r"en": r"impact assessment methods",
                        }
                    ),
                    category: Union() = None,
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"de": r"Normen, Standards, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                            r"en": r"Standards, methods for determining the greenhouse gas emissions of a product.",
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/PcfCalculationMethods/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if pcfcalculationmethods_items and not isinstance(
                        pcfcalculationmethods_items, SubmodelElement
                    ):
                        pcfcalculationmethods_items = self.Pcfcalculationmethods_item(
                            pcfcalculationmethods_items
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [pcfcalculationmethods_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

                def _check_constraints(self, new, existing) -> None:
                    # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                    # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                    saved_id_short = new.id_short
                    new.id_short = None

                    # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                    if not isinstance(new, self.type_value_list_element):
                        raise base.AASConstraintViolation(
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
                        raise base.AASConstraintViolation(
                            107,
                            f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                            "is specified all first level children must have the same "
                            f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                        )

                    # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                    # is either Property or Range. Thus, `new` must have the value_type property.
                    # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                    if (
                        isinstance(self.type_value_list_element, Property)
                        or isinstance(self.type_value_list_element, Range)
                        and not isinstance(new.value_type, self.value_type_list_element)
                    ):  # type: ignore
                        raise base.AASConstraintViolation(
                            109,
                            "All first level elements must have the value_type "  # type: ignore
                            "specified by value_type_list_element="
                            f"{self.value_type_list_element.__name__}, got "  # type: ignore
                            f"{new!r} with value_type={new.value_type.__name__}",
                        )  # type: ignore

                    # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                    # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise base.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            class PcfCO2eq(Property):

                def __init__(
                    self,
                    value: Decimal,
                    id_short: Union() = r"PcfCO2eq",
                    value_type: DataTypeDefXsd = Decimal,
                    value_id: Union() = None,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={r"de": r"CO2-Äquivalent", r"en": r"CO2 equivalent"}
                    ),
                    category: Union() = r"PARAMETER",
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": r"Sum of all greenhouse gas emissions of a product according to the quantification requirements of the standard."
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG855#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ReferenceImpactUnitForCalculation(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Union() = r"ReferenceImpactUnitForCalculation",
                    value_type: DataTypeDefXsd = str,
                    value_id: Union() = None,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Referenzeinheit für die Berechnung",
                            r"en": r"Reference value for calculation",
                        }
                    ),
                    category: Union() = r"PARAMETER",
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": r"Quantity unit of the product to which the PCF information on the CO2 footprint refers."
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG856#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class QuantityOfMeasureForCalculation(Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Union() = r"QuantityOfMeasureForCalculation",
                    value_type: DataTypeDefXsd = float,
                    value_id: Union() = None,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Mengenangabe für die Berechnung",
                            r"en": r"quantity of measure for calculation",
                        }
                    ),
                    category: Union() = r"PARAMETER",
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": r"provides the quantity number of pieces or mass or volume to compute the impact of climate change or product carbon footprint."
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG857#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class LifeCyclePhases(SubmodelElementList):

                class Lifecyclephases_item(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"lifecyclephases_item",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={
                                r"de": r"Lebenszyklusphase",
                                r"en": r"life cycle phase",
                            }
                        ),
                        category: Union() = r"PARAMETER",
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"en": r"Life cycle stages of the product according to the quantification requirements of the standard to which the PCF carbon footprint statement refers"
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABG858#003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    lifecyclephases_items: Union[str, Lifecyclephases_item],
                    id_short: Union() = r"LifeCyclePhases",
                    type_value_list_element: SubmodelElement = Property,
                    semantic_id_list_element: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG858#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    value_type_list_element: Optional[DataTypeDefXsd] = str,
                    order_relevant: bool = True,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Lebenszyklusphasen",
                            r"en": r"life cycle phases",
                        }
                    ),
                    category: Union() = None,
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": r"List of life cycle stages of the product according to the quantification requirements of the standard to which the PCF carbon footprint statement refers"
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/LifeCyclePhases/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if lifecyclephases_items and not isinstance(
                        lifecyclephases_items, SubmodelElement
                    ):
                        lifecyclephases_items = self.Lifecyclephases_item(
                            lifecyclephases_items
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [lifecyclephases_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

                def _check_constraints(self, new, existing) -> None:
                    # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                    # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                    saved_id_short = new.id_short
                    new.id_short = None

                    # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                    if not isinstance(new, self.type_value_list_element):
                        raise base.AASConstraintViolation(
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
                        raise base.AASConstraintViolation(
                            107,
                            f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                            "is specified all first level children must have the same "
                            f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                        )

                    # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                    # is either Property or Range. Thus, `new` must have the value_type property.
                    # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                    if (
                        isinstance(self.type_value_list_element, Property)
                        or isinstance(self.type_value_list_element, Range)
                        and not isinstance(new.value_type, self.value_type_list_element)
                    ):  # type: ignore
                        raise base.AASConstraintViolation(
                            109,
                            "All first level elements must have the value_type "  # type: ignore
                            "specified by value_type_list_element="
                            f"{self.value_type_list_element.__name__}, got "  # type: ignore
                            f"{new!r} with value_type={new.value_type.__name__}",
                        )  # type: ignore

                    # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                    # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise base.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            class ExplanatoryStatement(File):

                def __init__(
                    self,
                    value: str,
                    id_short: Union() = r"ExplanatoryStatement",
                    content_type: str = r"application/pdf",
                    display_name: Union() = MultiLanguageNameType(
                        dict_={r"de": r"Erklärung", r"en": r"Explanatory statement"}
                    ),
                    category: Union() = r"PARAMETER",
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": r"Explanation required or provided to ensure that a footprint communication can be properly understood by a purchaser, potential purchaser, or user of the product."
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/ExplanatoryStatement/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        content_type=content_type,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class GoodsHandoverAddress(SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Union() = r"GoodsHandoverAddress",
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Warenübergabeadresse",
                            r"en": r"goods address hand-over",
                        }
                    ),
                    category: Union() = None,
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates the hand-over address of the goods transport"
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (
                        ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/smt-dropin/smt-dropin-use/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0112/2///61360_7#AAS002#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAQ837#008",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in []:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class PublicationDate(Property):

                def __init__(
                    self,
                    value: datetime,
                    id_short: Union() = r"PublicationDate",
                    value_type: DataTypeDefXsd = datetime,
                    value_id: Union() = None,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Veröffentlichungsdatum",
                            r"en": r"Publication date",
                        }
                    ),
                    category: Union() = r"PARAMETER",
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": "The UTC timestamp on which a Product Carbon Footprint (PCF) - a calculation of a product's total greenhouse gas emissions - was created and published"
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/PublicationDate/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ExpirationDate(Property):

                def __init__(
                    self,
                    value: datetime,
                    id_short: Union() = r"ExpirationDate",
                    value_type: DataTypeDefXsd = datetime,
                    value_id: Union() = None,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={r"de": r"Ablaufdatum", r"en": r"Expiration date"}
                    ),
                    category: Union() = r"PARAMETER",
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"en": r"End date up to which a study or data collection for calculating an ecological footprint is considered current and valid before an update or new calculation is required."
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/ExpirationDate/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                pcfCalculationMethods: Union[Iterable[str], PcfCalculationMethods],
                pcfCO2eq: Union[Decimal, PcfCO2eq],
                referenceImpactUnitForCalculation: Union[
                    str, ReferenceImpactUnitForCalculation
                ],
                quantityOfMeasureForCalculation: Union[
                    float, QuantityOfMeasureForCalculation
                ],
                lifeCyclePhases: Union[Iterable[str], LifeCyclePhases],
                publicationDate: Union[datetime, PublicationDate],
                explanatoryStatement: Optional[ExplanatoryStatement] = None,
                goodsHandoverAddress: Optional[GoodsHandoverAddress] = None,
                expirationDate: Optional[Union[datetime, ExpirationDate]] = None,
                id_short: Union() = r"productcarbonfootprints_item",
                display_name: Union() = MultiLanguageNameType(
                    dict_={
                        r"de": r"Produkt CO2-Fußabdruck",
                        r"en": r"Product carbon footprint",
                    }
                ),
                category: Union() = None,
                description: Union() = MultiLanguageTextType(
                    dict_={
                        r"en": r"Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use."
                    }
                ),
                semantic_id: Union() = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if pcfCalculationMethods and not isinstance(
                    pcfCalculationMethods, SubmodelElement
                ):
                    pcfCalculationMethods = self.PcfCalculationMethods(
                        pcfCalculationMethods
                    )

                # Build a submodel element if a raw value was passed in the argument
                if pcfCO2eq and not isinstance(pcfCO2eq, SubmodelElement):
                    pcfCO2eq = self.PcfCO2eq(pcfCO2eq)

                # Build a submodel element if a raw value was passed in the argument
                if referenceImpactUnitForCalculation and not isinstance(
                    referenceImpactUnitForCalculation, SubmodelElement
                ):
                    referenceImpactUnitForCalculation = (
                        self.ReferenceImpactUnitForCalculation(
                            referenceImpactUnitForCalculation
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument
                if quantityOfMeasureForCalculation and not isinstance(
                    quantityOfMeasureForCalculation, SubmodelElement
                ):
                    quantityOfMeasureForCalculation = (
                        self.QuantityOfMeasureForCalculation(
                            quantityOfMeasureForCalculation
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument
                if lifeCyclePhases and not isinstance(lifeCyclePhases, SubmodelElement):
                    lifeCyclePhases = self.LifeCyclePhases(lifeCyclePhases)

                # Build a submodel element if a raw value was passed in the argument
                if publicationDate and not isinstance(publicationDate, SubmodelElement):
                    publicationDate = self.PublicationDate(publicationDate)

                # Build a submodel element if a raw value was passed in the argument
                if expirationDate and not isinstance(expirationDate, SubmodelElement):
                    expirationDate = self.ExpirationDate(expirationDate)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    pcfCalculationMethods,
                    pcfCO2eq,
                    referenceImpactUnitForCalculation,
                    quantityOfMeasureForCalculation,
                    lifeCyclePhases,
                    explanatoryStatement,
                    goodsHandoverAddress,
                    publicationDate,
                    expirationDate,
                ]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                        )

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            productcarbonfootprints_items: Productcarbonfootprints_item,
            id_short: Union() = r"ProductCarbonFootprints",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Union() = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Union() = MultiLanguageNameType(
                dict_={
                    r"de": r"Produkt CO2-Fußabdruck",
                    r"en": r"Product carbon footprint",
                }
            ),
            category: Union() = None,
            description: Union() = MultiLanguageTextType(
                dict_={
                    r"en": r"Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use."
                }
            ),
            semantic_id: Union() = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprints/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [productcarbonfootprints_items]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                type_value_list_element=type_value_list_element,
                semantic_id_list_element=semantic_id_list_element,
                value_type_list_element=value_type_list_element,
                order_relevant=order_relevant,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

        def _check_constraints(self, new, existing) -> None:
            # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
            # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
            saved_id_short = new.id_short
            new.id_short = None

            # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
            if not isinstance(new, self.type_value_list_element):
                raise base.AASConstraintViolation(
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
                raise base.AASConstraintViolation(
                    107,
                    f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                    "is specified all first level children must have the same "
                    f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                )

            # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
            # is either Property or Range. Thus, `new` must have the value_type property.
            # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
            if (
                isinstance(self.type_value_list_element, Property)
                or isinstance(self.type_value_list_element, Range)
                and not isinstance(new.value_type, self.value_type_list_element)
            ):  # type: ignore
                raise base.AASConstraintViolation(
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise base.AASConstraintViolation(
                            114,
                            f"Element to be added {new!r} has semantic_id "
                            f"{new.semantic_id!r}, while already contained element "
                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                            "aren't equal.",
                        )

            # Re-assign id_short
            new.id_short = saved_id_short

    class ProductOrSectorSpecificCarbonFootprints(SubmodelElementList):

        class Productorsectorspecificcarbonfootprints_item(SubmodelElementCollection):

            class PcfCalculationMethods(SubmodelElementList):

                class Pcfcalculationmethods_item(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"pcfcalculationmethods_item",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={
                                r"de": r"Folgenabschätzungsmethode / Berechnungsmethode",
                                r"en": r"impact assessment method / calculation method",
                            }
                        ),
                        category: Union() = r"PARAMETER",
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"en": r"Standard, method for determining the greenhouse gas emissions of a product.",
                                r"de": r"Norm, Standard, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABG854#003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    pcfcalculationmethods_items: Union[str, Pcfcalculationmethods_item],
                    id_short: Union() = r"PcfCalculationMethods",
                    type_value_list_element: SubmodelElement = Property,
                    semantic_id_list_element: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG854#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    value_type_list_element: Optional[DataTypeDefXsd] = str,
                    order_relevant: bool = True,
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Folgenabschätzungsmethoden",
                            r"en": r"impact assessment methods",
                        }
                    ),
                    category: Union() = None,
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"de": r"Normen, Standards, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                            r"en": r"Standards, methods for determining the greenhouse gas emissions of a product.",
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/PcfCalculationMethods/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if pcfcalculationmethods_items and not isinstance(
                        pcfcalculationmethods_items, SubmodelElement
                    ):
                        pcfcalculationmethods_items = self.Pcfcalculationmethods_item(
                            pcfcalculationmethods_items
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [pcfcalculationmethods_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

                def _check_constraints(self, new, existing) -> None:
                    # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                    # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                    saved_id_short = new.id_short
                    new.id_short = None

                    # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                    if not isinstance(new, self.type_value_list_element):
                        raise base.AASConstraintViolation(
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
                        raise base.AASConstraintViolation(
                            107,
                            f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                            "is specified all first level children must have the same "
                            f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                        )

                    # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                    # is either Property or Range. Thus, `new` must have the value_type property.
                    # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                    if (
                        isinstance(self.type_value_list_element, Property)
                        or isinstance(self.type_value_list_element, Range)
                        and not isinstance(new.value_type, self.value_type_list_element)
                    ):  # type: ignore
                        raise base.AASConstraintViolation(
                            109,
                            "All first level elements must have the value_type "  # type: ignore
                            "specified by value_type_list_element="
                            f"{self.value_type_list_element.__name__}, got "  # type: ignore
                            f"{new!r} with value_type={new.value_type.__name__}",
                        )  # type: ignore

                    # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                    # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise base.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            class ProductOrSectorSpecificRule(SubmodelElementCollection):

                class PcfRuleOperator(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"PcfRuleOperator",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={
                                r"de": r"Herausgeber der PCF Berechnungsmethode",
                                r"en": r"Operator of the PCF calculation method",
                            }
                        ),
                        category: Union() = None,
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"de": r"Einrichtung, welche spezifische Anweisungen und Methoden zur Berechnung und Überwachung des CO2-Fußabdrucks eines Produkts oder Sektors definiert und umsetzt.",
                                r"en": r"Organization that defines and implements specific instructions and methods for calculating and monitoring the carbon footprint of a product or sector.",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/Operator/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class PcfRuleName(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"PcfRuleName",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={
                                r"de": r"Name der PCF Berechnungsmethode",
                                r"en": r"Name of the PCF calculation method",
                            }
                        ),
                        category: Union() = None,
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"de": r"Folgenabschätzungsmethode / Berechnungsmethode",
                                r"en": r"Standard, method for determining the greenhouse gas emissions of a product",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/Name/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class PcfRuleVersion(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"PcfRuleVersion",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={
                                r"de": r"Version der PCF Berechnungsmethode",
                                r"en": r"Version of the PCF calculation method",
                            }
                        ),
                        category: Union() = None,
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"de": r"Spezifische Ausgabe oder Revision der Regel, die zur Berechnung des CO2-Fußabdrucks eines Produkts verwendet wird.",
                                r"en": r"Specific version or revision of the rule used to calculate the carbon footprint of a product.",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/Version/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class PcfRuleOnlineReference(File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"PcfRuleOnlineReference",
                        content_type: str = r"application/pdf",
                        display_name: Union() = MultiLanguageNameType(
                            dict_={
                                r"de": r"Online Referenz zur PCF Berechnungsmethode",
                                r"en": r"Online reference to the PCF calculation method",
                            }
                        ),
                        category: Union() = None,
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"de": r"Online-Referenz zur PCF-Berechnungsmethodik, die detaillierte Anweisungen und Richtlinien zur Berechnung des CO2-Fußabdrucks eines Produkts bereitstellt.",
                                r"en": "Online PCF calculation methodology reference that provides detailed instructions and guidelines for calculating a product's carbon footprint.",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/OnlineReference/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            content_type=content_type,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    pcfRuleOperator: Union[str, PcfRuleOperator],
                    pcfRuleName: Union[str, PcfRuleName],
                    pcfRuleVersion: Optional[Union[str, PcfRuleVersion]] = None,
                    pcfRuleOnlineReference: Optional[PcfRuleOnlineReference] = None,
                    id_short: Union() = r"ProductOrSectorSpecificRule",
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Produktspezifische oder sektorspezifische Regel",
                            r"en": r"Product or Sector Specific Rule",
                        }
                    ),
                    category: Union() = None,
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"de": r"Beinhaltet weiterführende Informationen zur produktspezifischen oder sektorspezifischen Regel, welche zur Berechnung des CO2-Fußabdrucks eingesetzt wird. ",
                            r"en": r"Contains further information on the product-specific or sector-specific rule used to calculate the carbon footprint.",
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificRule/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if pcfRuleOperator and not isinstance(
                        pcfRuleOperator, SubmodelElement
                    ):
                        pcfRuleOperator = self.PcfRuleOperator(pcfRuleOperator)

                    # Build a submodel element if a raw value was passed in the argument
                    if pcfRuleName and not isinstance(pcfRuleName, SubmodelElement):
                        pcfRuleName = self.PcfRuleName(pcfRuleName)

                    # Build a submodel element if a raw value was passed in the argument
                    if pcfRuleVersion and not isinstance(
                        pcfRuleVersion, SubmodelElement
                    ):
                        pcfRuleVersion = self.PcfRuleVersion(pcfRuleVersion)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        pcfRuleOperator,
                        pcfRuleName,
                        pcfRuleVersion,
                        pcfRuleOnlineReference,
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ExternalPcfApi(SubmodelElementCollection):

                class PcfApiEndpoint(Property):

                    def __init__(
                        self,
                        value: AnyURI,
                        id_short: Union() = r"PcfApiEndpoint",
                        value_type: DataTypeDefXsd = AnyURI,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={r"de": r"Endpunkt", r"en": r"Endpoint"}
                        ),
                        category: Union() = None,
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"de": r"Spezifische URL oder Adresse, über die Daten zur Berechnung des CO2-Fußabdrucks eines Produkts von externen Quellen abgerufen werden können.",
                                r"en": r"Specific URL or address that can be used to retrieve data from external sources to calculate the carbon footprint of a product.",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/CarbonFootprint/ExternalPcfApi/Endpoint/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class PcfApiQuery(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"PcfApiQuery",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = MultiLanguageNameType(
                            dict_={r"de": r"Abfrage", r"en": r"Query"}
                        ),
                        category: Union() = None,
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"de": r"Spezifische Abfrage, über die Daten zur Berechnung des CO2-Fußabdrucks eines Produkts von externen Quellen abgerufen werden können.",
                                r"en": r"Specific query that can be used to retrieve data from external sources to calculate the carbon footprint of a product.",
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/CarbonFootprint/ExternalPcfApi/Query/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    pcfApiEndpoint: Union[AnyURI, PcfApiEndpoint],
                    pcfApiQuery: Union[str, PcfApiQuery],
                    id_short: Union() = r"ExternalPcfApi",
                    display_name: Union() = MultiLanguageNameType(
                        dict_={
                            r"de": r"Externe API für PCF Informationen",
                            r"en": r"External API for PCF information",
                        }
                    ),
                    category: Union() = None,
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"de": r"Ein externer Dienst, der über eine Schnittstelle Informationen zum CO2-Fußabdruck bereitstellt und den Abruf dieser Daten auf Abruf ermöglicht.",
                            r"en": r"An external service that provides carbon footprint information via an interface, allowing on-demand retrieval of this data when required.",
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/ExternalPcfApi/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if pcfApiEndpoint and not isinstance(
                        pcfApiEndpoint, SubmodelElement
                    ):
                        pcfApiEndpoint = self.PcfApiEndpoint(pcfApiEndpoint)

                    # Build a submodel element if a raw value was passed in the argument
                    if pcfApiQuery and not isinstance(pcfApiQuery, SubmodelElement):
                        pcfApiQuery = self.PcfApiQuery(pcfApiQuery)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [pcfApiEndpoint, pcfApiQuery]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class PcfInformation(SubmodelElementCollection):

                class ArbitraryContent(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Union() = r"ArbitraryContent",
                        value_type: DataTypeDefXsd = str,
                        value_id: Union() = None,
                        display_name: Union() = None,
                        category: Union() = None,
                        description: Union() = MultiLanguageTextType(
                            dict_={
                                r"en": r"Free area for structured collection of specific items of a specific PCF."
                            }
                        ),
                        semantic_id: Union() = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SMT/General/Arbitrary",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToMany",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    arbitraryContent: Optional[
                        Iterable[Union[str, ArbitraryContent]]
                    ] = None,
                    id_short: Union() = r"PcfInformation",
                    display_name: Union() = None,
                    category: Union() = None,
                    description: Union() = MultiLanguageTextType(
                        dict_={
                            r"de": r"Ein Abschnitt, in dem weitere Inhalte entsprechend der Berechnungsmethode zum Product Carbon Footprint aufgeführt werden.",
                            r"en": r"A section in which further content is listed according to the calculation method for the Product Carbon Footprint.",
                        }
                    ),
                    semantic_id: Union() = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/CarbonFootprint/PcfInformation/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryContent and all(
                        [isinstance(i, str) for i in arbitraryContent]
                    ):
                        arbitraryContent = [
                            self.ArbitraryContent(i) for i in arbitraryContent
                        ]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [arbitraryContent]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                pcfCalculationMethods: Union[Iterable[str], PcfCalculationMethods],
                productOrSectorSpecificRule: ProductOrSectorSpecificRule,
                pcfInformation: PcfInformation,
                externalPcfApi: Optional[ExternalPcfApi] = None,
                id_short: Union() = r"productorsectorspecificcarbonfootprints_item",
                display_name: Union() = None,
                category: Union() = None,
                description: Union() = MultiLanguageTextType(
                    dict_={
                        r"en": r"Product Carbon Footprint, which is determined in accordance with sector or product group-specific rules or guidelines and covers the life cycle or parts of a product life cycle."
                    }
                ),
                semantic_id: Union() = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificCarbonFootprint/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if pcfCalculationMethods and not isinstance(
                    pcfCalculationMethods, SubmodelElement
                ):
                    pcfCalculationMethods = self.PcfCalculationMethods(
                        pcfCalculationMethods
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    pcfCalculationMethods,
                    productOrSectorSpecificRule,
                    externalPcfApi,
                    pcfInformation,
                ]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                        )

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            productorsectorspecificcarbonfootprints_items: Productorsectorspecificcarbonfootprints_item,
            id_short: Union() = r"ProductOrSectorSpecificCarbonFootprints",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Union() = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificCarbonFootprint/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Union() = MultiLanguageNameType(
                dict_={r"en": r"Product Or Sector Specific Carbon Footprints"}
            ),
            category: Union() = None,
            description: Union() = MultiLanguageTextType(
                dict_={
                    r"en": r"Product Carbon Footprints, which is determined in accordance with sector or product group-specific rules or guidelines and covers the life cycle or parts of a product life cycle."
                }
            ),
            semantic_id: Union() = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/CarbonFootprint/ProductOrSectorSpecificCarbonFootprints/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [productorsectorspecificcarbonfootprints_items]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                type_value_list_element=type_value_list_element,
                semantic_id_list_element=semantic_id_list_element,
                value_type_list_element=value_type_list_element,
                order_relevant=order_relevant,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

        def _check_constraints(self, new, existing) -> None:
            # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
            # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
            saved_id_short = new.id_short
            new.id_short = None

            # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
            if not isinstance(new, self.type_value_list_element):
                raise base.AASConstraintViolation(
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
                raise base.AASConstraintViolation(
                    107,
                    f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                    "is specified all first level children must have the same "
                    f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                )

            # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
            # is either Property or Range. Thus, `new` must have the value_type property.
            # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
            if (
                isinstance(self.type_value_list_element, Property)
                or isinstance(self.type_value_list_element, Range)
                and not isinstance(new.value_type, self.value_type_list_element)
            ):  # type: ignore
                raise base.AASConstraintViolation(
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise base.AASConstraintViolation(
                            114,
                            f"Element to be added {new!r} has semantic_id "
                            f"{new.semantic_id!r}, while already contained element "
                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                            "aren't equal.",
                        )

            # Re-assign id_short
            new.id_short = saved_id_short

    def __init__(
        self,
        id_: str,
        productCarbonFootprints: ProductCarbonFootprints,
        productOrSectorSpecificCarbonFootprints: Optional[
            ProductOrSectorSpecificCarbonFootprints
        ] = None,
        id_short: Union() = r"CarbonFootprint",
        display_name: Union() = MultiLanguageNameType(
            dict_={r"de": r"C02 Footprint", r"en": r"Carbon Footprint"}
        ),
        category: Union() = None,
        description: Union() = MultiLanguageTextType(
            dict_={
                r"en": r"The Submodel provides the means to access the Carbon Footprint of the asset."
            }
        ),
        administration: Union() = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/IDTA 02023-1-0",
            embedded_data_specifications=[],
        ),
        semantic_id: Union() = ExternalReference(
            key=(
                Key(
                    type_=KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/1/0",
                ),
            ),
            referred_semantic_id=None,
        ),
        qualifier: Iterable[Qualifier] = None,
        kind: ModellingKind = ModellingKind.TEMPLATE,
        extension: Iterable[Extension] = (),
        supplemental_semantic_id: Iterable[Reference] = (),
        embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
    ):

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            productCarbonFootprints,
            productOrSectorSpecificCarbonFootprints,
        ]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                )

        super().__init__(
            submodel_element=embedded_submodel_elements,
            id_=id_,
            id_short=id_short,
            display_name=display_name,
            category=category,
            description=description,
            administration=administration,
            semantic_id=semantic_id,
            qualifier=qualifier,
            kind=kind,
            extension=extension,
            supplemental_semantic_id=supplemental_semantic_id,
            embedded_data_specifications=embedded_data_specifications,
        )
