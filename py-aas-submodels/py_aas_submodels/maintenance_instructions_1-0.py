from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class MaintenanceInstructions(Submodel):

    class MaintenanceFreeAsset(Property):

        def __init__(
            self,
            value: bool,
            id_short: Optional[str] = r"MaintenanceFreeAsset",
            value_type: DataTypeDefXsd = bool,
            value_id: Optional[Reference] = None,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"de": r"Festlegung, ob ein Asset wartungsfrei ist, oder eine Wartung benötigt. Bei einem wartungsfreien Asset Wert =True . Wird eine Wartung benötig Wert = False. Somit kann ausgeschlossen werden, dass ein Hersteller vergessen hat das SM Maintenance zu erstellen und der Anwender hat die Sicherheit, dass das Asset wartungsfrei ist. ",
                    r"en": r"Determines whether an asset is maintenance-free or requires maintenance. If an asset is maintenance-free, value = true. If maintenance is required, value = false. This excludes the possibility that a manufacturer has forgotten to create the SM Maintenance and the user has the certainty that the asset is maintenance-free. ",
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancefreeasset/1/0",
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

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class MaintenanceInstructionsForSpecificInterval(SubmodelElementCollection):

        class MaintenanceTechnicians(SubmodelElementCollection):

            class NumberOfRequiredTechnicians(Property):

                def __init__(
                    self,
                    value: Decimal,
                    id_short: Optional[str] = r"NumberOfRequiredTechnicians",
                    value_type: DataTypeDefXsd = Decimal,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Anzahl der für die Wartung benötigten Techniker",
                            r"en": r"Number of technicians needed for maintenance",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/numberofrequiredtechnicians/1/0",
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

            class RequiredQualification(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"RequiredQualification",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Anforderung an die Mindestqualifikation der Techniker",
                            r"en": r"Requirement for the minimum qualification of technicians",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-BAF831#002",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class EstimatedTotalWorkingTime(SubmodelElementCollection):

                class ValueTotalEstimatedWorkingTime(Property):

                    def __init__(
                        self,
                        value: Decimal,
                        id_short: Optional[str] = r"ValueTotalEstimatedWorkingTime",
                        value_type: DataTypeDefXsd = Decimal,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Wert für die Dauer der gesamten Wartung",
                                r"en": r"Value for the duration of the entire maintenance",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/valuetotalestimatedworkingtime/1/0",
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

                class UnitValueTotalEstimatedWorkingTime(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"UnitValueTotalEstimatedWorkingTime",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Einheit für die Dauer der gesamten Wartung - Beispiel Stunden, Tage, Wochen",
                                r"en": r"Unit for the duration of the entire maintenance - example hours, days, weeks",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/unitvaluetotalestimatedworkingtime/1/0",
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
                    valueTotalEstimatedWorkingTime: Union[
                        Decimal, ValueTotalEstimatedWorkingTime
                    ],
                    unitValueTotalEstimatedWorkingTime: Union[
                        str, UnitValueTotalEstimatedWorkingTime
                    ],
                    id_short: Optional[str] = r"EstimatedTotalWorkingTime",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Sammlung, um den voraussichtlichen Zeitaufwand für die Durchführung der Wartung zu definieren",
                            r"en": r"Collection to define the expected time needed to perform the maintenance",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/estimatedtotalworkingtime/1/0",
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
                    if valueTotalEstimatedWorkingTime and not isinstance(
                        valueTotalEstimatedWorkingTime, SubmodelElement
                    ):
                        valueTotalEstimatedWorkingTime = (
                            self.ValueTotalEstimatedWorkingTime(
                                valueTotalEstimatedWorkingTime
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if unitValueTotalEstimatedWorkingTime and not isinstance(
                        unitValueTotalEstimatedWorkingTime, SubmodelElement
                    ):
                        unitValueTotalEstimatedWorkingTime = (
                            self.UnitValueTotalEstimatedWorkingTime(
                                unitValueTotalEstimatedWorkingTime
                            )
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        valueTotalEstimatedWorkingTime,
                        unitValueTotalEstimatedWorkingTime,
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
                numberOfRequiredTechnicians: Optional[
                    Union[Decimal, NumberOfRequiredTechnicians]
                ] = None,
                requiredQualification: Optional[
                    Iterable[Union[LangStringSet, RequiredQualification]]
                ] = None,
                estimatedTotalWorkingTime: Optional[EstimatedTotalWorkingTime] = None,
                id_short: Optional[str] = r"MaintenanceTechnicians",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"de": r"Details zu den für die Wartung benötigten Technikern",
                        r"en": r"Details of the technicians required for maintenance",
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancetechnicians/1/0",
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
                if numberOfRequiredTechnicians and not isinstance(
                    numberOfRequiredTechnicians, SubmodelElement
                ):
                    numberOfRequiredTechnicians = self.NumberOfRequiredTechnicians(
                        numberOfRequiredTechnicians
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if requiredQualification and all(
                    [isinstance(i, LangStringSet) for i in requiredQualification]
                ):
                    requiredQualification = [
                        self.RequiredQualification(i) for i in requiredQualification
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    numberOfRequiredTechnicians,
                    requiredQualification,
                    estimatedTotalWorkingTime,
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

        class ListMaintenanceSteps(SubmodelElementCollection):

            class MaintenanceStep(SubmodelElementCollection):

                class MaintenanceStepID(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"MaintenanceStepID",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"ID oder Nummer des Wartungsschritts für eine klare Strukturierung der Wartung",
                                r"en": r"ID or number of the maintenance step for a clear structuring of the maintenance",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancestepid/1/0",
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

                class MaintenanceStepName(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"MaintenanceStepName",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Benennung des Wartungsschritt - Beispiel Wartungsstart",
                                r"en": r"Naming of the maintenance step - example maintenance start",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancestepname/1/0",
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
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class LocalizationDescription(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"LocalizationDescription",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Angabe zur Lokalisierung des Wartungsschritts",
                                r"en": r"Indication of the localization of the maintenance.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/localizationdescription/1/0",
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
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class LinkSMMaintenanceComponentModuleMachine(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[
                            str
                        ] = r"LinkSMMaintenanceComponentModuleMachine",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Link zu einem anderen SM Maintenance. Beispiel Link zum SM Maintenance eines Sensors in einer Maschine. Von hier kann somit in eine Wartungsinformation einer unterlagerten Komponente gesprungen werden.",
                                r"en": r"Link to another SM Maintenance. Example Link to the SM Maintenance of a sensor in a machine. From here, it is possible to jump to the maintenance information of a subordinate component.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/linksmmaintenancecomponentmodulemachine/1/0",
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
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class LinkAASComponentModuleMachine(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"LinkAASComponentModuleMachine",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Link zu einer unterlagerten AAS. Beispiel Link zur Sensors in einer Maschine. Von hier kann somit zu den Inforamtionen einer unterlagerten Komponente gesprungen werden.",
                                r"en": r"Link to a subordinate AAS. Example Link to the sensors in a machine. From here you can jump to the information of a subordinate component.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/linkaascomponentmodulemachine/1/0",
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
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class InstructionMaintenanceStep(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"InstructionMaintenanceStep",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Arbeitsanweisung/ Beschreibung eines Wartungsschritts als Alternative zu dem Sprung in eine Wartungsinformation von unterlagerten Komponenten.",
                                r"en": r"Work instruction/ description of a maintenance step as an alternative to jumping to a maintenance information of subordinate components.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/instructionmaintenancestep/1/0",
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
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class RelatedDocumentOrFileMaintenanceStep(File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[
                            str
                        ] = r"RelatedDocumentOrFileMaintenanceStep",
                        content_type: Optional[str] = r"application/pdf",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Verknüpfung von unterstützenden Dokumenten die zu diesem Wartungsschritt gehören",
                                r"en": r"Linking of supporting documents that belong to this maintenance step.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/relateddocumentorfilemaintenancestep/1/0",
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

                class SparePartForMaintenanceStep(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"SparePartForMaintenanceStep",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Link auf ein in diesem Wartungsschritt benötigtes Ersatzteils. Eine Liste aller benötigten Ersatzteile für eine Wartung befindet sich in der SMC SparePartList des SM Maintenance",
                                r"en": r"Link to a spare part required in this maintenance step. A list of all the spare parts required for maintenance can be found in the SMC SparePartList of the SM Maintenance",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/sparepartformaintenancestep/1/0",
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
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class QuantityOfSparePartForMaintenanceStep(Property):

                    def __init__(
                        self,
                        value: Decimal,
                        id_short: Optional[
                            str
                        ] = r"QuantityOfSparePartForMaintenanceStep",
                        value_type: DataTypeDefXsd = Decimal,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Nummer des in diesem Wartungsschritt benötigten Ersatzteils.",
                                r"en": r"Number of spare part required in this maintenance step.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/quantityofsparepartformaintenancestep/1/0",
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

                class ConsumablesForMaintenanceStep(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"ConsumablesForMaintenanceStep",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Link auf ein benötigtes Verbrauchsmaterial.",
                                r"en": r"Link to a required consumable.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/consumablesformaintenancestep/1/0",
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
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class QuantityOfConsumablesForMaintenanceStep(Property):

                    def __init__(
                        self,
                        value: Decimal,
                        id_short: Optional[
                            str
                        ] = r"QuantityOfConsumablesForMaintenanceStep",
                        value_type: DataTypeDefXsd = Decimal,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Angabe zur benötigten Menge des unter ConsumablesForMaintenanceStep referenzierten Verbrauchmaterials für diesen Wartungsschritt",
                                r"en": r"Indication of the required number of consumables referenced under ConsumablesForMaintenanceStep for this maintenance step.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/quantityofconsumablesformaintenancestep/1/0",
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

                class UnitForQuantityOfConsumablesForMaintenanceStep(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[
                            str
                        ] = r"UnitForQuantityOfConsumablesForMaintenanceStep",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Einheit der benötigten Anzahl des unter ConsumablesForMaintenanceStep referenzierten Verbrauchmaterials für diesen Wartungsschritt. Beispiele: Blatt, Gramm, Milliliter",
                                r"en": r"Unit of the required number of consumables referenced under ConsumablesForMaintenanceStep for this maintenance step. Examples: Sheet, gram, millilitre",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/unitforquantityofconsumablesformaintenancestep/1/0",
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

                class ToolsForMaintenanceStep(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"ToolsForMaintenanceStep",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Verweis auf ein benötigtes Werkzeug. Eine Liste aller benötigten Ersatzteile für eine Wartung befindet sich in der SMC MaintenanceToolList des SM Maintenance",
                                r"en": r"Reference to a required tool. A list of all required spare parts for a maintenance can be found in the SMC MaintenanceToolList of the SM Maintenance",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/toolsformaintenancestep/1/0",
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
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class QuantityOfToolsForMaintenanceStep(Property):

                    def __init__(
                        self,
                        value: Decimal,
                        id_short: Optional[str] = r"QuantityOfToolsForMaintenanceStep",
                        value_type: DataTypeDefXsd = Decimal,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Angabe zur benötigten Anzahl des unter ToolsForMaintenanceStep referenzierten Werkzeugs für diesen Wartungsschritt",
                                r"en": r"Indication of the required number of the tool referenced under ToolsForMaintenanceStep for this maintenance step.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/quantityoftoolsformaintenancestep/1/0",
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

                class DocumentationSignatureMandatory(Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"DocumentationSignatureMandatory",
                        value_type: DataTypeDefXsd = bool,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Vorgabe, ob dieser Wartungsschritt dokumentiert werden muss. O entspricht keine Dokumentation notwendig, 1 entspricht Dokumentation notwendig",
                                r"en": r"Specifies whether this maintenance step must be documented. O corresponds to no documentation necessary, 1 corresponds to documentation necessary",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/documentationsignaturemandatory/1/0",
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

                class EstimatedDurationTimeMaintenanceStep(SubmodelElementCollection):

                    class ValueEstimatedDurationTimeMaintenanceStep(Property):

                        def __init__(
                            self,
                            value: Decimal,
                            id_short: Optional[
                                str
                            ] = r"ValueEstimatedDurationTimeMaintenanceStep",
                            value_type: DataTypeDefXsd = Decimal,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Angabe der Dauer für diesen Wartungsschritt (Wert)",
                                    r"en": r"Indication of the duration for this maintenance step (value)",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/valueestimateddurationtimemaintenancestep/1/0",
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

                    class UnitEstimatedDurationTimeMaintenanceStep(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[
                                str
                            ] = r"UnitEstimatedDurationTimeMaintenanceStep",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Zeiteinheit für den Wert der Dauer für diesen wArtungsschritt - Beispiel Stunden, Tage, Wochen",
                                    r"en": r"Time unit for the value of the duration for this wArting step - example hours, days, weeks",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/unitestimateddurationtimemaintenancestep/1/0",
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
                        valueEstimatedDurationTimeMaintenanceStep: Optional[
                            Union[Decimal, ValueEstimatedDurationTimeMaintenanceStep]
                        ] = None,
                        unitEstimatedDurationTimeMaintenanceStep: Optional[
                            Union[str, UnitEstimatedDurationTimeMaintenanceStep]
                        ] = None,
                        id_short: Optional[
                            str
                        ] = r"EstimatedDurationTimeMaintenanceStep",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Estimated duration for this maintenance step"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/estimateddurationtimemaintenancestep/1/0",
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
                        if (
                            valueEstimatedDurationTimeMaintenanceStep
                            and not isinstance(
                                valueEstimatedDurationTimeMaintenanceStep,
                                SubmodelElement,
                            )
                        ):
                            valueEstimatedDurationTimeMaintenanceStep = (
                                self.ValueEstimatedDurationTimeMaintenanceStep(
                                    valueEstimatedDurationTimeMaintenanceStep
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if unitEstimatedDurationTimeMaintenanceStep and not isinstance(
                            unitEstimatedDurationTimeMaintenanceStep, SubmodelElement
                        ):
                            unitEstimatedDurationTimeMaintenanceStep = (
                                self.UnitEstimatedDurationTimeMaintenanceStep(
                                    unitEstimatedDurationTimeMaintenanceStep
                                )
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            valueEstimatedDurationTimeMaintenanceStep,
                            unitEstimatedDurationTimeMaintenanceStep,
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

                class ConditionForNextMaintenanceStep(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"ConditionForNextMaintenanceStep",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Bedinung für den nächsten Wartungsschritt ",
                                r"en": r"Condition for the next maintenance step ",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/conditionfornextmaintenancestep/1/0",
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
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class NextMaintenanceStep(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"NextMaintenanceStep",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Referenz auf den folgenden Wartungsschritt, wenn die Bedingung erfüllt ist.",
                                r"en": r"Reference to the following maintenance step if the condition is fulfilled.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/nextmaintenancestep/1/0",
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
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ConditionForAlternativeNextStep(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"ConditionForAlternativeNextStep",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Alternativer nächster Schritt, wenn die vorherige Bedingung nicht erfüllt ist. ",
                                r"en": r"Alternative next step if the previous condition is not fulfilled. ",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/conditionforalternativenextstep/1/0",
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
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class AlternativeNextMaintenanceStep(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"AlternativeNextMaintenanceStep",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Referenz auf den folgenden Wartungsschritt, wenn die Bedingung nicht erfüllt ist.",
                                r"en": r"Reference to the following maintenance step if the condition is not fulfilled.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/alternativenextmaintenancestep/1/0",
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
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class EndOfMaintenance(Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"EndOfMaintenance",
                        value_type: DataTypeDefXsd = bool,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Beendigung der Wartung, wenn dies der letzte Wartungsschritt war. 1 = Ende der Wartung erreicht",
                                r"en": r"End of maintenance if this was the last maintenance step. 1 = End of maintenance reached",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/endofmaintenance/1/0",
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
                    maintenanceStepID: Optional[Union[str, MaintenanceStepID]] = None,
                    maintenanceStepName: Optional[
                        Union[LangStringSet, MaintenanceStepName]
                    ] = None,
                    localizationDescription: Optional[
                        Union[LangStringSet, LocalizationDescription]
                    ] = None,
                    linkSMMaintenanceComponentModuleMachine: Optional[
                        Union[Reference, LinkSMMaintenanceComponentModuleMachine]
                    ] = None,
                    linkAASComponentModuleMachine: Optional[
                        Union[Reference, LinkAASComponentModuleMachine]
                    ] = None,
                    instructionMaintenanceStep: Optional[
                        Union[LangStringSet, InstructionMaintenanceStep]
                    ] = None,
                    relatedDocumentOrFileMaintenanceStep: Optional[
                        Iterable[RelatedDocumentOrFileMaintenanceStep]
                    ] = None,
                    sparePartForMaintenanceStep: Optional[
                        Iterable[Union[Reference, SparePartForMaintenanceStep]]
                    ] = None,
                    quantityOfSparePartForMaintenanceStep: Optional[
                        Union[Decimal, QuantityOfSparePartForMaintenanceStep]
                    ] = None,
                    consumablesForMaintenanceStep: Optional[
                        Iterable[Union[Reference, ConsumablesForMaintenanceStep]]
                    ] = None,
                    quantityOfConsumablesForMaintenanceStep: Optional[
                        Iterable[
                            Union[Decimal, QuantityOfConsumablesForMaintenanceStep]
                        ]
                    ] = None,
                    unitForQuantityOfConsumablesForMaintenanceStep: Optional[
                        Union[str, UnitForQuantityOfConsumablesForMaintenanceStep]
                    ] = None,
                    toolsForMaintenanceStep: Optional[
                        Iterable[Union[Reference, ToolsForMaintenanceStep]]
                    ] = None,
                    quantityOfToolsForMaintenanceStep: Optional[
                        Union[Decimal, QuantityOfToolsForMaintenanceStep]
                    ] = None,
                    documentationSignatureMandatory: Optional[
                        Union[bool, DocumentationSignatureMandatory]
                    ] = None,
                    estimatedDurationTimeMaintenanceStep: Optional[
                        EstimatedDurationTimeMaintenanceStep
                    ] = None,
                    conditionForNextMaintenanceStep: Optional[
                        Union[LangStringSet, ConditionForNextMaintenanceStep]
                    ] = None,
                    nextMaintenanceStep: Optional[
                        Union[Reference, NextMaintenanceStep]
                    ] = None,
                    conditionForAlternativeNextStep: Optional[
                        Iterable[Union[LangStringSet, ConditionForAlternativeNextStep]]
                    ] = None,
                    alternativeNextMaintenanceStep: Optional[
                        Iterable[Union[Reference, AlternativeNextMaintenanceStep]]
                    ] = None,
                    endOfMaintenance: Optional[Union[bool, EndOfMaintenance]] = None,
                    id_short: Optional[str] = r"MaintenanceStep",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Sammlung aller Details und Informationen zu einem Wartungsschritt ",
                            r"en": r"Collection of all details and information about a maintenance site",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancestep/1/0",
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

                    # Build a submodel element if a raw value was passed in the argument
                    if maintenanceStepID and not isinstance(
                        maintenanceStepID, SubmodelElement
                    ):
                        maintenanceStepID = self.MaintenanceStepID(maintenanceStepID)

                    # Build a submodel element if a raw value was passed in the argument
                    if maintenanceStepName and not isinstance(
                        maintenanceStepName, SubmodelElement
                    ):
                        maintenanceStepName = self.MaintenanceStepName(
                            maintenanceStepName
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if localizationDescription and not isinstance(
                        localizationDescription, SubmodelElement
                    ):
                        localizationDescription = self.LocalizationDescription(
                            localizationDescription
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if linkSMMaintenanceComponentModuleMachine and not isinstance(
                        linkSMMaintenanceComponentModuleMachine, SubmodelElement
                    ):
                        linkSMMaintenanceComponentModuleMachine = (
                            self.LinkSMMaintenanceComponentModuleMachine(
                                linkSMMaintenanceComponentModuleMachine
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if linkAASComponentModuleMachine and not isinstance(
                        linkAASComponentModuleMachine, SubmodelElement
                    ):
                        linkAASComponentModuleMachine = (
                            self.LinkAASComponentModuleMachine(
                                linkAASComponentModuleMachine
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if instructionMaintenanceStep and not isinstance(
                        instructionMaintenanceStep, SubmodelElement
                    ):
                        instructionMaintenanceStep = self.InstructionMaintenanceStep(
                            instructionMaintenanceStep
                        )

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if sparePartForMaintenanceStep and all(
                        [isinstance(i, Reference) for i in sparePartForMaintenanceStep]
                    ):
                        sparePartForMaintenanceStep = [
                            self.SparePartForMaintenanceStep(i)
                            for i in sparePartForMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument
                    if quantityOfSparePartForMaintenanceStep and not isinstance(
                        quantityOfSparePartForMaintenanceStep, SubmodelElement
                    ):
                        quantityOfSparePartForMaintenanceStep = (
                            self.QuantityOfSparePartForMaintenanceStep(
                                quantityOfSparePartForMaintenanceStep
                            )
                        )

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if consumablesForMaintenanceStep and all(
                        [
                            isinstance(i, Reference)
                            for i in consumablesForMaintenanceStep
                        ]
                    ):
                        consumablesForMaintenanceStep = [
                            self.ConsumablesForMaintenanceStep(i)
                            for i in consumablesForMaintenanceStep
                        ]

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if quantityOfConsumablesForMaintenanceStep and all(
                        [
                            isinstance(i, Decimal)
                            for i in quantityOfConsumablesForMaintenanceStep
                        ]
                    ):
                        quantityOfConsumablesForMaintenanceStep = [
                            self.QuantityOfConsumablesForMaintenanceStep(i)
                            for i in quantityOfConsumablesForMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument
                    if (
                        unitForQuantityOfConsumablesForMaintenanceStep
                        and not isinstance(
                            unitForQuantityOfConsumablesForMaintenanceStep,
                            SubmodelElement,
                        )
                    ):
                        unitForQuantityOfConsumablesForMaintenanceStep = (
                            self.UnitForQuantityOfConsumablesForMaintenanceStep(
                                unitForQuantityOfConsumablesForMaintenanceStep
                            )
                        )

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if toolsForMaintenanceStep and all(
                        [isinstance(i, Reference) for i in toolsForMaintenanceStep]
                    ):
                        toolsForMaintenanceStep = [
                            self.ToolsForMaintenanceStep(i)
                            for i in toolsForMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument
                    if quantityOfToolsForMaintenanceStep and not isinstance(
                        quantityOfToolsForMaintenanceStep, SubmodelElement
                    ):
                        quantityOfToolsForMaintenanceStep = (
                            self.QuantityOfToolsForMaintenanceStep(
                                quantityOfToolsForMaintenanceStep
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if documentationSignatureMandatory and not isinstance(
                        documentationSignatureMandatory, SubmodelElement
                    ):
                        documentationSignatureMandatory = (
                            self.DocumentationSignatureMandatory(
                                documentationSignatureMandatory
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if conditionForNextMaintenanceStep and not isinstance(
                        conditionForNextMaintenanceStep, SubmodelElement
                    ):
                        conditionForNextMaintenanceStep = (
                            self.ConditionForNextMaintenanceStep(
                                conditionForNextMaintenanceStep
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if nextMaintenanceStep and not isinstance(
                        nextMaintenanceStep, SubmodelElement
                    ):
                        nextMaintenanceStep = self.NextMaintenanceStep(
                            nextMaintenanceStep
                        )

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if conditionForAlternativeNextStep and all(
                        [
                            isinstance(i, LangStringSet)
                            for i in conditionForAlternativeNextStep
                        ]
                    ):
                        conditionForAlternativeNextStep = [
                            self.ConditionForAlternativeNextStep(i)
                            for i in conditionForAlternativeNextStep
                        ]

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if alternativeNextMaintenanceStep and all(
                        [
                            isinstance(i, Reference)
                            for i in alternativeNextMaintenanceStep
                        ]
                    ):
                        alternativeNextMaintenanceStep = [
                            self.AlternativeNextMaintenanceStep(i)
                            for i in alternativeNextMaintenanceStep
                        ]

                    # Build a submodel element if a raw value was passed in the argument
                    if endOfMaintenance and not isinstance(
                        endOfMaintenance, SubmodelElement
                    ):
                        endOfMaintenance = self.EndOfMaintenance(endOfMaintenance)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        maintenanceStepID,
                        maintenanceStepName,
                        localizationDescription,
                        linkSMMaintenanceComponentModuleMachine,
                        linkAASComponentModuleMachine,
                        instructionMaintenanceStep,
                        relatedDocumentOrFileMaintenanceStep,
                        sparePartForMaintenanceStep,
                        quantityOfSparePartForMaintenanceStep,
                        consumablesForMaintenanceStep,
                        quantityOfConsumablesForMaintenanceStep,
                        unitForQuantityOfConsumablesForMaintenanceStep,
                        toolsForMaintenanceStep,
                        quantityOfToolsForMaintenanceStep,
                        documentationSignatureMandatory,
                        estimatedDurationTimeMaintenanceStep,
                        conditionForNextMaintenanceStep,
                        nextMaintenanceStep,
                        conditionForAlternativeNextStep,
                        alternativeNextMaintenanceStep,
                        endOfMaintenance,
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
                maintenanceStep: Optional[Iterable[MaintenanceStep]] = None,
                id_short: Optional[str] = r"ListMaintenanceSteps",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"de": r"Auflistung der einzelnen Wartungsschritte inkl. aller benötigten Details je Wartungsschritt",
                        r"en": r"Listing of the individual maintenance steps incl. all required details per maintenance step",
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/maintenanceinstructions/listmaintenancesteps/1/0",
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

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [maintenanceStep]:
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
            maintenanceTechnicians: Optional[MaintenanceTechnicians] = None,
            listMaintenanceSteps: Optional[ListMaintenanceSteps] = None,
            id_short: Optional[str] = r"MaintenanceInstructionsForSpecificInterval",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"de": r"Wartungsdetails für eine spezifischen Zeitinterval - Beispiel Wartung nach 6 Monaten",
                    r"en": r"Collection that includes all the details of a maintenance interval. ",
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenanceinstructionsforspecificinterval/1/0",
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
                        value=r"ZeroToMany",
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
            for se_arg in [maintenanceTechnicians, listMaintenanceSteps]:
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

    class MaintenanceToolList(SubmodelElementList):

        class Maintenancetoollist_item(SubmodelElementCollection):

            class ToolID(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ToolID",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"ID des Werkzeugs",
                            r"en": r"An ID can be assigned to uniquely identify a tool.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/toolid/1/0",
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

            class ToolName(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"ToolName",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Ein Name für das Werkzeug kann gespeichert werden, um das Werkzeug für Menschen verständlicher zu machen.",
                            r"en": r"A name for the tool can be stored to make the tool more understandable for humans.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/toolname/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class CollectionMaxQuantityOfTool(SubmodelElementCollection):

                class CollectionMaxQuantityOfToolForSpecificInterval(
                    SubmodelElementCollection
                ):

                    class MaxQuantityOfTool(Property):

                        def __init__(
                            self,
                            value: Decimal,
                            id_short: Optional[str] = r"MaxQuantityOfTool",
                            value_type: DataTypeDefXsd = Decimal,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Benötigte Gesamtanzahl des Werkzeugs für einen Wartungsinterval",
                                    r"en": r"Total number of tools required for specific maintenance interval",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/maxquantityoftool/1/0",
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

                    class ReferenceNameOfMaintenance(ReferenceElement):

                        def __init__(
                            self,
                            value: Reference,
                            id_short: Optional[str] = r"ReferenceNameOfMaintenance",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Referenz zur ID eines spezifischen Wartungsintervals",
                                    r"en": r"Reference to ID of specific maintenance interval",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmaintenance/1/0",
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
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ReferenceToMaintenanceID(ReferenceElement):

                        def __init__(
                            self,
                            value: Reference,
                            id_short: Optional[str] = r"ReferenceToMaintenanceID",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Referenz zur ID eines spezifischen Wartungsintervals",
                                    r"en": r"Reference to ID of specific maintenance interval",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmaintenance/1/0",
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
                        maxQuantityOfTool: Optional[
                            Union[Decimal, MaxQuantityOfTool]
                        ] = None,
                        referenceNameOfMaintenance: Optional[
                            Union[Reference, ReferenceNameOfMaintenance]
                        ] = None,
                        referenceToMaintenanceID: Optional[
                            Union[Reference, ReferenceToMaintenanceID]
                        ] = None,
                        id_short: Optional[
                            str
                        ] = r"CollectionMaxQuantityOfToolForSpecificInterval",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Kollektion Benötige Anzahl des Werkzeugs für ein spezifisches Wartungsintervall.",
                                r"en": r"Collection Total quantity of tools required for one specific maintenance intervals.",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/collectionmaxquantityoftoolforspecificinterval/1/0",
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
                        if maxQuantityOfTool and not isinstance(
                            maxQuantityOfTool, SubmodelElement
                        ):
                            maxQuantityOfTool = self.MaxQuantityOfTool(
                                maxQuantityOfTool
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if referenceNameOfMaintenance and not isinstance(
                            referenceNameOfMaintenance, SubmodelElement
                        ):
                            referenceNameOfMaintenance = (
                                self.ReferenceNameOfMaintenance(
                                    referenceNameOfMaintenance
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if referenceToMaintenanceID and not isinstance(
                            referenceToMaintenanceID, SubmodelElement
                        ):
                            referenceToMaintenanceID = self.ReferenceToMaintenanceID(
                                referenceToMaintenanceID
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            maxQuantityOfTool,
                            referenceNameOfMaintenance,
                            referenceToMaintenanceID,
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
                    collectionMaxQuantityOfToolForSpecificInterval: Optional[
                        CollectionMaxQuantityOfToolForSpecificInterval
                    ] = None,
                    id_short: Optional[str] = r"CollectionMaxQuantityOfTool",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Liste der Werkzeuge, die für alle Wartungsintervalle einer Anlage benötigt werden. Die Menge richtet sich nach den verschiedenen Wartungsintervallen. Jede Menge pro Wartungsintervall wird in einer eigenen SMC beschrieben/definiert.",
                            r"en": r"List of tools required for all maintenance intervals of an asset. The quantity is devied by the different maintenance intervals. Each quantity per maintenance interval is described/ defined in an own SMC.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/collectionmaxquantityoftool/1/0",
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

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [collectionMaxQuantityOfToolForSpecificInterval]:
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

            class CompanyNameToolSupplier(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"CompanyNameToolSupplier",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Name des Werkzeugherstellers",
                            r"en": r"Name of the tool manufacturer",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/companynametoolsupplier/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class OrderCodeToolOfManufacturer(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OrderCodeToolOfManufacturer",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Eine vom Hersteller vergebene eindeutige Kombination aus Zahlen und Buchstaben, die zur Identifizierung des Werkzeugs bei der Bestellung verwendet wird",
                            r"en": r"unique combination of numbers and letters issued by the manufacturer that is used to identify the tool for ordering",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0112/2///61987#ABA950#008",
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
                                    value=r"0173-1#02-AAO227#004",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ToolDescription(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"ToolDescription",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Detaillierte Beschreibung des Werkzeugs",
                            r"en": r"Detailed description of the tool",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/tooldescription/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AddressOfAdditionalLinkTool(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AddressOfAdditionalLinkTool",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Web site address where information about the tool is given, e.g. link to shop"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAQ326#004",
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
                toolID: Optional[Union[str, ToolID]] = None,
                toolName: Optional[Union[LangStringSet, ToolName]] = None,
                collectionMaxQuantityOfTool: Optional[
                    CollectionMaxQuantityOfTool
                ] = None,
                companyNameToolSupplier: Optional[
                    Union[LangStringSet, CompanyNameToolSupplier]
                ] = None,
                orderCodeToolOfManufacturer: Optional[
                    Union[str, OrderCodeToolOfManufacturer]
                ] = None,
                toolDescription: Optional[
                    Iterable[Union[LangStringSet, ToolDescription]]
                ] = None,
                addressOfAdditionalLinkTool: Optional[
                    Iterable[Union[str, AddressOfAdditionalLinkTool]]
                ] = None,
                id_short: Optional[str] = r"maintenancetoollist_item",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"de": r"Die Sammlung enthält alle Informationen und Details zu einem Werkzeug, das für die Wartung benötigt wird. Dazu gehören der Name, die Bestellnummer, der Hersteller und eine Beschreibung.",
                        r"en": r"The collection contains all the information and details about a tool needed for maintenance. This includes the name, order number, manufacturer and a description.",
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancetool/1/0",
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

                # Build a submodel element if a raw value was passed in the argument
                if toolID and not isinstance(toolID, SubmodelElement):
                    toolID = self.ToolID(toolID)

                # Build a submodel element if a raw value was passed in the argument
                if toolName and not isinstance(toolName, SubmodelElement):
                    toolName = self.ToolName(toolName)

                # Build a submodel element if a raw value was passed in the argument
                if companyNameToolSupplier and not isinstance(
                    companyNameToolSupplier, SubmodelElement
                ):
                    companyNameToolSupplier = self.CompanyNameToolSupplier(
                        companyNameToolSupplier
                    )

                # Build a submodel element if a raw value was passed in the argument
                if orderCodeToolOfManufacturer and not isinstance(
                    orderCodeToolOfManufacturer, SubmodelElement
                ):
                    orderCodeToolOfManufacturer = self.OrderCodeToolOfManufacturer(
                        orderCodeToolOfManufacturer
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if toolDescription and all(
                    [isinstance(i, LangStringSet) for i in toolDescription]
                ):
                    toolDescription = [self.ToolDescription(i) for i in toolDescription]

                # Build a list of submodel elements if a raw values were passed in the argument
                if addressOfAdditionalLinkTool and all(
                    [isinstance(i, str) for i in addressOfAdditionalLinkTool]
                ):
                    addressOfAdditionalLinkTool = [
                        self.AddressOfAdditionalLinkTool(i)
                        for i in addressOfAdditionalLinkTool
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    toolID,
                    toolName,
                    collectionMaxQuantityOfTool,
                    companyNameToolSupplier,
                    orderCodeToolOfManufacturer,
                    toolDescription,
                    addressOfAdditionalLinkTool,
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
            maintenancetoollist_items: Optional[
                Iterable[Maintenancetoollist_item]
            ] = None,
            id_short: Optional[str] = r"MaintenanceToolList",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"de": r"Gesamtliste der benötigten Werkzeuge für alle Wartungsintervalle eines Assets",
                    r"en": r"Total list of tools required for all maintenance intervals of an asset",
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancetoollist/1/0",
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
            for se_arg in [maintenancetoollist_items]:
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

    class MaintenanceConsumablesList(SubmodelElementList):

        class Maintenanceconsumableslist_item(SubmodelElementCollection):

            class ConsumableID(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ConsumableID",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"An ID can be assigned to uniquely identify a consumable, e.g. the globalAssetId of the tool."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/consumableid/1/0",
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

            class ConsumableName(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"ConsumableName",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"A name for the consumable can be stored to name the consumable more understandable for humans."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/consumablename/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class CollectionQuantityOfConsumable(SubmodelElementCollection):

                class QuantityOfConsumableForSpecificInterval(
                    SubmodelElementCollection
                ):

                    class QuantityOfConsumable(Property):

                        def __init__(
                            self,
                            value: Decimal,
                            id_short: Optional[str] = r"QuantityOfConsumable",
                            value_type: DataTypeDefXsd = Decimal,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Benötigte Gesamtanzahl des Verbrauchsmaterials für einen Wartungsinterval",
                                    r"en": r"Total number of consumble required for specific maintenance interval",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/quantityofconsumable/1/0",
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

                    class ReferenceNameOfMaintenance(ReferenceElement):

                        def __init__(
                            self,
                            value: Reference,
                            id_short: Optional[str] = r"ReferenceNameOfMaintenance",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Referenz zu Namen eines spezifischen Wartungsintervals",
                                    r"en": r"Referenceto name of specific maintenance interval",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmanintainance/1/0",
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
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ReferenceToMaintenanceID(ReferenceElement):

                        def __init__(
                            self,
                            value: Reference,
                            id_short: Optional[str] = r"ReferenceToMaintenanceID",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"de": r"Referenz zur ID eines spezifischen Wartungsintervals",
                                    r"en": r"Reference to ID of specific maintenance interval",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/maintenanceinstructions/referencenameofmaintenance/1/0",
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
                        quantityOfConsumable: Optional[
                            Union[Decimal, QuantityOfConsumable]
                        ] = None,
                        referenceNameOfMaintenance: Optional[
                            Union[Reference, ReferenceNameOfMaintenance]
                        ] = None,
                        referenceToMaintenanceID: Optional[
                            Union[Reference, ReferenceToMaintenanceID]
                        ] = None,
                        id_short: Optional[
                            str
                        ] = r"QuantityOfConsumableForSpecificInterval",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"de": r"Kollektion benötige Anzahl des Verbrauchmaterials für ein spezifisches Wartungsintervall",
                                r"en": r"Collection total quantity of consumable required for a specific maintenance intervals",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/maintenanceinstructions/quantityofconsumableforspecificinterval/1/0",
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
                        if quantityOfConsumable and not isinstance(
                            quantityOfConsumable, SubmodelElement
                        ):
                            quantityOfConsumable = self.QuantityOfConsumable(
                                quantityOfConsumable
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if referenceNameOfMaintenance and not isinstance(
                            referenceNameOfMaintenance, SubmodelElement
                        ):
                            referenceNameOfMaintenance = (
                                self.ReferenceNameOfMaintenance(
                                    referenceNameOfMaintenance
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if referenceToMaintenanceID and not isinstance(
                            referenceToMaintenanceID, SubmodelElement
                        ):
                            referenceToMaintenanceID = self.ReferenceToMaintenanceID(
                                referenceToMaintenanceID
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            quantityOfConsumable,
                            referenceNameOfMaintenance,
                            referenceToMaintenanceID,
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
                    quantityOfConsumableForSpecificInterval: Optional[
                        QuantityOfConsumableForSpecificInterval
                    ] = None,
                    id_short: Optional[str] = r"CollectionQuantityOfConsumable",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Sammelmenge des für die Wartungsintervalle benötigten Verbrauchsmaterials.",
                            r"en": r"Collection quantity of consumable required for maintenance intervals.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/collectionquantityofconsumables/1/0",
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

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [quantityOfConsumableForSpecificInterval]:
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

            class UnitMaxQuantityOfConsumable(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"UnitMaxQuantityOfConsumable",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Einheit zur benötigten Gesamtmenge des Verbauchsmaterials. Beispiel: Blatt, Milliliter, Gramm, ...",
                            r"en": r"Unit for the total quantity of consumable material required. Example: sheet, millilitre, gram, ...",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/unitmaxquantityofconsumable/1/0",
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

            class CompanyNameSupplierConsumable(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"CompanyNameSupplierConsumable",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Name des Verbrauchsmaterialherstellers z.B. Max Mustermann GmbH",
                            r"en": r"Name of the consumables manufacturer e.g. Max Mustermann GmbH",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/companynamesupplierconsumable/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class OrderCodeConsumableOfManufacturer(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OrderCodeConsumableOfManufacturer",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"unique combination of numbers and letters issued by the manufacturer that is used to identify the consumable for ordering"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0112/2///61987#ABA950#008",
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
                                    value=r"0173-1#02-AAO227#004",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ConsumableDescription(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"ConsumableDescription",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Beschreibung des Verbauchsmaterials. Beispiel: Reinigungspapier; Farbe blau; Blattgröße 380x 380 mm doppellagig.",
                            r"en": r"Description of the consumables. Example: Cleaning paper; colour blue; sheet size 380x 380 mm double-ply.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/consumabledescription/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class DisposalInstructionsForConsumable(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"DisposalInstructionsForConsumable",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Angabe zur fachgerechten Entsorgung des Verbauchsmaterials.",
                            r"en": r"Information on the proper disposal of the consumables.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/disposalinstructionsforconsumable/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AddressOfAdditionalLinkConsumable(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AddressOfAdditionalLinkConsumable",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Web site address where information about the consumable is given, e.g. link to shop"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAQ326#004",
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
                consumableID: Optional[Union[str, ConsumableID]] = None,
                consumableName: Optional[Union[LangStringSet, ConsumableName]] = None,
                collectionQuantityOfConsumable: Optional[
                    CollectionQuantityOfConsumable
                ] = None,
                unitMaxQuantityOfConsumable: Optional[
                    Union[str, UnitMaxQuantityOfConsumable]
                ] = None,
                companyNameSupplierConsumable: Optional[
                    Union[LangStringSet, CompanyNameSupplierConsumable]
                ] = None,
                orderCodeConsumableOfManufacturer: Optional[
                    Union[str, OrderCodeConsumableOfManufacturer]
                ] = None,
                consumableDescription: Optional[
                    Iterable[Union[LangStringSet, ConsumableDescription]]
                ] = None,
                disposalInstructionsForConsumable: Optional[
                    Iterable[Union[LangStringSet, DisposalInstructionsForConsumable]]
                ] = None,
                addressOfAdditionalLinkConsumable: Optional[
                    Iterable[Union[str, AddressOfAdditionalLinkConsumable]]
                ] = None,
                id_short: Optional[str] = r"maintenanceconsumableslist_item",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"de": r"Die Sammlung enthält alle Informationen und Details zu einem Verbrauchsmaterial, das für die Wartung benötigt wird. Dazu gehören die Bezeichnung, die Bestellnummer, der Hersteller und eine Beschreibung.",
                        r"en": r"The collection contains all information and details about a consumable required for maintenance. This includes the designation, order number, manufacturer and a description.",
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenanceconsumable/1/0",
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

                # Build a submodel element if a raw value was passed in the argument
                if consumableID and not isinstance(consumableID, SubmodelElement):
                    consumableID = self.ConsumableID(consumableID)

                # Build a submodel element if a raw value was passed in the argument
                if consumableName and not isinstance(consumableName, SubmodelElement):
                    consumableName = self.ConsumableName(consumableName)

                # Build a submodel element if a raw value was passed in the argument
                if unitMaxQuantityOfConsumable and not isinstance(
                    unitMaxQuantityOfConsumable, SubmodelElement
                ):
                    unitMaxQuantityOfConsumable = self.UnitMaxQuantityOfConsumable(
                        unitMaxQuantityOfConsumable
                    )

                # Build a submodel element if a raw value was passed in the argument
                if companyNameSupplierConsumable and not isinstance(
                    companyNameSupplierConsumable, SubmodelElement
                ):
                    companyNameSupplierConsumable = self.CompanyNameSupplierConsumable(
                        companyNameSupplierConsumable
                    )

                # Build a submodel element if a raw value was passed in the argument
                if orderCodeConsumableOfManufacturer and not isinstance(
                    orderCodeConsumableOfManufacturer, SubmodelElement
                ):
                    orderCodeConsumableOfManufacturer = (
                        self.OrderCodeConsumableOfManufacturer(
                            orderCodeConsumableOfManufacturer
                        )
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if consumableDescription and all(
                    [isinstance(i, LangStringSet) for i in consumableDescription]
                ):
                    consumableDescription = [
                        self.ConsumableDescription(i) for i in consumableDescription
                    ]

                # Build a list of submodel elements if a raw values were passed in the argument
                if disposalInstructionsForConsumable and all(
                    [
                        isinstance(i, LangStringSet)
                        for i in disposalInstructionsForConsumable
                    ]
                ):
                    disposalInstructionsForConsumable = [
                        self.DisposalInstructionsForConsumable(i)
                        for i in disposalInstructionsForConsumable
                    ]

                # Build a list of submodel elements if a raw values were passed in the argument
                if addressOfAdditionalLinkConsumable and all(
                    [isinstance(i, str) for i in addressOfAdditionalLinkConsumable]
                ):
                    addressOfAdditionalLinkConsumable = [
                        self.AddressOfAdditionalLinkConsumable(i)
                        for i in addressOfAdditionalLinkConsumable
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    consumableID,
                    consumableName,
                    collectionQuantityOfConsumable,
                    unitMaxQuantityOfConsumable,
                    companyNameSupplierConsumable,
                    orderCodeConsumableOfManufacturer,
                    consumableDescription,
                    disposalInstructionsForConsumable,
                    addressOfAdditionalLinkConsumable,
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
            maintenanceconsumableslist_items: Optional[
                Iterable[Maintenanceconsumableslist_item]
            ] = None,
            id_short: Optional[str] = r"MaintenanceConsumablesList",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"de": r"Gesamtliste der benötigten Verbrauchsmaterialien für alle Wartungsintervalle",
                    r"en": r"Total list of consumables required for all maintenance intervals of an asset. Each consumable is described/defined in its own SMC’s",
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenanceconsumableslist/1/0",
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
            for se_arg in [maintenanceconsumableslist_items]:
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

    class MaintenanceSparePartList(SubmodelElementList):

        class Maintenancesparepartlist_item(SubmodelElementCollection):

            class SparePartID(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SparePartID",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"An ID can be assigned to uniquely identify a spare part, e.g. the globalAssetId of the spare part."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/sparepartid/1/0",
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

            class SparePartName(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"SparePartName",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Eine Bezeichnung des Ersatzteils kann gespeichert werden, um das Ersatzteil für den Menschen verständlicher zu benennen.",
                            r"en": r"A designation of the spare part can be stored to name the spare part more understandable for people.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/sparepartname/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class CollectionQuantityOfSparePart(SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"CollectionQuantityOfSparePart",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Kollektion benötige Anzahl des Ersatzteils für die Wartungsintervalle.",
                            r"en": r"Collection quantity of spare part required for maintenance intervals.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/collectionquantityofsparepart/1/0",
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

            class CompanyNameSupplierSparePart(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"CompanyNameSupplierSparePart",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Name des Ersatzteilherstellers z.B. Max Mustermann GmbH",
                            r"en": r"Name of the spare parts manufacturer e.g. Max Mustermann GmbH",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/companynamesuppliersparepart/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class OrderCodeSparePartOfManufacturer(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OrderCodeSparePartOfManufacturer",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"unique combination of numbers and letters issued by the manufacturer that is used to identify the spare part for ordering"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0112/2///61987#ABA950#008",
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

            class SparePartDescription(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"SparePartDescription",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Beschreibung des Ersatzteils.",
                            r"en": r"Description of the spare part.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/sparepartdescription/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class DisposalInstructionsForSparePart(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"DisposalInstructionsForSparePart",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"de": r"Angabe zur fachgerechten Entsorgung des Ersatzteils.",
                            r"en": r"Information on the proper disposal of the spare part.",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/maintenanceinstructions/disposalinstructionsforsparepart/1/0",
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
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AddressOfAdditionalLinkSparePart(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AddressOfAdditionalLinkSparePart",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Web site address where information about the consumable is given, e.g. link to shop"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAQ326#004",
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
                sparePartID: Optional[Union[str, SparePartID]] = None,
                sparePartName: Optional[Union[LangStringSet, SparePartName]] = None,
                collectionQuantityOfSparePart: Optional[
                    CollectionQuantityOfSparePart
                ] = None,
                companyNameSupplierSparePart: Optional[
                    Union[LangStringSet, CompanyNameSupplierSparePart]
                ] = None,
                orderCodeSparePartOfManufacturer: Optional[
                    Union[str, OrderCodeSparePartOfManufacturer]
                ] = None,
                sparePartDescription: Optional[
                    Iterable[Union[LangStringSet, SparePartDescription]]
                ] = None,
                disposalInstructionsForSparePart: Optional[
                    Iterable[Union[LangStringSet, DisposalInstructionsForSparePart]]
                ] = None,
                addressOfAdditionalLinkSparePart: Optional[
                    Iterable[Union[str, AddressOfAdditionalLinkSparePart]]
                ] = None,
                id_short: Optional[str] = r"maintenancesparepartlist_item",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"de": r"Die Sammlung enthält alle Informationen und Details zu einem Verbrauchsmaterial, das für die Wartung benötigt wird. Dazu gehören die Bezeichnung, die Bestellnummer, der Hersteller und eine Beschreibung.",
                        r"en": r"The collection contains all information and details about a consumable required for maintenance. This includes the designation, order number, manufacturer and a description.",
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"htthttps://admin-shell.io/idta/maintenanceinstructions/maintenancesparepart/1/0",
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

                # Build a submodel element if a raw value was passed in the argument
                if sparePartID and not isinstance(sparePartID, SubmodelElement):
                    sparePartID = self.SparePartID(sparePartID)

                # Build a submodel element if a raw value was passed in the argument
                if sparePartName and not isinstance(sparePartName, SubmodelElement):
                    sparePartName = self.SparePartName(sparePartName)

                # Build a submodel element if a raw value was passed in the argument
                if companyNameSupplierSparePart and not isinstance(
                    companyNameSupplierSparePart, SubmodelElement
                ):
                    companyNameSupplierSparePart = self.CompanyNameSupplierSparePart(
                        companyNameSupplierSparePart
                    )

                # Build a submodel element if a raw value was passed in the argument
                if orderCodeSparePartOfManufacturer and not isinstance(
                    orderCodeSparePartOfManufacturer, SubmodelElement
                ):
                    orderCodeSparePartOfManufacturer = (
                        self.OrderCodeSparePartOfManufacturer(
                            orderCodeSparePartOfManufacturer
                        )
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if sparePartDescription and all(
                    [isinstance(i, LangStringSet) for i in sparePartDescription]
                ):
                    sparePartDescription = [
                        self.SparePartDescription(i) for i in sparePartDescription
                    ]

                # Build a list of submodel elements if a raw values were passed in the argument
                if disposalInstructionsForSparePart and all(
                    [
                        isinstance(i, LangStringSet)
                        for i in disposalInstructionsForSparePart
                    ]
                ):
                    disposalInstructionsForSparePart = [
                        self.DisposalInstructionsForSparePart(i)
                        for i in disposalInstructionsForSparePart
                    ]

                # Build a list of submodel elements if a raw values were passed in the argument
                if addressOfAdditionalLinkSparePart and all(
                    [isinstance(i, str) for i in addressOfAdditionalLinkSparePart]
                ):
                    addressOfAdditionalLinkSparePart = [
                        self.AddressOfAdditionalLinkSparePart(i)
                        for i in addressOfAdditionalLinkSparePart
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    sparePartID,
                    sparePartName,
                    collectionQuantityOfSparePart,
                    companyNameSupplierSparePart,
                    orderCodeSparePartOfManufacturer,
                    sparePartDescription,
                    disposalInstructionsForSparePart,
                    addressOfAdditionalLinkSparePart,
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
            maintenancesparepartlist_items: Optional[
                Iterable[Maintenancesparepartlist_item]
            ] = None,
            id_short: Optional[str] = r"MaintenanceSparePartList",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"de": r"Gesamtliste der benötigten Ersatzteile für alle Wartungsintervalle",
                    r"en": r"Total list of required spare parts for all maintenance intervals of an asset. Each spare part is described/ defined in its own SMC.",
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/maintenanceinstructions/maintenancesparepartlist/1/0",
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
            for se_arg in [maintenancesparepartlist_items]:
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
        maintenanceFreeAsset: Union[bool, MaintenanceFreeAsset],
        maintenanceInstructionsForSpecificInterval: Optional[
            Iterable[MaintenanceInstructionsForSpecificInterval]
        ] = None,
        maintenanceToolList: Optional[MaintenanceToolList] = None,
        maintenanceConsumablesList: Optional[MaintenanceConsumablesList] = None,
        maintenanceSparePartList: Optional[MaintenanceSparePartList] = None,
        id_short: Optional[str] = r"MaintenanceInstructions",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"de": r"Submodell zur Übermittlung aller wartungsrelevanten Informatationen",
                r"en": r"The Submodel defines a set of maintenance instructions and additional details, files or documents related to the maintenance of an asset",
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell-io/idta-02018",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(
                Key(
                    type_=KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/MaintenanceInstructions/1/0",
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

        # Build a submodel element if a raw value was passed in the argument
        if maintenanceFreeAsset and not isinstance(
            maintenanceFreeAsset, SubmodelElement
        ):
            maintenanceFreeAsset = self.MaintenanceFreeAsset(maintenanceFreeAsset)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            maintenanceFreeAsset,
            maintenanceInstructionsForSpecificInterval,
            maintenanceToolList,
            maintenanceConsumablesList,
            maintenanceSparePartList,
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
