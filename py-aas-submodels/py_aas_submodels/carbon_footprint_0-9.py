from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class CarbonFootprint(Submodel):

    class ProductCarbonFootprint(SubmodelElementCollection):

        class PCFCalculationMethod(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PCFCalculationMethod",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"Folgenabschätzungsmethode / Berechnungsmethode",
                        r"en": r"impact assessment method / calculation method",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Standard, method for determining the greenhouse gas emissions of a product",
                        r"de": r"Norm, Standard, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts",
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG854#001",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"OneToMany",
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

        class PCFCO2eq(Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"PCFCO2eq",
                value_type: DataTypeDefXsd = float,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"CO2 eq Klimawandel",
                        r"en": r"CO2 eq Climate Change",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Sum of all greenhouse gas emissions of a product according to the quantification requirements of the standard"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG855#001",
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
                            type_=r"Cardinality",
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

        class PCFReferenceValueForCalculation(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PCFReferenceValueForCalculation",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"Referenzeinheit für die Berechnung",
                        r"en": r"Reference value for calculation",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Quantity unit of the product to which the PCF information on the CO2 footprint refers"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG856#001",
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
                            type_=r"Cardinality",
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

        class PCFQuantityOfMeasureForCalculation(Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"PCFQuantityOfMeasureForCalculation",
                value_type: DataTypeDefXsd = float,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"Mengenangabe für die Berechnung",
                        r"en": r"quantity of measure for calculation",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Quantity of the product to which the PCF information on the CO2 footprint refers"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG857#001",
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
                            type_=r"Cardinality",
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

        class PCFLifeCyclePhase(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PCFLifeCyclePhase",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Lebenszyklusphase", r"en": r"life cycle phase"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Life cycle stages of the product according to the quantification requirements of the standard to which the PCF carbon footprint statement refers"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG858#001",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"OneToMany",
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

        class ExplanatoryStatement(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ExplanatoryStatement",
                content_type: str = r"application/pdf",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Erklärung", r"en": r"Explanatory statement"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Explanation which is needed or given so that a footprint communication can be properly understood by a purchaser, potential purchaser or user of the product"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
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
                            type_=r"Cardinality",
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

        class PCFGoodsAddressHandover(SubmodelElementCollection):

            class Street(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Street",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Street indication of the place of transfer of goods"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH956#001",
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
                                type_=r"Cardinality",
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

            class HouseNumber(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"HouseNumber",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Number for identification or differentiation of individual houses of a street"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH957#001",
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
                                type_=r"Cardinality",
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

            class ZipCode(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ZipCode",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Zip code of the goods transfer address"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH958#001",
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
                                type_=r"Cardinality",
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

            class CityTown(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CityTown",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Indication of the city or town of the transfer of goods"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH959#001",
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
                                type_=r"Cardinality",
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

            class Country(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Country",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Country where the product is transmitted"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO259#005",
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
                                type_=r"Cardinality",
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
                street: Optional[Union[str, Street]] = None,
                houseNumber: Optional[Union[str, HouseNumber]] = None,
                zipCode: Optional[Union[str, ZipCode]] = None,
                cityTown: Optional[Union[str, CityTown]] = None,
                country: Optional[Union[str, Country]] = None,
                id_short: Optional[str] = r"PCFGoodsAddressHandover",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"PCF Warenübergabeadresse",
                        r"en": r"PCF goods address hand-over",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"Indicates the place of hand-over of the goods"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI497#001",
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
                            type_=r"Cardinality",
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
                if street and not isinstance(street, SubmodelElement):
                    street = self.Street(street)

                # Build a submodel element if a raw value was passed in the argument
                if houseNumber and not isinstance(houseNumber, SubmodelElement):
                    houseNumber = self.HouseNumber(houseNumber)

                # Build a submodel element if a raw value was passed in the argument
                if zipCode and not isinstance(zipCode, SubmodelElement):
                    zipCode = self.ZipCode(zipCode)

                # Build a submodel element if a raw value was passed in the argument
                if cityTown and not isinstance(cityTown, SubmodelElement):
                    cityTown = self.CityTown(cityTown)

                # Build a submodel element if a raw value was passed in the argument
                if country and not isinstance(country, SubmodelElement):
                    country = self.Country(country)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [street, houseNumber, zipCode, cityTown, country]:
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
                value: str,
                id_short: Optional[str] = r"PublicationDate",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Veröffentlichungsdatum", r"en": r"Publication date"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Time at which something was first published or made available"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
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
                            type_=r"Cardinality",
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
                value: str,
                id_short: Optional[str] = r"ExpirationDate",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Ablaufdatum", r"en": r"Expiration date"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Time at which something should no longer be used effectively because it may lose its validity, quality or safety"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/CarbonFootprint/ExpirationnDate/1/0",
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
                            type_=r"Cardinality",
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
            pCFCalculationMethod: Iterable[Union[str, PCFCalculationMethod]],
            pCFCO2eq: Union[float, PCFCO2eq],
            pCFReferenceValueForCalculation: Union[
                str, PCFReferenceValueForCalculation
            ],
            pCFQuantityOfMeasureForCalculation: Union[
                float, PCFQuantityOfMeasureForCalculation
            ],
            pCFLifeCyclePhase: Iterable[Union[str, PCFLifeCyclePhase]],
            pCFGoodsAddressHandover: PCFGoodsAddressHandover,
            publicationDate: Union[str, PublicationDate],
            explanatoryStatement: Optional[ExplanatoryStatement] = None,
            expirationDate: Optional[Union[str, ExpirationDate]] = None,
            id_short: Optional[str] = r"ProductCarbonFootprint",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={
                    r"de": r"Produkt C02-Fußabdruck",
                    r"en": r"Product carbon footprint",
                }
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/0/9",
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
                        type_=r"Cardinality",
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

            # Build a list of submodel elements if a raw values were passed in the argument
            if pCFCalculationMethod and all(
                [isinstance(i, str) for i in pCFCalculationMethod]
            ):
                pCFCalculationMethod = [
                    self.PCFCalculationMethod(i) for i in pCFCalculationMethod
                ]

            # Build a submodel element if a raw value was passed in the argument
            if pCFCO2eq and not isinstance(pCFCO2eq, SubmodelElement):
                pCFCO2eq = self.PCFCO2eq(pCFCO2eq)

            # Build a submodel element if a raw value was passed in the argument
            if pCFReferenceValueForCalculation and not isinstance(
                pCFReferenceValueForCalculation, SubmodelElement
            ):
                pCFReferenceValueForCalculation = self.PCFReferenceValueForCalculation(
                    pCFReferenceValueForCalculation
                )

            # Build a submodel element if a raw value was passed in the argument
            if pCFQuantityOfMeasureForCalculation and not isinstance(
                pCFQuantityOfMeasureForCalculation, SubmodelElement
            ):
                pCFQuantityOfMeasureForCalculation = (
                    self.PCFQuantityOfMeasureForCalculation(
                        pCFQuantityOfMeasureForCalculation
                    )
                )

            # Build a list of submodel elements if a raw values were passed in the argument
            if pCFLifeCyclePhase and all(
                [isinstance(i, str) for i in pCFLifeCyclePhase]
            ):
                pCFLifeCyclePhase = [
                    self.PCFLifeCyclePhase(i) for i in pCFLifeCyclePhase
                ]

            # Build a submodel element if a raw value was passed in the argument
            if publicationDate and not isinstance(publicationDate, SubmodelElement):
                publicationDate = self.PublicationDate(publicationDate)

            # Build a submodel element if a raw value was passed in the argument
            if expirationDate and not isinstance(expirationDate, SubmodelElement):
                expirationDate = self.ExpirationDate(expirationDate)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                pCFCalculationMethod,
                pCFCO2eq,
                pCFReferenceValueForCalculation,
                pCFQuantityOfMeasureForCalculation,
                pCFLifeCyclePhase,
                explanatoryStatement,
                pCFGoodsAddressHandover,
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

    class TransportCarbonFootprint(SubmodelElementCollection):

        class TCFCalculationMethod(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TCFCalculationMethod",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"TCF Berechnungsmethode",
                        r"en": r"TCF calculation method",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Standard, method for determining the greenhouse gas emissions for the transport of a product"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG859#001",
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
                            type_=r"Cardinality",
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

        class TCFCO2eq(Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"TCFCO2eq",
                value_type: DataTypeDefXsd = float,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"TCF CO2eq", r"en": r"TCF CO2eq"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Sum of all greenhouse gas emissions from vehicle operation"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG860#001",
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
                            type_=r"Cardinality",
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

        class TCFReferenceValueForCalculation(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TCFReferenceValueForCalculation",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"TCF Bezugsgröße für die Berechnung",
                        r"en": r"TCF reference value for calculation",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Amount of product to which the TCF carbon footprint statement relates"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG861#001",
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
                            type_=r"Cardinality",
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

        class TCFQuantityOfMeasureForCalculation(Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"TCFQuantityOfMeasureForCalculation",
                value_type: DataTypeDefXsd = float,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"TCF Mengenangabe für die Berechnung",
                        r"en": r"TCF quantity of measure for calculation",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Quantity of the product to which the TCF information on the CO2 footprint refers"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG862#001",
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
                            type_=r"Cardinality",
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

        class TCFProcessesForGreenhouseGasEmissionInATransportService(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[
                    str
                ] = r"TCFProcessesForGreenhouseGasEmissionInATransportService",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"TCF Prozesse für Treibhausgas-Emissionen bei Transportdiensten",
                        r"en": r"TCF processes for greenhouse gas emissions in a transport servi…",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Processes in a transport service to determine the sum of all direct or indirect greenhouse gas emissions from fuel supply and vehicle operation"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABG863#001",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"OneToMany",
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

        class ExplanatoryStatement(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ExplanatoryStatement",
                content_type: str = r"application/pdf",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Erklärung", r"en": r"Explanatory statement"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Explanation which is needed or given so that a footprint communication can be properly understood by a purchaser, potential purchaser or user of the product"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://example.com/ids/cd/3291_7022_2032_0718",
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
                            type_=r"Cardinality",
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

        class TCFGoodsTransportAddressTakeover(SubmodelElementCollection):

            class Street(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Street",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"de": r"Straße", r"en": r"street"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Street indication of the place of transfer of goods"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH956#001",
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
                                type_=r"Cardinality",
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

            class HouseNumber(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"HouseNumber",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"de": r"Hausnummer", r"en": r"house number"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Street indication of the place of transfer of goods"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH957#001",
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
                                type_=r"Cardinality",
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

            class ZipCode(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ZipCode",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"de": r"Postleitzahl", r"en": r"zip code"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Zip code of the goods transfer address"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH958#001",
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
                                type_=r"Cardinality",
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

            class CityTown(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CityTown",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"de": r"Ort", r"en": r"city, town"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Indication of the city or town of the transfer of goods"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH959#001",
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
                                type_=r"Cardinality",
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

            class Country(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Country",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"de": r"Land", r"en": r"Country"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Country where the product is transmitted"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO259#005",
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
                                type_=r"Cardinality",
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
                street: Optional[Union[str, Street]] = None,
                houseNumber: Optional[Union[str, HouseNumber]] = None,
                zipCode: Optional[Union[str, ZipCode]] = None,
                cityTown: Optional[Union[str, CityTown]] = None,
                country: Optional[Union[str, Country]] = None,
                id_short: Optional[str] = r"TCFGoodsTransportAddressTakeover",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"Warenübernahmeadresse für die Distributionsstufe",
                        r"en": r"Goods transport address take-over for distribution stage",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"Indication of the place of receipt of goods "}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI499#001",
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
                            type_=r"Cardinality",
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
                if street and not isinstance(street, SubmodelElement):
                    street = self.Street(street)

                # Build a submodel element if a raw value was passed in the argument
                if houseNumber and not isinstance(houseNumber, SubmodelElement):
                    houseNumber = self.HouseNumber(houseNumber)

                # Build a submodel element if a raw value was passed in the argument
                if zipCode and not isinstance(zipCode, SubmodelElement):
                    zipCode = self.ZipCode(zipCode)

                # Build a submodel element if a raw value was passed in the argument
                if cityTown and not isinstance(cityTown, SubmodelElement):
                    cityTown = self.CityTown(cityTown)

                # Build a submodel element if a raw value was passed in the argument
                if country and not isinstance(country, SubmodelElement):
                    country = self.Country(country)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [street, houseNumber, zipCode, cityTown, country]:
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

        class TCFGoodsTransportAddressHandover(SubmodelElementCollection):

            class Street(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Street",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Street indication of the place of transfer of goods"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH956#001",
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
                                type_=r"Cardinality",
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

            class HouseNumber(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"HouseNumber",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Number for identification or differentiation of individual houses of a street"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH957#001",
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
                                type_=r"Cardinality",
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

            class ZipCode(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ZipCode",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Zip code of the goods transfer address"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH958#001",
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
                                type_=r"Cardinality",
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

            class CityTown(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CityTown",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Indication of the city or town of the transfer of goods"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH959#001",
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
                                type_=r"Cardinality",
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

            class Country(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Country",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Country where the product is transmitted"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO259#005",
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
                                type_=r"Cardinality",
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
                street: Optional[Union[str, Street]] = None,
                houseNumber: Optional[Union[str, HouseNumber]] = None,
                zipCode: Optional[Union[str, ZipCode]] = None,
                cityTown: Optional[Union[str, CityTown]] = None,
                country: Optional[Union[str, Country]] = None,
                id_short: Optional[str] = r"TCFGoodsTransportAddressHandover",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"de": r"Warenübergabeadresse für die Distributionsstufe",
                        r"en": r"Goods transport address hand-over for distribution stage",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Indicates the hand-over address of the goods transport "
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI498#001",
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
                            type_=r"Cardinality",
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
                if street and not isinstance(street, SubmodelElement):
                    street = self.Street(street)

                # Build a submodel element if a raw value was passed in the argument
                if houseNumber and not isinstance(houseNumber, SubmodelElement):
                    houseNumber = self.HouseNumber(houseNumber)

                # Build a submodel element if a raw value was passed in the argument
                if zipCode and not isinstance(zipCode, SubmodelElement):
                    zipCode = self.ZipCode(zipCode)

                # Build a submodel element if a raw value was passed in the argument
                if cityTown and not isinstance(cityTown, SubmodelElement):
                    cityTown = self.CityTown(cityTown)

                # Build a submodel element if a raw value was passed in the argument
                if country and not isinstance(country, SubmodelElement):
                    country = self.Country(country)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [street, houseNumber, zipCode, cityTown, country]:
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
                value: str,
                id_short: Optional[str] = r"PublicationDate",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Veröffentlichungsdatum", r"en": r"Publication date"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Time at which something was first published or made available"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
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
                            type_=r"Cardinality",
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
                value: str,
                id_short: Optional[str] = r"ExpirationDate",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Ablaufdatum", r"en": r"Expiration Date"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Time at which something should no longer be used effectively because it may lose its validity, quality or safety"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/CarbonFootprint/ExpirationnDate/1/0",
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
                            type_=r"Cardinality",
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
            tCFCalculationMethod: Union[str, TCFCalculationMethod],
            tCFCO2eq: Union[float, TCFCO2eq],
            tCFReferenceValueForCalculation: Union[
                str, TCFReferenceValueForCalculation
            ],
            tCFQuantityOfMeasureForCalculation: Union[
                float, TCFQuantityOfMeasureForCalculation
            ],
            tCFProcessesForGreenhouseGasEmissionInATransportService: Iterable[
                Union[str, TCFProcessesForGreenhouseGasEmissionInATransportService]
            ],
            tCFGoodsTransportAddressTakeover: TCFGoodsTransportAddressTakeover,
            tCFGoodsTransportAddressHandover: TCFGoodsTransportAddressHandover,
            publicationDate: Union[str, PublicationDate],
            explanatoryStatement: Optional[ExplanatoryStatement] = None,
            expirationDate: Optional[Union[str, ExpirationDate]] = None,
            id_short: Optional[str] = r"TransportCarbonFootprint",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={
                    r"de": r"Transport C02-Fußabdruck",
                    r"en": r"Transport carbon footprint",
                }
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Balance of greenhouse gas emissions generated by a transport service of a product"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/CarbonFootprint/TransportCarbonFootprint/0/9",
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
                        type_=r"Cardinality",
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

            # Build a submodel element if a raw value was passed in the argument
            if tCFCalculationMethod and not isinstance(
                tCFCalculationMethod, SubmodelElement
            ):
                tCFCalculationMethod = self.TCFCalculationMethod(tCFCalculationMethod)

            # Build a submodel element if a raw value was passed in the argument
            if tCFCO2eq and not isinstance(tCFCO2eq, SubmodelElement):
                tCFCO2eq = self.TCFCO2eq(tCFCO2eq)

            # Build a submodel element if a raw value was passed in the argument
            if tCFReferenceValueForCalculation and not isinstance(
                tCFReferenceValueForCalculation, SubmodelElement
            ):
                tCFReferenceValueForCalculation = self.TCFReferenceValueForCalculation(
                    tCFReferenceValueForCalculation
                )

            # Build a submodel element if a raw value was passed in the argument
            if tCFQuantityOfMeasureForCalculation and not isinstance(
                tCFQuantityOfMeasureForCalculation, SubmodelElement
            ):
                tCFQuantityOfMeasureForCalculation = (
                    self.TCFQuantityOfMeasureForCalculation(
                        tCFQuantityOfMeasureForCalculation
                    )
                )

            # Build a list of submodel elements if a raw values were passed in the argument
            if tCFProcessesForGreenhouseGasEmissionInATransportService and all(
                [
                    isinstance(i, str)
                    for i in tCFProcessesForGreenhouseGasEmissionInATransportService
                ]
            ):
                tCFProcessesForGreenhouseGasEmissionInATransportService = [
                    self.TCFProcessesForGreenhouseGasEmissionInATransportService(i)
                    for i in tCFProcessesForGreenhouseGasEmissionInATransportService
                ]

            # Build a submodel element if a raw value was passed in the argument
            if publicationDate and not isinstance(publicationDate, SubmodelElement):
                publicationDate = self.PublicationDate(publicationDate)

            # Build a submodel element if a raw value was passed in the argument
            if expirationDate and not isinstance(expirationDate, SubmodelElement):
                expirationDate = self.ExpirationDate(expirationDate)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                tCFCalculationMethod,
                tCFCO2eq,
                tCFReferenceValueForCalculation,
                tCFQuantityOfMeasureForCalculation,
                tCFProcessesForGreenhouseGasEmissionInATransportService,
                explanatoryStatement,
                tCFGoodsTransportAddressTakeover,
                tCFGoodsTransportAddressHandover,
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
        id_: str,
        productCarbonFootprint: Optional[Iterable[ProductCarbonFootprint]] = None,
        transportCarbonFootprint: Optional[Iterable[TransportCarbonFootprint]] = None,
        id_short: Optional[str] = r"CarbonFootprint",
        display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
            dict_={r"de": r"C02 Footprint", r"en": r"Carbon Footprint"}
        ),
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"The Submodel provides the means to access the Carbon Footprint …"
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"0",
            revision=r"9",
            creator=None,
            template_id=r"https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/0/9",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(
                Key(
                    type_=KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/0/9",
                ),
            ),
            type_=Submodel,
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
        for se_arg in [productCarbonFootprint, transportCarbonFootprint]:
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
