from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class WorkstationWorkerMatchingData(aas.Submodel):

    class GeneralWorkstationData(aas.SubmodelElementCollection):

        class WorkstationInformation(aas.SubmodelElementCollection):

            class WorkstationName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"WorkstationName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Workstation name",
                            r"de": r"Name der Arbeitsstation",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(dict_={r"en": r"Workstation name"}),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/workstationname/1/0",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class WorkstationId(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"WorkstationId",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Workstation ID", r"de": r"Arbeitsstation ID"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/workstationid/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class OrgName(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"OrgName",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Organizational name",
                            r"de": r"Organisationsname",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/orgname/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

            class TypeOfWorkstation(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"TypeOfWorkstation",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Workstation type", r"de": r"Arbeitsstationsart"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/typeofworkstation/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

            class WorkerAssistanceInformation(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"WorkerAssistanceInformation",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Worker assistance information",
                            r"de": r"Informationen zur Werkerassistenz",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={r"en": r"Worker assistance information"}
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/mlp/workerassistanceeinformation/1/0",
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

            class RequiredPersonalSafetyEquipment(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"RequiredPersonalSafetyEquipment",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Required personal safety equipment",
                            r"de": r"Erforderliche persönliche Schutzausrüstung",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={r"en": r"Required personal safety equipment"}
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/requiredpersonalsafetyequipment/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

            class NecessaryPersonalTools(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"NecessaryPersonalTools",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Necessary personal tools",
                            r"de": r"Notwendige persönliche Werkzeuge",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/necessarypersonaltools/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

            class PersonalDataProcessing(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"PersonalDataProcessing",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Personal data processing ",
                            r"de": r"Verarbeitung persönlicher Daten",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/mlp/personaldataprocessing/1/0",
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

            class LocationDescription(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"LocationDescription",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Location description",
                            r"de": r"Ortsbeschreibung",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/locationdescription/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

            class Directions(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Directions",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Directions", r"de": r"Wegbeschreibung"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/directions/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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
                workstationId: Union[str, WorkstationId],
                workstationName: Optional[Union[str, WorkstationName]] = None,
                orgName: Optional[Union[aas.LangStringSet, OrgName]] = None,
                typeOfWorkstation: Optional[
                    Union[aas.LangStringSet, TypeOfWorkstation]
                ] = None,
                workerAssistanceInformation: Optional[
                    Union[aas.LangStringSet, WorkerAssistanceInformation]
                ] = None,
                requiredPersonalSafetyEquipment: Optional[
                    Union[aas.LangStringSet, RequiredPersonalSafetyEquipment]
                ] = None,
                necessaryPersonalTools: Optional[
                    Union[aas.LangStringSet, NecessaryPersonalTools]
                ] = None,
                personalDataProcessing: Optional[
                    Union[aas.LangStringSet, PersonalDataProcessing]
                ] = None,
                locationDescription: Optional[
                    Union[aas.LangStringSet, LocationDescription]
                ] = None,
                directions: Optional[Union[aas.LangStringSet, Directions]] = None,
                id_short: Optional[str] = r"WorkstationInformation",
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(
                    dict_={
                        r"en": r"General workstation information",
                        r"de": r"Allgemeine Arbeitsstationsinformationen",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"General information about the workstation in respect of worker deployment",
                        r"de": r"Allgemeine Informationen zur Arbeitsstation mit Relevanz für die Mitarbeitereinsatzplanung",
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/smc/workstationinformation/1/0",
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if workstationName and not isinstance(
                    workstationName, aas.SubmodelElement
                ):
                    workstationName = self.WorkstationName(workstationName)

                # Build a submodel element if a raw value was passed in the argument
                if workstationId and not isinstance(workstationId, aas.SubmodelElement):
                    workstationId = self.WorkstationId(workstationId)

                # Build a submodel element if a raw value was passed in the argument
                if orgName and not isinstance(orgName, aas.SubmodelElement):
                    orgName = self.OrgName(orgName)

                # Build a submodel element if a raw value was passed in the argument
                if typeOfWorkstation and not isinstance(
                    typeOfWorkstation, aas.SubmodelElement
                ):
                    typeOfWorkstation = self.TypeOfWorkstation(typeOfWorkstation)

                # Build a submodel element if a raw value was passed in the argument
                if workerAssistanceInformation and not isinstance(
                    workerAssistanceInformation, aas.SubmodelElement
                ):
                    workerAssistanceInformation = self.WorkerAssistanceInformation(
                        workerAssistanceInformation
                    )

                # Build a submodel element if a raw value was passed in the argument
                if requiredPersonalSafetyEquipment and not isinstance(
                    requiredPersonalSafetyEquipment, aas.SubmodelElement
                ):
                    requiredPersonalSafetyEquipment = (
                        self.RequiredPersonalSafetyEquipment(
                            requiredPersonalSafetyEquipment
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument
                if necessaryPersonalTools and not isinstance(
                    necessaryPersonalTools, aas.SubmodelElement
                ):
                    necessaryPersonalTools = self.NecessaryPersonalTools(
                        necessaryPersonalTools
                    )

                # Build a submodel element if a raw value was passed in the argument
                if personalDataProcessing and not isinstance(
                    personalDataProcessing, aas.SubmodelElement
                ):
                    personalDataProcessing = self.PersonalDataProcessing(
                        personalDataProcessing
                    )

                # Build a submodel element if a raw value was passed in the argument
                if locationDescription and not isinstance(
                    locationDescription, aas.SubmodelElement
                ):
                    locationDescription = self.LocationDescription(locationDescription)

                # Build a submodel element if a raw value was passed in the argument
                if directions and not isinstance(directions, aas.SubmodelElement):
                    directions = self.Directions(directions)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    workstationName,
                    workstationId,
                    orgName,
                    typeOfWorkstation,
                    workerAssistanceInformation,
                    requiredPersonalSafetyEquipment,
                    necessaryPersonalTools,
                    personalDataProcessing,
                    locationDescription,
                    directions,
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

        class GeneralQualificationDemand(aas.SubmodelElementList):

            class Generalqualificationdemand_item(aas.SubmodelElementCollection):

                class QualificationClassificationId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"QualificationClassificationId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Qualification classification (ID)",
                                r"de": r"Qualifikationsklassifizierung (ID)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/qualificationclassificationid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class QualificationId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"QualificationId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Qualification (ID)",
                                r"de": r"Qualifikation (ID)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/qualificationid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ExceptionRules(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ExceptionRules",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Exception rules",
                                r"de": r"Ausnahmeregelungen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/exceptionrules/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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
                    qualificationClassificationId: Union[
                        str, QualificationClassificationId
                    ],
                    qualificationId: Union[str, QualificationId],
                    exceptionRules: Optional[
                        Union[aas.LangStringSet, ExceptionRules]
                    ] = None,
                    id_short: Optional[str] = r"generalqualificationdemand_item",
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Worker qualification that is required to work at the workstation"
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Worker qualification that is required to work at the workstation"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/smc/generalqualificationdemandrecord/1/0",
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
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
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

                    # Build a submodel element if a raw value was passed in the argument
                    if qualificationClassificationId and not isinstance(
                        qualificationClassificationId, aas.SubmodelElement
                    ):
                        qualificationClassificationId = (
                            self.QualificationClassificationId(
                                qualificationClassificationId
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if qualificationId and not isinstance(
                        qualificationId, aas.SubmodelElement
                    ):
                        qualificationId = self.QualificationId(qualificationId)

                    # Build a submodel element if a raw value was passed in the argument
                    if exceptionRules and not isinstance(
                        exceptionRules, aas.SubmodelElement
                    ):
                        exceptionRules = self.ExceptionRules(exceptionRules)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        qualificationClassificationId,
                        qualificationId,
                        exceptionRules,
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
                generalqualificationdemand_items: Optional[
                    Iterable[Generalqualificationdemand_item]
                ] = None,
                id_short: Optional[str] = r"GeneralQualificationDemand",
                type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                semantic_id_list_element: Optional[aas.Reference] = None,
                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(
                    dict_={
                        r"en": r"General qualification demand",
                        r"de": r"Allgemeine Qualifikationsanforderungen",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Worker qualifications that are required in order to work at the workstation",
                        r"de": r"Mitarbeiterqualifikationen die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/sml/generalqualificationdemand/1/0",
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

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [generalqualificationdemand_items]:
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
                    isinstance(self.type_value_list_element, aas.Property)
                    or isinstance(self.type_value_list_element, aas.Range)
                    and not isinstance(new.value_type, self.value_type_list_element)
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
                if (
                    new.semantic_id is not None
                    and self.semantic_id_list_element is None
                ):
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

        class GeneralSkillDemand(aas.SubmodelElementList):

            class Generalskilldemand_item(aas.SubmodelElementCollection):

                class SkillClassificationId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"SkillClassificationId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Skill classification (ID)",
                                r"de": r"Fähigkeitenklassifizierung (ID)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/skillclassificationid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class SkillLevelClassificationId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"SkillLevelClassificationId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Skill level classification (ID)",
                                r"de": r"Fähigkeitenklassifizierung (ID)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/skilllevelclassificationid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class SkillLevelId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"SkillLevelId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Skill level (ID)",
                                r"de": r"Fähigkeitenstufe (ID)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/skilllevelid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class SkillId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"SkillId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={r"en": r"Skill (ID)", r"de": r"Fähigkeit (ID)"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/skillid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ExceptionRules(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ExceptionRules",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Exception rules",
                                r"de": r"Ausnahmeregelungen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/mlp/exceptionrules/1/0",
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
                    skillClassificationId: Union[str, SkillClassificationId],
                    skillId: Union[str, SkillId],
                    skillLevelClassificationId: Optional[
                        Union[str, SkillLevelClassificationId]
                    ] = None,
                    skillLevelId: Optional[Union[str, SkillLevelId]] = None,
                    exceptionRules: Optional[
                        Union[aas.LangStringSet, ExceptionRules]
                    ] = None,
                    id_short: Optional[str] = r"generalskilldemand_item",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Worker skill that is required in order to work at the workstation"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/smc/generalskilldemandrecord/1/0",
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
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
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

                    # Build a submodel element if a raw value was passed in the argument
                    if skillClassificationId and not isinstance(
                        skillClassificationId, aas.SubmodelElement
                    ):
                        skillClassificationId = self.SkillClassificationId(
                            skillClassificationId
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if skillLevelClassificationId and not isinstance(
                        skillLevelClassificationId, aas.SubmodelElement
                    ):
                        skillLevelClassificationId = self.SkillLevelClassificationId(
                            skillLevelClassificationId
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if skillLevelId and not isinstance(
                        skillLevelId, aas.SubmodelElement
                    ):
                        skillLevelId = self.SkillLevelId(skillLevelId)

                    # Build a submodel element if a raw value was passed in the argument
                    if skillId and not isinstance(skillId, aas.SubmodelElement):
                        skillId = self.SkillId(skillId)

                    # Build a submodel element if a raw value was passed in the argument
                    if exceptionRules and not isinstance(
                        exceptionRules, aas.SubmodelElement
                    ):
                        exceptionRules = self.ExceptionRules(exceptionRules)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        skillClassificationId,
                        skillLevelClassificationId,
                        skillLevelId,
                        skillId,
                        exceptionRules,
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
                generalskilldemand_items: Optional[
                    Iterable[Generalskilldemand_item]
                ] = None,
                id_short: Optional[str] = r"GeneralSkillDemand",
                type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                semantic_id_list_element: Optional[aas.Reference] = None,
                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(
                    dict_={
                        r"en": r"General skill demand",
                        r"de": r"Allgemeine Fähigkeitsanforderungen",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Worker skills that are required in order to work at the workstation",
                        r"de": r"Mitarbeiterfähigkeiten die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/sml/generalskilldemand/1/0",
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

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [generalskilldemand_items]:
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
                    isinstance(self.type_value_list_element, aas.Property)
                    or isinstance(self.type_value_list_element, aas.Range)
                    and not isinstance(new.value_type, self.value_type_list_element)
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
                if (
                    new.semantic_id is not None
                    and self.semantic_id_list_element is None
                ):
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
            workstationInformation: WorkstationInformation,
            generalQualificationDemand: Optional[GeneralQualificationDemand] = None,
            generalSkillDemand: Optional[GeneralSkillDemand] = None,
            id_short: Optional[str] = r"GeneralWorkstationData",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"General workstation data, which are relevant for worker deployment control and deployment planning",
                    r"de": r"Allgemeine Arbeitsstationsdaten, die für die Mitarbeitereinsatzsteuerung und -planung relevant sind",
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/smc/generalworkstationdata/1/0",
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
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                workstationInformation,
                generalQualificationDemand,
                generalSkillDemand,
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

    class ErgonomicWorkstationProfile(aas.SubmodelElementCollection):

        class MaxLiftingWeight(aas.Property):

            def __init__(
                self,
                value: int,
                id_short: Optional[str] = r"MaxLiftingWeight",
                value_type: aas.DataTypeDefXsd = int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(
                    dict_={r"en": r"Max. lifting weight", r"de": r"Max. Hebegewicht"}
                ),
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ModelReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                            value=r"https://admin-shell.io/idta/prop/maxliftingweight/1/0",
                        ),
                    ),
                    type_=aas.ConceptDescription,
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class MinWorkerHeight(aas.Property):

            def __init__(
                self,
                value: int,
                id_short: Optional[str] = r"MinWorkerHeight",
                value_type: aas.DataTypeDefXsd = int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(
                    dict_={
                        r"en": r"Minimum worker height ",
                        r"de": r"Minimale Mitarbeitergröße ",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ModelReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                            value=r"https://admin-shell.io/idta/prop/minworkerheight/1/0",
                        ),
                    ),
                    type_=aas.ConceptDescription,
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class AllowedPersonalLimitations(aas.SubmodelElementList):

            class Allowedpersonallimitations_item(aas.SubmodelElementCollection):

                class LimitationClassificationId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"LimitationClassificationId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Limitation classification (ID)",
                                r"de": r"Einschränkungsklassifizierung (ID)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/prop/limitationclassificationid/1/0",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class PersonalLimitationId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"PersonalLimitationId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Personal limitation (ID)",
                                r"de": r"Persönliche Einschränkung (ID)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/personallimitationid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
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
                    limitationClassificationId: Union[str, LimitationClassificationId],
                    personalLimitationId: Union[str, PersonalLimitationId],
                    id_short: Optional[str] = r"allowedpersonallimitations_item",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Personal limitation that is accepted for working at the workstation, e.g., special measures have been implemented"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/smc/allowedpersonallimitationsrecord/1/0",
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
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if limitationClassificationId and not isinstance(
                        limitationClassificationId, aas.SubmodelElement
                    ):
                        limitationClassificationId = self.LimitationClassificationId(
                            limitationClassificationId
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if personalLimitationId and not isinstance(
                        personalLimitationId, aas.SubmodelElement
                    ):
                        personalLimitationId = self.PersonalLimitationId(
                            personalLimitationId
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [limitationClassificationId, personalLimitationId]:
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
                allowedpersonallimitations_items: Allowedpersonallimitations_item,
                id_short: Optional[str] = r"AllowedPersonalLimitations",
                type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                semantic_id_list_element: Optional[aas.Reference] = None,
                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(
                    dict_={
                        r"en": r"Allowed personal limitations",
                        r"de": r"Akzeptierte Mitarbeitereinschränkungen",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"List of all personal limitations that are accepted for working at the workstation, e.g., special measures have been implemented",
                        r"de": r"Liste von persönlichen Einschränkungen, die an der Arbeitsstation zugelassen sind. Zum Beispiel weil bestimmte Arbeitsgestaltungsmaßnahmen getroffen wurden.",
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/sml/allowedpersonallimitations/1/0",
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

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [allowedpersonallimitations_items]:
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
                    isinstance(self.type_value_list_element, aas.Property)
                    or isinstance(self.type_value_list_element, aas.Range)
                    and not isinstance(new.value_type, self.value_type_list_element)
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
                if (
                    new.semantic_id is not None
                    and self.semantic_id_list_element is None
                ):
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
            maxLiftingWeight: Optional[Union[int, MaxLiftingWeight]] = None,
            minWorkerHeight: Optional[Union[int, MinWorkerHeight]] = None,
            allowedPersonalLimitations: Optional[AllowedPersonalLimitations] = None,
            id_short: Optional[str] = r"ErgonomicWorkstationProfile",
            display_name: Optional[
                aas.MultiLanguageNameType
            ] = aas.MultiLanguageNameType(
                dict_={
                    r"en": r"Ergonomic workstation profile",
                    r"de": r"Ergonomisches Arbeitsplatzprofil",
                }
            ),
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Ergonomic characteristics of the workstation which might influence the worker deployment",
                    r"de": r"Ergonomische Arbeitsplatzeigenschaften, die einen Einfluss auf den Mitarbeitereinsatz haben",
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/smc/ergonomicworkstationprofile/1/0",
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

            # Build a submodel element if a raw value was passed in the argument
            if maxLiftingWeight and not isinstance(
                maxLiftingWeight, aas.SubmodelElement
            ):
                maxLiftingWeight = self.MaxLiftingWeight(maxLiftingWeight)

            # Build a submodel element if a raw value was passed in the argument
            if minWorkerHeight and not isinstance(minWorkerHeight, aas.SubmodelElement):
                minWorkerHeight = self.MinWorkerHeight(minWorkerHeight)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                maxLiftingWeight,
                minWorkerHeight,
                allowedPersonalLimitations,
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

    class WorkstationConfigurationRecords(aas.SubmodelElementList):

        class Workstationconfigurationrecords_item(aas.SubmodelElementCollection):

            class WorkerId(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"WorkerId",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Worker (ID)", r"de": r"Werker (ID)"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/workerid/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AccessStart(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"AccessStart",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Access start ", r"de": r"Zugriffsstart"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/accessstart/1/0",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AccessEnd(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"AccessEnd",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Access end", r"de": r"Zugriffsende"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/accessend/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class PreferredHeight(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"PreferredHeight",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Preferred height", r"de": r"Bevorzugte Höhe"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/prop/preferredheight/1/0",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ProprietaryConfigurations(aas.SubmodelElementList):

                class Proprietaryconfigurations_item(aas.SubmodelElementCollection):

                    class ConfigurationName(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"ConfigurationName",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Configuation name",
                                    r"de": r"Konfigurationsname",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/configurationname/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ConfigurationValue(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"ConfigurationValue",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Configuration value",
                                    r"de": r"Konfigurationswert",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/configurationvalue/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        configurationName: Union[str, ConfigurationName],
                        configurationValue: Union[str, ConfigurationValue],
                        id_short: Optional[str] = r"proprietaryconfigurations_item",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={r"en": r"Proprietary worker-depending configuration"}
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/smc/proprietaryconfigurationsrecord/1/0",
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
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument
                        if configurationName and not isinstance(
                            configurationName, aas.SubmodelElement
                        ):
                            configurationName = self.ConfigurationName(
                                configurationName
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if configurationValue and not isinstance(
                            configurationValue, aas.SubmodelElement
                        ):
                            configurationValue = self.ConfigurationValue(
                                configurationValue
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [configurationName, configurationValue]:
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
                    proprietaryconfigurations_items: Proprietaryconfigurations_item,
                    id_short: Optional[str] = r"ProprietaryConfigurations",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Proprietary configurations",
                            r"de": r"Proprietäre Konfigurationen",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Proprietary worker-depending configurations ",
                            r"de": r"Proprietäre werkerindividuelle Konfigurationsmerkmale",
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/sml/proprietaryconfigurations/1/0",
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

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [proprietaryconfigurations_items]:
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
                        isinstance(self.type_value_list_element, aas.Property)
                        or isinstance(self.type_value_list_element, aas.Range)
                        and not isinstance(new.value_type, self.value_type_list_element)
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
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
                workerId: Union[str, WorkerId],
                accessStart: Optional[Union[xsd.DateTime, AccessStart]] = None,
                accessEnd: Optional[Union[xsd.DateTime, AccessEnd]] = None,
                preferredHeight: Optional[Union[int, PreferredHeight]] = None,
                proprietaryConfigurations: Optional[ProprietaryConfigurations] = None,
                id_short: Optional[str] = r"workstationconfigurationrecords_item",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Worker specific configuration options of a workstation"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/smc/workstationconfigurationrecord/1/0",
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
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if workerId and not isinstance(workerId, aas.SubmodelElement):
                    workerId = self.WorkerId(workerId)

                # Build a submodel element if a raw value was passed in the argument
                if accessStart and not isinstance(accessStart, aas.SubmodelElement):
                    accessStart = self.AccessStart(accessStart)

                # Build a submodel element if a raw value was passed in the argument
                if accessEnd and not isinstance(accessEnd, aas.SubmodelElement):
                    accessEnd = self.AccessEnd(accessEnd)

                # Build a submodel element if a raw value was passed in the argument
                if preferredHeight and not isinstance(
                    preferredHeight, aas.SubmodelElement
                ):
                    preferredHeight = self.PreferredHeight(preferredHeight)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    workerId,
                    accessStart,
                    accessEnd,
                    preferredHeight,
                    proprietaryConfigurations,
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
            workstationconfigurationrecords_items: Workstationconfigurationrecords_item,
            id_short: Optional[str] = r"WorkstationConfigurationRecords",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[
                aas.MultiLanguageNameType
            ] = aas.MultiLanguageNameType(
                dict_={
                    r"en": r"Workstation configuration records ",
                    r"de": r"Arbeitsstationskonfigurationseinträge",
                }
            ),
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Worker specific configuration options of a workstation",
                    r"de": r"Arbeitsstationskonfigurationsoptionen für einen Mitarbeiter",
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/sml/workstationconfigurationrecords/1/0",
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
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [workstationconfigurationrecords_items]:
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
                isinstance(self.type_value_list_element, aas.Property)
                or isinstance(self.type_value_list_element, aas.Range)
                and not isinstance(new.value_type, self.value_type_list_element)
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

    class PlannedQualificationDemand(aas.SubmodelElementList):

        class Plannedqualificationdemand_item(aas.SubmodelElementCollection):

            class IntervalDescription(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"IntervalDescription",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Interval description",
                            r"de": r"Intervallbeschreibung",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/intervaldescription/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

            class IntervalStart(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"IntervalStart",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Interval start", r"de": r"Intervallstart"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/intervalstart/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class IntervalEnd(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"IntervalEnd",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Interval end", r"de": r"Intervallende"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/intervalend/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class QualificationDemandRecords(aas.SubmodelElementList):

                class Qualificationdemandrecords_item(aas.SubmodelElementCollection):

                    class QualificationClassificationId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"QualificationClassificationId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Qualification classification (ID)",
                                    r"de": r"Qualifikationsklassifizierung (ID)",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/qualificationclassificationid/1/0",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class QualificationId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"QualificationId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Qualification (ID)",
                                    r"de": r"Qualifikation (ID)",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/qualificationid/1/0",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ExceptionRules(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"ExceptionRules",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Exception rules",
                                    r"de": r"Ausnahmeregelungen",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/mlp/exceptionrules/1/0",
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

                    class DemandKind(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"DemandKind",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/enum/adhocdemand",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/enum/generaldemand",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/enum/orderdependingdemand",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Demand kind", r"de": r"Bedarfsquelle"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/demandkind/1/0",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class StartTime(aas.Property):

                        def __init__(
                            self,
                            value: xsd.DateTime,
                            id_short: Optional[str] = r"StartTime",
                            value_type: aas.DataTypeDefXsd = xsd.DateTime,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Start time", r"de": r"Startzeit"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/starttime/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class EndTime(aas.Property):

                        def __init__(
                            self,
                            value: xsd.DateTime,
                            id_short: Optional[str] = r"EndTime",
                            value_type: aas.DataTypeDefXsd = xsd.DateTime,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"End time", r"de": r"Endzeit"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/endtime/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ProcessTime(aas.Property):

                        def __init__(
                            self,
                            value: int,
                            id_short: Optional[str] = r"ProcessTime",
                            value_type: aas.DataTypeDefXsd = int,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Process time", r"de": r"Prozesszeit"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/processtime/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        qualificationClassificationId: Union[
                            str, QualificationClassificationId
                        ],
                        qualificationId: Union[str, QualificationId],
                        startTime: Union[xsd.DateTime, StartTime],
                        endTime: Union[xsd.DateTime, EndTime],
                        processTime: Union[int, ProcessTime],
                        exceptionRules: Optional[
                            Union[aas.LangStringSet, ExceptionRules]
                        ] = None,
                        demandKind: Optional[Union[str, DemandKind]] = None,
                        id_short: Optional[str] = r"qualificationdemandrecords_item",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Worker qualification that is required to work at the workstation"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/smc/qualificationdemandrecord/1/0",
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
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument
                        if qualificationClassificationId and not isinstance(
                            qualificationClassificationId, aas.SubmodelElement
                        ):
                            qualificationClassificationId = (
                                self.QualificationClassificationId(
                                    qualificationClassificationId
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if qualificationId and not isinstance(
                            qualificationId, aas.SubmodelElement
                        ):
                            qualificationId = self.QualificationId(qualificationId)

                        # Build a submodel element if a raw value was passed in the argument
                        if exceptionRules and not isinstance(
                            exceptionRules, aas.SubmodelElement
                        ):
                            exceptionRules = self.ExceptionRules(exceptionRules)

                        # Build a submodel element if a raw value was passed in the argument
                        if demandKind and not isinstance(
                            demandKind, aas.SubmodelElement
                        ):
                            demandKind = self.DemandKind(demandKind)

                        # Build a submodel element if a raw value was passed in the argument
                        if startTime and not isinstance(startTime, aas.SubmodelElement):
                            startTime = self.StartTime(startTime)

                        # Build a submodel element if a raw value was passed in the argument
                        if endTime and not isinstance(endTime, aas.SubmodelElement):
                            endTime = self.EndTime(endTime)

                        # Build a submodel element if a raw value was passed in the argument
                        if processTime and not isinstance(
                            processTime, aas.SubmodelElement
                        ):
                            processTime = self.ProcessTime(processTime)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            qualificationClassificationId,
                            qualificationId,
                            exceptionRules,
                            demandKind,
                            startTime,
                            endTime,
                            processTime,
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
                    qualificationdemandrecords_items: Qualificationdemandrecords_item,
                    id_short: Optional[str] = r"QualificationDemandRecords",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Worker qualifications that are required in order to work at the workstation",
                            r"de": r"Mitarbeiterqualifikationen die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/sml/qualificationdemandrecords/1/0",
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

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [qualificationdemandrecords_items]:
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
                        isinstance(self.type_value_list_element, aas.Property)
                        or isinstance(self.type_value_list_element, aas.Range)
                        and not isinstance(new.value_type, self.value_type_list_element)
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
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
                intervalDescription: Optional[
                    Union[aas.LangStringSet, IntervalDescription]
                ] = None,
                intervalStart: Optional[Union[xsd.DateTime, IntervalStart]] = None,
                intervalEnd: Optional[Union[xsd.DateTime, IntervalEnd]] = None,
                qualificationDemandRecords: Optional[QualificationDemandRecords] = None,
                id_short: Optional[str] = r"plannedqualificationdemand_item",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Production plan depending planned qualification demand at a workstation"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/smc/plannedqualificationdemandrecord/1/0",
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
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
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

                # Build a submodel element if a raw value was passed in the argument
                if intervalDescription and not isinstance(
                    intervalDescription, aas.SubmodelElement
                ):
                    intervalDescription = self.IntervalDescription(intervalDescription)

                # Build a submodel element if a raw value was passed in the argument
                if intervalStart and not isinstance(intervalStart, aas.SubmodelElement):
                    intervalStart = self.IntervalStart(intervalStart)

                # Build a submodel element if a raw value was passed in the argument
                if intervalEnd and not isinstance(intervalEnd, aas.SubmodelElement):
                    intervalEnd = self.IntervalEnd(intervalEnd)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    intervalDescription,
                    intervalStart,
                    intervalEnd,
                    qualificationDemandRecords,
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
            plannedqualificationdemand_items: Optional[
                Iterable[Plannedqualificationdemand_item]
            ] = None,
            id_short: Optional[str] = r"PlannedQualificationDemand",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[
                aas.MultiLanguageNameType
            ] = aas.MultiLanguageNameType(
                dict_={
                    r"en": r"Planned qualification demand",
                    r"de": r"Geplanter Qualifikationsbedarf",
                }
            ),
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Production plan depending planned qualification demand at a workstation",
                    r"de": r"Vom Produktionsplan abhängiger und geplanter Qualifikationsbedarf an einer Arbeitsstation",
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/sml/plannedqualificationdemand/1/0",
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [plannedqualificationdemand_items]:
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
                isinstance(self.type_value_list_element, aas.Property)
                or isinstance(self.type_value_list_element, aas.Range)
                and not isinstance(new.value_type, self.value_type_list_element)
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

    class PlannedSkillDemand(aas.SubmodelElementList):

        class Plannedskilldemand_item(aas.SubmodelElementCollection):

            class IntervalDescription(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"IntervalDescription",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Interval description",
                            r"de": r"Intervallbeschreibung",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/mlp/intervaldescription/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

            class IntervalStart(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"IntervalStart",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Interval start", r"de": r"Intervallstart"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/intervalstart/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class IntervalEnd(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"IntervalEnd",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Interval end", r"de": r"Intervallende"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/intervalend/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SkillDemandRecords(aas.SubmodelElementList):

                class Skilldemandrecords_item(aas.SubmodelElementCollection):

                    class SkillClassificationId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SkillClassificationId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Skill classification (ID)",
                                    r"de": r"Fähigkeitenklassifizierung (ID)",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/skillclassificationid/1/0",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SkillLevelClassificationId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SkillLevelClassificationId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Skill level classification (ID)",
                                    r"de": r"Fähigkeitenklassifizierung (ID)",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/skilllevelclassificationid/1/0",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SkillLevelId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SkillLevelId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Skill level (ID)",
                                    r"de": r"Fähigkeitenstufe (ID)",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/skilllevelid/1/0",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SkillId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SkillId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Skill (ID)", r"de": r"Fähigkeit (ID)"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/skillid/1/0",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ExceptionRules(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"ExceptionRules",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Exception rules",
                                    r"de": r"Ausnahmeregelungen",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/mlp/exceptionrules/1/0",
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

                    class DemandKind(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"DemandKind",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/enum/adhocdemand",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/enum/generaldemand",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/enum/orderdependingdemand",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Demand kind", r"de": r"Bedarfsquelle"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/prop/demandkind/1/0",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class StartTime(aas.Property):

                        def __init__(
                            self,
                            value: xsd.DateTime,
                            id_short: Optional[str] = r"StartTime",
                            value_type: aas.DataTypeDefXsd = xsd.DateTime,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Start time", r"de": r"Startzeit"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/starttime/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class EndTime(aas.Property):

                        def __init__(
                            self,
                            value: xsd.DateTime,
                            id_short: Optional[str] = r"EndTime",
                            value_type: aas.DataTypeDefXsd = xsd.DateTime,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"End time", r"de": r"Endzeit"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/endtime/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ProcessTime(aas.Property):

                        def __init__(
                            self,
                            value: int,
                            id_short: Optional[str] = r"ProcessTime",
                            value_type: aas.DataTypeDefXsd = int,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Process time", r"de": r"Prozesszeit"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/processtime/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        skillClassificationId: Union[str, SkillClassificationId],
                        skillId: Union[str, SkillId],
                        startTime: Union[xsd.DateTime, StartTime],
                        endTime: Union[xsd.DateTime, EndTime],
                        processTime: Union[int, ProcessTime],
                        skillLevelClassificationId: Optional[
                            Union[str, SkillLevelClassificationId]
                        ] = None,
                        skillLevelId: Optional[Union[str, SkillLevelId]] = None,
                        exceptionRules: Optional[
                            Union[aas.LangStringSet, ExceptionRules]
                        ] = None,
                        demandKind: Optional[Union[str, DemandKind]] = None,
                        id_short: Optional[str] = r"skilldemandrecords_item",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Worker skill that is required in order to work at the workstation"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/smc/skilldemandrecord/1/0",
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
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument
                        if skillClassificationId and not isinstance(
                            skillClassificationId, aas.SubmodelElement
                        ):
                            skillClassificationId = self.SkillClassificationId(
                                skillClassificationId
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if skillLevelClassificationId and not isinstance(
                            skillLevelClassificationId, aas.SubmodelElement
                        ):
                            skillLevelClassificationId = (
                                self.SkillLevelClassificationId(
                                    skillLevelClassificationId
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if skillLevelId and not isinstance(
                            skillLevelId, aas.SubmodelElement
                        ):
                            skillLevelId = self.SkillLevelId(skillLevelId)

                        # Build a submodel element if a raw value was passed in the argument
                        if skillId and not isinstance(skillId, aas.SubmodelElement):
                            skillId = self.SkillId(skillId)

                        # Build a submodel element if a raw value was passed in the argument
                        if exceptionRules and not isinstance(
                            exceptionRules, aas.SubmodelElement
                        ):
                            exceptionRules = self.ExceptionRules(exceptionRules)

                        # Build a submodel element if a raw value was passed in the argument
                        if demandKind and not isinstance(
                            demandKind, aas.SubmodelElement
                        ):
                            demandKind = self.DemandKind(demandKind)

                        # Build a submodel element if a raw value was passed in the argument
                        if startTime and not isinstance(startTime, aas.SubmodelElement):
                            startTime = self.StartTime(startTime)

                        # Build a submodel element if a raw value was passed in the argument
                        if endTime and not isinstance(endTime, aas.SubmodelElement):
                            endTime = self.EndTime(endTime)

                        # Build a submodel element if a raw value was passed in the argument
                        if processTime and not isinstance(
                            processTime, aas.SubmodelElement
                        ):
                            processTime = self.ProcessTime(processTime)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            skillClassificationId,
                            skillLevelClassificationId,
                            skillLevelId,
                            skillId,
                            exceptionRules,
                            demandKind,
                            startTime,
                            endTime,
                            processTime,
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
                    skilldemandrecords_items: Skilldemandrecords_item,
                    id_short: Optional[str] = r"SkillDemandRecords",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Worker skills that are required in order to work at the workstation",
                            r"de": r"Mitarbeiterfähigkeiten die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/sml/skilldemandrecords/1/0",
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
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [skilldemandrecords_items]:
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
                        isinstance(self.type_value_list_element, aas.Property)
                        or isinstance(self.type_value_list_element, aas.Range)
                        and not isinstance(new.value_type, self.value_type_list_element)
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
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
                skillDemandRecords: SkillDemandRecords,
                intervalDescription: Optional[
                    Union[aas.LangStringSet, IntervalDescription]
                ] = None,
                intervalStart: Optional[Union[xsd.DateTime, IntervalStart]] = None,
                intervalEnd: Optional[Union[xsd.DateTime, IntervalEnd]] = None,
                id_short: Optional[str] = r"plannedskilldemand_item",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Production plan depending planned skill demand at a workstation"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/smc/plannedskilldemandrecord/1/0",
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
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
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

                # Build a submodel element if a raw value was passed in the argument
                if intervalDescription and not isinstance(
                    intervalDescription, aas.SubmodelElement
                ):
                    intervalDescription = self.IntervalDescription(intervalDescription)

                # Build a submodel element if a raw value was passed in the argument
                if intervalStart and not isinstance(intervalStart, aas.SubmodelElement):
                    intervalStart = self.IntervalStart(intervalStart)

                # Build a submodel element if a raw value was passed in the argument
                if intervalEnd and not isinstance(intervalEnd, aas.SubmodelElement):
                    intervalEnd = self.IntervalEnd(intervalEnd)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    intervalDescription,
                    intervalStart,
                    intervalEnd,
                    skillDemandRecords,
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
            plannedskilldemand_items: Optional[
                Iterable[Plannedskilldemand_item]
            ] = None,
            id_short: Optional[str] = r"PlannedSkillDemand",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[
                aas.MultiLanguageNameType
            ] = aas.MultiLanguageNameType(
                dict_={
                    r"en": r"Planned skill demand",
                    r"de": r"Geplanter Fähigkeitenbedarf",
                }
            ),
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Production plan depending planned skill demand at a workstation",
                    r"de": r"Vom Produktionsplan abhängiger und geplanter Qualifikationsbedarf an einer Arbeitsstation",
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/sml/plannedskilldemand/1/0",
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [plannedskilldemand_items]:
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
                isinstance(self.type_value_list_element, aas.Property)
                or isinstance(self.type_value_list_element, aas.Range)
                and not isinstance(new.value_type, self.value_type_list_element)
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
        generalWorkstationData: GeneralWorkstationData,
        workstationConfigurationRecords: WorkstationConfigurationRecords,
        ergonomicWorkstationProfile: Optional[ErgonomicWorkstationProfile] = None,
        plannedQualificationDemand: Optional[PlannedQualificationDemand] = None,
        plannedSkillDemand: Optional[PlannedSkillDemand] = None,
        id_short: Optional[str] = r"WorkstationWorkerMatchingData",
        display_name: Optional[aas.MultiLanguageNameType] = aas.MultiLanguageNameType(
            dict_={
                r"en": r"Workstation Worker Matching Data",
                r"de": r"Daten für die Mitarbeitereinsatzplanung",
            }
        ),
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = aas.MultiLanguageTextType(
            dict_={
                r"en": r"Submodel containing workstation data in order to match and deploy workers to workstations",
                r"de": r"Teilmodell mit Arbeitsstationsdaten für die Mitarbeitereinsatzplanung",
            }
        ),
        administration: Optional[
            aas.AdministrativeInformation
        ] = aas.AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=None,
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/sm/workstationworkermatchingdata",
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

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            generalWorkstationData,
            ergonomicWorkstationProfile,
            workstationConfigurationRecords,
            plannedQualificationDemand,
            plannedSkillDemand,
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
