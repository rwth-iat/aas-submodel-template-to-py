from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class PredictiveMaintenance(aas.Submodel):

    class RemainingUsefulLifePrediction(aas.SubmodelElementCollection):

        class RemainingUsefulLifetime(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RemainingUsefulLifetime",
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
                            value=r"https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLifetime/1/0",
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
                            id_short=r"IndicationType",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=None,
                            description=aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Type of wear-relevant duration, e.g. time, cycles, distance, etc.",
                                    r"de": r"Art der verschleißrelevanten Dauer, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                                }
                            ),
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PredictiveMaintenance/IndicationType/1/0",
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
                            id_short=r"DurationValue",
                            value_type=float,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=None,
                            description=aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Value of duration in the wear relevant unit, e.g. time, operation cycles, distance, etc.",
                                    r"de": r"Zahlenwert der Dauer in der verschleißrelevanten Einheit, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                                }
                            ),
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PredictiveMaintenance/DurationValue/1/0",
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
                            id_short=r"EngineeringUnit",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=None,
                            description=aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Wear relevant physical unit, e.g. time, operation cycles, distance, etc.",
                                    r"de": r"Verschleißrelevante physikalische Einheit, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                                }
                            ),
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PredictiveMaintenance/EngineeringUnit/1/0",
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
                            id_short=r"StartValue",
                            value_type=float,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=None,
                            description=aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Starting value from which the duration is measured in the wear-relevant unit, e.g. time, cycles, distance, etc.",
                                    r"de": r"Startwert, von dem ab die Dauer gemessen wird in der verschleißrelevanten Einheit, z.B. Zeit, Zyklen, Wegstrecke, etc.",
                                }
                            ),
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PredictiveMaintenance/StartValue/1/0",
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
                            id_short=r"StartDateTime",
                            value_type=xsd.DateTime,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=None,
                            description=aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Start date and time from which the duration is measured",
                                    r"de": r"Startdatum und -zeit, von der ab die Dauer gemessen wird",
                                }
                            ),
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PredictiveMaintenance/StartDateTime/1/0",
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
                            id_short=r"Description",
                            value_type=str,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=None,
                            description=aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the wear duration information",
                                    r"de": r"Beschreibung der Angabe zur verschleißrelevanten Dauer",
                                }
                            ),
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/PredictiveMaintenance/Description/1/0",
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

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Remaining useful life time, bades on Lifetime model of OPC Foundation (https://reference.opcfoundation.org/DI/v104/docs/10)",
                            r"de": r"Verbleibende Betriebszeit in Anlehnung an Lifetime model der OPC Foundation (https://reference.opcfoundation.org/DI/v104/docs/10)",
                        }
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

        class RemainingUsfulLifeDateTime(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"RemainingUsfulLifeDateTime",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsfulLifeDateTime/1/0",
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
                            r"en": r"mark attributed to an instant by means of a specified timescale, expressed as a date and a time",
                            r"de": r"Markierung, zugeordnet zu einem Moment mittles einer spezifischen Zeitskala, ausgedrückt als Datum und Uhrzeit",
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ConfidenceInterval(aas.Range):

            def __init__(
                self,
                min: float,
                max: float,
                id_short: Optional[str] = r"ConfidenceInterval",
                value_type: aas.DataTypeDefXsd = float,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PredictiveMaintenance/ConfidenceInterval/1/0",
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
                            r"en": r"confidence interval, measured in the unit of the predicted value",
                            r"de": r"Konfidenzintervall in der Einheit des prognositizierten Wertes",
                        }
                    )

                if qualifier is None:
                    qualifier = ()

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

        class ListRULBoundaryConditions(aas.SubmodelElementList):

            class Listrulboundaryconditions_item(aas.SubmodelElementCollection):

                class ConditionName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ConditionName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0",
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
                                    r"en": r"Name of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL prediction is valid.",
                                    r"de": r"Bezeichnung des Indikators (Prozesswert, KPI, Materialeigenschaft, Anlageneigenschaft), der eine Randbedingung beschreibt, für die die RUL-Vorhersage gültig ist.",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class IsBoundaryConditionUsedInModel(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"IsBoundaryConditionUsedInModel",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryConditionUsedInModel/1/0",
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
                                    r"en": r"If this boundary condition is used in the model for RUL prediction true, else false",
                                    r"de": r"Wenn diese Randbedingung im Modell für die RUL Prognose verwendet true sonst false",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class BoundaryValueRange(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"BoundaryValueRange",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/1/0",
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
                                    r"en": r"Value range of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL prediction is valid.",
                                    r"de": r"Wertebereich des Indikators (Prozesswert, KPI, Materialeigenschaft, Anlageneigenschaft), der eine Randbedingung beschreibt, für die die RUL-Vorhersage gültig ist.",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class BoundaryEngineeringUnit(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"BoundaryEngineeringUnit",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineeringUnit/1/0",
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
                                    r"en": r"Engineering Unit of the boundary condition indicator",
                                    r"de": r"Physikalische Einheit des Indikators, der die Randbedingung beschreibt",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class DriftInfoAIModel(aas.Range):

                    def __init__(
                        self,
                        min: float,
                        max: float,
                        id_short: Optional[str] = r"DriftInfoAIModel",
                        value_type: aas.DataTypeDefXsd = float,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0",
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
                                    r"en": r"Drift information of AI model",
                                    r"de": r"Drift Information of AI Model",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

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

                class MeanValue(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"MeanValue",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0",
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
                                    r"en": r"Mean value of the distribution of indicator values",
                                    r"de": r"Mttelwert der Verteilung des Indikators",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Standarddeviation(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"Standarddeviation",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1/0",
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
                                    r"en": r"Standard deviation of the distribution of indicator values",
                                    r"de": r"Standardabweichung der Verteilung des Indikators",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Skewness(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"Skewness",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0",
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
                                    r"en": r"Skewness of the distribution of indicator values",
                                    r"de": r"Schiefe der Verteilung des Indikators",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class BoundaryDescription(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"BoundaryDescription",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription/1/0",
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
                                    r"en": r"Description of the boundary of a RUL prediction condition",
                                    r"de": r"Beschreibung einer RUL Vorhersage-Randbedingung",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
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
                    conditionName: Union[str, ConditionName],
                    isBoundaryConditionUsedInModel: Union[
                        bool, IsBoundaryConditionUsedInModel
                    ],
                    boundaryValueRange: Union[float, BoundaryValueRange],
                    boundaryEngineeringUnit: Union[str, BoundaryEngineeringUnit],
                    driftInfoAIModel: Optional[
                        Union[Tuple[float, float], DriftInfoAIModel]
                    ] = None,
                    meanValue: Optional[Union[float, MeanValue]] = None,
                    standarddeviation: Optional[Union[float, Standarddeviation]] = None,
                    skewness: Optional[Union[float, Skewness]] = None,
                    boundaryDescription: Optional[
                        Union[str, BoundaryDescription]
                    ] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0",
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
                                r"en": r"Boundary condition for which remaining useful life has been predicted",
                                r"de": r"Randbedingung unter der die nutzbare Restlebensdauer prognositiziert wurde",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if conditionName is not None and not isinstance(
                        conditionName, aas.SubmodelElement
                    ):
                        conditionName = self.ConditionName(conditionName)

                    # Build a submodel element if a raw value was passed in the argument

                    if isBoundaryConditionUsedInModel is not None and not isinstance(
                        isBoundaryConditionUsedInModel, aas.SubmodelElement
                    ):
                        isBoundaryConditionUsedInModel = (
                            self.IsBoundaryConditionUsedInModel(
                                isBoundaryConditionUsedInModel
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if boundaryValueRange is not None and not isinstance(
                        boundaryValueRange, aas.SubmodelElement
                    ):
                        boundaryValueRange = self.BoundaryValueRange(boundaryValueRange)

                    # Build a submodel element if a raw value was passed in the argument

                    if boundaryEngineeringUnit is not None and not isinstance(
                        boundaryEngineeringUnit, aas.SubmodelElement
                    ):
                        boundaryEngineeringUnit = self.BoundaryEngineeringUnit(
                            boundaryEngineeringUnit
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if driftInfoAIModel is not None and not isinstance(
                        driftInfoAIModel, aas.SubmodelElement
                    ):
                        driftInfoAIModel = self.DriftInfoAIModel(
                            min=driftInfoAIModel[0], max=driftInfoAIModel[1]
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if meanValue is not None and not isinstance(
                        meanValue, aas.SubmodelElement
                    ):
                        meanValue = self.MeanValue(meanValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if standarddeviation is not None and not isinstance(
                        standarddeviation, aas.SubmodelElement
                    ):
                        standarddeviation = self.Standarddeviation(standarddeviation)

                    # Build a submodel element if a raw value was passed in the argument

                    if skewness is not None and not isinstance(
                        skewness, aas.SubmodelElement
                    ):
                        skewness = self.Skewness(skewness)

                    # Build a submodel element if a raw value was passed in the argument

                    if boundaryDescription is not None and not isinstance(
                        boundaryDescription, aas.SubmodelElement
                    ):
                        boundaryDescription = self.BoundaryDescription(
                            boundaryDescription
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        conditionName,
                        isBoundaryConditionUsedInModel,
                        boundaryValueRange,
                        boundaryEngineeringUnit,
                        driftInfoAIModel,
                        meanValue,
                        standarddeviation,
                        skewness,
                        boundaryDescription,
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
                listrulboundaryconditions_items: Iterable[
                    Listrulboundaryconditions_item
                ],
                id_short: Optional[str] = r"ListRULBoundaryConditions",
                type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                semantic_id_list_element: Optional[aas.Reference] = None,
                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PredictiveMaintenance/ListRULBoundaryConditions/1/0",
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
                            r"en": r"List of boundary conditions for which remaining useful life has been predicted",
                            r"de": r"Liste der Randbedingungen unter denen die nutzbare Restlebensdauer prognostiziert wurde",
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(listrulboundaryconditions_items, str):
                    raise TypeError(
                        "listrulboundaryconditions_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [listrulboundaryconditions_items]:
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

        class PredictionModelInformation(aas.SubmodelElementCollection):

            class ModelType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ModelType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PredictiveMaintenance/ModelType/1/0",
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
                                r"en": r"Model type as an enumerated value: physical based methods, data-driven methods, hybrid methods",
                                r"de": r"Modeltyp als enumerierter Wert: physical based methods, data-driven methods, hybrid methods",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ModelDescription(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ModelDescription",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PredictiveMaintenance/ModelDescription/1/0",
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
                                r"en": r"More detailed description of the model type used for RUL prediction (optional)",
                                r"de": r"Detailliertere Beschreibung des Modelltyps, der für die RUL Prognose verwendet wird (optional)",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SMAIModelNamePlate(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"SMAIModelNamePlate",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PredictiveMaintenance/SMAIModelNamePlate/1/0",
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
                                r"en": r"Reference to AIModelNameplate",
                                r"de": r"Referenz auf AIModelNameplate",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

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
                modelType: Union[str, ModelType],
                modelDescription: Optional[Union[str, ModelDescription]] = None,
                sMAIModelNamePlate: Optional[
                    Union[aas.Reference, SMAIModelNamePlate]
                ] = None,
                id_short: Optional[str] = r"PredictionModelInformation",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PredictiveMaintenance/PredictionModelInformation/1/0",
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
                            r"en": r"Information about the model for RUL prediction relevant in the context of predictive maintenance",
                            r"de": r"Informationen über das Modell zur Prognose der RUL im Kontext der vorausschauenden Wartung",
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if modelType is not None and not isinstance(
                    modelType, aas.SubmodelElement
                ):
                    modelType = self.ModelType(modelType)

                # Build a submodel element if a raw value was passed in the argument

                if modelDescription is not None and not isinstance(
                    modelDescription, aas.SubmodelElement
                ):
                    modelDescription = self.ModelDescription(modelDescription)

                # Build a submodel element if a raw value was passed in the argument

                if sMAIModelNamePlate is not None and not isinstance(
                    sMAIModelNamePlate, aas.SubmodelElement
                ):
                    sMAIModelNamePlate = self.SMAIModelNamePlate(sMAIModelNamePlate)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [modelType, modelDescription, sMAIModelNamePlate]:
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

        class ListPreAlerts(aas.SubmodelElementList):

            class Listprealerts_item(aas.SubmodelElementCollection):

                class PreAlertMessage(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"PreAlertMessage",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/PreAlertMessage/1/0",
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
                                    r"en": r"Message to be displayed when alarm regarding predicted remaining useful life is raised",
                                    r"de": r"Nachricht, die bei Auslösen eines Alarms bezüglich der vorhergesagten verbleibenden Restnutzungsdauer angezeigt wird",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class PreAlertValue(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"PreAlertValue",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/PredictiveMaintenance/PreAlertValue/1/0",
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
                                    r"en": r"Pre-warning duration in wear relevant unit before remaining useful life is exceeded",
                                    r"de": r"Vorwarndauer in verschleißrelevanter Einheit vor Eintritt der Überschreitung verbleibenden Restnutzungsdauer",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
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
                    preAlertValue: Union[float, PreAlertValue],
                    preAlertMessage: Optional[Union[str, PreAlertMessage]] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PredictiveMaintenance/PreAlerts/1/0",
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
                                r"en": r"Definition of a pre-alert which should be raised before remaining useful life is exceeded",
                                r"de": r"Definition eiens Voralarms, der vor Erreichen der Restlebensdauer ausgelöst werden sollen",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if preAlertMessage is not None and not isinstance(
                        preAlertMessage, aas.SubmodelElement
                    ):
                        preAlertMessage = self.PreAlertMessage(preAlertMessage)

                    # Build a submodel element if a raw value was passed in the argument

                    if preAlertValue is not None and not isinstance(
                        preAlertValue, aas.SubmodelElement
                    ):
                        preAlertValue = self.PreAlertValue(preAlertValue)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [preAlertMessage, preAlertValue]:
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
                listprealerts_items: Optional[Iterable[Listprealerts_item]] = None,
                id_short: Optional[str] = r"ListPreAlerts",
                type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                semantic_id_list_element: Optional[aas.Reference] = None,
                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PredictiveMaintenance/ListPreAlerts/1/0",
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
                            r"en": r"List for defining pre-alerts which should be raised before remaining useful life is exceeded",
                            r"de": r"Liste, um Voralarme zu definieren, die vor Erreichen der Restlebensdauer ausgelöst werden sollen",
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(listprealerts_items, str):
                    raise TypeError(
                        "listprealerts_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [listprealerts_items]:
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

        class AlertAfterExceedingRemainingUsableLife(aas.SubmodelElementCollection):

            class AlertMessage(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AlertMessage",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PredictiveMaintenance/AlertMessage/1/0",
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
                                r"en": r"Message to be displayed when alarm regarding predicted remaining useful life is raised",
                                r"de": r"Nachricht, die bei Auslösen eines Alarms bezüglich der vorhergesagten verbleibenden Restnutzungsdauer angezeigt wird",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class MaintenanceRequired(aas.Property):

                def __init__(
                    self,
                    value: bool,
                    id_short: Optional[str] = r"MaintenanceRequired",
                    value_type: aas.DataTypeDefXsd = bool,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/PredictiveMaintenance/MaintenanceRequired/1/0",
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
                                r"en": r"Maintenance required",
                                r"de": r"Wartung erforderlich",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
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
                maintenanceRequired: Union[bool, MaintenanceRequired],
                alertMessage: Optional[Union[str, AlertMessage]] = None,
                id_short: Optional[str] = r"AlertAfterExceedingRemainingUsableLife",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/PredictiveMaintenance/AlertAfterExceedingRemainingUsableLife/1/0",
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
                            r"en": r"Alert information which should be triggered or displayed after exceeding remaining useful life",
                            r"de": r"Alarminformationen die ausgelöst oder angezeigt werden sollen, wenn die Restlebensdauer überschritten wird",
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if alertMessage is not None and not isinstance(
                    alertMessage, aas.SubmodelElement
                ):
                    alertMessage = self.AlertMessage(alertMessage)

                # Build a submodel element if a raw value was passed in the argument

                if maintenanceRequired is not None and not isinstance(
                    maintenanceRequired, aas.SubmodelElement
                ):
                    maintenanceRequired = self.MaintenanceRequired(maintenanceRequired)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [alertMessage, maintenanceRequired]:
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
            remainingUsefulLifetime: RemainingUsefulLifetime,
            confidenceInterval: Union[Tuple[float, float], ConfidenceInterval],
            listRULBoundaryConditions: Union[
                Iterable[ListRULBoundaryConditions.Listrulboundaryconditions_item],
                ListRULBoundaryConditions,
            ],
            predictionModelInformation: PredictionModelInformation,
            remainingUsfulLifeDateTime: Optional[
                Union[xsd.DateTime, RemainingUsfulLifeDateTime]
            ] = None,
            listPreAlerts: Optional[
                Union[Iterable[ListPreAlerts.Listprealerts_item], ListPreAlerts]
            ] = None,
            alertAfterExceedingRemainingUsableLife: Optional[
                AlertAfterExceedingRemainingUsableLife
            ] = None,
            id_short: Optional[str] = r"RemainingUsefulLifePrediction",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLifePrediction/1/0",
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
                        r"en": r"Information about remaining useful life (RUL) prediction in the context of predictive maintenance",
                        r"de": r"Informationen über die Prognose der nutzbaren Restlebensdauer (RUL) im Kontext der vorausschauenden Wartung",
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if remainingUsfulLifeDateTime is not None and not isinstance(
                remainingUsfulLifeDateTime, aas.SubmodelElement
            ):
                remainingUsfulLifeDateTime = self.RemainingUsfulLifeDateTime(
                    remainingUsfulLifeDateTime
                )

            # Build a submodel element if a raw value was passed in the argument

            if confidenceInterval is not None and not isinstance(
                confidenceInterval, aas.SubmodelElement
            ):
                confidenceInterval = self.ConfidenceInterval(
                    min=confidenceInterval[0], max=confidenceInterval[1]
                )

            # A str would be split into its characters
            if isinstance(listRULBoundaryConditions, str):
                raise TypeError(
                    "listRULBoundaryConditions takes several elements, got a str"
                )

            # Build a submodel element if a raw value was passed in the argument

            if listRULBoundaryConditions is not None and not isinstance(
                listRULBoundaryConditions, aas.SubmodelElement
            ):
                listRULBoundaryConditions = self.ListRULBoundaryConditions(
                    listRULBoundaryConditions
                )

            # A str would be split into its characters
            if isinstance(listPreAlerts, str):
                raise TypeError("listPreAlerts takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if listPreAlerts is not None and not isinstance(
                listPreAlerts, aas.SubmodelElement
            ):
                listPreAlerts = self.ListPreAlerts(listPreAlerts)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                remainingUsefulLifetime,
                remainingUsfulLifeDateTime,
                confidenceInterval,
                listRULBoundaryConditions,
                predictionModelInformation,
                listPreAlerts,
                alertAfterExceedingRemainingUsableLife,
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
        remainingUsefulLifePrediction: RemainingUsefulLifePrediction,
        id_short: Optional[str] = r"PredictiveMaintenance",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0",
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
                    r"en": r"The Submodel Predictive Maintenance is a collection of properties to provide information for predictive maintenance use cases. It is intended to use this submodel in sub-systems of production lines to describe predictive maintenance relevant topics for the sub-system, as well as to use this submodel in predictive maintenance software applications",
                    r"de": r"Das Teilmodell Predictive Maintenance stellt Informationen für Anwendungsfälle von Predictive Maintenance bereit. Dieses Teilmodell ist für Sub-Systeme von Produktionslinien vorgesehen, um Predictive Maintenance relevante Informationen für das Sub-System zu beschreiben sowie für Software-Anwendungen für vorausschauende Wartung",
                }
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [remainingUsefulLifePrediction]:
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
