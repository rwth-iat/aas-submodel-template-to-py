from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class DppMetadata(aas.Submodel):

    class DigitalProductPassportId(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"digitalProductPassportId",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/digitalProductPassportId/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Unique Product Passport Identifier (DPP ID)"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Unique identifier of an instance of the digital product"
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=str,
                        value=r"https://www.example.org/dpp/1234545",
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class UniqueProductIdentifier(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"uniqueProductIdentifier",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/uniqueProductIdentifier/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Unique Product Identifier"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Unique string of characters for the identification of a product, that also enables a web link to the digital product passport."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=str,
                        value=r"https://www.example.org/1234545",
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class Granularity(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"granularity",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/granularity/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/aas/3/2/AssetKind",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Granularity"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The granularity of the Product. There are three values: ‘Model‘, ‘Item‘ and ‘Batch‘."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=str,
                        value=r"Item",
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class DppSchemaVersion(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"dppSchemaVersion",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/dppSchemaVersion/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"DPP Schema Version"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference standard the DPP instance schema refers to."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=str,
                        value=r"ENXXX:v1.0",
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class DppStatus(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"dppStatus",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/dppStatus/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"DPP Status"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Status of the DPP instance as digital resource."}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=str,
                        value=r"Active",
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class LastUpdate(aas.Property):

        def __init__(
            self,
            value: xsd.DateTime,
            id_short: Optional[str] = r"lastUpdate",
            value_type: aas.DataTypeDefXsd = xsd.DateTime,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/lastUpdate/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"<https://admin-shell.io/aas/3/2/AdministrativeInformation/updatedAt",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Last Update"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Date and time of the latest update to the DPP instance."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=xsd.DateTime,
                        value=xsd.from_xsd(r"2025-08-22T03:12:00+00:00", xsd.DateTime),
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class EconomicOperatorId(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"economicOperatorId",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/economicOperatorId/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Economic Operator ID"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Unique string of characters for the identification of an actor involved in a product’s life cycle."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=str,
                        value=r"gxx:ppp456789",
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class FacilityId(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"facilityId",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/facilityId/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Facility ID"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Unique string of characters for the identification of locations or buildings involved in a product’s value chain or used by actors involved in a product’s life cycle."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/ExampleValue",
                        value_type=str,
                        value=r"gxx:xxx987654",
                        value_id=None,
                        kind=aas.QualifierKind.VALUE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
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

    class ContentSpecificationIds(aas.SubmodelElementList):

        class Contentspecificationids_item(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = None,
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/contentSpecificationId/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Content Specification ID"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"https://admin-shell-io/idta/digitalproductpassport/Circularity/1",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
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
            contentspecificationids_items: Iterable[
                Union[str, Contentspecificationids_item]
            ],
            id_short: Optional[str] = r"contentSpecificationIds",
            type_value_list_element: aas.SubmodelElement = aas.Property,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
            order_relevant: bool = False,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/contentSpecificationIds/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Content Specification IDs"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference to horizontal or product-type related content specifications for the DPP."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(contentspecificationids_items, str):
                raise TypeError(
                    "contentspecificationids_items takes several elements, got a str"
                )

            # Build submodel elements from raw values passed in the argument
            if contentspecificationids_items:
                contentspecificationids_items = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.Contentspecificationids_item(i)
                    )
                    for i in contentspecificationids_items
                ]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [contentspecificationids_items]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    embedded_submodel_elements.extend(se_arg)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise aas.AASConstraintViolation(
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
        digitalProductPassportId: Union[str, DigitalProductPassportId],
        uniqueProductIdentifier: Union[str, UniqueProductIdentifier],
        granularity: Union[str, Granularity],
        dppSchemaVersion: Union[str, DppSchemaVersion],
        dppStatus: Union[str, DppStatus],
        lastUpdate: Union[xsd.DateTime, LastUpdate],
        economicOperatorId: Union[str, EconomicOperatorId],
        facilityId: Optional[Union[str, FacilityId]] = None,
        contentSpecificationIds: Optional[
            Union[
                Iterable[
                    Union[str, ContentSpecificationIds.Contentspecificationids_item]
                ],
                ContentSpecificationIds,
            ]
        ] = None,
        id_short: Optional[str] = r"DppMetadata",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/cds/dppMetadata/1",
                ),
            ),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.TEMPLATE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": "\n   Digital record of product characteristics throughout its life cycle.\n   \n   SOURCE: FprEN 18223:2026(en)   \n   "
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=None,
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if digitalProductPassportId is not None and not isinstance(
            digitalProductPassportId, aas.SubmodelElement
        ):
            digitalProductPassportId = self.DigitalProductPassportId(
                digitalProductPassportId
            )

        # Build a submodel element if a raw value was passed in the argument

        if uniqueProductIdentifier is not None and not isinstance(
            uniqueProductIdentifier, aas.SubmodelElement
        ):
            uniqueProductIdentifier = self.UniqueProductIdentifier(
                uniqueProductIdentifier
            )

        # Build a submodel element if a raw value was passed in the argument

        if granularity is not None and not isinstance(granularity, aas.SubmodelElement):
            granularity = self.Granularity(granularity)

        # Build a submodel element if a raw value was passed in the argument

        if dppSchemaVersion is not None and not isinstance(
            dppSchemaVersion, aas.SubmodelElement
        ):
            dppSchemaVersion = self.DppSchemaVersion(dppSchemaVersion)

        # Build a submodel element if a raw value was passed in the argument

        if dppStatus is not None and not isinstance(dppStatus, aas.SubmodelElement):
            dppStatus = self.DppStatus(dppStatus)

        # Build a submodel element if a raw value was passed in the argument

        if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
            lastUpdate = self.LastUpdate(lastUpdate)

        # Build a submodel element if a raw value was passed in the argument

        if economicOperatorId is not None and not isinstance(
            economicOperatorId, aas.SubmodelElement
        ):
            economicOperatorId = self.EconomicOperatorId(economicOperatorId)

        # Build a submodel element if a raw value was passed in the argument

        if facilityId is not None and not isinstance(facilityId, aas.SubmodelElement):
            facilityId = self.FacilityId(facilityId)

        # A str would be split into its characters
        if isinstance(contentSpecificationIds, str):
            raise TypeError("contentSpecificationIds takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if contentSpecificationIds is not None and not isinstance(
            contentSpecificationIds, aas.SubmodelElement
        ):
            contentSpecificationIds = self.ContentSpecificationIds(
                contentSpecificationIds
            )

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            digitalProductPassportId,
            uniqueProductIdentifier,
            granularity,
            dppSchemaVersion,
            dppStatus,
            lastUpdate,
            economicOperatorId,
            facilityId,
            contentSpecificationIds,
        ]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, aas.SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
