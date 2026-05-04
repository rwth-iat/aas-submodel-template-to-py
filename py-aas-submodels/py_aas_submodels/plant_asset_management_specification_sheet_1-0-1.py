from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class PAMSpecificationSheet(Submodel):

    class DocumentHeader(SubmodelElementCollection):

        class PAMSpecificationSheetIdentification(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PAMSpecificationSheetIdentification",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"PAM Specification Sheet Identification",
                        r"de": r"PAM Spezifikationsbaltt Identification",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"Unique identifier for the PAM specification sheet."}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV929#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Unique identifier for the PAM specification sheet.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"PAM Specifications Sheet - Loop - 2014-04-28 - Version 1.00",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class AssetTypeClass(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"AssetTypeClass",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Asset Type Class", r"de": r"Allgemeiner Asset-Typ"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Defines the general category of the asset described in the PAM specification sheet."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV939#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Defines the general category of the asset described in the PAM specification sheet.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"Dosage control loop",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class AssetTypeIdentification(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"AssetTypeIdentification",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Asset Type Identification",
                        r"de": r"Identifizierung des allgemeinen Asset-Typs",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": "Unique identifier for a general asset type's PAM specification sheet."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV940#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value="Unique identifier for a general asset type's PAM specification sheet.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"Dosage Control Loop - 2014-04-28 - Version 1.00",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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
            pAMSpecificationSheetIdentification: Union[
                str, PAMSpecificationSheetIdentification
            ],
            assetTypeClass: Union[str, AssetTypeClass],
            assetTypeIdentification: Union[str, AssetTypeIdentification],
            id_short: Optional[str] = r"DocumentHeader",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"Document Header", r"de": r"Dokumentenkopf"}
            ),
            category: Optional[str] = r"PARAMETER",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Identifier for the asset type and associated PAM specification sheet."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#01-AGC974#002"),
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
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Document Header",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Identifier for the asset type and associated PAM specification sheet.",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument
            if pAMSpecificationSheetIdentification and not isinstance(
                pAMSpecificationSheetIdentification, SubmodelElement
            ):
                pAMSpecificationSheetIdentification = (
                    self.PAMSpecificationSheetIdentification(
                        pAMSpecificationSheetIdentification
                    )
                )

            # Build a submodel element if a raw value was passed in the argument
            if assetTypeClass and not isinstance(assetTypeClass, SubmodelElement):
                assetTypeClass = self.AssetTypeClass(assetTypeClass)

            # Build a submodel element if a raw value was passed in the argument
            if assetTypeIdentification and not isinstance(
                assetTypeIdentification, SubmodelElement
            ):
                assetTypeIdentification = self.AssetTypeIdentification(
                    assetTypeIdentification
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                pAMSpecificationSheetIdentification,
                assetTypeClass,
                assetTypeIdentification,
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

    class GeneralInformation(SubmodelElementCollection):

        class FunctionalLocation(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FunctionalLocation",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"FunctionalLocation", r"de": r"Technischer Platz"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": "Specifies the asset's logical position within a piping and instrumentation diagram."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV946#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value="Specifies the asset's logical position within a piping and instrumentation diagram.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"LEVNAMUR-V220-CA23-Y2233",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class TechnicalLocation(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TechnicalLocation",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Technical Location", r"de": r"Technischer Ort"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Specifies the actual location of the asset within the plant."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV947#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Specifies the actual location of the asset within the plant.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"V220",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class Description(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Description",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Description", r"de": r"Beschreibung"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": "Offers a concise explanation of the asset's primary function."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV948#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value="Offers a concise explanation of the asset's primary function.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"SISO Control Loop for the dosing valve",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class AssetSubtype(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"AssetSubtype",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Asset Subtype", r"de": r"Asset-Typ"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"Defines the specific subtype of the asset."}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV949#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Defines the specific subtype of the asset.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"SISO Control Loop",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class SpecificationSheetReference(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SpecificationSheetReference",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Specification Sheet Reference",
                        r"de": r"Link zum technischen Spezifikationsblatt",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference to the technical specification sheet accompanying the asset."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV952#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Reference to the technical specification sheet accompanying the asset.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"-",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class SafetyMeasure(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SafetyMeasure",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Safety Measure", r"de": r"Schutzeinrichtung"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Denotes whether the asset is part of a safety equipment."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV950#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Denotes whether the asset is part of a safety equipment.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"True;False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/InitialValue",
                            value_type=str,
                            value=r"False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/DefaultValue",
                            value_type=str,
                            value=r"False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/AllowedValue",
                            value_type=str,
                            value=r"True;False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class RedundantAssets(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"RedundantAssets",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Redundant Assets", r"de": r"Redundanz vorhanden"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"References zero (if empty), one or more backup assets for redundancy purposes."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV951#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"References zero (if empty), one or more backup assets for redundancy purposes.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/InitialValue",
                            value_type=str,
                            value=r"False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/DefaultValue",
                            value_type=str,
                            value=r"False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"True;False",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
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

        class SILCategory(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SILCategory",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"SIL Category", r"de": r"SIL Kategorie"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Denotes the safety integrity level (SIL), categorized into four levels."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV930#002",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"0;1;2;3;4",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/InitialValue",
                            value_type=str,
                            value=r"0",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/DefaultValue",
                            value_type=str,
                            value=r"0",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"2",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/AllowedValue",
                            value_type=str,
                            value=r"0;1;2;3;4",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
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

        class FailureProbability(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FailureProbability",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"FailureProbability",
                        r"de": r"Fehlerwahrscheinlichkeit",
                    }
                ),
                category: Optional[str] = r"VARIABLE",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Indicates the probability of a failure occurring, classified into three levels."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV942#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Indicates the probability of a failure occurring, classified into three levels.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"low;medium;high;critical",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/InitialValue",
                            value_type=str,
                            value=r"low",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/DefaultValue",
                            value_type=str,
                            value=r"low",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/AllowedValue",
                            value_type=str,
                            value=r"low;medium;high;critical",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"low",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class FailureSeverity(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FailureSeverity",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Failure Severity", r"de": r"Fehlerschwere"}
                ),
                category: Optional[str] = r"VARIABLE",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Indicates the potential impact or seriousness of a failure, classified into three levels."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV943#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Indicates the potential impact or seriousness of a failure, classified into three levels.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"no impact;potential;measureable;significant",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/InitialValue",
                            value_type=str,
                            value=r"significant",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/DefaultValue",
                            value_type=str,
                            value=r"significant",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"significant",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/AllowedValue",
                            value_type=str,
                            value=r"no impact;potential;measureable;significant",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
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

        class CriticalityCategory(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CriticalityCategory",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Criticality Category",
                        r"de": r"Kritikalitätskategorie",
                    }
                ),
                category: Optional[str] = r"VARIABLE",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"A computed value based on Failure Probability and Failure Severity, usually calculated automatically."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV941#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"A computed value based on Failure Probability and Failure Severity, usually calculated automatically.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"low;medium;high;critical",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/InitialValue",
                            value_type=str,
                            value=r"critical",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/DefaultValue",
                            value_type=str,
                            value=r"critical",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"critical",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class FurtherInformation(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FurtherInformation",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"FurtherInformation",
                        r"de": r"Weitere Angaben nach Bedarf",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Additional relevant details about the asset, such as maintenance schedules."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAW617#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"A field for including references to supplementary information.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"-",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class FurtherInformationReference(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FurtherInformationReference",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Further Information Reference",
                        r"de": r"Referenz auf weitere Informationen",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"A field for including references to supplementary information"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"A field for including references to supplementary information.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"-",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class GeneralTask(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"GeneralTask",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"General Task",
                        r"de": r"Allgemeine Aufgabenstellung",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Detailed description of the task and installation or placement conditions of the specific asset."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV956#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Detailed description of the task and installation or placement conditions of the specific asset.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"control loop is used to control the ratio between two input product.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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
            sILCategory: Union[str, SILCategory],
            functionalLocation: Optional[Union[str, FunctionalLocation]] = None,
            technicalLocation: Optional[Union[str, TechnicalLocation]] = None,
            description_: Optional[Union[str, Description]] = None,
            assetSubtype: Optional[Union[str, AssetSubtype]] = None,
            specificationSheetReference: Optional[
                Union[str, SpecificationSheetReference]
            ] = None,
            safetyMeasure: Optional[Union[str, SafetyMeasure]] = None,
            redundantAssets: Optional[Union[str, RedundantAssets]] = None,
            failureProbability: Optional[Union[str, FailureProbability]] = None,
            failureSeverity: Optional[Union[str, FailureSeverity]] = None,
            criticalityCategory: Optional[Union[str, CriticalityCategory]] = None,
            furtherInformation: Optional[
                Iterable[Union[str, FurtherInformation]]
            ] = None,
            furtherInformationReference: Optional[
                Iterable[Union[str, FurtherInformationReference]]
            ] = None,
            generalTask: Optional[Union[str, GeneralTask]] = None,
            id_short: Optional[str] = r"GeneralInformation",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"GeneralInformation", r"de": r"Allgemeine Angaben"}
            ),
            category: Optional[str] = r"PARAMETER",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"Provides details about the specific asset."}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#01-AGC975#002"),
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
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"General Information",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Provides details about the specific asset.",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument
            if functionalLocation and not isinstance(
                functionalLocation, SubmodelElement
            ):
                functionalLocation = self.FunctionalLocation(functionalLocation)

            # Build a submodel element if a raw value was passed in the argument
            if technicalLocation and not isinstance(technicalLocation, SubmodelElement):
                technicalLocation = self.TechnicalLocation(technicalLocation)

            # Build a submodel element if a raw value was passed in the argument
            if description_ and not isinstance(description_, SubmodelElement):
                description_ = self.Description(description_)

            # Build a submodel element if a raw value was passed in the argument
            if assetSubtype and not isinstance(assetSubtype, SubmodelElement):
                assetSubtype = self.AssetSubtype(assetSubtype)

            # Build a submodel element if a raw value was passed in the argument
            if specificationSheetReference and not isinstance(
                specificationSheetReference, SubmodelElement
            ):
                specificationSheetReference = self.SpecificationSheetReference(
                    specificationSheetReference
                )

            # Build a submodel element if a raw value was passed in the argument
            if safetyMeasure and not isinstance(safetyMeasure, SubmodelElement):
                safetyMeasure = self.SafetyMeasure(safetyMeasure)

            # Build a submodel element if a raw value was passed in the argument
            if redundantAssets and not isinstance(redundantAssets, SubmodelElement):
                redundantAssets = self.RedundantAssets(redundantAssets)

            # Build a submodel element if a raw value was passed in the argument
            if sILCategory and not isinstance(sILCategory, SubmodelElement):
                sILCategory = self.SILCategory(sILCategory)

            # Build a submodel element if a raw value was passed in the argument
            if failureProbability and not isinstance(
                failureProbability, SubmodelElement
            ):
                failureProbability = self.FailureProbability(failureProbability)

            # Build a submodel element if a raw value was passed in the argument
            if failureSeverity and not isinstance(failureSeverity, SubmodelElement):
                failureSeverity = self.FailureSeverity(failureSeverity)

            # Build a submodel element if a raw value was passed in the argument
            if criticalityCategory and not isinstance(
                criticalityCategory, SubmodelElement
            ):
                criticalityCategory = self.CriticalityCategory(criticalityCategory)

            # Build a list of submodel elements if a raw values were passed in the argument
            if furtherInformation and all(
                [isinstance(i, str) for i in furtherInformation]
            ):
                furtherInformation = [
                    self.FurtherInformation(i) for i in furtherInformation
                ]

            # Build a list of submodel elements if a raw values were passed in the argument
            if furtherInformationReference and all(
                [isinstance(i, str) for i in furtherInformationReference]
            ):
                furtherInformationReference = [
                    self.FurtherInformationReference(i)
                    for i in furtherInformationReference
                ]

            # Build a submodel element if a raw value was passed in the argument
            if generalTask and not isinstance(generalTask, SubmodelElement):
                generalTask = self.GeneralTask(generalTask)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                functionalLocation,
                technicalLocation,
                description_,
                assetSubtype,
                specificationSheetReference,
                safetyMeasure,
                redundantAssets,
                sILCategory,
                failureProbability,
                failureSeverity,
                criticalityCategory,
                furtherInformation,
                furtherInformationReference,
                generalTask,
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

    class CompleteSystem(SubmodelElementCollection):

        class StatusCondition(SubmodelElementCollection):

            class StatusConditionName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"StatusConditionName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Status Condition Name",
                            r"de": r"Zustands- und Fehlerbild",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "Name of the asset's state, highlighting deviations from normal operations or reduced lifespan."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV958#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="Name of the asset's state, highlighting deviations from normal operations or reduced lifespan.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Friction in valve",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class MonitoringRequired(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MonitoringRequired",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Monitoring Required",
                            r"de": r"Überwachung benötigt",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Specifies whether the user is requiring monitoring."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV959#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Specifies whether the user is requiring monitoring.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
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

            class Description(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Description",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Description", r"de": r"Beschreibung"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "Offers further information about the asset's status/fault profile or status monitoring."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV960#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="Offers further information about the asset's status/fault profile or status monitoring.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"-",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class MethodAbbreviation(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MethodAbbreviation",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Method Abbreviation", r"de": r"Methode"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Captures the abbreviated name of the PAM method employed for monitoring purposes."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV961#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Captures the abbreviated name of the PAM method employed for monitoring purposes.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"friction_dect",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class NE107Status(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NE107Status",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"NE107Status",
                            r"de": r"Status nach NAMUR-Empfehlung NE 107",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Status according to NAMUR recommendation NE 107."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV962#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"failure;function check;out of specification;maintenance request",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"failure",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"failure",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"failure",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"failure;function check;out of specification;maintenance request",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Status according to NAMUR recommendation NE 107.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
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

            class NE129AlarmCategory(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NE129AlarmCategory",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"NE129 Alarm Category",
                            r"de": r"Alarm-/Meldekategorie nach NAMUR Empfehlung NE129",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Alarm/signaling category according to NAMUR recommendation NE 129."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV963#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Asset-Alarm",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"Asset-Alarm",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"Asset-Alarm",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"Asset-Alarm;Asset-Notification;Asset-State Chance",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"Asset-Alarm;Asset-Notification;Asset-State Chance",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
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
                statusConditionName: Union[str, StatusConditionName],
                monitoringRequired: Union[str, MonitoringRequired],
                description_: Union[str, Description],
                methodAbbreviation: Optional[Union[str, MethodAbbreviation]] = None,
                nE107Status: Optional[Union[str, NE107Status]] = None,
                nE129AlarmCategory: Optional[Union[str, NE129AlarmCategory]] = None,
                id_short: Optional[str] = r"StatusCondition",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Status Condition",
                        r"de": r"Zustands- und Fehlerbild",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": "Characteristics of the asset's operational and failure states."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#01-AGC980#001",
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
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Status Condition",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value="Characteristics of the asset's operational and failure states.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

                # Build a submodel element if a raw value was passed in the argument
                if statusConditionName and not isinstance(
                    statusConditionName, SubmodelElement
                ):
                    statusConditionName = self.StatusConditionName(statusConditionName)

                # Build a submodel element if a raw value was passed in the argument
                if monitoringRequired and not isinstance(
                    monitoringRequired, SubmodelElement
                ):
                    monitoringRequired = self.MonitoringRequired(monitoringRequired)

                # Build a submodel element if a raw value was passed in the argument
                if description_ and not isinstance(description_, SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument
                if methodAbbreviation and not isinstance(
                    methodAbbreviation, SubmodelElement
                ):
                    methodAbbreviation = self.MethodAbbreviation(methodAbbreviation)

                # Build a submodel element if a raw value was passed in the argument
                if nE107Status and not isinstance(nE107Status, SubmodelElement):
                    nE107Status = self.NE107Status(nE107Status)

                # Build a submodel element if a raw value was passed in the argument
                if nE129AlarmCategory and not isinstance(
                    nE129AlarmCategory, SubmodelElement
                ):
                    nE129AlarmCategory = self.NE129AlarmCategory(nE129AlarmCategory)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    statusConditionName,
                    monitoringRequired,
                    description_,
                    methodAbbreviation,
                    nE107Status,
                    nE129AlarmCategory,
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
            statusCondition: Optional[Iterable[StatusCondition]] = None,
            id_short: Optional[str] = r"CompleteSystem",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"Complete System", r"de": r"Komplettsystem"}
            ),
            category: Optional[str] = r"PARAMETER",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Interconnected fields, incorporating status/fault profiles that apply to the entire asset rather than specific parts."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#01-AGC979#001"),
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
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Complete System",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Interconnected fields, incorporating status/fault profiles that apply to the entire asset rather than specific parts.",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [statusCondition]:
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

    class SubSystem(SubmodelElementCollection):

        class SubSystemName(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SubSystemName",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Subsystem Name", r"de": r"Teilsystem Name"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"Specifies the name of the subsystem."}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV965#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Specifies the name of the subsystem.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"Control valve",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class FunctionalLocation(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FunctionalLocation",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Functional Location", r"de": r"Technischer Platz"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": "Indicates the subsystem's logical position within a piping and instrumentation diagram."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV946#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Specifies the actual location of the subsystem in the plant.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"LEVTDA-V220-AB13-WT013",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class TechnicalLocation(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TechnicalLocation",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Technical Location", r"de": r"Technischer Ort"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Specifies the actual location of the subsystem in the plant."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV947#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Specifies the actual location of the subsystem in the plant.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/ExampleValue",
                            value_type=str,
                            value=r"V220",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

        class StatusCondition(SubmodelElementCollection):

            class StatusConditionName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"StatusConditionName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Status Condition Name",
                            r"de": r"Zustands- und Fehlerbild",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "Name of the subsystem's state, highlighting deviations from normal operations or reduced lifespan."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV958#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="Name of the subsystem's state, highlighting deviations from normal operations or reduced lifespan.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Low temperature",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class MonitoringRequired(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MonitoringRequired",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Monitoring Required",
                            r"de": r"Überwachung benötigt",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Specifies whether the user is requiring monitoring."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV959#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"To be filled; longer explanation",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
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

            class Description(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Description",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Description", r"de": r"Beschreibung"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "Offers further information about the subsystem's status/fault profile or status monitoring."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV960#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="Offers further information about the subsystem's status/fault profile or status monitoring.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Outlet temperature drops below threshold",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class MethodAbbreviation(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MethodAbbreviation",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Method Abbreviation", r"de": r"Methode"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Captures the abbreviated name of the PAM method employed for monitoring purposes."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV961#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Captures the abbreviated name of the PAM method employed for monitoring purposes.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"OutletTemperatureMonitoring",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class NE107Status(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NE107Status",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"NE 107 Status",
                            r"de": r"Status nach NAMUR-Empfehlung NE 107",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Status according to NAMUR recommendation NE 107."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV962#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Status according to NAMUR recommendation NE 107.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"failure",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"failure;function check;out of specification;maintenance request",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"failure;function check;out of specification;maintenance request",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"failure",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"failure",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
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

            class NE129AlarmCategory(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NE129AlarmCategory",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"NE 129 Alarm Category",
                            r"de": r"Alarm-/Meldekategorie nach NAMUR Empfehlung",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Alarm/signaling category according to NAMUR recommendation NE 129."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV963#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Alarm/signaling category according to NAMUR recommendation NE 129.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"Asset-Alarm;Asset-Notification;Asset-State Chance",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"Asset-Alarm;Asset-Notification;Asset-State Chance",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"Asset-Alarm",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"Asset-Alarm",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Asset-Alarm",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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
                statusConditionName: Union[str, StatusConditionName],
                monitoringRequired: Union[str, MonitoringRequired],
                description_: Union[str, Description],
                methodAbbreviation: Optional[Union[str, MethodAbbreviation]] = None,
                nE107Status: Optional[Union[str, NE107Status]] = None,
                nE129AlarmCategory: Optional[Union[str, NE129AlarmCategory]] = None,
                id_short: Optional[str] = r"StatusCondition",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Status Condition",
                        r"de": r"Zustands- und Fehlerbild",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": "Characteristics of the subsystems's operational and failure states."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#01-AGC980#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Status Condition",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value="Characteristics of the subsystems's operational and failure states.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if statusConditionName and not isinstance(
                    statusConditionName, SubmodelElement
                ):
                    statusConditionName = self.StatusConditionName(statusConditionName)

                # Build a submodel element if a raw value was passed in the argument
                if monitoringRequired and not isinstance(
                    monitoringRequired, SubmodelElement
                ):
                    monitoringRequired = self.MonitoringRequired(monitoringRequired)

                # Build a submodel element if a raw value was passed in the argument
                if description_ and not isinstance(description_, SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument
                if methodAbbreviation and not isinstance(
                    methodAbbreviation, SubmodelElement
                ):
                    methodAbbreviation = self.MethodAbbreviation(methodAbbreviation)

                # Build a submodel element if a raw value was passed in the argument
                if nE107Status and not isinstance(nE107Status, SubmodelElement):
                    nE107Status = self.NE107Status(nE107Status)

                # Build a submodel element if a raw value was passed in the argument
                if nE129AlarmCategory and not isinstance(
                    nE129AlarmCategory, SubmodelElement
                ):
                    nE129AlarmCategory = self.NE129AlarmCategory(nE129AlarmCategory)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    statusConditionName,
                    monitoringRequired,
                    description_,
                    methodAbbreviation,
                    nE107Status,
                    nE129AlarmCategory,
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

        class SubSystemReference(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SubSystemReference",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Subsystem Reference", r"de": r"Subsystem Referenze"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"Additional references associated to the subsystem."}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAW622#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Additional references associated to the subsystem.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
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

        class PAMSpecificationSheetIdentification(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PAMSpecificationSheetIdentification",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"PAM Specification Sheet Identification",
                        r"de": r"PAM Spezifikationsblatt Identifikation",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"The distinct identifier for the PAM specification sheet for the subsystem."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV929#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"The distinct identifier for the PAM specification sheet for the subsystem.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
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

        class PAMSpecificationSheetReference(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PAMSpecificationSheetReference",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"PAM Specification Sheet Reference",
                        r"de": r"PAM Spezifikationsblatt Referenz",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Links to relevant PAM specification documentation for the subsystem."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAV967#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Links to relevant PAM specification documentation for the subsystem.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
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
            subSystemName: Union[str, SubSystemName],
            functionalLocation: Optional[Union[str, FunctionalLocation]] = None,
            technicalLocation: Optional[Union[str, TechnicalLocation]] = None,
            statusCondition: Optional[Iterable[StatusCondition]] = None,
            subSystemReference: Optional[Union[str, SubSystemReference]] = None,
            pAMSpecificationSheetIdentification: Optional[
                Union[str, PAMSpecificationSheetIdentification]
            ] = None,
            pAMSpecificationSheetReference: Optional[
                Union[str, PAMSpecificationSheetReference]
            ] = None,
            id_short: Optional[str] = r"SubSystem",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"Subsystem", r"de": r"Teilsystem"}
            ),
            category: Optional[str] = r"PARAMETER",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"Properties of the subsystem."}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#01-AGC981#001"),
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
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Subsystem",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Properties of the subsystem.",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToMany",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
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

            # Build a submodel element if a raw value was passed in the argument
            if subSystemName and not isinstance(subSystemName, SubmodelElement):
                subSystemName = self.SubSystemName(subSystemName)

            # Build a submodel element if a raw value was passed in the argument
            if functionalLocation and not isinstance(
                functionalLocation, SubmodelElement
            ):
                functionalLocation = self.FunctionalLocation(functionalLocation)

            # Build a submodel element if a raw value was passed in the argument
            if technicalLocation and not isinstance(technicalLocation, SubmodelElement):
                technicalLocation = self.TechnicalLocation(technicalLocation)

            # Build a submodel element if a raw value was passed in the argument
            if subSystemReference and not isinstance(
                subSystemReference, SubmodelElement
            ):
                subSystemReference = self.SubSystemReference(subSystemReference)

            # Build a submodel element if a raw value was passed in the argument
            if pAMSpecificationSheetIdentification and not isinstance(
                pAMSpecificationSheetIdentification, SubmodelElement
            ):
                pAMSpecificationSheetIdentification = (
                    self.PAMSpecificationSheetIdentification(
                        pAMSpecificationSheetIdentification
                    )
                )

            # Build a submodel element if a raw value was passed in the argument
            if pAMSpecificationSheetReference and not isinstance(
                pAMSpecificationSheetReference, SubmodelElement
            ):
                pAMSpecificationSheetReference = self.PAMSpecificationSheetReference(
                    pAMSpecificationSheetReference
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                subSystemName,
                functionalLocation,
                technicalLocation,
                statusCondition,
                subSystemReference,
                pAMSpecificationSheetIdentification,
                pAMSpecificationSheetReference,
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

    class ApplicableMethod(SubmodelElementCollection):

        class StaticParameters(SubmodelElementCollection):

            class ParameterName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ParameterName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Parameter Name", r"de": r"Parametername"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Name of method parameter."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV978#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Name of method parameter.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Warning limit for efficiency",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Description(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Description",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Description", r"de": r"Beschreibung"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "Provides a concise explanation of the parameter's purpose."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV979#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="Provides a concise explanation of the parameter's purpose.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Falling below the limit triggers an alarm",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class StaticParameterValue(Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"StaticParameterValue",
                    value_type: DataTypeDefXsd = float,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Static Parameter Value",
                            r"de": r"Statischer Parameter Wert",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"A static parameter value of a method used for monitoring of this subsystem."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV980#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"A static parameter value of a method used for monitoring of this subsystem.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=float,
                                value=75.0,
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class PhysicalUnit(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PhysicalUnit",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"PhysicalUnit", r"de": r"Einheit"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Specifies the physical unit of the static parameter."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV981#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Specifies the physical unit of the static parameter.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"%",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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
                parameterName: Union[str, ParameterName],
                staticParameterValue: Union[float, StaticParameterValue],
                physicalUnit: Union[str, PhysicalUnit],
                description_: Optional[Union[str, Description]] = None,
                id_short: Optional[str] = r"StaticParameters",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Static Parameters", r"de": r"Statische Parameter"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"List of static parameters such as trigger limits."}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#01-AGC984#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Static Parameter",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"List of static parameters such as trigger limits.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if parameterName and not isinstance(parameterName, SubmodelElement):
                    parameterName = self.ParameterName(parameterName)

                # Build a submodel element if a raw value was passed in the argument
                if description_ and not isinstance(description_, SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument
                if staticParameterValue and not isinstance(
                    staticParameterValue, SubmodelElement
                ):
                    staticParameterValue = self.StaticParameterValue(
                        staticParameterValue
                    )

                # Build a submodel element if a raw value was passed in the argument
                if physicalUnit and not isinstance(physicalUnit, SubmodelElement):
                    physicalUnit = self.PhysicalUnit(physicalUnit)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    parameterName,
                    description_,
                    staticParameterValue,
                    physicalUnit,
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

        class GeneratedSignals(SubmodelElementCollection):

            class SignalName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SignalName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Signal Name", r"de": r"Signalname"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Name of the generated signal."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV983#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Name of the generated signal.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Efficiency Bad",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Description(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Description",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Description", r"de": r"Beschreibung"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Provides a concise explanation of the generated signal."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV984#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Provides a concise explanation of the generated signal.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Binary alarm signal",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class ValueRange(Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"ValueRange",
                    value_type: DataTypeDefXsd = float,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Wertebereich"}),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Specifies the possible range of values for the generated signal."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV985#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Specifies the possible range of values for the generated signal (optional).",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=float,
                                value=100.0,
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class PhysicalUnit(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PhysicalUnit",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"PhysicalUnit", r"de": r"Einheit"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Physical unit of the generated signal."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV981#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Physical unit of the generated signal.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"m",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class RecordingRequired(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"RecordingRequired",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Recording Required",
                            r"de": r"Aufzeichnung im PAM-System",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Determines whether the signal is transmitted to the PAM system for long-term archiving."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV986#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Determines whether the signal is transmitted to the PAM system for long-term archiving.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class SignalType(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SignalType",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Signal Type", r"de": r"Signalart"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates whether the generated signal from the method is a floating point, integer or binary value."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV987#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"floating point;integer;binary",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"floating point;integer;binary",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"floating point",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"floating point",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"floating point",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Indicates whether the generated signal from the method is a floating point, integer or binary value.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
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
                signalName: Union[str, SignalName],
                recordingRequired: Union[str, RecordingRequired],
                signalType: Union[str, SignalType],
                description_: Optional[Union[str, Description]] = None,
                valueRange: Optional[Union[float, ValueRange]] = None,
                physicalUnit: Optional[Union[str, PhysicalUnit]] = None,
                id_short: Optional[str] = r"GeneratedSignals",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Generated Signals",
                        r"de": r"Generiertes Signal aus Methode",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"List of generated signals."}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#01-AGC985#001",
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
                            value=r"OneToMany",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Generated Signals",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"List of generated signals.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if signalName and not isinstance(signalName, SubmodelElement):
                    signalName = self.SignalName(signalName)

                # Build a submodel element if a raw value was passed in the argument
                if description_ and not isinstance(description_, SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument
                if valueRange and not isinstance(valueRange, SubmodelElement):
                    valueRange = self.ValueRange(valueRange)

                # Build a submodel element if a raw value was passed in the argument
                if physicalUnit and not isinstance(physicalUnit, SubmodelElement):
                    physicalUnit = self.PhysicalUnit(physicalUnit)

                # Build a submodel element if a raw value was passed in the argument
                if recordingRequired and not isinstance(
                    recordingRequired, SubmodelElement
                ):
                    recordingRequired = self.RecordingRequired(recordingRequired)

                # Build a submodel element if a raw value was passed in the argument
                if signalType and not isinstance(signalType, SubmodelElement):
                    signalType = self.SignalType(signalType)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    signalName,
                    description_,
                    valueRange,
                    physicalUnit,
                    recordingRequired,
                    signalType,
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

        class RequiredInputSignals(SubmodelElementCollection):

            class Name(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Name",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Name", r"de": r"Eingangssignal-Name"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Name of the required input signal."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV989#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Name of the required input signal.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Flow1",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Description(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Description",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Description", r"de": r"Beschreibung"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Provides a concise explanation of the input signal."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV990#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Provides a concise explanation of the input signal.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"Primary flow",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class ValueRange(Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"ValueRange",
                    value_type: DataTypeDefXsd = float,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Value Range", r"de": r"Wertebereich"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Specifies the value range of the input signal."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV991#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Specifies the value range of the input signal (optional).",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=float,
                                value=100.0,
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class PhysicalUnit(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PhysicalUnit",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Physical Unit", r"de": r"Einheit"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Physical unit of the input signal."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV981#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Physical unit of the input signal (optional).",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"m",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Required(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Required",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Required", r"de": r"Benötigt"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Specifies whether the input signal is required for the method."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV992#001",
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
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Specifies whether the input signal is required for the method.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
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

            class InputAvailable(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InputAvailable",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Input Available", r"de": r"Vorhanden"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Clarification whether this input signal for the method is already available."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV993#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Clarification whether this input signal for the method is already available.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
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

            class FunctionalLocation(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"FunctionalLocation",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Functional Location",
                            r"de": r"Technischer Platz",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "Indicates the asset's logical position within a piping and instrumentation diagram"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV946#001",
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
                                type_=r"FormInfo",
                                value_type=str,
                                value="Specifies the input signal's source.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"LEVTDA-V220-AB13-FV01",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class RecordingRequired(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"RecordingRequired",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Recording Required",
                            r"de": r"Aufzeichnung im PAM-System",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Determines whether the values of the input signal are transmitted to the PAM system for long-term archiving."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV994#001",
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
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"True;False",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Determines whether the values of the input signal are transmitted to the PAM system for long-term archiving.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/InitialValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/InitialValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/DefaultValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/DefaultValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/AllowedValue",
                                value_type=str,
                                value=r"True",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0",
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
                name: Union[str, Name],
                required: Union[str, Required],
                inputAvailable: Union[str, InputAvailable],
                recordingRequired: Union[str, RecordingRequired],
                description_: Optional[Union[str, Description]] = None,
                valueRange: Optional[Union[float, ValueRange]] = None,
                physicalUnit: Optional[Union[str, PhysicalUnit]] = None,
                functionalLocation: Optional[Union[str, FunctionalLocation]] = None,
                id_short: Optional[str] = r"RequiredInputSignals",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Required Input Signals",
                        r"de": r"Vorhandene, benötigte Sensoren, Geräte",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"List of necessary input signals of the method."}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#01-AGC986#001",
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
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Requird Input Signals",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"List of necessary input signals of the method.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if name and not isinstance(name, SubmodelElement):
                    name = self.Name(name)

                # Build a submodel element if a raw value was passed in the argument
                if description_ and not isinstance(description_, SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument
                if valueRange and not isinstance(valueRange, SubmodelElement):
                    valueRange = self.ValueRange(valueRange)

                # Build a submodel element if a raw value was passed in the argument
                if physicalUnit and not isinstance(physicalUnit, SubmodelElement):
                    physicalUnit = self.PhysicalUnit(physicalUnit)

                # Build a submodel element if a raw value was passed in the argument
                if required and not isinstance(required, SubmodelElement):
                    required = self.Required(required)

                # Build a submodel element if a raw value was passed in the argument
                if inputAvailable and not isinstance(inputAvailable, SubmodelElement):
                    inputAvailable = self.InputAvailable(inputAvailable)

                # Build a submodel element if a raw value was passed in the argument
                if functionalLocation and not isinstance(
                    functionalLocation, SubmodelElement
                ):
                    functionalLocation = self.FunctionalLocation(functionalLocation)

                # Build a submodel element if a raw value was passed in the argument
                if recordingRequired and not isinstance(
                    recordingRequired, SubmodelElement
                ):
                    recordingRequired = self.RecordingRequired(recordingRequired)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    name,
                    description_,
                    valueRange,
                    physicalUnit,
                    required,
                    inputAvailable,
                    functionalLocation,
                    recordingRequired,
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
            generatedSignals: Iterable[GeneratedSignals],
            staticParameters: Optional[Iterable[StaticParameters]] = None,
            requiredInputSignals: Optional[Iterable[RequiredInputSignals]] = None,
            id_short: Optional[str] = r"ApplicableMethod",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"Applicable Method", r"de": r"Anwendbare Methode"}
            ),
            category: Optional[str] = r"PARAMETER",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Characteristics of the method used for state or fault detection."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#01-AGC983#002"),
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
                        value=r"OneToMany",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Applicable Method",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Characteristics of the method used for state or fault detection.",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [staticParameters, generatedSignals, requiredInputSignals]:
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

    class DocumentFooter(SubmodelElementCollection):

        class DocumentConfirmation(SubmodelElementCollection):

            class Date(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Date",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Datum"}),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Date of revision of the PAM specification sheet."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAR969#002",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Date of revision of the PAM specification sheet.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"2024-05-17",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Author(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Author",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Author", r"de": r"Verfasser"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "The individual responsible for the document's revision."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV997#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="The individual responsible for the document's revision.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"H. Müller",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Checked(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Checked",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Checked", r"de": r"Geprüft"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"The person who has checked the document."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV999#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"The person who has checked the document.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"T. Mayer",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Released(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Released",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Released", r"de": r"Genehmigt"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"The individual who has authorized the document for release."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAV998#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"The individual who has authorized the document for release.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"O. Boss",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class DocumentVersion(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DocumentVersion",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Document Version",
                            r"de": r"Dokumentenidentifikation",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "Identifier for the document's version."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAW000#001",
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
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="Identifier for the document's version.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"V0.8",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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

            class Company(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Company",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Company", r"de": r"Firma"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"The name of the company associated with the confirmation of the document."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAW001#001",
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
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"The name of the company associated with the confirmation of the document.",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"SMT/ExampleValue",
                                value_type=str,
                                value=r"IDTA",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
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
                date: Union[str, Date],
                author: Union[str, Author],
                checked: Optional[Union[str, Checked]] = None,
                released: Optional[Union[str, Released]] = None,
                documentVersion: Optional[Union[str, DocumentVersion]] = None,
                company: Optional[Union[str, Company]] = None,
                id_short: Optional[str] = r"DocumentConfirmation",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Document Confirmation",
                        r"de": r"Dokument Bestätigung",
                    }
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Information regarding the confirmation to the current status of the PAM specification sheet."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#01-AGC988#001",
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
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Information regarding the confirmation to the current status of the PAM specification sheet.",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Document Confirmation",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
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

                # Build a submodel element if a raw value was passed in the argument
                if date and not isinstance(date, SubmodelElement):
                    date = self.Date(date)

                # Build a submodel element if a raw value was passed in the argument
                if author and not isinstance(author, SubmodelElement):
                    author = self.Author(author)

                # Build a submodel element if a raw value was passed in the argument
                if checked and not isinstance(checked, SubmodelElement):
                    checked = self.Checked(checked)

                # Build a submodel element if a raw value was passed in the argument
                if released and not isinstance(released, SubmodelElement):
                    released = self.Released(released)

                # Build a submodel element if a raw value was passed in the argument
                if documentVersion and not isinstance(documentVersion, SubmodelElement):
                    documentVersion = self.DocumentVersion(documentVersion)

                # Build a submodel element if a raw value was passed in the argument
                if company and not isinstance(company, SubmodelElement):
                    company = self.Company(company)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    date,
                    author,
                    checked,
                    released,
                    documentVersion,
                    company,
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
            documentConfirmation: Iterable[DocumentConfirmation],
            id_short: Optional[str] = r"DocumentFooter",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={
                    r"en": r"Document Footer",
                    r"de": r"Dokumentenfuß Anwender und Anbieter",
                }
            ),
            category: Optional[str] = r"PARAMETER",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Release information related to the complete PAM specification sheet."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"173-1#02-AAW627#001"),
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
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Release information related to the complete PAM specification sheet.",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Document Footer",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documentConfirmation]:
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
        documentHeader: DocumentHeader,
        generalInformation: GeneralInformation,
        applicableMethod: Iterable[ApplicableMethod],
        documentFooter: DocumentFooter,
        completeSystem: Optional[CompleteSystem] = None,
        subSystem: Optional[Iterable[SubSystem]] = None,
        id_short: Optional[str] = r"PAMSpecificationSheet",
        display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
            dict_={r"en": r"PAM Specification Sheet", r"de": r"PAM Spezificationsblatt"}
        ),
        category: Optional[str] = r"VARIABLE",
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"PAM Specification Sheet according to VDI/VDE GMA RL 2651-2 and specification of Plant Asset Management functions ",
                r"de": r"Beschreibung und Spezifikation PAM Funktionen nach VDI GMA",
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/idta-02019-1-0",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(Key(type_=KeyTypes.SUBMODEL, value=r"0173-1#01-AGC973#003"),),
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
            qualifier = (
                Qualifier(
                    type_=r"FormInfo",
                    value_type=str,
                    value=r"PAM Specification Sheet according to VDI/VDE GMA RL 2651-2 and specification of Plant Asset Management functions ",
                    value_id=None,
                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
                Qualifier(
                    type_=r"SMT/Cardinality",
                    value_type=str,
                    value=r"One",
                    value_id=None,
                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                    semantic_id=ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    supplemental_semantic_id=(),
                ),
                Qualifier(
                    type_=r"FormTitle",
                    value_type=str,
                    value=r"PAM Specification Sheet",
                    value_id=None,
                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
            )

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            documentHeader,
            generalInformation,
            completeSystem,
            subSystem,
            applicableMethod,
            documentFooter,
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
