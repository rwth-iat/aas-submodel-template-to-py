from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class SafetyInstrumentedSystem(Submodel):

    class SISName(Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"SISName",
            value_type: DataTypeDefXsd = str,
            value_id: Optional[Reference] = None,
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"SIS name"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"gives relevant information about the SIS"}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/SISName/1",
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

    class SRSRequirements(SubmodelElementCollection):

        class SurvivabilityRequirement(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SurvivabilityRequirement",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"survivability requirement"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/SurvivabilityRequirement/1",
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

        class RequirementForStartingUpAndRestartingSIS(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"RequirementForStartingUpAndRestartingSIS",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"requirement for starting up and restarting SIS"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/RequirementForStartingUpAndRestartingSIS/1",
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

        class InterfacingSystemSpecification(SubmodelElementCollection):

            class InterfacingSystem(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InterfacingSystem",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Interfacing system"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the SIS"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/cds/InterfacingSystem/1",
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

            class NetworkType(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NetworkType",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"type of network"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the SIS"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SafetyInstrumentedSystem/TypeOfNetwork/1/0",
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
                                type_=r"enumeration",
                                value_type=str,
                                value=r"control network, safety network",
                                value_id=None,
                                kind=QualifierKind.VALUE_QUALIFIER,
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

            class TypeOfLinksHardwiredOrSoftware(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"TypeOfLinksHardwiredOrSoftware",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"type of links"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the SIS"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SafetyInstrumentedSystem/TypeOfLinks/1/0",
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
                                type_=r"enumeration",
                                value_type=str,
                                value=r"hardwired, software",
                                value_id=None,
                                kind=QualifierKind.VALUE_QUALIFIER,
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
                interfacingSystem: Union[str, InterfacingSystem],
                networkType: Union[str, NetworkType],
                typeOfLinksHardwiredOrSoftware: Union[
                    str, TypeOfLinksHardwiredOrSoftware
                ],
                id_short: Optional[str] = r"InterfacingSystemSpecification",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"interfacing system specification"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"gives relevant information about the SIS"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/InterfacingSystemSpecification/1",
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if interfacingSystem and not isinstance(
                    interfacingSystem, SubmodelElement
                ):
                    interfacingSystem = self.InterfacingSystem(interfacingSystem)

                # Build a submodel element if a raw value was passed in the argument
                if networkType and not isinstance(networkType, SubmodelElement):
                    networkType = self.NetworkType(networkType)

                # Build a submodel element if a raw value was passed in the argument
                if typeOfLinksHardwiredOrSoftware and not isinstance(
                    typeOfLinksHardwiredOrSoftware, SubmodelElement
                ):
                    typeOfLinksHardwiredOrSoftware = (
                        self.TypeOfLinksHardwiredOrSoftware(
                            typeOfLinksHardwiredOrSoftware
                        )
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    interfacingSystem,
                    networkType,
                    typeOfLinksHardwiredOrSoftware,
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

        class PerformanceStandard(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PerformanceStandard",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"performance standard"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"gives relevant information about the SIS"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/PerformanceStandard/1",
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

        class ApplicationProgramSafetyRequirements(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ApplicationProgramSafetyRequirements",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"application program safety requirements"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/ApplicationProgramSafetyRequirements/1",
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

        class DALSpec(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"DALSpec",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"DAL spec"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/DALSpec/1",
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

        class Document(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Document",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"URL of document"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"gives information about relevant document(s)"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/Document/1",
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
            survivabilityRequirement: Optional[
                Iterable[Union[str, SurvivabilityRequirement]]
            ] = None,
            requirementForStartingUpAndRestartingSIS: Optional[
                Iterable[Union[str, RequirementForStartingUpAndRestartingSIS]]
            ] = None,
            interfacingSystemSpecification: Optional[
                Iterable[InterfacingSystemSpecification]
            ] = None,
            performanceStandard: Optional[Iterable[PerformanceStandard]] = None,
            applicationProgramSafetyRequirements: Optional[
                ApplicationProgramSafetyRequirements
            ] = None,
            dALSpec: Optional[DALSpec] = None,
            document: Optional[Iterable[Document]] = None,
            id_short: Optional[str] = r"SRSRequirements",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"SRS requirements"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/SRSRequirements/1",
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

            # Build a list of submodel elements if a raw values were passed in the argument
            if survivabilityRequirement and all(
                [isinstance(i, str) for i in survivabilityRequirement]
            ):
                survivabilityRequirement = [
                    self.SurvivabilityRequirement(i) for i in survivabilityRequirement
                ]

            # Build a list of submodel elements if a raw values were passed in the argument
            if requirementForStartingUpAndRestartingSIS and all(
                [isinstance(i, str) for i in requirementForStartingUpAndRestartingSIS]
            ):
                requirementForStartingUpAndRestartingSIS = [
                    self.RequirementForStartingUpAndRestartingSIS(i)
                    for i in requirementForStartingUpAndRestartingSIS
                ]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                survivabilityRequirement,
                requirementForStartingUpAndRestartingSIS,
                interfacingSystemSpecification,
                performanceStandard,
                applicationProgramSafetyRequirements,
                dALSpec,
                document,
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
        sISName: Union[str, SISName],
        sRSRequirements: SRSRequirements,
        id_short: Optional[str] = r"SafetyInstrumentedSystem",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"The submodel Safety Instrumented System is a collection of properties about the functional safety requirements and information for the lifecycle of a device of a safety instrumented system realising one or more safety instrumented functions."
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/idta-02097-1-0",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ExternalReference(
            key=(
                Key(
                    type_=KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/SafetyInstrumentedSystem/1/0",
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

        # Build a submodel element if a raw value was passed in the argument
        if sISName and not isinstance(sISName, SubmodelElement):
            sISName = self.SISName(sISName)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [sISName, sRSRequirements]:
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
