from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class PowerDriveTrainSizing(aas.Submodel):

    class SizingProjectInformation(aas.SubmodelElementCollection):

        class ClientName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ClientName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ClientName/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class SizingProjectName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingProjectName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectName/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class SizingProjectAxisReference(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingProjectAxisReference",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectAxisReference/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class SizingProjectDescription(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"SizingProjectDescription",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectDescription/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class SizingProjectLink(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingProjectLink",
                content_type: Optional[str] = r"text/xml",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectLink/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class SizingToolName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingToolName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingToolName/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class DateCreated(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"DateCreated",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DateCreated/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class DateChanged(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"DateChanged",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DateChanged/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class ContactInformation(aas.SubmodelElementCollection):

            def __init__(
                self,
                id_short: Optional[str] = r"ContactInformation",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in []:
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

        class AmlDriveConfigVersion(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"AmlDriveConfigVersion",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmlDriveConfigVersion/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
            clientName: Union[str, ClientName],
            sizingProjectName: Union[str, SizingProjectName],
            sizingProjectLink: Iterable[SizingProjectLink],
            sizingToolName: Union[str, SizingToolName],
            dateCreated: Union[xsd.DateTime, DateCreated],
            dateChanged: Union[xsd.DateTime, DateChanged],
            contactInformation: Iterable[ContactInformation],
            sizingProjectAxisReference: Optional[
                Union[str, SizingProjectAxisReference]
            ] = None,
            sizingProjectDescription: Optional[
                Union[aas.LangStringSet, SizingProjectDescription]
            ] = None,
            amlDriveConfigVersion: Optional[Union[str, AmlDriveConfigVersion]] = None,
            id_short: Optional[str] = r"SizingProjectInformation",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectInformation1/0",
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
                    dict_={
                        r"de": r"Auslegungsprojektinformationen",
                        r"en": r"Sizing project information",
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            # Build a submodel element if a raw value was passed in the argument

            if clientName is not None and not isinstance(
                clientName, aas.SubmodelElement
            ):
                clientName = self.ClientName(clientName)

            # Build a submodel element if a raw value was passed in the argument

            if sizingProjectName is not None and not isinstance(
                sizingProjectName, aas.SubmodelElement
            ):
                sizingProjectName = self.SizingProjectName(sizingProjectName)

            # Build a submodel element if a raw value was passed in the argument

            if sizingProjectAxisReference is not None and not isinstance(
                sizingProjectAxisReference, aas.SubmodelElement
            ):
                sizingProjectAxisReference = self.SizingProjectAxisReference(
                    sizingProjectAxisReference
                )

            # Build a submodel element if a raw value was passed in the argument

            if sizingProjectDescription is not None and not isinstance(
                sizingProjectDescription, aas.SubmodelElement
            ):
                sizingProjectDescription = self.SizingProjectDescription(
                    sizingProjectDescription
                )

            # A str would be split into its characters
            if isinstance(sizingProjectLink, str):
                raise TypeError("sizingProjectLink takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if sizingToolName is not None and not isinstance(
                sizingToolName, aas.SubmodelElement
            ):
                sizingToolName = self.SizingToolName(sizingToolName)

            # Build a submodel element if a raw value was passed in the argument

            if dateCreated is not None and not isinstance(
                dateCreated, aas.SubmodelElement
            ):
                dateCreated = self.DateCreated(dateCreated)

            # Build a submodel element if a raw value was passed in the argument

            if dateChanged is not None and not isinstance(
                dateChanged, aas.SubmodelElement
            ):
                dateChanged = self.DateChanged(dateChanged)

            # A str would be split into its characters
            if isinstance(contactInformation, str):
                raise TypeError("contactInformation takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if amlDriveConfigVersion is not None and not isinstance(
                amlDriveConfigVersion, aas.SubmodelElement
            ):
                amlDriveConfigVersion = self.AmlDriveConfigVersion(
                    amlDriveConfigVersion
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                clientName,
                sizingProjectName,
                sizingProjectAxisReference,
                sizingProjectDescription,
                sizingProjectLink,
                sizingToolName,
                dateCreated,
                dateChanged,
                contactInformation,
                amlDriveConfigVersion,
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

    class ApplicationRequirements(aas.SubmodelElementCollection):

        class MotionPattern(aas.SubmodelElementCollection):

            class MotionPatternName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MotionPatternName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPatternName/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class MotionPatternSections(aas.SubmodelElementCollection):

                class RotativeSection(aas.SubmodelElementCollection):

                    class FrictionTorque(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"FrictionTorque",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionTorque/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class LeverArmAxialForce(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"LeverArmAxialForce",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class AxialForce(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"AxialForce",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AxialForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class LeverArmRadialForce(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"LeverArmRadialForce",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class RadialForce(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"RadialForce",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RadialForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class MomentOfInertiaOfLoad(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"MomentOfInertiaOfLoad",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MomentOfInertiaOfLoad/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class LoadTorque(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"LoadTorque",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadTorque/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class MetadataRotativeMotionFile(aas.SubmodelElementCollection):

                        class Time(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"Time",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class AngularPosition(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"AngularPosition",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularPosition/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class AngularVelocity(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"AngularVelocity",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularVelocity/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class AngularAcceleration(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"AngularAcceleration",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularAcceleration/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class AngularJerk(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"AngularJerk",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularJerk/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class FrictionTorque(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"FrictionTorque",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionTorque/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class AxialForce(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"AxialForce",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AxialForce/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class RadialForce(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"RadialForce",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"CONSTANT",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RadialForce/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class LoadTorque(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"LoadTorque",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"CONSTANT",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadTorque/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            time: Union[xsd.Long, Time],
                            angularPosition: Union[xsd.Long, AngularPosition],
                            angularVelocity: Union[xsd.Long, AngularVelocity],
                            angularAcceleration: Union[xsd.Long, AngularAcceleration],
                            angularJerk: Optional[Union[xsd.Long, AngularJerk]] = None,
                            frictionTorque: Optional[
                                Union[xsd.Long, FrictionTorque]
                            ] = None,
                            axialForce: Optional[Union[xsd.Long, AxialForce]] = None,
                            radialForce: Optional[Union[xsd.Long, RadialForce]] = None,
                            loadTorque: Optional[Union[xsd.Long, LoadTorque]] = None,
                            id_short: Optional[str] = r"MetadataRotativeMotionFile",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MetadataRotativeMotionFile/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if time is not None and not isinstance(
                                time, aas.SubmodelElement
                            ):
                                time = self.Time(time)

                            # Build a submodel element if a raw value was passed in the argument

                            if angularPosition is not None and not isinstance(
                                angularPosition, aas.SubmodelElement
                            ):
                                angularPosition = self.AngularPosition(angularPosition)

                            # Build a submodel element if a raw value was passed in the argument

                            if angularVelocity is not None and not isinstance(
                                angularVelocity, aas.SubmodelElement
                            ):
                                angularVelocity = self.AngularVelocity(angularVelocity)

                            # Build a submodel element if a raw value was passed in the argument

                            if angularAcceleration is not None and not isinstance(
                                angularAcceleration, aas.SubmodelElement
                            ):
                                angularAcceleration = self.AngularAcceleration(
                                    angularAcceleration
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if angularJerk is not None and not isinstance(
                                angularJerk, aas.SubmodelElement
                            ):
                                angularJerk = self.AngularJerk(angularJerk)

                            # Build a submodel element if a raw value was passed in the argument

                            if frictionTorque is not None and not isinstance(
                                frictionTorque, aas.SubmodelElement
                            ):
                                frictionTorque = self.FrictionTorque(frictionTorque)

                            # Build a submodel element if a raw value was passed in the argument

                            if axialForce is not None and not isinstance(
                                axialForce, aas.SubmodelElement
                            ):
                                axialForce = self.AxialForce(axialForce)

                            # Build a submodel element if a raw value was passed in the argument

                            if radialForce is not None and not isinstance(
                                radialForce, aas.SubmodelElement
                            ):
                                radialForce = self.RadialForce(radialForce)

                            # Build a submodel element if a raw value was passed in the argument

                            if loadTorque is not None and not isinstance(
                                loadTorque, aas.SubmodelElement
                            ):
                                loadTorque = self.LoadTorque(loadTorque)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                time,
                                angularPosition,
                                angularVelocity,
                                angularAcceleration,
                                angularJerk,
                                frictionTorque,
                                axialForce,
                                radialForce,
                                loadTorque,
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

                    class MotionSectionFile(aas.File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"MotionSectionFile",
                            content_type: Optional[str] = r"image/png",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionSectionFile/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                        metadataRotativeMotionFile: MetadataRotativeMotionFile,
                        frictionTorque: Optional[
                            Union[xsd.Long, FrictionTorque]
                        ] = None,
                        leverArmAxialForce: Optional[
                            Union[xsd.Long, LeverArmAxialForce]
                        ] = None,
                        axialForce: Optional[Union[xsd.Long, AxialForce]] = None,
                        leverArmRadialForce: Optional[
                            Union[xsd.Long, LeverArmRadialForce]
                        ] = None,
                        radialForce: Optional[Union[xsd.Long, RadialForce]] = None,
                        momentOfInertiaOfLoad: Optional[
                            Union[xsd.Long, MomentOfInertiaOfLoad]
                        ] = None,
                        loadTorque: Optional[Union[xsd.Long, LoadTorque]] = None,
                        motionSectionFile: Optional[MotionSectionFile] = None,
                        id_short: Optional[str] = r"RotativeSection",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RotativeMotionPatternSection/1/0",
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
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        # Build a submodel element if a raw value was passed in the argument

                        if frictionTorque is not None and not isinstance(
                            frictionTorque, aas.SubmodelElement
                        ):
                            frictionTorque = self.FrictionTorque(frictionTorque)

                        # Build a submodel element if a raw value was passed in the argument

                        if leverArmAxialForce is not None and not isinstance(
                            leverArmAxialForce, aas.SubmodelElement
                        ):
                            leverArmAxialForce = self.LeverArmAxialForce(
                                leverArmAxialForce
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if axialForce is not None and not isinstance(
                            axialForce, aas.SubmodelElement
                        ):
                            axialForce = self.AxialForce(axialForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if leverArmRadialForce is not None and not isinstance(
                            leverArmRadialForce, aas.SubmodelElement
                        ):
                            leverArmRadialForce = self.LeverArmRadialForce(
                                leverArmRadialForce
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if radialForce is not None and not isinstance(
                            radialForce, aas.SubmodelElement
                        ):
                            radialForce = self.RadialForce(radialForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if momentOfInertiaOfLoad is not None and not isinstance(
                            momentOfInertiaOfLoad, aas.SubmodelElement
                        ):
                            momentOfInertiaOfLoad = self.MomentOfInertiaOfLoad(
                                momentOfInertiaOfLoad
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if loadTorque is not None and not isinstance(
                            loadTorque, aas.SubmodelElement
                        ):
                            loadTorque = self.LoadTorque(loadTorque)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            frictionTorque,
                            leverArmAxialForce,
                            axialForce,
                            leverArmRadialForce,
                            radialForce,
                            momentOfInertiaOfLoad,
                            loadTorque,
                            metadataRotativeMotionFile,
                            motionSectionFile,
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

                class LinearSection(aas.SubmodelElementCollection):

                    class FrictionCoefficient(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"FrictionCoefficient",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class FrictionForce(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"FrictionForce",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class CompensationForce(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"CompensationForce",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CompensationForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class LoadMass(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"LoadMass",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadMass/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class LoadSideForce(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"LoadSideForce",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadSideForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class CounterMass(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Long,
                            id_short: Optional[str] = r"CounterMass",
                            value_type: aas.DataTypeDefXsd = xsd.Long,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CounterMass/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class MetadataLinearMotionFile(aas.SubmodelElementCollection):

                        class Time(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"Time",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"VARIABLE",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class Position(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"Position",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Position/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class LinearVelocity(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"LinearVelocity",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearVelocity/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class LinearAcceleration(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"LinearAcceleration",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearAcceleration/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class LinearJerk(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"LinearJerk",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearJerk/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class FrictionForce(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"FrictionForce",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"CONSTANT",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionForce/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class LoadSideForce(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Long,
                                id_short: Optional[str] = r"LoadSideForce",
                                value_type: aas.DataTypeDefXsd = xsd.Long,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadSideForce/1/0",
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
                                            type_=r"Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            time: Union[xsd.Long, Time],
                            position: Union[xsd.Long, Position],
                            linearVelocity: Union[xsd.Long, LinearVelocity],
                            linearAcceleration: Union[xsd.Long, LinearAcceleration],
                            linearJerk: Optional[Union[xsd.Long, LinearJerk]] = None,
                            frictionForce: Optional[
                                Union[xsd.Long, FrictionForce]
                            ] = None,
                            loadSideForce: Optional[
                                Union[xsd.Long, LoadSideForce]
                            ] = None,
                            id_short: Optional[str] = r"MetadataLinearMotionFile",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MetadataLinearMotionFile/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if time is not None and not isinstance(
                                time, aas.SubmodelElement
                            ):
                                time = self.Time(time)

                            # Build a submodel element if a raw value was passed in the argument

                            if position is not None and not isinstance(
                                position, aas.SubmodelElement
                            ):
                                position = self.Position(position)

                            # Build a submodel element if a raw value was passed in the argument

                            if linearVelocity is not None and not isinstance(
                                linearVelocity, aas.SubmodelElement
                            ):
                                linearVelocity = self.LinearVelocity(linearVelocity)

                            # Build a submodel element if a raw value was passed in the argument

                            if linearAcceleration is not None and not isinstance(
                                linearAcceleration, aas.SubmodelElement
                            ):
                                linearAcceleration = self.LinearAcceleration(
                                    linearAcceleration
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if linearJerk is not None and not isinstance(
                                linearJerk, aas.SubmodelElement
                            ):
                                linearJerk = self.LinearJerk(linearJerk)

                            # Build a submodel element if a raw value was passed in the argument

                            if frictionForce is not None and not isinstance(
                                frictionForce, aas.SubmodelElement
                            ):
                                frictionForce = self.FrictionForce(frictionForce)

                            # Build a submodel element if a raw value was passed in the argument

                            if loadSideForce is not None and not isinstance(
                                loadSideForce, aas.SubmodelElement
                            ):
                                loadSideForce = self.LoadSideForce(loadSideForce)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                time,
                                position,
                                linearVelocity,
                                linearAcceleration,
                                linearJerk,
                                frictionForce,
                                loadSideForce,
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

                    class MotionSectionFile(aas.File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"MotionSectionFile",
                            content_type: Optional[str] = r"image/png",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionSectionFile/1/0",
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
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                        metadataLinearMotionFile: MetadataLinearMotionFile,
                        frictionCoefficient: Optional[
                            Union[xsd.Long, FrictionCoefficient]
                        ] = None,
                        frictionForce: Optional[Union[xsd.Long, FrictionForce]] = None,
                        compensationForce: Optional[
                            Union[xsd.Long, CompensationForce]
                        ] = None,
                        loadMass: Optional[Union[xsd.Long, LoadMass]] = None,
                        loadSideForce: Optional[Union[xsd.Long, LoadSideForce]] = None,
                        counterMass: Optional[Union[xsd.Long, CounterMass]] = None,
                        motionSectionFile: Optional[MotionSectionFile] = None,
                        id_short: Optional[str] = r"LinearSection",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearMotionPatternSection/1/0",
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
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        # Build a submodel element if a raw value was passed in the argument

                        if frictionCoefficient is not None and not isinstance(
                            frictionCoefficient, aas.SubmodelElement
                        ):
                            frictionCoefficient = self.FrictionCoefficient(
                                frictionCoefficient
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if frictionForce is not None and not isinstance(
                            frictionForce, aas.SubmodelElement
                        ):
                            frictionForce = self.FrictionForce(frictionForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if compensationForce is not None and not isinstance(
                            compensationForce, aas.SubmodelElement
                        ):
                            compensationForce = self.CompensationForce(
                                compensationForce
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if loadMass is not None and not isinstance(
                            loadMass, aas.SubmodelElement
                        ):
                            loadMass = self.LoadMass(loadMass)

                        # Build a submodel element if a raw value was passed in the argument

                        if loadSideForce is not None and not isinstance(
                            loadSideForce, aas.SubmodelElement
                        ):
                            loadSideForce = self.LoadSideForce(loadSideForce)

                        # Build a submodel element if a raw value was passed in the argument

                        if counterMass is not None and not isinstance(
                            counterMass, aas.SubmodelElement
                        ):
                            counterMass = self.CounterMass(counterMass)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            frictionCoefficient,
                            frictionForce,
                            compensationForce,
                            loadMass,
                            loadSideForce,
                            counterMass,
                            metadataLinearMotionFile,
                            motionSectionFile,
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
                    rotativeSection: Optional[Iterable[RotativeSection]] = None,
                    linearSection: Optional[Iterable[LinearSection]] = None,
                    id_short: Optional[str] = r"MotionPatternSections",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPatternSections/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                    if isinstance(rotativeSection, str):
                        raise TypeError(
                            "rotativeSection takes several elements, got a str"
                        )

                    # A str would be split into its characters
                    if isinstance(linearSection, str):
                        raise TypeError(
                            "linearSection takes several elements, got a str"
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [rotativeSection, linearSection]:
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
                motionPatternSections: MotionPatternSections,
                motionPatternName: Optional[Union[str, MotionPatternName]] = None,
                id_short: Optional[str] = r"MotionPattern",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPattern/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                # Build a submodel element if a raw value was passed in the argument

                if motionPatternName is not None and not isinstance(
                    motionPatternName, aas.SubmodelElement
                ):
                    motionPatternName = self.MotionPatternName(motionPatternName)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [motionPatternName, motionPatternSections]:
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

        class Environmental(aas.SubmodelElementCollection):

            class InstallationAltitude(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InstallationAltitude",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAZ614#003",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class Atex2Gas(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Atex2Gas",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAR865#004",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class Atex2Dust(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Atex2Dust",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAR866#004",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class AmbientTemperatureController(aas.Range):

                def __init__(
                    self,
                    min: str,
                    max: str,
                    id_short: Optional[str] = r"AmbientTemperatureController",
                    value_type: aas.DataTypeDefXsd = str,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmbientTemperatureController/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    super().__init__(
                        min=min,
                        max=max,
                        id_short=id_short,
                        value_type=value_type,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AmbientTemperatureMotor(aas.Range):

                def __init__(
                    self,
                    min: str,
                    max: str,
                    id_short: Optional[str] = r"AmbientTemperatureMotor",
                    value_type: aas.DataTypeDefXsd = str,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmbientTemperatureMotor/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    super().__init__(
                        min=min,
                        max=max,
                        id_short=id_short,
                        value_type=value_type,
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
                installationAltitude: Optional[Union[str, InstallationAltitude]] = None,
                atex2Gas: Optional[Union[str, Atex2Gas]] = None,
                atex2Dust: Optional[Union[str, Atex2Dust]] = None,
                ambientTemperatureController: Optional[
                    Union[Tuple[str, str], AmbientTemperatureController]
                ] = None,
                ambientTemperatureMotor: Optional[
                    Union[Tuple[str, str], AmbientTemperatureMotor]
                ] = None,
                id_short: Optional[str] = r"Environmental",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnvironmentalRequirements/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                # Build a submodel element if a raw value was passed in the argument

                if installationAltitude is not None and not isinstance(
                    installationAltitude, aas.SubmodelElement
                ):
                    installationAltitude = self.InstallationAltitude(
                        installationAltitude
                    )

                # Build a submodel element if a raw value was passed in the argument

                if atex2Gas is not None and not isinstance(
                    atex2Gas, aas.SubmodelElement
                ):
                    atex2Gas = self.Atex2Gas(atex2Gas)

                # Build a submodel element if a raw value was passed in the argument

                if atex2Dust is not None and not isinstance(
                    atex2Dust, aas.SubmodelElement
                ):
                    atex2Dust = self.Atex2Dust(atex2Dust)

                # Build a submodel element if a raw value was passed in the argument

                if ambientTemperatureController is not None and not isinstance(
                    ambientTemperatureController, aas.SubmodelElement
                ):
                    ambientTemperatureController = self.AmbientTemperatureController(
                        min=ambientTemperatureController[0],
                        max=ambientTemperatureController[1],
                    )

                # Build a submodel element if a raw value was passed in the argument

                if ambientTemperatureMotor is not None and not isinstance(
                    ambientTemperatureMotor, aas.SubmodelElement
                ):
                    ambientTemperatureMotor = self.AmbientTemperatureMotor(
                        min=ambientTemperatureMotor[0], max=ambientTemperatureMotor[1]
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    installationAltitude,
                    atex2Gas,
                    atex2Dust,
                    ambientTemperatureController,
                    ambientTemperatureMotor,
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

        class OverallSystemRequirements(aas.SubmodelElementCollection):

            class DcLinkCoupling(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DcLinkCoupling",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DcLinkCoupling/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class BrakePresent(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"BrakePresent",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAE085#007",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class MainsConnection(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MainsConnection",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABF822#003",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class MountingType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MountingType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAH167#006",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class MinSwitchingFrequency(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MinSwitchingFrequency",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAN329#003",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class CoolingType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CoolingType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAE122#007",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class ProtectionType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ProtectionType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAG342#007",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class CertificateApproval(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CertificateApproval",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAB392#018",
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
                            dict_={
                                r"de": r"Zertifikat/Zulassung",
                                r"en": r"Certificate/Approval",
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class SafetyIntegrityLevel(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SafetyIntegrityLevel",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH715#002",
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
                                r"en": r"safety integrity level (SIL) according to IEC 61508"
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                dcLinkCoupling: Optional[Union[str, DcLinkCoupling]] = None,
                brakePresent: Optional[Union[str, BrakePresent]] = None,
                mainsConnection: Optional[Union[str, MainsConnection]] = None,
                mountingType: Optional[Union[str, MountingType]] = None,
                minSwitchingFrequency: Optional[
                    Union[str, MinSwitchingFrequency]
                ] = None,
                coolingType: Optional[Union[str, CoolingType]] = None,
                protectionType: Optional[Union[str, ProtectionType]] = None,
                certificateApproval: Optional[Union[str, CertificateApproval]] = None,
                safetyIntegrityLevel: Optional[Union[str, SafetyIntegrityLevel]] = None,
                id_short: Optional[str] = r"OverallSystemRequirements",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OverallSystemRequirements/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if dcLinkCoupling is not None and not isinstance(
                    dcLinkCoupling, aas.SubmodelElement
                ):
                    dcLinkCoupling = self.DcLinkCoupling(dcLinkCoupling)

                # Build a submodel element if a raw value was passed in the argument

                if brakePresent is not None and not isinstance(
                    brakePresent, aas.SubmodelElement
                ):
                    brakePresent = self.BrakePresent(brakePresent)

                # Build a submodel element if a raw value was passed in the argument

                if mainsConnection is not None and not isinstance(
                    mainsConnection, aas.SubmodelElement
                ):
                    mainsConnection = self.MainsConnection(mainsConnection)

                # Build a submodel element if a raw value was passed in the argument

                if mountingType is not None and not isinstance(
                    mountingType, aas.SubmodelElement
                ):
                    mountingType = self.MountingType(mountingType)

                # Build a submodel element if a raw value was passed in the argument

                if minSwitchingFrequency is not None and not isinstance(
                    minSwitchingFrequency, aas.SubmodelElement
                ):
                    minSwitchingFrequency = self.MinSwitchingFrequency(
                        minSwitchingFrequency
                    )

                # Build a submodel element if a raw value was passed in the argument

                if coolingType is not None and not isinstance(
                    coolingType, aas.SubmodelElement
                ):
                    coolingType = self.CoolingType(coolingType)

                # Build a submodel element if a raw value was passed in the argument

                if protectionType is not None and not isinstance(
                    protectionType, aas.SubmodelElement
                ):
                    protectionType = self.ProtectionType(protectionType)

                # Build a submodel element if a raw value was passed in the argument

                if certificateApproval is not None and not isinstance(
                    certificateApproval, aas.SubmodelElement
                ):
                    certificateApproval = self.CertificateApproval(certificateApproval)

                # Build a submodel element if a raw value was passed in the argument

                if safetyIntegrityLevel is not None and not isinstance(
                    safetyIntegrityLevel, aas.SubmodelElement
                ):
                    safetyIntegrityLevel = self.SafetyIntegrityLevel(
                        safetyIntegrityLevel
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    dcLinkCoupling,
                    brakePresent,
                    mainsConnection,
                    mountingType,
                    minSwitchingFrequency,
                    coolingType,
                    protectionType,
                    certificateApproval,
                    safetyIntegrityLevel,
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

        class UsageProfile(aas.SubmodelElementCollection):

            class CyclesPerMinute(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"CyclesPerMinute",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CyclesPerMinute/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class OperatingHoursPerDay(aas.Property):

                def __init__(
                    self,
                    value: xsd.Long,
                    id_short: Optional[str] = r"OperatingHoursPerDay",
                    value_type: aas.DataTypeDefXsd = xsd.Long,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OperatingHoursPerDay/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            class OperatingDaysPerYear(aas.Property):

                def __init__(
                    self,
                    value: xsd.Long,
                    id_short: Optional[str] = r"OperatingDaysPerYear",
                    value_type: aas.DataTypeDefXsd = xsd.Long,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OperatingDaysPerYear/1/0",
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
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                cyclesPerMinute: Union[int, CyclesPerMinute],
                operatingHoursPerDay: Union[xsd.Long, OperatingHoursPerDay],
                operatingDaysPerYear: Union[xsd.Long, OperatingDaysPerYear],
                id_short: Optional[str] = r"UsageProfile",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/UsageProfile/1/0",
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
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                # Build a submodel element if a raw value was passed in the argument

                if cyclesPerMinute is not None and not isinstance(
                    cyclesPerMinute, aas.SubmodelElement
                ):
                    cyclesPerMinute = self.CyclesPerMinute(cyclesPerMinute)

                # Build a submodel element if a raw value was passed in the argument

                if operatingHoursPerDay is not None and not isinstance(
                    operatingHoursPerDay, aas.SubmodelElement
                ):
                    operatingHoursPerDay = self.OperatingHoursPerDay(
                        operatingHoursPerDay
                    )

                # Build a submodel element if a raw value was passed in the argument

                if operatingDaysPerYear is not None and not isinstance(
                    operatingDaysPerYear, aas.SubmodelElement
                ):
                    operatingDaysPerYear = self.OperatingDaysPerYear(
                        operatingDaysPerYear
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    cyclesPerMinute,
                    operatingHoursPerDay,
                    operatingDaysPerYear,
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
            motionPattern: Optional[MotionPattern] = None,
            environmental: Optional[Environmental] = None,
            overallSystemRequirements: Optional[OverallSystemRequirements] = None,
            usageProfile: Optional[UsageProfile] = None,
            id_short: Optional[str] = r"ApplicationRequirements",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ApplicationRequirements/1/0",
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
                    dict_={
                        r"de": r"Applikationsanforderungen",
                        r"en": r"Application requirements",
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                motionPattern,
                environmental,
                overallSystemRequirements,
                usageProfile,
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

    class TransformationMechanism(aas.SubmodelElementCollection):

        class Fan(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"Fan",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Fan/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Lüfter", r"en": r"Fan"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Pump(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"Pump",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Pump/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Pumpe", r"en": r"Pump"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class RotraryTable(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RotraryTable",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RotraryTable/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"StaticEccentricity",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={r"de": r"Exzentrität", r"en": r"Eccentricity"}
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/StaticEccentricity/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"CentroidAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Mittelpunktswinkel",
                                    r"en": r"Centroid angle",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CentroidAngle/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Drehtisch", r"en": r"Rotrary table"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ChainConveyor(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"ChainConveyor",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ChainConveyor/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrictionCoefficient",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Reibungskoeffizient",
                                    r"en": r"Coefficient of friction",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FeedConstant",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Vorschubkonstante",
                                    r"en": r"Feed Constant",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Kettenförderer", r"en": r"Chain conveyor"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class BeltConveyor(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"BeltConveyor",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/BeltConveyor/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrictionCoefficient",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Reibungskoeffizient",
                                    r"en": r"Coefficient of friction",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FeedConstant",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Vorschubkonstante",
                                    r"en": r"Feed Constant",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Bandförderer", r"en": r"Belt conveyor"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class RollerConveyor(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RollerConveyor",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RollerConveyor/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrictionCoefficient",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Reibungskoeffizient",
                                    r"en": r"Coefficient of friction",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FeedConstant",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Vorschubkonstante",
                                    r"en": r"Feed Constant",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Rollenbahn", r"en": r"Roller conveyor"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class BeltDrive(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"BeltDrive",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/BeltDrive/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrictionCoefficient",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Reibungskoeffizient",
                                    r"en": r"Coefficient of friction",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FeedConstant",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Vorschubkonstante",
                                    r"en": r"Feed Constant",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Riemenantrieb", r"en": r"Belt drive"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class TravelingDrive(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"TravelingDrive",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/TravelingDrive/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrictionCoefficient",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Reibungskoeffizient",
                                    r"en": r"Coefficient of friction",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FeedConstant",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Vorschubkonstante",
                                    r"en": r"Feed Constant",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Fahrender Antrieb", r"en": r"Traveling drive"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class RackDrive(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RackDrive",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RackDrive/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrictionCoefficient",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Reibungskoeffizient",
                                    r"en": r"Coefficient of friction",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FeedConstant",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Vorschubkonstante",
                                    r"en": r"Feed Constant",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"DiameterPinion",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Durchmesser Ritzel",
                                    r"en": r"Diameter of pinion",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DiameterPinion/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"HelixAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Schrägungswinkel der Verzahnung",
                                    r"en": r"Helix angle of the toothing",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/HelixAngle/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MovingPart",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={r"de": r"Bewegtes Teil", r"en": r"Moving part"}
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RackMovingPart/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Zahnstangenapplikation", r"en": r"Rack drive"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class SpindleDrive(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"SpindleDrive",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SpindleDrive/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"Efficiency",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InertiaMotorSide",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmAxialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"LeverArmRadialForce",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Hebelarm Axialkraft",
                                    r"en": r"Lever arm axial force",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"NoLoadTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Leerlaufdrehmoment",
                                    r"en": r"No-load Torque",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InclinationAngle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrictionCoefficient",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Reibungskoeffizient",
                                    r"en": r"Coefficient of friction",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FeedConstant",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Vorschubkonstante",
                                    r"en": r"Feed Constant",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Spindelantrieb", r"en": r"Spindle drive"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
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
            fan: Optional[Fan] = None,
            pump: Optional[Pump] = None,
            rotraryTable: Optional[RotraryTable] = None,
            chainConveyor: Optional[ChainConveyor] = None,
            beltConveyor: Optional[BeltConveyor] = None,
            rollerConveyor: Optional[RollerConveyor] = None,
            beltDrive: Optional[BeltDrive] = None,
            travelingDrive: Optional[TravelingDrive] = None,
            rackDrive: Optional[RackDrive] = None,
            spindleDrive: Optional[SpindleDrive] = None,
            id_short: Optional[str] = r"TransformationMechanism",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/TransformationMechanism/1/0",
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
                    dict_={
                        r"de": r"Transformationsmechanismen",
                        r"en": r"Transformation mechanism",
                    }
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"All application mechanisms are listed in the submodel template - note that only one application mechanism can be selected in the design project instance."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                fan,
                pump,
                rotraryTable,
                chainConveyor,
                beltConveyor,
                rollerConveyor,
                beltDrive,
                travelingDrive,
                rackDrive,
                spindleDrive,
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

    class SizingResult(aas.SubmodelElementCollection):

        class OverallSystem(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"OverallSystem",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.CO_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OverallSystem/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"ManufacturerName",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAO677#002",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ManufacturerArticleNumber",
                            value_type=str,
                            value=r"-",
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAO676#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.MultiLanguageProperty(
                            id_short=r"ManufacturerProductDesignation",
                            value=aas.MultiLanguageTextType(
                                dict_={r"en": r"ManufacturerProductDesignation"}
                            ),
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAW338#001",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ManufacturerOrderCode",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r" 0173-1#02-AAO227#002",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ExternalMomentOfInertia",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ExternalMomentOfInertia/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"InternalMomentOfIntertia",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InternalMomentOfInertia/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MassInertiaRatio",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MassInertiaRatio/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"DecelerationForEmergencyStop",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DecelerationForEmergencyStop/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"CurrentForEmergencyStop",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CurrentForEmergencyStop/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"DisplacementDuringEmergencyStop",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DisplacementDuringEmergencyStop/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"EnergyConsumtionPerCycle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Gesamtsystem", r"en": r"Overall system"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class MainComponent(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"MainComponent",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.CO_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MainComponent/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"MainComponentType",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Typ der Hauptkomponente",
                                    r"en": r"Main component type",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MainComponentType/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"OneToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ManufacturerName",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAO677#002",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ManufacturerArticleNumber",
                            value_type=str,
                            value=r"5001xxxx-xx-x",
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAO676#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.MultiLanguageProperty(
                            id_short=r"ManufacturerProductDesignation",
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAW338#001",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ManufacturerOrderCode",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r" 0173-1#02-AAO227#002",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxCurrentUtilizationPercentage",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxCurrentUtilizationPercentage/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxCurrentUtilization",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxCurrentUtilization/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxThermalUtilizationPercentage",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxThermalUtilizationPercentage/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxThermalUtilization",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxThermalUtilization/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"AveragePowerLosses",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AveragePowerLosses/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"AverageRegenerativePowerDcLink",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageRegenerativePowerDcLink/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxRegenerativePowerDcLink",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRegenerativePowerDcLink/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"AverageFeedInPowerDcLink",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageFeedInPowerDcLink/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"AverageFeedInPowerMains",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"CONSTANT",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageFeedInPowerMains/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxFeedInPowerMains",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxFeedInPowerMains/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ContinuousCurrent",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ContinuousCurrent/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"RmsOfPower",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RmsOfPower/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxTorqueUtilizationPercentage",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxTorqueUtilizationPercentage/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxTorqueUtilization",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxTorqueUtilization/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxRotationSpeedUtilizationPercentage",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRotationSpeedUtilizationPercentage/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MaxRotationSpeedUtilization",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"CONSTANT",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRotationSpeedUtilization/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"EffectiveUtilization",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"CONSTANT",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EffectiveUtilization/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"CalculatedServiceLife",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CalculatedServiceLife/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"MassInertiaRatio",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MassInertiaRatio/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"FrequencyAtMaxSpeed",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrequencyAtMaxSpeed/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"PowerInRegenerativeOperation",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/PowerInRegenerativeOperation/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"PowerInMotorOperation",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/PowerInMotorOperation/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"RmsOfMotorTorque",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RmsOfMotorTorque/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"EnergyConsumtionPerCycle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Hauptkomponente", r"en": r"Main component"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class OtherComponent(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"OtherComponent",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.CO_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = None,
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OtherComponent/1/0",
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

                if statement is None:
                    statement = (
                        aas.Property(
                            id_short=r"ManufacturerName",
                            value_type=str,
                            value=r"Machine Builder GmbH",
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAO677#002",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ManufacturerArticleNumber",
                            value_type=str,
                            value=r"-",
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAO676#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.MultiLanguageProperty(
                            id_short=r"ManufacturerProductDesignation",
                            value=aas.MultiLanguageTextType(
                                dict_={r"en": r"ManufacturerProductDesignation"}
                            ),
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAW338#001",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"ManufacturerOrderCode",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r" 0173-1#02-AAO227#002",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"QuantityOfParts",
                            value_type=int,
                            value=None,
                            value_id=None,
                            display_name=aas.MultiLanguageNameType(
                                dict_={
                                    r"de": r"Anzahl Einzelteile",
                                    r"en": r"Quantity of parts",
                                }
                            ),
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/QuantityOfParts/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"BulkCount",
                            value_type=xsd.UnsignedLong,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        aas.Property(
                            id_short=r"EnergyConsumtionPerCycle",
                            value_type=xsd.Long,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=r"PARAMETER",
                            description=None,
                            semantic_id=aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    )

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Komponente", r"en": r"Component"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                super().__init__(
                    id_short=id_short,
                    entity_type=entity_type,
                    statement=statement,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Messages(aas.SubmodelElementCollection):

            class Message(aas.SubmodelElementCollection):

                class CriticalityOfMessage(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"CriticalityOfMessage",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CriticalityOfMessage/1/0",
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
                                dict_={
                                    r"de": r"Kritikalität der Meldung",
                                    r"en": r"Criticality of message",
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                class MessageText(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"MessageText",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MessageText/1/0",
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
                                dict_={
                                    r"de": r"Nachrichtentext",
                                    r"en": r"Message text",
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                    criticalityOfMessage: Union[str, CriticalityOfMessage],
                    messageText: Union[aas.LangStringSet, MessageText],
                    id_short: Optional[str] = r"Message",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Message/1/0",
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
                            dict_={r"de": r"Nachricht", r"en": r"Message"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    # Build a submodel element if a raw value was passed in the argument

                    if criticalityOfMessage is not None and not isinstance(
                        criticalityOfMessage, aas.SubmodelElement
                    ):
                        criticalityOfMessage = self.CriticalityOfMessage(
                            criticalityOfMessage
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if messageText is not None and not isinstance(
                        messageText, aas.SubmodelElement
                    ):
                        messageText = self.MessageText(messageText)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [criticalityOfMessage, messageText]:
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
                message: Optional[Iterable[Message]] = None,
                id_short: Optional[str] = r"Messages",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Messages/1/0",
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
                        dict_={r"de": r"Nachrichten", r"en": r"Messages"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                if isinstance(message, str):
                    raise TypeError("message takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [message]:
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

        class TextStatement(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"TextStatement",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/TextStatement/1/0",
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
                        dict_={r"de": r"Textaussage", r"en": r"Text statement"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
            messages: Messages,
            overallSystem: Optional[OverallSystem] = None,
            mainComponent: Optional[Iterable[MainComponent]] = None,
            otherComponent: Optional[Iterable[OtherComponent]] = None,
            textStatement: Optional[Union[aas.LangStringSet, TextStatement]] = None,
            id_short: Optional[str] = r"SizingResult",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingResult/1/0",
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
                    dict_={r"de": r"Auslegungsergebnisse", r"en": r"Sizing result"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
            if isinstance(mainComponent, str):
                raise TypeError("mainComponent takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(otherComponent, str):
                raise TypeError("otherComponent takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if textStatement is not None and not isinstance(
                textStatement, aas.SubmodelElement
            ):
                textStatement = self.TextStatement(textStatement)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                overallSystem,
                mainComponent,
                otherComponent,
                messages,
                textStatement,
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
        sizingProjectInformation: SizingProjectInformation,
        applicationRequirements: ApplicationRequirements,
        transformationMechanism: Optional[TransformationMechanism] = None,
        sizingResult: Optional[SizingResult] = None,
        id_short: Optional[str] = r"PowerDriveTrainSizing",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/1/0",
                ),
            ),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel containing customer specifications for motion and load profile, limitations and requirements of an industrial motion application."
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

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            sizingProjectInformation,
            applicationRequirements,
            transformationMechanism,
            sizingResult,
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
