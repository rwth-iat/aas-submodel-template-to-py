from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class PowerDriveTrainSizing(Submodel):

    class SizingProjectInformation(SubmodelElementCollection):

        class ClientName(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ClientName",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ClientName/1/0",
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

        class SizingProjectName(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingProjectName",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectName/1/0",
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

        class SizingProjectAxisReference(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingProjectAxisReference",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectAxisReference/1/0",
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

        class SizingProjectDescription(MultiLanguageProperty):

            def __init__(
                self,
                value: LangStringSet,
                id_short: Optional[str] = r"SizingProjectDescription",
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectDescription/1/0",
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

        class SizingProjectLink(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingProjectLink",
                content_type: str = r"text/xml",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectLink/1/0",
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

        class SizingToolName(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SizingToolName",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingToolName/1/0",
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

        class DateCreated(Property):

            def __init__(
                self,
                value: datetime,
                id_short: Optional[str] = r"DateCreated",
                value_type: DataTypeDefXsd = datetime,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DateCreated/1/0",
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

        class DateChanged(Property):

            def __init__(
                self,
                value: datetime,
                id_short: Optional[str] = r"DateChanged",
                value_type: DataTypeDefXsd = datetime,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DateChanged/1/0",
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

        class ContactInformation(SubmodelElementCollection):

            def __init__(
                self,
                id_short: Optional[str] = r"ContactInformation",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation",
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

        class AmlDriveConfigVersion(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"AmlDriveConfigVersion",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmlDriveConfigVersion/1/0",
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
            dateCreated: Union[datetime, DateCreated],
            dateChanged: Union[datetime, DateChanged],
            contactInformation: Iterable[ContactInformation],
            sizingProjectAxisReference: Optional[
                Union[str, SizingProjectAxisReference]
            ] = None,
            sizingProjectDescription: Optional[
                Union[LangStringSet, SizingProjectDescription]
            ] = None,
            amlDriveConfigVersion: Optional[Union[str, AmlDriveConfigVersion]] = None,
            id_short: Optional[str] = r"SizingProjectInformation",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={
                    r"de": r"Auslegungsprojektinformationen",
                    r"en": r"Sizing project information",
                }
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = None,
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingProjectInformation1/0",
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
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
            if clientName and not isinstance(clientName, SubmodelElement):
                clientName = self.ClientName(clientName)

            # Build a submodel element if a raw value was passed in the argument
            if sizingProjectName and not isinstance(sizingProjectName, SubmodelElement):
                sizingProjectName = self.SizingProjectName(sizingProjectName)

            # Build a submodel element if a raw value was passed in the argument
            if sizingProjectAxisReference and not isinstance(
                sizingProjectAxisReference, SubmodelElement
            ):
                sizingProjectAxisReference = self.SizingProjectAxisReference(
                    sizingProjectAxisReference
                )

            # Build a submodel element if a raw value was passed in the argument
            if sizingProjectDescription and not isinstance(
                sizingProjectDescription, SubmodelElement
            ):
                sizingProjectDescription = self.SizingProjectDescription(
                    sizingProjectDescription
                )

            # Build a submodel element if a raw value was passed in the argument
            if sizingToolName and not isinstance(sizingToolName, SubmodelElement):
                sizingToolName = self.SizingToolName(sizingToolName)

            # Build a submodel element if a raw value was passed in the argument
            if dateCreated and not isinstance(dateCreated, SubmodelElement):
                dateCreated = self.DateCreated(dateCreated)

            # Build a submodel element if a raw value was passed in the argument
            if dateChanged and not isinstance(dateChanged, SubmodelElement):
                dateChanged = self.DateChanged(dateChanged)

            # Build a submodel element if a raw value was passed in the argument
            if amlDriveConfigVersion and not isinstance(
                amlDriveConfigVersion, SubmodelElement
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

    class ApplicationRequirements(SubmodelElementCollection):

        class MotionPattern(SubmodelElementCollection):

            class MotionPatternName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MotionPatternName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPatternName/1/0",
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

            class MotionPatternSections(SubmodelElementCollection):

                class RotativeSection(SubmodelElementCollection):

                    class FrictionTorque(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"FrictionTorque",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionTorque/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class LeverArmAxialForce(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"LeverArmAxialForce",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
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

                    class AxialForce(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"AxialForce",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AxialForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class LeverArmRadialForce(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"LeverArmRadialForce",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
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

                    class RadialForce(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"RadialForce",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RadialForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class MomentOfInertiaOfLoad(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"MomentOfInertiaOfLoad",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MomentOfInertiaOfLoad/1/0",
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

                    class LoadTorque(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"LoadTorque",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadTorque/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class MetadataRotativeMotionFile(SubmodelElementCollection):

                        class Time(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"Time",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1",
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

                        class AngularPosition(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"AngularPosition",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularPosition/1/0",
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

                        class AngularVelocity(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"AngularVelocity",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularVelocity/1/0",
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

                        class AngularAcceleration(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"AngularAcceleration",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularAcceleration/1/0",
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

                        class AngularJerk(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"AngularJerk",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AngularJerk/1/0",
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

                        class FrictionTorque(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"FrictionTorque",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionTorque/1/0",
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
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

                        class AxialForce(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"AxialForce",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AxialForce/1/0",
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
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

                        class RadialForce(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"RadialForce",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"CONSTANT",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RadialForce/1/0",
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
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

                        class LoadTorque(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"LoadTorque",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"CONSTANT",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadTorque/1/0",
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
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
                            time: Union[Long, Time],
                            angularPosition: Union[Long, AngularPosition],
                            angularVelocity: Union[Long, AngularVelocity],
                            angularAcceleration: Union[Long, AngularAcceleration],
                            angularJerk: Optional[Union[Long, AngularJerk]] = None,
                            frictionTorque: Optional[
                                Union[Long, FrictionTorque]
                            ] = None,
                            axialForce: Optional[Union[Long, AxialForce]] = None,
                            radialForce: Optional[Union[Long, RadialForce]] = None,
                            loadTorque: Optional[Union[Long, LoadTorque]] = None,
                            id_short: Optional[str] = r"MetadataRotativeMotionFile",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MetadataRotativeMotionFile/1/0",
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
                            if time and not isinstance(time, SubmodelElement):
                                time = self.Time(time)

                            # Build a submodel element if a raw value was passed in the argument
                            if angularPosition and not isinstance(
                                angularPosition, SubmodelElement
                            ):
                                angularPosition = self.AngularPosition(angularPosition)

                            # Build a submodel element if a raw value was passed in the argument
                            if angularVelocity and not isinstance(
                                angularVelocity, SubmodelElement
                            ):
                                angularVelocity = self.AngularVelocity(angularVelocity)

                            # Build a submodel element if a raw value was passed in the argument
                            if angularAcceleration and not isinstance(
                                angularAcceleration, SubmodelElement
                            ):
                                angularAcceleration = self.AngularAcceleration(
                                    angularAcceleration
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if angularJerk and not isinstance(
                                angularJerk, SubmodelElement
                            ):
                                angularJerk = self.AngularJerk(angularJerk)

                            # Build a submodel element if a raw value was passed in the argument
                            if frictionTorque and not isinstance(
                                frictionTorque, SubmodelElement
                            ):
                                frictionTorque = self.FrictionTorque(frictionTorque)

                            # Build a submodel element if a raw value was passed in the argument
                            if axialForce and not isinstance(
                                axialForce, SubmodelElement
                            ):
                                axialForce = self.AxialForce(axialForce)

                            # Build a submodel element if a raw value was passed in the argument
                            if radialForce and not isinstance(
                                radialForce, SubmodelElement
                            ):
                                radialForce = self.RadialForce(radialForce)

                            # Build a submodel element if a raw value was passed in the argument
                            if loadTorque and not isinstance(
                                loadTorque, SubmodelElement
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

                    class MotionSectionFile(File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"MotionSectionFile",
                            content_type: str = r"image/png",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionSectionFile/1/0",
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

                    def __init__(
                        self,
                        metadataRotativeMotionFile: MetadataRotativeMotionFile,
                        frictionTorque: Optional[Union[Long, FrictionTorque]] = None,
                        leverArmAxialForce: Optional[
                            Union[Long, LeverArmAxialForce]
                        ] = None,
                        axialForce: Optional[Union[Long, AxialForce]] = None,
                        leverArmRadialForce: Optional[
                            Union[Long, LeverArmRadialForce]
                        ] = None,
                        radialForce: Optional[Union[Long, RadialForce]] = None,
                        momentOfInertiaOfLoad: Optional[
                            Union[Long, MomentOfInertiaOfLoad]
                        ] = None,
                        loadTorque: Optional[Union[Long, LoadTorque]] = None,
                        motionSectionFile: Optional[MotionSectionFile] = None,
                        id_short: Optional[str] = r"RotativeSection",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RotativeMotionPatternSection/1/0",
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
                                    value=r"ZeroToMany",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        if frictionTorque and not isinstance(
                            frictionTorque, SubmodelElement
                        ):
                            frictionTorque = self.FrictionTorque(frictionTorque)

                        # Build a submodel element if a raw value was passed in the argument
                        if leverArmAxialForce and not isinstance(
                            leverArmAxialForce, SubmodelElement
                        ):
                            leverArmAxialForce = self.LeverArmAxialForce(
                                leverArmAxialForce
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if axialForce and not isinstance(axialForce, SubmodelElement):
                            axialForce = self.AxialForce(axialForce)

                        # Build a submodel element if a raw value was passed in the argument
                        if leverArmRadialForce and not isinstance(
                            leverArmRadialForce, SubmodelElement
                        ):
                            leverArmRadialForce = self.LeverArmRadialForce(
                                leverArmRadialForce
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if radialForce and not isinstance(radialForce, SubmodelElement):
                            radialForce = self.RadialForce(radialForce)

                        # Build a submodel element if a raw value was passed in the argument
                        if momentOfInertiaOfLoad and not isinstance(
                            momentOfInertiaOfLoad, SubmodelElement
                        ):
                            momentOfInertiaOfLoad = self.MomentOfInertiaOfLoad(
                                momentOfInertiaOfLoad
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if loadTorque and not isinstance(loadTorque, SubmodelElement):
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

                class LinearSection(SubmodelElementCollection):

                    class FrictionCoefficient(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"FrictionCoefficient",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
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

                    class FrictionForce(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"FrictionForce",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class CompensationForce(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"CompensationForce",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CompensationForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class LoadMass(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"LoadMass",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadMass/1/0",
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

                    class LoadSideForce(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"LoadSideForce",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadSideForce/1/0",
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
                                        type_=r"Note",
                                        value_type=str,
                                        value=r"if variable in the segment, then do not use it here",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class CounterMass(Property):

                        def __init__(
                            self,
                            value: Long,
                            id_short: Optional[str] = r"CounterMass",
                            value_type: DataTypeDefXsd = Long,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CounterMass/1/0",
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

                    class MetadataLinearMotionFile(SubmodelElementCollection):

                        class Time(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"Time",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"VARIABLE",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1",
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

                        class Position(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"Position",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Position/1/0",
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

                        class LinearVelocity(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"LinearVelocity",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearVelocity/1/0",
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

                        class LinearAcceleration(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"LinearAcceleration",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearAcceleration/1/0",
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

                        class LinearJerk(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"LinearJerk",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearJerk/1/0",
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

                        class FrictionForce(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"FrictionForce",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"CONSTANT",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionForce/1/0",
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
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

                        class LoadSideForce(Property):

                            def __init__(
                                self,
                                value: Long,
                                id_short: Optional[str] = r"LoadSideForce",
                                value_type: DataTypeDefXsd = Long,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LoadSideForce/1/0",
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
                                            type_=r"Note",
                                            value_type=str,
                                            value=r"if static in the segment, then do not use it here",
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
                            time: Union[Long, Time],
                            position: Union[Long, Position],
                            linearVelocity: Union[Long, LinearVelocity],
                            linearAcceleration: Union[Long, LinearAcceleration],
                            linearJerk: Optional[Union[Long, LinearJerk]] = None,
                            frictionForce: Optional[Union[Long, FrictionForce]] = None,
                            loadSideForce: Optional[Union[Long, LoadSideForce]] = None,
                            id_short: Optional[str] = r"MetadataLinearMotionFile",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MetadataLinearMotionFile/1/0",
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
                            if time and not isinstance(time, SubmodelElement):
                                time = self.Time(time)

                            # Build a submodel element if a raw value was passed in the argument
                            if position and not isinstance(position, SubmodelElement):
                                position = self.Position(position)

                            # Build a submodel element if a raw value was passed in the argument
                            if linearVelocity and not isinstance(
                                linearVelocity, SubmodelElement
                            ):
                                linearVelocity = self.LinearVelocity(linearVelocity)

                            # Build a submodel element if a raw value was passed in the argument
                            if linearAcceleration and not isinstance(
                                linearAcceleration, SubmodelElement
                            ):
                                linearAcceleration = self.LinearAcceleration(
                                    linearAcceleration
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if linearJerk and not isinstance(
                                linearJerk, SubmodelElement
                            ):
                                linearJerk = self.LinearJerk(linearJerk)

                            # Build a submodel element if a raw value was passed in the argument
                            if frictionForce and not isinstance(
                                frictionForce, SubmodelElement
                            ):
                                frictionForce = self.FrictionForce(frictionForce)

                            # Build a submodel element if a raw value was passed in the argument
                            if loadSideForce and not isinstance(
                                loadSideForce, SubmodelElement
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

                    class MotionSectionFile(File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"MotionSectionFile",
                            content_type: str = r"image/png",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionSectionFile/1/0",
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

                    def __init__(
                        self,
                        metadataLinearMotionFile: MetadataLinearMotionFile,
                        frictionCoefficient: Optional[
                            Union[Long, FrictionCoefficient]
                        ] = None,
                        frictionForce: Optional[Union[Long, FrictionForce]] = None,
                        compensationForce: Optional[
                            Union[Long, CompensationForce]
                        ] = None,
                        loadMass: Optional[Union[Long, LoadMass]] = None,
                        loadSideForce: Optional[Union[Long, LoadSideForce]] = None,
                        counterMass: Optional[Union[Long, CounterMass]] = None,
                        motionSectionFile: Optional[MotionSectionFile] = None,
                        id_short: Optional[str] = r"LinearSection",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LinearMotionPatternSection/1/0",
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
                                    value=r"ZeroToMany",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        if frictionCoefficient and not isinstance(
                            frictionCoefficient, SubmodelElement
                        ):
                            frictionCoefficient = self.FrictionCoefficient(
                                frictionCoefficient
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if frictionForce and not isinstance(
                            frictionForce, SubmodelElement
                        ):
                            frictionForce = self.FrictionForce(frictionForce)

                        # Build a submodel element if a raw value was passed in the argument
                        if compensationForce and not isinstance(
                            compensationForce, SubmodelElement
                        ):
                            compensationForce = self.CompensationForce(
                                compensationForce
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if loadMass and not isinstance(loadMass, SubmodelElement):
                            loadMass = self.LoadMass(loadMass)

                        # Build a submodel element if a raw value was passed in the argument
                        if loadSideForce and not isinstance(
                            loadSideForce, SubmodelElement
                        ):
                            loadSideForce = self.LoadSideForce(loadSideForce)

                        # Build a submodel element if a raw value was passed in the argument
                        if counterMass and not isinstance(counterMass, SubmodelElement):
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
                    rotativeSection: Optional[Iterable[RotativeSection]] = None,
                    linearSection: Optional[Iterable[LinearSection]] = None,
                    id_short: Optional[str] = r"MotionPatternSections",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPatternSections/1/0",
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
                    for se_arg in [rotativeSection, linearSection]:
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
                motionPatternSections: MotionPatternSections,
                motionPatternName: Optional[Union[str, MotionPatternName]] = None,
                id_short: Optional[str] = r"MotionPattern",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MotionPattern/1/0",
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
                if motionPatternName and not isinstance(
                    motionPatternName, SubmodelElement
                ):
                    motionPatternName = self.MotionPatternName(motionPatternName)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [motionPatternName, motionPatternSections]:
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

        class Environmental(SubmodelElementCollection):

            class InstallationAltitude(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InstallationAltitude",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAZ614#003",
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

            class Atex2Gas(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Atex2Gas",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAR865#004",
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

            class Atex2Dust(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Atex2Dust",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAR866#004",
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

            class AmbientTemperatureController(Range):

                def __init__(
                    self,
                    min: str,
                    max: str,
                    id_short: Optional[str] = r"AmbientTemperatureController",
                    value_type: DataTypeDefXsd = str,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmbientTemperatureController/1/0",
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

            class AmbientTemperatureMotor(Range):

                def __init__(
                    self,
                    min: str,
                    max: str,
                    id_short: Optional[str] = r"AmbientTemperatureMotor",
                    value_type: DataTypeDefXsd = str,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AmbientTemperatureMotor/1/0",
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
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnvironmentalRequirements/1/0",
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
                if installationAltitude and not isinstance(
                    installationAltitude, SubmodelElement
                ):
                    installationAltitude = self.InstallationAltitude(
                        installationAltitude
                    )

                # Build a submodel element if a raw value was passed in the argument
                if atex2Gas and not isinstance(atex2Gas, SubmodelElement):
                    atex2Gas = self.Atex2Gas(atex2Gas)

                # Build a submodel element if a raw value was passed in the argument
                if atex2Dust and not isinstance(atex2Dust, SubmodelElement):
                    atex2Dust = self.Atex2Dust(atex2Dust)

                # Build a submodel element if a raw value was passed in the argument
                if ambientTemperatureController and not isinstance(
                    ambientTemperatureController, SubmodelElement
                ):
                    ambientTemperatureController = self.AmbientTemperatureController(
                        ambientTemperatureController
                    )

                # Build a submodel element if a raw value was passed in the argument
                if ambientTemperatureMotor and not isinstance(
                    ambientTemperatureMotor, SubmodelElement
                ):
                    ambientTemperatureMotor = self.AmbientTemperatureMotor(
                        ambientTemperatureMotor
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

        class OverallSystemRequirements(SubmodelElementCollection):

            class DcLinkCoupling(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DcLinkCoupling",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DcLinkCoupling/1/0",
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

            class BrakePresent(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"BrakePresent",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAE085#007",
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

            class MainsConnection(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MainsConnection",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABF822#003",
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

            class MountingType(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MountingType",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAH167#006",
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

            class MinSwitchingFrequency(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MinSwitchingFrequency",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAN329#003",
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

            class CoolingType(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CoolingType",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAE122#007",
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

            class ProtectionType(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ProtectionType",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAG342#007",
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

            class CertificateApproval(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CertificateApproval",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"de": r"Zertifikat/Zulassung",
                            r"en": r"Certificate/Approval",
                        }
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAB392#018",
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

            class SafetyIntegrityLevel(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SafetyIntegrityLevel",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"safety integrity level (SIL) according to IEC 61508"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH715#002",
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
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OverallSystemRequirements/1/0",
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

                # Build a submodel element if a raw value was passed in the argument
                if dcLinkCoupling and not isinstance(dcLinkCoupling, SubmodelElement):
                    dcLinkCoupling = self.DcLinkCoupling(dcLinkCoupling)

                # Build a submodel element if a raw value was passed in the argument
                if brakePresent and not isinstance(brakePresent, SubmodelElement):
                    brakePresent = self.BrakePresent(brakePresent)

                # Build a submodel element if a raw value was passed in the argument
                if mainsConnection and not isinstance(mainsConnection, SubmodelElement):
                    mainsConnection = self.MainsConnection(mainsConnection)

                # Build a submodel element if a raw value was passed in the argument
                if mountingType and not isinstance(mountingType, SubmodelElement):
                    mountingType = self.MountingType(mountingType)

                # Build a submodel element if a raw value was passed in the argument
                if minSwitchingFrequency and not isinstance(
                    minSwitchingFrequency, SubmodelElement
                ):
                    minSwitchingFrequency = self.MinSwitchingFrequency(
                        minSwitchingFrequency
                    )

                # Build a submodel element if a raw value was passed in the argument
                if coolingType and not isinstance(coolingType, SubmodelElement):
                    coolingType = self.CoolingType(coolingType)

                # Build a submodel element if a raw value was passed in the argument
                if protectionType and not isinstance(protectionType, SubmodelElement):
                    protectionType = self.ProtectionType(protectionType)

                # Build a submodel element if a raw value was passed in the argument
                if certificateApproval and not isinstance(
                    certificateApproval, SubmodelElement
                ):
                    certificateApproval = self.CertificateApproval(certificateApproval)

                # Build a submodel element if a raw value was passed in the argument
                if safetyIntegrityLevel and not isinstance(
                    safetyIntegrityLevel, SubmodelElement
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

        class UsageProfile(SubmodelElementCollection):

            class CyclesPerMinute(Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"CyclesPerMinute",
                    value_type: DataTypeDefXsd = int,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CyclesPerMinute/1/0",
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

            class OperatingHoursPerDay(Property):

                def __init__(
                    self,
                    value: Long,
                    id_short: Optional[str] = r"OperatingHoursPerDay",
                    value_type: DataTypeDefXsd = Long,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OperatingHoursPerDay/1/0",
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

            class OperatingDaysPerYear(Property):

                def __init__(
                    self,
                    value: Long,
                    id_short: Optional[str] = r"OperatingDaysPerYear",
                    value_type: DataTypeDefXsd = Long,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OperatingDaysPerYear/1/0",
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
                operatingHoursPerDay: Union[Long, OperatingHoursPerDay],
                operatingDaysPerYear: Union[Long, OperatingDaysPerYear],
                id_short: Optional[str] = r"UsageProfile",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/UsageProfile/1/0",
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
                if cyclesPerMinute and not isinstance(cyclesPerMinute, SubmodelElement):
                    cyclesPerMinute = self.CyclesPerMinute(cyclesPerMinute)

                # Build a submodel element if a raw value was passed in the argument
                if operatingHoursPerDay and not isinstance(
                    operatingHoursPerDay, SubmodelElement
                ):
                    operatingHoursPerDay = self.OperatingHoursPerDay(
                        operatingHoursPerDay
                    )

                # Build a submodel element if a raw value was passed in the argument
                if operatingDaysPerYear and not isinstance(
                    operatingDaysPerYear, SubmodelElement
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
            motionPattern: Optional[MotionPattern] = None,
            environmental: Optional[Environmental] = None,
            overallSystemRequirements: Optional[OverallSystemRequirements] = None,
            usageProfile: Optional[UsageProfile] = None,
            id_short: Optional[str] = r"ApplicationRequirements",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={
                    r"de": r"Applikationsanforderungen",
                    r"en": r"Application requirements",
                }
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = None,
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ApplicationRequirements/1/0",
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
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
            for se_arg in [
                motionPattern,
                environmental,
                overallSystemRequirements,
                usageProfile,
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

    class TransformationMechanism(SubmodelElementCollection):

        class Fan(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"Fan",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Lüfter", r"en": r"Fan"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Fan/1/0",
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

        class Pump(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"Pump",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Pumpe", r"en": r"Pump"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Pump/1/0",
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

        class RotraryTable(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RotraryTable",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"StaticEccentricity",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Exzentrität", r"en": r"Eccentricity"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/StaticEccentricity/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"CentroidAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Mittelpunktswinkel",
                                r"en": r"Centroid angle",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CentroidAngle/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Drehtisch", r"en": r"Rotrary table"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RotraryTable/1/0",
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

        class ChainConveyor(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"ChainConveyor",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrictionCoefficient",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Reibungskoeffizient",
                                r"en": r"Coefficient of friction",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FeedConstant",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Kettenförderer", r"en": r"Chain conveyor"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ChainConveyor/1/0",
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

        class BeltConveyor(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"BeltConveyor",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrictionCoefficient",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Reibungskoeffizient",
                                r"en": r"Coefficient of friction",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FeedConstant",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Bandförderer", r"en": r"Belt conveyor"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/BeltConveyor/1/0",
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

        class RollerConveyor(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RollerConveyor",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrictionCoefficient",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Reibungskoeffizient",
                                r"en": r"Coefficient of friction",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FeedConstant",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Rollenbahn", r"en": r"Roller conveyor"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RollerConveyor/1/0",
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

        class BeltDrive(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"BeltDrive",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrictionCoefficient",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Reibungskoeffizient",
                                r"en": r"Coefficient of friction",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FeedConstant",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Riemenantrieb", r"en": r"Belt drive"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/BeltDrive/1/0",
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

        class TravelingDrive(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"TravelingDrive",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrictionCoefficient",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Reibungskoeffizient",
                                r"en": r"Coefficient of friction",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FeedConstant",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Fahrender Antrieb", r"en": r"Traveling drive"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/TravelingDrive/1/0",
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

        class RackDrive(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RackDrive",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrictionCoefficient",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Reibungskoeffizient",
                                r"en": r"Coefficient of friction",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FeedConstant",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"DiameterPinion",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Durchmesser Ritzel",
                                r"en": r"Diameter of pinion",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DiameterPinion/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"HelixAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Schrägungswinkel der Verzahnung",
                                r"en": r"Helix angle of the toothing",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/HelixAngle/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MovingPart",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Bewegtes Teil", r"en": r"Moving part"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RackMovingPart/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Zahnstangenapplikation", r"en": r"Rack drive"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RackDrive/1/0",
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

        class SpindleDrive(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"SpindleDrive",
                entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"Efficiency",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Efficiency/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InertiaMotorSide",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InertiaMotorSide/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmAxialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmAxialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"LeverArmRadialForce",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Hebelarm Axialkraft",
                                r"en": r"Lever arm axial force",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/LeverArmRadialForce/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"NoLoadTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Leerlaufdrehmoment",
                                r"en": r"No-load Torque",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/NoLoadTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InclinationAngle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InclinationAngle/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrictionCoefficient",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Reibungskoeffizient",
                                r"en": r"Coefficient of friction",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrictionCoefficient/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FeedConstant",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={r"de": r"Vorschubkonstante", r"en": r"Feed Constant"}
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FeedConstant/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/SelfManagedEntity/1/0",
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Spindelantrieb", r"en": r"Spindle drive"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SpindleDrive/1/0",
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
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={
                    r"de": r"Transformationsmechanismen",
                    r"en": r"Transformation mechanism",
                }
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"All application mechanisms are listed in the submodel template - note that only one application mechanism can be selected in the design project instance."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/TransformationMechanism/1/0",
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
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

    class SizingResult(SubmodelElementCollection):

        class OverallSystem(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"OverallSystem",
                entity_type: EntityType = EntityType.CO_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"ManufacturerName",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO677#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ManufacturerArticleNumber",
                        value_type=str,
                        value=r"-",
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO676#003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    MultiLanguageProperty(
                        id_short=r"ManufacturerProductDesignation",
                        value=MultiLanguageTextType(
                            dict_={r"en": r"ManufacturerProductDesignation"}
                        ),
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAW338#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ManufacturerOrderCode",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r" 0173-1#02-AAO227#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ExternalMomentOfInertia",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ExternalMomentOfInertia/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"InternalMomentOfIntertia",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/InternalMomentOfInertia/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MassInertiaRatio",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MassInertiaRatio/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"DecelerationForEmergencyStop",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DecelerationForEmergencyStop/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"CurrentForEmergencyStop",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CurrentForEmergencyStop/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"DisplacementDuringEmergencyStop",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/DisplacementDuringEmergencyStop/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"EnergyConsumtionPerCycle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Gesamtsystem", r"en": r"Overall system"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OverallSystem/1/0",
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

        class MainComponent(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"MainComponent",
                entity_type: EntityType = EntityType.CO_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"MainComponentType",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Typ der Hauptkomponente",
                                r"en": r"Main component type",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MainComponentType/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"OneToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ManufacturerName",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO677#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ManufacturerArticleNumber",
                        value_type=str,
                        value=r"5001xxxx-xx-x",
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO676#003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    MultiLanguageProperty(
                        id_short=r"ManufacturerProductDesignation",
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAW338#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ManufacturerOrderCode",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r" 0173-1#02-AAO227#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxCurrentUtilizationPercentage",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxCurrentUtilizationPercentage/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxCurrentUtilization",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxCurrentUtilization/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxThermalUtilizationPercentage",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxThermalUtilizationPercentage/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxThermalUtilization",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxThermalUtilization/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"AveragePowerLosses",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AveragePowerLosses/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"AverageRegenerativePowerDcLink",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageRegenerativePowerDcLink/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxRegenerativePowerDcLink",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRegenerativePowerDcLink/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"AverageFeedInPowerDcLink",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageFeedInPowerDcLink/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"AverageFeedInPowerMains",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"CONSTANT",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/AverageFeedInPowerMains/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxFeedInPowerMains",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxFeedInPowerMains/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ContinuousCurrent",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/ContinuousCurrent/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"RmsOfPower",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RmsOfPower/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxTorqueUtilizationPercentage",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxTorqueUtilizationPercentage/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxTorqueUtilization",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxTorqueUtilization/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxRotationSpeedUtilizationPercentage",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRotationSpeedUtilizationPercentage/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MaxRotationSpeedUtilization",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"CONSTANT",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MaxRotationSpeedUtilization/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"EffectiveUtilization",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"CONSTANT",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EffectiveUtilization/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"CalculatedServiceLife",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CalculatedServiceLife/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"MassInertiaRatio",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MassInertiaRatio/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"FrequencyAtMaxSpeed",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/FrequencyAtMaxSpeed/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"PowerInRegenerativeOperation",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/PowerInRegenerativeOperation/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"PowerInMotorOperation",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/PowerInMotorOperation/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"RmsOfMotorTorque",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/RmsOfMotorTorque/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"EnergyConsumtionPerCycle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Hauptkomponente", r"en": r"Main component"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MainComponent/1/0",
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
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

        class OtherComponent(Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"OtherComponent",
                entity_type: EntityType = EntityType.CO_MANAGED_ENTITY,
                statement: Iterable[SubmodelElement] = (
                    Property(
                        id_short=r"ManufacturerName",
                        value_type=str,
                        value=r"Machine Builder GmbH",
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO677#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ManufacturerArticleNumber",
                        value_type=str,
                        value=r"-",
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO676#003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    MultiLanguageProperty(
                        id_short=r"ManufacturerProductDesignation",
                        value=MultiLanguageTextType(
                            dict_={r"en": r"ManufacturerProductDesignation"}
                        ),
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAW338#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"ManufacturerOrderCode",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r" 0173-1#02-AAO227#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"QuantityOfParts",
                        value_type=int,
                        value=None,
                        value_id=None,
                        display_name=MultiLanguageNameType(
                            dict_={
                                r"de": r"Anzahl Einzelteile",
                                r"en": r"Quantity of parts",
                            }
                        ),
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/QuantityOfParts/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"BulkCount",
                        value_type=UnsignedLong,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    Property(
                        id_short=r"EnergyConsumtionPerCycle",
                        value_type=Long,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=r"PARAMETER",
                        description=None,
                        semantic_id=ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/EnergyConsumtionPerCycle/1/0",
                                ),
                            ),
                            type_=ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        qualifier=(
                            Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        ),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[SpecificAssetId] = (),
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Komponente", r"en": r"Component"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/OtherComponent/1/0",
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
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

        class Messages(SubmodelElementCollection):

            class Message(SubmodelElementCollection):

                class CriticalityOfMessage(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"CriticalityOfMessage",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"de": r"Kritikalität der Meldung",
                                r"en": r"Criticality of message",
                            }
                        ),
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/CriticalityOfMessage/1/0",
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

                class MessageText(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"MessageText",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"de": r"Nachrichtentext", r"en": r"Message text"}
                        ),
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/MessageText/1/0",
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
                    messageText: Union[LangStringSet, MessageText],
                    id_short: Optional[str] = r"Message",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"de": r"Nachricht", r"en": r"Message"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Message/1/0",
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
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                    if criticalityOfMessage and not isinstance(
                        criticalityOfMessage, SubmodelElement
                    ):
                        criticalityOfMessage = self.CriticalityOfMessage(
                            criticalityOfMessage
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if messageText and not isinstance(messageText, SubmodelElement):
                        messageText = self.MessageText(messageText)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [criticalityOfMessage, messageText]:
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
                message: Optional[Iterable[Message]] = None,
                id_short: Optional[str] = r"Messages",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Nachrichten", r"en": r"Messages"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/Messages/1/0",
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
                for se_arg in [message]:
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

        class TextStatement(MultiLanguageProperty):

            def __init__(
                self,
                value: LangStringSet,
                id_short: Optional[str] = r"TextStatement",
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"de": r"Textaussage", r"en": r"Text statement"}
                ),
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/TextStatement/1/0",
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
            textStatement: Optional[Union[LangStringSet, TextStatement]] = None,
            id_short: Optional[str] = r"SizingResult",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"de": r"Auslegungsergebnisse", r"en": r"Sizing result"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = None,
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/SizingResult/1/0",
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
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
            if textStatement and not isinstance(textStatement, SubmodelElement):
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
        sizingProjectInformation: SizingProjectInformation,
        applicationRequirements: ApplicationRequirements,
        transformationMechanism: Optional[TransformationMechanism] = None,
        sizingResult: Optional[SizingResult] = None,
        id_short: Optional[str] = r"PowerDriveTrainSizing",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"Submodel containing customer specifications for motion and load profile, limitations and requirements of an industrial motion application."
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=None,
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(
                Key(
                    type_=KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/PowerDriveTrainSizing/1/0",
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
        for se_arg in [
            sizingProjectInformation,
            applicationRequirements,
            transformationMechanism,
            sizingResult,
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
