from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class SoftwareNameplate(aas.Submodel):

    class SoftwareNameplateType(aas.SubmodelElementCollection):

        class URIOfTheProduct(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"URIOfTheProduct",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAY811#001",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class ManufacturerName(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ManufacturerName",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAO677#002",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class ManufacturerProductDesignation(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ManufacturerProductDesignation",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAW338#001",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class ManufacturerProductDescription(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ManufacturerProductDescription",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/ManufacturerProductDescription",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class ManufacturerProductFamily(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ManufacturerProductFamily",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAU731#001",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class ManufacturerProductType(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ManufacturerProductType",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAO057#002",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class SoftwareType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SoftwareType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/SoftwareType",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class Version(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Version",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/Version",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class VersionName(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"VersionName",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/VersionName",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Name der Version",
                            r"en": r"the name this particular version is given",
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class VersionInfo(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"VersionInfo",
                value_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/ZVEI/AkItInAutomation/NameplateSoftware/ReleaseNotes/1/0//example.com/ids/cd/8500_7052_2012_2916",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/VersionInfo",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Provides a textual description of most relevant characteristics of the version of the software"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class ReleaseDate(aas.Property):

            def __init__(
                self,
                value: xsd.Date,
                id_short: Optional[str] = r"ReleaseDate",
                value_type: aas.DataTypeDefXsd = xsd.Date,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/ReleaseDate",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class ReleaseNotes(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ReleaseNotes",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/ReleaseNotes",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Provides a textual description of most relevant characteristics of the version of the software"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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

        class ReleaseInformation(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ReleaseInformation",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/ReleaseInformation",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"EMPTY", r"de": r"EMPTY"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class BuildDate(aas.Property):

            def __init__(
                self,
                value: xsd.Date,
                id_short: Optional[str] = r"BuildDate",
                value_type: aas.DataTypeDefXsd = xsd.Date,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/BuildDate",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstallationURI(aas.Property):

            def __init__(
                self,
                value: xsd.AnyURI,
                id_short: Optional[str] = r"InstallationURI",
                value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/InstallationURI",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates the resource, where the software is being provided by the manufacturer."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstallationFile(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstallationFile",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/InstallationFile",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"EMPTY", r"de": r"EMPTY"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstallerType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstallerType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/InstallerType",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Indicates the type of installation package."}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstallationChecksum(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstallationChecksum",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/InstallationChecksum",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"provides the checksum for the software available at InstallationURI",
                            r"de": r"beinhaltet die Prüfsumme für die Software, die über InstallationURI angegeben ist",
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
            uRIOfTheProduct: Union[str, URIOfTheProduct],
            manufacturerName: Union[aas.LangStringSet, ManufacturerName],
            manufacturerProductDesignation: Union[
                aas.LangStringSet, ManufacturerProductDesignation
            ],
            version: Union[str, Version],
            releaseDate: Union[xsd.Date, ReleaseDate],
            buildDate: Union[xsd.Date, BuildDate],
            manufacturerProductDescription: Optional[
                Union[aas.LangStringSet, ManufacturerProductDescription]
            ] = None,
            manufacturerProductFamily: Optional[
                Union[aas.LangStringSet, ManufacturerProductFamily]
            ] = None,
            manufacturerProductType: Optional[
                Union[aas.LangStringSet, ManufacturerProductType]
            ] = None,
            softwareType: Optional[Union[str, SoftwareType]] = None,
            versionName: Optional[Union[aas.LangStringSet, VersionName]] = None,
            versionInfo: Optional[Union[aas.LangStringSet, VersionInfo]] = None,
            releaseNotes: Optional[Union[aas.LangStringSet, ReleaseNotes]] = None,
            releaseInformation: Optional[Union[str, ReleaseInformation]] = None,
            installationURI: Optional[Union[xsd.AnyURI, InstallationURI]] = None,
            installationFile: Optional[Union[str, InstallationFile]] = None,
            installerType: Optional[Union[str, InstallerType]] = None,
            installationChecksum: Optional[Union[str, InstallationChecksum]] = None,
            id_short: Optional[str] = r"SoftwareNameplateType",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType",
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

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Multiplicity",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if uRIOfTheProduct is not None and not isinstance(
                uRIOfTheProduct, aas.SubmodelElement
            ):
                uRIOfTheProduct = self.URIOfTheProduct(uRIOfTheProduct)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerName is not None and not isinstance(
                manufacturerName, aas.SubmodelElement
            ):
                manufacturerName = self.ManufacturerName(manufacturerName)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerProductDesignation is not None and not isinstance(
                manufacturerProductDesignation, aas.SubmodelElement
            ):
                manufacturerProductDesignation = self.ManufacturerProductDesignation(
                    manufacturerProductDesignation
                )

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerProductDescription is not None and not isinstance(
                manufacturerProductDescription, aas.SubmodelElement
            ):
                manufacturerProductDescription = self.ManufacturerProductDescription(
                    manufacturerProductDescription
                )

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerProductFamily is not None and not isinstance(
                manufacturerProductFamily, aas.SubmodelElement
            ):
                manufacturerProductFamily = self.ManufacturerProductFamily(
                    manufacturerProductFamily
                )

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerProductType is not None and not isinstance(
                manufacturerProductType, aas.SubmodelElement
            ):
                manufacturerProductType = self.ManufacturerProductType(
                    manufacturerProductType
                )

            # Build a submodel element if a raw value was passed in the argument

            if softwareType is not None and not isinstance(
                softwareType, aas.SubmodelElement
            ):
                softwareType = self.SoftwareType(softwareType)

            # Build a submodel element if a raw value was passed in the argument

            if version is not None and not isinstance(version, aas.SubmodelElement):
                version = self.Version(version)

            # Build a submodel element if a raw value was passed in the argument

            if versionName is not None and not isinstance(
                versionName, aas.SubmodelElement
            ):
                versionName = self.VersionName(versionName)

            # Build a submodel element if a raw value was passed in the argument

            if versionInfo is not None and not isinstance(
                versionInfo, aas.SubmodelElement
            ):
                versionInfo = self.VersionInfo(versionInfo)

            # Build a submodel element if a raw value was passed in the argument

            if releaseDate is not None and not isinstance(
                releaseDate, aas.SubmodelElement
            ):
                releaseDate = self.ReleaseDate(releaseDate)

            # Build a submodel element if a raw value was passed in the argument

            if releaseNotes is not None and not isinstance(
                releaseNotes, aas.SubmodelElement
            ):
                releaseNotes = self.ReleaseNotes(releaseNotes)

            # Build a submodel element if a raw value was passed in the argument

            if releaseInformation is not None and not isinstance(
                releaseInformation, aas.SubmodelElement
            ):
                releaseInformation = self.ReleaseInformation(releaseInformation)

            # Build a submodel element if a raw value was passed in the argument

            if buildDate is not None and not isinstance(buildDate, aas.SubmodelElement):
                buildDate = self.BuildDate(buildDate)

            # Build a submodel element if a raw value was passed in the argument

            if installationURI is not None and not isinstance(
                installationURI, aas.SubmodelElement
            ):
                installationURI = self.InstallationURI(installationURI)

            # Build a submodel element if a raw value was passed in the argument

            if installationFile is not None and not isinstance(
                installationFile, aas.SubmodelElement
            ):
                installationFile = self.InstallationFile(installationFile)

            # Build a submodel element if a raw value was passed in the argument

            if installerType is not None and not isinstance(
                installerType, aas.SubmodelElement
            ):
                installerType = self.InstallerType(installerType)

            # Build a submodel element if a raw value was passed in the argument

            if installationChecksum is not None and not isinstance(
                installationChecksum, aas.SubmodelElement
            ):
                installationChecksum = self.InstallationChecksum(installationChecksum)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                uRIOfTheProduct,
                manufacturerName,
                manufacturerProductDesignation,
                manufacturerProductDescription,
                manufacturerProductFamily,
                manufacturerProductType,
                softwareType,
                version,
                versionName,
                versionInfo,
                releaseDate,
                releaseNotes,
                releaseInformation,
                buildDate,
                installationURI,
                installationFile,
                installerType,
                installationChecksum,
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

    class SoftwareNameplateInstance(aas.SubmodelElementCollection):

        class SerialNumber(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SerialNumber",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAM556#002",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InventoryTag(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InventoryTag",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InventoryTag",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"contains inventory information of the user"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstanceName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstanceName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstanceName",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Der Name der konkreten Instanz"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstalledVersion(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstalledVersion",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstalledVersion",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"indicates the actual version of the instance"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstallationDate(aas.Property):

            def __init__(
                self,
                value: xsd.Date,
                id_short: Optional[str] = r"InstallationDate",
                value_type: aas.DataTypeDefXsd = xsd.Date,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstallationDate",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"containes the time of installation of this instance"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstallationPath(aas.Property):

            def __init__(
                self,
                value: xsd.AnyURI,
                id_short: Optional[str] = r"InstallationPath",
                value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstallationPath",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates the path to the installed instance of the software.",
                            r"de": r"gibt den Pfad an, an dem diese Instanz der Software installiert wurde.",
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstallationSource(aas.Property):

            def __init__(
                self,
                value: xsd.AnyURI,
                id_short: Optional[str] = r"InstallationSource",
                value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstallationSource",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstalledOnArchitecture(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstalledOnArchitecture",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstalledOnArchitecture",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstalledOnOS(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstalledOnOS",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstalledOnOS",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstalledOnHost(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InstalledOnHost",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstalledOnHost",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class InstalledModules(aas.SubmodelElementCollection):

            class InstalledModule(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InstalledModule",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstalledModule",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"OneToMany",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                installedModule: Iterable[Union[str, InstalledModule]],
                id_short: Optional[str] = r"InstalledModules",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/InstalledModules",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(installedModule, str):
                    raise TypeError("installedModule takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if installedModule:
                    installedModule = [
                        (
                            i
                            if isinstance(i, aas.SubmodelElement)
                            else self.InstalledModule(i)
                        )
                        for i in installedModule
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [installedModule]:
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

        class ConfigurationPaths(aas.SubmodelElementCollection):

            class ConfigurationPath(aas.SubmodelElementCollection):

                class ConfigurationURI(aas.Property):

                    def __init__(
                        self,
                        value: xsd.AnyURI,
                        id_short: Optional[str] = r"ConfigurationURI",
                        value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"VARIABLE",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/ConfigurationURI",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                class ConfigurationType(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ConfigurationType",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"VARIABLE",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/ConfigurationType",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                    configurationURI: Union[xsd.AnyURI, ConfigurationURI],
                    configurationType: Optional[Union[str, ConfigurationType]] = None,
                    id_short: Optional[str] = r"ConfigurationPath",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"VARIABLE",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/ConfigurationPath",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"OneToMany",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if configurationURI is not None and not isinstance(
                        configurationURI, aas.SubmodelElement
                    ):
                        configurationURI = self.ConfigurationURI(configurationURI)

                    # Build a submodel element if a raw value was passed in the argument

                    if configurationType is not None and not isinstance(
                        configurationType, aas.SubmodelElement
                    ):
                        configurationType = self.ConfigurationType(configurationType)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [configurationURI, configurationType]:
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
                configurationPath: Iterable[ConfigurationPath],
                id_short: Optional[str] = r"ConfigurationPaths",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/ConfigurationPaths",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(configurationPath, str):
                    raise TypeError(
                        "configurationPath takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [configurationPath]:
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

        class SLAInformation(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SLAInformation",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance/SLAInformation",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

        class Contact(aas.SubmodelElementCollection):

            class RoleOfContactPerson(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"RoleOfContactPerson",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO204#003",
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

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"enumeration: 0173-1#07-AAS927#001 (administrativ contact), 0173-1#07-AAS928#001 (commercial contact), 0173-1#07-AAS929#001 (other contact), 0173-1#07-AAS930#001 (hazardous goods contact), 0173-1#07-AAS931#001 (technical contact). Note: the above mentioned ECLASS enumeration should be declared as “open” for further addition. ECLASS enumeration IRDI is preferable. If no IRDI available, custom input as String may also be accepted."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class NationalCode(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"NationalCode",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO134#002",
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

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r" Note: country codes defined accord. to ISO 3166-1. Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class Language(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Language",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Language",
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

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: language codes defined accord. to ISO 639-1. Note: as per ECLASS definition, Expression and representation of thoughts, information, feelings, ideas through characters."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class TimeZone(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"TimeZone",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/TimeZone",
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

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: notation accord. to ISO 8601 Note: for time in UTC the zone designator “Z” is to be used"
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class CityTown(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"CityTown",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO132#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class Company(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Company",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAW001#001",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class Department(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Department",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO127#003",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class Phone(aas.SubmodelElementCollection):

                class TelephoneNumber(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"TelephoneNumber",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO136#002",
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

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
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

                class TypeOfTelephone(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TypeOfTelephone",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO137#003",
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

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r" enumeration: 0173-1#07-AAS754#001 (office), 0173-1#07-AAS755#001 (office mobile), 0173-1#07-AAS756#001 (secretary), 0173-1#07-AAS757#001 (substitute), 0173-1#07-AAS758#001 (home), 0173-1#07-AAS759#001 (private mobile)"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                class AvailableTime(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"AvailableTime",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
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
                    telephoneNumber: Union[aas.LangStringSet, TelephoneNumber],
                    typeOfTelephone: Optional[Union[str, TypeOfTelephone]] = None,
                    availableTime: Optional[
                        Union[aas.LangStringSet, AvailableTime]
                    ] = None,
                    id_short: Optional[str] = r"Phone",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Phone",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if telephoneNumber is not None and not isinstance(
                        telephoneNumber, aas.SubmodelElement
                    ):
                        telephoneNumber = self.TelephoneNumber(telephoneNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfTelephone is not None and not isinstance(
                        typeOfTelephone, aas.SubmodelElement
                    ):
                        typeOfTelephone = self.TypeOfTelephone(typeOfTelephone)

                    # Build a submodel element if a raw value was passed in the argument

                    if availableTime is not None and not isinstance(
                        availableTime, aas.SubmodelElement
                    ):
                        availableTime = self.AvailableTime(availableTime)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [telephoneNumber, typeOfTelephone, availableTime]:
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

            class Fax(aas.SubmodelElementCollection):

                class FaxNumber(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"FaxNumber",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO195#002",
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

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
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

                class TypeOfFaxNumber(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TypeOfFaxNumber",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO196#003",
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

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"enumeration: 0173-1#07-AAS754#001 (office), 0173-1#07-AAS756#001 (secretary), 0173-1#07-AAS758#001 (home)"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                    faxNumber: Union[aas.LangStringSet, FaxNumber],
                    typeOfFaxNumber: Optional[Union[str, TypeOfFaxNumber]] = None,
                    id_short: Optional[str] = r"Fax",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAQ834#005",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if faxNumber is not None and not isinstance(
                        faxNumber, aas.SubmodelElement
                    ):
                        faxNumber = self.FaxNumber(faxNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfFaxNumber is not None and not isinstance(
                        typeOfFaxNumber, aas.SubmodelElement
                    ):
                        typeOfFaxNumber = self.TypeOfFaxNumber(typeOfFaxNumber)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [faxNumber, typeOfFaxNumber]:
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

            class Email(aas.SubmodelElementCollection):

                class EmailAddress(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"EmailAddress",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO198#002",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                class PublicKey(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"PublicKey",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO200#002",
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

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
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

                class TypeOfEmailAddress(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TypeOfEmailAddress",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO199#003",
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

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"enumeration: 0173-1#07-AAS754#001 (office), 0173-1#07-AAS756#001 (secretary), 0173-1#07-AAS757#001 (substitute), 0173-1#07-AAS758#001 (home)"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                class TypeOfPublicKey(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"TypeOfPublicKey",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO201#002",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
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
                    emailAddress: Union[str, EmailAddress],
                    publicKey: Optional[Union[aas.LangStringSet, PublicKey]] = None,
                    typeOfEmailAddress: Optional[Union[str, TypeOfEmailAddress]] = None,
                    typeOfPublicKey: Optional[
                        Union[aas.LangStringSet, TypeOfPublicKey]
                    ] = None,
                    id_short: Optional[str] = r"Email",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAQ836#005",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if emailAddress is not None and not isinstance(
                        emailAddress, aas.SubmodelElement
                    ):
                        emailAddress = self.EmailAddress(emailAddress)

                    # Build a submodel element if a raw value was passed in the argument

                    if publicKey is not None and not isinstance(
                        publicKey, aas.SubmodelElement
                    ):
                        publicKey = self.PublicKey(publicKey)

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfEmailAddress is not None and not isinstance(
                        typeOfEmailAddress, aas.SubmodelElement
                    ):
                        typeOfEmailAddress = self.TypeOfEmailAddress(typeOfEmailAddress)

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfPublicKey is not None and not isinstance(
                        typeOfPublicKey, aas.SubmodelElement
                    ):
                        typeOfPublicKey = self.TypeOfPublicKey(typeOfPublicKey)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        emailAddress,
                        publicKey,
                        typeOfEmailAddress,
                        typeOfPublicKey,
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

            class IPCommunication(aas.SubmodelElementCollection):

                class AddressOfAdditionalLink(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AddressOfAdditionalLink",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAQ326#002",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                class TypeOfCommunication(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TypeOfCommunication",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/IPCommunication/TypeOfCommunication",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                class AvailableTime(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"AvailableTime",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
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
                    addressOfAdditionalLink: Union[str, AddressOfAdditionalLink],
                    typeOfCommunication: Optional[
                        Union[str, TypeOfCommunication]
                    ] = None,
                    availableTime: Optional[
                        Union[aas.LangStringSet, AvailableTime]
                    ] = None,
                    id_short: Optional[str] = r"IPCommunication",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if addressOfAdditionalLink is not None and not isinstance(
                        addressOfAdditionalLink, aas.SubmodelElement
                    ):
                        addressOfAdditionalLink = self.AddressOfAdditionalLink(
                            addressOfAdditionalLink
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfCommunication is not None and not isinstance(
                        typeOfCommunication, aas.SubmodelElement
                    ):
                        typeOfCommunication = self.TypeOfCommunication(
                            typeOfCommunication
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if availableTime is not None and not isinstance(
                        availableTime, aas.SubmodelElement
                    ):
                        availableTime = self.AvailableTime(availableTime)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        addressOfAdditionalLink,
                        typeOfCommunication,
                        availableTime,
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

            class Street(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Street",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO128#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class Zipcode(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Zipcode",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO129#002",
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

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class POBox(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"POBox",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO130#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class ZipCodeOfPOBox(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"ZipCodeOfPOBox",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO131#002",
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

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class StateCounty(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"StateCounty",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO133#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class NameOfContact(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"NameOfContact",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO205#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class FirstName(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"FirstName",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO206#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class MiddleNames(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"MiddleNames",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO207#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class Title(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Title",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO208#003",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class AcademicTitle(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"AcademicTitle",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO209#003",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class FurtherDetailsOfContact(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"FurtherDetailsOfContact",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO210#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
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

            class AddressOfAdditionalLink(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AddressOfAdditionalLink",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAQ326#002",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                roleOfContactPerson: Optional[Union[str, RoleOfContactPerson]] = None,
                nationalCode: Optional[Union[aas.LangStringSet, NationalCode]] = None,
                language: Optional[Iterable[Union[str, Language]]] = None,
                timeZone: Optional[Union[str, TimeZone]] = None,
                cityTown: Optional[Union[aas.LangStringSet, CityTown]] = None,
                company: Optional[Union[aas.LangStringSet, Company]] = None,
                department: Optional[Union[aas.LangStringSet, Department]] = None,
                phone: Optional[Phone] = None,
                fax: Optional[Fax] = None,
                email: Optional[Email] = None,
                iPCommunication: Optional[Iterable[IPCommunication]] = None,
                street: Optional[Union[aas.LangStringSet, Street]] = None,
                zipcode: Optional[Union[aas.LangStringSet, Zipcode]] = None,
                pOBox: Optional[Union[aas.LangStringSet, POBox]] = None,
                zipCodeOfPOBox: Optional[
                    Union[aas.LangStringSet, ZipCodeOfPOBox]
                ] = None,
                stateCounty: Optional[Union[aas.LangStringSet, StateCounty]] = None,
                nameOfContact: Optional[Union[aas.LangStringSet, NameOfContact]] = None,
                firstName: Optional[Union[aas.LangStringSet, FirstName]] = None,
                middleNames: Optional[Union[aas.LangStringSet, MiddleNames]] = None,
                title: Optional[Union[aas.LangStringSet, Title]] = None,
                academicTitle: Optional[Union[aas.LangStringSet, AcademicTitle]] = None,
                furtherDetailsOfContact: Optional[
                    Union[aas.LangStringSet, FurtherDetailsOfContact]
                ] = None,
                addressOfAdditionalLink: Optional[
                    Union[str, AddressOfAdditionalLink]
                ] = None,
                id_short: Optional[str] = r"Contact",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if roleOfContactPerson is not None and not isinstance(
                    roleOfContactPerson, aas.SubmodelElement
                ):
                    roleOfContactPerson = self.RoleOfContactPerson(roleOfContactPerson)

                # Build a submodel element if a raw value was passed in the argument

                if nationalCode is not None and not isinstance(
                    nationalCode, aas.SubmodelElement
                ):
                    nationalCode = self.NationalCode(nationalCode)

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if language:
                    language = [
                        i if isinstance(i, aas.SubmodelElement) else self.Language(i)
                        for i in language
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if timeZone is not None and not isinstance(
                    timeZone, aas.SubmodelElement
                ):
                    timeZone = self.TimeZone(timeZone)

                # Build a submodel element if a raw value was passed in the argument

                if cityTown is not None and not isinstance(
                    cityTown, aas.SubmodelElement
                ):
                    cityTown = self.CityTown(cityTown)

                # Build a submodel element if a raw value was passed in the argument

                if company is not None and not isinstance(company, aas.SubmodelElement):
                    company = self.Company(company)

                # Build a submodel element if a raw value was passed in the argument

                if department is not None and not isinstance(
                    department, aas.SubmodelElement
                ):
                    department = self.Department(department)

                # A str would be split into its characters
                if isinstance(iPCommunication, str):
                    raise TypeError("iPCommunication takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if street is not None and not isinstance(street, aas.SubmodelElement):
                    street = self.Street(street)

                # Build a submodel element if a raw value was passed in the argument

                if zipcode is not None and not isinstance(zipcode, aas.SubmodelElement):
                    zipcode = self.Zipcode(zipcode)

                # Build a submodel element if a raw value was passed in the argument

                if pOBox is not None and not isinstance(pOBox, aas.SubmodelElement):
                    pOBox = self.POBox(pOBox)

                # Build a submodel element if a raw value was passed in the argument

                if zipCodeOfPOBox is not None and not isinstance(
                    zipCodeOfPOBox, aas.SubmodelElement
                ):
                    zipCodeOfPOBox = self.ZipCodeOfPOBox(zipCodeOfPOBox)

                # Build a submodel element if a raw value was passed in the argument

                if stateCounty is not None and not isinstance(
                    stateCounty, aas.SubmodelElement
                ):
                    stateCounty = self.StateCounty(stateCounty)

                # Build a submodel element if a raw value was passed in the argument

                if nameOfContact is not None and not isinstance(
                    nameOfContact, aas.SubmodelElement
                ):
                    nameOfContact = self.NameOfContact(nameOfContact)

                # Build a submodel element if a raw value was passed in the argument

                if firstName is not None and not isinstance(
                    firstName, aas.SubmodelElement
                ):
                    firstName = self.FirstName(firstName)

                # Build a submodel element if a raw value was passed in the argument

                if middleNames is not None and not isinstance(
                    middleNames, aas.SubmodelElement
                ):
                    middleNames = self.MiddleNames(middleNames)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if academicTitle is not None and not isinstance(
                    academicTitle, aas.SubmodelElement
                ):
                    academicTitle = self.AcademicTitle(academicTitle)

                # Build a submodel element if a raw value was passed in the argument

                if furtherDetailsOfContact is not None and not isinstance(
                    furtherDetailsOfContact, aas.SubmodelElement
                ):
                    furtherDetailsOfContact = self.FurtherDetailsOfContact(
                        furtherDetailsOfContact
                    )

                # Build a submodel element if a raw value was passed in the argument

                if addressOfAdditionalLink is not None and not isinstance(
                    addressOfAdditionalLink, aas.SubmodelElement
                ):
                    addressOfAdditionalLink = self.AddressOfAdditionalLink(
                        addressOfAdditionalLink
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    roleOfContactPerson,
                    nationalCode,
                    language,
                    timeZone,
                    cityTown,
                    company,
                    department,
                    phone,
                    fax,
                    email,
                    iPCommunication,
                    street,
                    zipcode,
                    pOBox,
                    zipCodeOfPOBox,
                    stateCounty,
                    nameOfContact,
                    firstName,
                    middleNames,
                    title,
                    academicTitle,
                    furtherDetailsOfContact,
                    addressOfAdditionalLink,
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
            installationDate: Union[xsd.Date, InstallationDate],
            serialNumber: Optional[Union[str, SerialNumber]] = None,
            inventoryTag: Optional[Union[str, InventoryTag]] = None,
            instanceName: Optional[Union[str, InstanceName]] = None,
            installedVersion: Optional[Union[str, InstalledVersion]] = None,
            installationPath: Optional[Union[xsd.AnyURI, InstallationPath]] = None,
            installationSource: Optional[Union[xsd.AnyURI, InstallationSource]] = None,
            installedOnArchitecture: Optional[
                Union[str, InstalledOnArchitecture]
            ] = None,
            installedOnOS: Optional[Union[str, InstalledOnOS]] = None,
            installedOnHost: Optional[Union[str, InstalledOnHost]] = None,
            installedModules: Optional[InstalledModules] = None,
            configurationPaths: Optional[ConfigurationPaths] = None,
            sLAInformation: Optional[Union[str, SLAInformation]] = None,
            contact: Optional[Iterable[Contact]] = None,
            id_short: Optional[str] = r"SoftwareNameplateInstance",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateInstance",
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

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Multiplicity",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if serialNumber is not None and not isinstance(
                serialNumber, aas.SubmodelElement
            ):
                serialNumber = self.SerialNumber(serialNumber)

            # Build a submodel element if a raw value was passed in the argument

            if inventoryTag is not None and not isinstance(
                inventoryTag, aas.SubmodelElement
            ):
                inventoryTag = self.InventoryTag(inventoryTag)

            # Build a submodel element if a raw value was passed in the argument

            if instanceName is not None and not isinstance(
                instanceName, aas.SubmodelElement
            ):
                instanceName = self.InstanceName(instanceName)

            # Build a submodel element if a raw value was passed in the argument

            if installedVersion is not None and not isinstance(
                installedVersion, aas.SubmodelElement
            ):
                installedVersion = self.InstalledVersion(installedVersion)

            # Build a submodel element if a raw value was passed in the argument

            if installationDate is not None and not isinstance(
                installationDate, aas.SubmodelElement
            ):
                installationDate = self.InstallationDate(installationDate)

            # Build a submodel element if a raw value was passed in the argument

            if installationPath is not None and not isinstance(
                installationPath, aas.SubmodelElement
            ):
                installationPath = self.InstallationPath(installationPath)

            # Build a submodel element if a raw value was passed in the argument

            if installationSource is not None and not isinstance(
                installationSource, aas.SubmodelElement
            ):
                installationSource = self.InstallationSource(installationSource)

            # Build a submodel element if a raw value was passed in the argument

            if installedOnArchitecture is not None and not isinstance(
                installedOnArchitecture, aas.SubmodelElement
            ):
                installedOnArchitecture = self.InstalledOnArchitecture(
                    installedOnArchitecture
                )

            # Build a submodel element if a raw value was passed in the argument

            if installedOnOS is not None and not isinstance(
                installedOnOS, aas.SubmodelElement
            ):
                installedOnOS = self.InstalledOnOS(installedOnOS)

            # Build a submodel element if a raw value was passed in the argument

            if installedOnHost is not None and not isinstance(
                installedOnHost, aas.SubmodelElement
            ):
                installedOnHost = self.InstalledOnHost(installedOnHost)

            # Build a submodel element if a raw value was passed in the argument

            if sLAInformation is not None and not isinstance(
                sLAInformation, aas.SubmodelElement
            ):
                sLAInformation = self.SLAInformation(sLAInformation)

            # A str would be split into its characters
            if isinstance(contact, str):
                raise TypeError("contact takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                serialNumber,
                inventoryTag,
                instanceName,
                installedVersion,
                installationDate,
                installationPath,
                installationSource,
                installedOnArchitecture,
                installedOnOS,
                installedOnHost,
                installedModules,
                configurationPaths,
                sLAInformation,
                contact,
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
        softwareNameplateType: Optional[SoftwareNameplateType] = None,
        softwareNameplateInstance: Optional[SoftwareNameplateInstance] = None,
        id_short: Optional[str] = r"SoftwareNameplate",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/SoftwareNameplate/1/0",
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
                    r"en": r"Contains the nameplate information attached to the software product"
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"0",
                revision=r"15",
                creator=None,
                template_id=None,
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = (
                aas.Qualifier(
                    type_=r"FormTitle",
                    value_type=str,
                    value=r"A template for a software nameplate submodel, v0.15",
                    value_id=None,
                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
                aas.Qualifier(
                    type_=r"FormInfo",
                    value_type=str,
                    value=r"This form is based on Version 0.15",
                    value_id=None,
                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
                aas.Qualifier(
                    type_=r"FormUrl",
                    value_type=str,
                    value=r"https://admin-shell.io/idta/SoftwareNameplate_15",
                    value_id=None,
                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
            )

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [softwareNameplateType, softwareNameplateInstance]:
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
