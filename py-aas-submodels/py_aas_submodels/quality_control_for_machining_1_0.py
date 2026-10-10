from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class QualityControlForMachining(aas.Submodel):

    class QualityFeatures(aas.SubmodelElementCollection):

        class LinearFeaturesList(aas.SubmodelElementList):

            class Linearfeatureslist_item(aas.SubmodelElementCollection):

                class LinearFeatureName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"LinearFeatureName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/LinearFeatureName/1/0",
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
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class DimensionDescription(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"DimensionDescription",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/DimensionDescription/1/0",
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
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class MeasurementProcedure(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"MeasurementProcedure",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0",
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
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class InspectionRelevant(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"InspectionRelevant",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0",
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
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ToleranceNorm(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ToleranceNorm",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0",
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
                                        value=r"0173-1#02-AAO933#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            )

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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class NominalValue(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"NominalValue",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/NominalValue/1/0",
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
                                        value=r"0112/2///61360_4#AAA235#001",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Value for physical quantities that may be expressed as the nominal value of the quantity together with deviations from that nominal value as percentages or absolute values",
                                    r"de": r"Wert für physikalische Größen, der als Nominalwert der Größe zusammen mit Abweichungen von diesem Nominalwert als Prozentsätze oder absolute Werte ausgedrückt werden kann",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class UpperTolerance(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"UpperTolerance",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/UpperTolerance/1/0",
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
                                    r"en": r"Upper tolerance limit of the feature as an absolute value.If there is a one-sided tolerance, only one tolerance limit is specified.",
                                    r"de": r"Obere Toranzgrenze des Merkmals als absoluter Wert. Wenn eine einseitige Tolerierung vorliegt, wird entsprechend nur eine Toleranzgrenze angegeben.",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class LowerTolerance(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"LowerTolerance",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/LowerTolerance/1/0",
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
                                    r"en": r"Lower tolerance limit of the feature as an absolute value. If there is a one-sided tolerance, only one tolerance limit is specified.",
                                    r"de": r"Untere Toranzgrenze des Merkmals als absoluter Wert. Wenn eine einseitige Tolerierung vorliegt, wird entsprechend nur eine Toleranzgrenze angegeben.",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class OneSided(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"OneSided",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/OneSided/1/0",
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
                                    r"en": r"Is the measure tolerated one-sidedly? True means yes, false means no. If there is a one-sided tolerance, only one tolerance limit is specified",
                                    r"de": r"Ist das Maß einseitig toleriert? True bedeutet ja, false nein. Wenn eine einseitige Tolerierung vorliegt, wird entsprechend nur eine Toleranzgrenze angegeben",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class EngineeringUnit(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"EngineeringUnit",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/EngineeringUnit/1/0",
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
                                    r"en": r"Physical unit of feature",
                                    r"de": r"Physikalische Einheit des Merkmals",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class GeometryReferenceList(aas.SubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0",
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
                                        r"en": r"Reference to a Geometry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometrie, beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                )

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
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        id_short: Optional[str] = r"GeometryReferenceList",
                        type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0",
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
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
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
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError(
                                "geometryreferencelist_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Geometryreferencelist_item(i)
                                )
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [geometryreferencelist_items]:
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

                class IDList3DModel(aas.SubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0",
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
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        idlist3dmodel_items: Optional[
                            Iterable[Union[str, Idlist3dmodel_item]]
                        ] = None,
                        id_short: Optional[str] = r"IDList3DModel",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0",
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
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
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
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError(
                                "idlist3dmodel_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Idlist3dmodel_item(i)
                                )
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [idlist3dmodel_items]:
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

                class Reference2DList(aas.SubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Page",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0",
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
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Coordinate(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Coordinate",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0",
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
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
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
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0",
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                )

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

                            if page is not None and not isinstance(
                                page, aas.SubmodelElement
                            ):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(
                                coordinate, aas.SubmodelElement
                            ):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [page, coordinate]:
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
                        reference2dlist_items: Optional[
                            Iterable[Reference2dlist_item]
                        ] = None,
                        id_short: Optional[str] = r"Reference2DList",
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0",
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
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
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
                        if isinstance(reference2dlist_items, str):
                            raise TypeError(
                                "reference2dlist_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [reference2dlist_items]:
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

                def __init__(
                    self,
                    linearFeatureName: Union[str, LinearFeatureName],
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    nominalValue: Union[float, NominalValue],
                    engineeringUnit: Union[str, EngineeringUnit],
                    dimensionDescription: Optional[
                        Union[str, DimensionDescription]
                    ] = None,
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    upperTolerance: Optional[Union[float, UpperTolerance]] = None,
                    lowerTolerance: Optional[Union[float, LowerTolerance]] = None,
                    oneSided: Optional[Union[bool, OneSided]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[
                                Union[
                                    aas.Reference,
                                    GeometryReferenceList.Geometryreferencelist_item,
                                ]
                            ],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[
                            Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]],
                            IDList3DModel,
                        ]
                    ] = None,
                    reference2DList: Optional[
                        Union[
                            Iterable[Reference2DList.Reference2dlist_item],
                            Reference2DList,
                        ]
                    ] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/LinearFeature/1/0",
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
                                r"en": r"Description of the definition of a linear quality characteristic such as length, weight, angle, according to DIN EN ISO 14405-1: Dimensional tolerancing - Part 1: Linear size dimensions",
                                r"de": r"Beschreibung der Definition eines linearen Qualitätsmerkmals wie z.B. Länge, Gewicht, Winkel, gemäß DIN EN ISO 14405-1: Dimensionelle Tolerierung – Teil 1: Lineare Größenmaße",
                            }
                        )

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

                    if linearFeatureName is not None and not isinstance(
                        linearFeatureName, aas.SubmodelElement
                    ):
                        linearFeatureName = self.LinearFeatureName(linearFeatureName)

                    # Build a submodel element if a raw value was passed in the argument

                    if dimensionDescription is not None and not isinstance(
                        dimensionDescription, aas.SubmodelElement
                    ):
                        dimensionDescription = self.DimensionDescription(
                            dimensionDescription
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(
                        measurementProcedure, aas.SubmodelElement
                    ):
                        measurementProcedure = self.MeasurementProcedure(
                            measurementProcedure
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(
                        inspectionRelevant, aas.SubmodelElement
                    ):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError(
                            "toleranceNorm takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.ToleranceNorm(i)
                            )
                            for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if nominalValue is not None and not isinstance(
                        nominalValue, aas.SubmodelElement
                    ):
                        nominalValue = self.NominalValue(nominalValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if upperTolerance is not None and not isinstance(
                        upperTolerance, aas.SubmodelElement
                    ):
                        upperTolerance = self.UpperTolerance(upperTolerance)

                    # Build a submodel element if a raw value was passed in the argument

                    if lowerTolerance is not None and not isinstance(
                        lowerTolerance, aas.SubmodelElement
                    ):
                        lowerTolerance = self.LowerTolerance(lowerTolerance)

                    # Build a submodel element if a raw value was passed in the argument

                    if oneSided is not None and not isinstance(
                        oneSided, aas.SubmodelElement
                    ):
                        oneSided = self.OneSided(oneSided)

                    # Build a submodel element if a raw value was passed in the argument

                    if engineeringUnit is not None and not isinstance(
                        engineeringUnit, aas.SubmodelElement
                    ):
                        engineeringUnit = self.EngineeringUnit(engineeringUnit)

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError(
                            "geometryReferenceList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(
                        geometryReferenceList, aas.SubmodelElement
                    ):
                        geometryReferenceList = self.GeometryReferenceList(
                            geometryReferenceList
                        )

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError(
                            "iDList3DModel takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(
                        iDList3DModel, aas.SubmodelElement
                    ):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError(
                            "reference2DList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(
                        reference2DList, aas.SubmodelElement
                    ):
                        reference2DList = self.Reference2DList(reference2DList)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        linearFeatureName,
                        dimensionDescription,
                        measurementProcedure,
                        inspectionRelevant,
                        toleranceNorm,
                        nominalValue,
                        upperTolerance,
                        lowerTolerance,
                        oneSided,
                        engineeringUnit,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
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
                linearfeatureslist_items: Optional[
                    Iterable[Linearfeatureslist_item]
                ] = None,
                id_short: Optional[str] = r"LinearFeaturesList",
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
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/LinearFeaturesList/1/0",
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
                            r"en": r"List of linear quality characteristics, such as dimensions, weight, angles",
                            r"de": r"Liste linearer Qualitätsmerkmale, wie Dimensionen, Gewicht, Winkel",
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
                if isinstance(linearfeatureslist_items, str):
                    raise TypeError(
                        "linearfeatureslist_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [linearfeatureslist_items]:
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

        class AttributiveFeaturesList(aas.SubmodelElementList):

            class Attributivefeatureslist_item(aas.SubmodelElementCollection):

                class AttributiveFeatureName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AttributiveFeatureName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/AttributiveFeatureName/1/0",
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
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class AttibutiveFeatureDescription(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AttibutiveFeatureDescription",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/AttibutiveFeatureDescription/1/0",
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
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class MeasurementProcedure(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"MeasurementProcedure",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0",
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
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ToleranceNorm(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ToleranceNorm",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0",
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
                                        value=r"0173-1#02-AAO933#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            )

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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class InspectionRelevant(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"InspectionRelevant",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0",
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
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class GeometryReferenceList(aas.SubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0",
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
                                        r"en": r"Reference to a Geomatry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometry beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                )

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
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        id_short: Optional[str] = r"GeometryReferenceList",
                        type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0",
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
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
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
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError(
                                "geometryreferencelist_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Geometryreferencelist_item(i)
                                )
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [geometryreferencelist_items]:
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

                class IDList3DModel(aas.SubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0",
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
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        idlist3dmodel_items: Optional[
                            Iterable[Union[str, Idlist3dmodel_item]]
                        ] = None,
                        id_short: Optional[str] = r"IDList3DModel",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0",
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
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
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
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError(
                                "idlist3dmodel_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Idlist3dmodel_item(i)
                                )
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [idlist3dmodel_items]:
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

                class Reference2DList(aas.SubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Page",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0",
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
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Coordinate(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Coordinate",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0",
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
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
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
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0",
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                )

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

                            if page is not None and not isinstance(
                                page, aas.SubmodelElement
                            ):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(
                                coordinate, aas.SubmodelElement
                            ):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [page, coordinate]:
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
                        reference2dlist_items: Optional[
                            Iterable[Reference2dlist_item]
                        ] = None,
                        id_short: Optional[str] = r"Reference2DList",
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0",
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
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
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
                        if isinstance(reference2dlist_items, str):
                            raise TypeError(
                                "reference2dlist_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [reference2dlist_items]:
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

                class OKAttributesList(aas.SubmodelElementList):

                    class Okattributeslist_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/OKAttributName/1/0",
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
                                        r"en": r"Name of an attribute that is accepted or tolerable in terms of quality assurance (OK attribute)",
                                        r"de": r"Bezeichnung eines Attributs, das akzeptiert bzw. im Sinne der Qualitätssicherung tolerabel ist (i.O.-Attribut)",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        okattributeslist_items: Optional[
                            Iterable[Union[str, Okattributeslist_item]]
                        ] = None,
                        id_short: Optional[str] = r"OKAttributesList",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/OKAttributesList/1/0",
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
                                    r"en": r"List of attributes that are accepted or tolerable in terms of quality assurance (OK attributes)",
                                    r"de": r"Liste der Attribute, die akzeptiert bzw. im Sinne der Qualitätssicherung tolerabel sind (i.O.-Attribute)",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(okattributeslist_items, str):
                            raise TypeError(
                                "okattributeslist_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if okattributeslist_items:
                            okattributeslist_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Okattributeslist_item(i)
                                )
                                for i in okattributeslist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [okattributeslist_items]:
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

                class NOKAttributesList(aas.SubmodelElementList):

                    class Nokattributeslist_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/NOKAttributName/1/0",
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
                                        r"en": r"Name of an attribute that is not accepted or intolerable in terms of quality assurance (not OK attribute)",
                                        r"de": r"Bezeichnung eines Attributs, das nicht akzeptiert bzw. im Sinne der Qualitätssicherung intolerabel ist (n.i.O.-Attribut)",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        nokattributeslist_items: Optional[
                            Iterable[Union[str, Nokattributeslist_item]]
                        ] = None,
                        id_short: Optional[str] = r"NOKAttributesList",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/NOKAttributesList/1/0",
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
                                    r"en": r"List of attributes that are not accepted or intolerable in terms of quality assurance (not OK attributes)",
                                    r"de": r"Liste der Attribute, die nicht akzeptiert bzw. im Sinne der Qualitätssicherung intolerabel sind (n.i.O.-Attribute)",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(nokattributeslist_items, str):
                            raise TypeError(
                                "nokattributeslist_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if nokattributeslist_items:
                            nokattributeslist_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Nokattributeslist_item(i)
                                )
                                for i in nokattributeslist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [nokattributeslist_items]:
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

                def __init__(
                    self,
                    attributiveFeatureName: Union[str, AttributiveFeatureName],
                    attibutiveFeatureDescription: Union[
                        str, AttibutiveFeatureDescription
                    ],
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    oKAttributesList: Union[
                        Iterable[Union[str, OKAttributesList.Okattributeslist_item]],
                        OKAttributesList,
                    ],
                    nOKAttributesList: Union[
                        Iterable[Union[str, NOKAttributesList.Nokattributeslist_item]],
                        NOKAttributesList,
                    ],
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[
                                Union[
                                    aas.Reference,
                                    GeometryReferenceList.Geometryreferencelist_item,
                                ]
                            ],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[
                            Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]],
                            IDList3DModel,
                        ]
                    ] = None,
                    reference2DList: Optional[
                        Union[
                            Iterable[Reference2DList.Reference2dlist_item],
                            Reference2DList,
                        ]
                    ] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/AttributiveFeature/1/0",
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
                                r"en": r"Information about an attributive quality feature",
                                r"de": r"Informationen zu einem attributiven Qualitätsmerkmal",
                            }
                        )

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

                    if attributiveFeatureName is not None and not isinstance(
                        attributiveFeatureName, aas.SubmodelElement
                    ):
                        attributiveFeatureName = self.AttributiveFeatureName(
                            attributiveFeatureName
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if attibutiveFeatureDescription is not None and not isinstance(
                        attibutiveFeatureDescription, aas.SubmodelElement
                    ):
                        attibutiveFeatureDescription = (
                            self.AttibutiveFeatureDescription(
                                attibutiveFeatureDescription
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(
                        measurementProcedure, aas.SubmodelElement
                    ):
                        measurementProcedure = self.MeasurementProcedure(
                            measurementProcedure
                        )

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError(
                            "toleranceNorm takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.ToleranceNorm(i)
                            )
                            for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(
                        inspectionRelevant, aas.SubmodelElement
                    ):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError(
                            "geometryReferenceList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(
                        geometryReferenceList, aas.SubmodelElement
                    ):
                        geometryReferenceList = self.GeometryReferenceList(
                            geometryReferenceList
                        )

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError(
                            "iDList3DModel takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(
                        iDList3DModel, aas.SubmodelElement
                    ):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError(
                            "reference2DList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(
                        reference2DList, aas.SubmodelElement
                    ):
                        reference2DList = self.Reference2DList(reference2DList)

                    # A str would be split into its characters
                    if isinstance(oKAttributesList, str):
                        raise TypeError(
                            "oKAttributesList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if oKAttributesList is not None and not isinstance(
                        oKAttributesList, aas.SubmodelElement
                    ):
                        oKAttributesList = self.OKAttributesList(oKAttributesList)

                    # A str would be split into its characters
                    if isinstance(nOKAttributesList, str):
                        raise TypeError(
                            "nOKAttributesList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if nOKAttributesList is not None and not isinstance(
                        nOKAttributesList, aas.SubmodelElement
                    ):
                        nOKAttributesList = self.NOKAttributesList(nOKAttributesList)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        attributiveFeatureName,
                        attibutiveFeatureDescription,
                        measurementProcedure,
                        toleranceNorm,
                        inspectionRelevant,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
                        oKAttributesList,
                        nOKAttributesList,
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
                attributivefeatureslist_items: Optional[
                    Iterable[Attributivefeatureslist_item]
                ] = None,
                id_short: Optional[str] = r"AttributiveFeaturesList",
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
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/AttributiveFeaturesList/1/0",
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
                            r"en": r"List of attributive quality characteristics",
                            r"de": r"Liste attributiver Qualtätsmerkmale",
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
                if isinstance(attributivefeatureslist_items, str):
                    raise TypeError(
                        "attributivefeatureslist_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [attributivefeatureslist_items]:
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

        class GeometricFeaturesList(aas.SubmodelElementList):

            class Geometricfeatureslist_item(aas.SubmodelElementCollection):

                class GPS_FeatureName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"GPS_FeatureName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GPS_FeatureName/1/0",
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
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class GPS_Description(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"GPS_Description",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Description/1/0",
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
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class MeasurementProcedure(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"MeasurementProcedure",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0",
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
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ToleranceNorm(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ToleranceNorm",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0",
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
                                        value=r"0173-1#02-AAO933#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            )

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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class InspectionRelevant(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"InspectionRelevant",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0",
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
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class GPS_Type(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"GPS_Type",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Type/1/0",
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
                                    r"en": r"ValueList (straightness, flatness, roundness, cylindricity, line shape, surface shape, parallelism, perpendicularity, inclination, line profile direction, surface profile direction, position, coaxiality, concentricity, symmetry, line profile location, surface profile location, concentricity, axial runout, total concentricity, overall plan run)",
                                    r"de": r"ValueList (Geradheit, Ebenheit, Rundheit, Zylindrizität, Linienform, Flächenform, Parallelität, Rechtwinkligkeit, Neigung, Linienprofil-Richtung, Flächenprofil-Richtung, Position, Koaxialität, Konzentrizität, Symmetrie, Linienprofil-Ort, Flächenprofil-Ort, Rundlauf, Planlauf, Gesamtrundlauf, Gesamtplanlauf)",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class GPS_ReferenceRequired(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"GPS_ReferenceRequired",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GPS_ReferenceRequired/1/0",
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
                                    r"en": r"Does a geometric reference have to be specified to make the feature unique? true corresponds to yes, false no",
                                    r"de": r"Muss zur Eindeutigkeit des Merkmals ein geometrischer Bezug angegeben werden? true entspricht ja, false nein",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class GPS_ToleranceZone(aas.SubmodelElementCollection):

                    class Shape(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Shape",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Shape/1/0",
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
                                        r"en": r"Shape of the tolerance zone according to DIN EN ISO 1101",
                                        r"de": r"Gestalt der Toreanzzone gemäß DIN EN ISO 1101",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ToleranceZoneDescription(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"ToleranceZoneDescription",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceZoneDescription/1/0",
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
                                            value=r"0173-1#02-AAH964#005",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Information on the partition based on the deviation from the ideal value within a certain area",
                                        r"de": r"Angaben zur Toleranzzone anhand der Abweichung vom Sollwert innerhalb eines bestimmten Bereichs",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SpecificationModificator(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SpecificationModificator",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SpecificationModificator/1/0",
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
                                        r"en": r"Specification modifier according to DIN EN ISO 14405-1: LP, LS, GG, GX, GN, GC, CC, CA, CV, SX, SN, SA, SM, SD, SR, SQ)",
                                        r"de": r"Spezifikationsmodifikator gemäß DIN EN ISO 14405-1: LP, LS, GG, GX, GN, GC, CC, CA, CV, SX, SN, SA, SM, SD, SR, SQ)",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class WidthExtendValue(aas.Property):

                        def __init__(
                            self,
                            value: float,
                            id_short: Optional[str] = r"WidthExtendValue",
                            value_type: aas.DataTypeDefXsd = float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendValue/1/0",
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
                                        r"en": r"Value for the width or extent of the tolerance zone according to DIN EN ISO 1101",
                                        r"de": r"Wert für Weite bzw.  Ausdehnung der Toleranzzone gemäß DIN EN ISO 1101",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class WidthExtendTolerance1(aas.Property):

                        def __init__(
                            self,
                            value: float,
                            id_short: Optional[str] = r"WidthExtendTolerance1",
                            value_type: aas.DataTypeDefXsd = float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendTolerance1/1/0",
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
                                        r"en": r"Tolerated deviation",
                                        r"de": r"TolerierteAbweichung",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class WidthExtendSign1(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"WidthExtendSign1",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendSign1/1/0",
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
                                        r"en": r"Sign of tolerance (p, m, pm)",
                                        r"de": r"Vorzeichen der Tolerienung (p, m, pm)",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class WidthExtendTolerance2(aas.Property):

                        def __init__(
                            self,
                            value: float,
                            id_short: Optional[str] = r"WidthExtendTolerance2",
                            value_type: aas.DataTypeDefXsd = float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendTolerance2/1/0",
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
                                        r"en": r"Tolerated deviation",
                                        r"de": r"TolerierteAbweichung",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class WidthExtendSign2(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"WidthExtendSign2",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendSign2/1/0",
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
                                        r"en": r"Sign of tolerance (p, m, pm)",
                                        r"de": r"Vorzeichen der Tolerienung (p, m, pm)",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class EngineeringUnit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"EngineeringUnit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/EngineeringUnit/1/0",
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
                                        r"en": r"Physical unit of feature",
                                        r"de": r"Physikalische Einheit des Merkmals",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        shape: Union[str, Shape],
                        widthExtendTolerance1: Union[float, WidthExtendTolerance1],
                        widthExtendSign1: Union[str, WidthExtendSign1],
                        engineeringUnit: Union[str, EngineeringUnit],
                        toleranceZoneDescription: Optional[
                            Union[str, ToleranceZoneDescription]
                        ] = None,
                        specificationModificator: Optional[
                            Iterable[Union[str, SpecificationModificator]]
                        ] = None,
                        widthExtendValue: Optional[
                            Iterable[Union[float, WidthExtendValue]]
                        ] = None,
                        widthExtendTolerance2: Optional[
                            Union[float, WidthExtendTolerance2]
                        ] = None,
                        widthExtendSign2: Optional[Union[str, WidthExtendSign2]] = None,
                        id_short: Optional[str] = r"GPS_ToleranceZone",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GPS_ToleranceZone/1/0",
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
                                    r"en": r"Tolerance zone according to DIN EN ISO 1101. The tolerance zone must be arranged symmetrically around the reference geometry element, unless otherwise stated.",
                                    r"de": r"Toleranzzone gemäß DIN EN ISO 1101. Die Toleranzzone muss symmetrisch um das Referenzgeometrieelement herum angeordnet werden, soweit nichts anderes angegeben ist.",
                                }
                            )

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

                        if shape is not None and not isinstance(
                            shape, aas.SubmodelElement
                        ):
                            shape = self.Shape(shape)

                        # Build a submodel element if a raw value was passed in the argument

                        if toleranceZoneDescription is not None and not isinstance(
                            toleranceZoneDescription, aas.SubmodelElement
                        ):
                            toleranceZoneDescription = self.ToleranceZoneDescription(
                                toleranceZoneDescription
                            )

                        # A str would be split into its characters
                        if isinstance(specificationModificator, str):
                            raise TypeError(
                                "specificationModificator takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if specificationModificator:
                            specificationModificator = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.SpecificationModificator(i)
                                )
                                for i in specificationModificator
                            ]

                        # A str would be split into its characters
                        if isinstance(widthExtendValue, str):
                            raise TypeError(
                                "widthExtendValue takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if widthExtendValue:
                            widthExtendValue = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.WidthExtendValue(i)
                                )
                                for i in widthExtendValue
                            ]

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendTolerance1 is not None and not isinstance(
                            widthExtendTolerance1, aas.SubmodelElement
                        ):
                            widthExtendTolerance1 = self.WidthExtendTolerance1(
                                widthExtendTolerance1
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendSign1 is not None and not isinstance(
                            widthExtendSign1, aas.SubmodelElement
                        ):
                            widthExtendSign1 = self.WidthExtendSign1(widthExtendSign1)

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendTolerance2 is not None and not isinstance(
                            widthExtendTolerance2, aas.SubmodelElement
                        ):
                            widthExtendTolerance2 = self.WidthExtendTolerance2(
                                widthExtendTolerance2
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendSign2 is not None and not isinstance(
                            widthExtendSign2, aas.SubmodelElement
                        ):
                            widthExtendSign2 = self.WidthExtendSign2(widthExtendSign2)

                        # Build a submodel element if a raw value was passed in the argument

                        if engineeringUnit is not None and not isinstance(
                            engineeringUnit, aas.SubmodelElement
                        ):
                            engineeringUnit = self.EngineeringUnit(engineeringUnit)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            shape,
                            toleranceZoneDescription,
                            specificationModificator,
                            widthExtendValue,
                            widthExtendTolerance1,
                            widthExtendSign1,
                            widthExtendTolerance2,
                            widthExtendSign2,
                            engineeringUnit,
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

                class GeometryReferenceList(aas.SubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0",
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
                                        r"en": r"Reference to a Geomatry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometry beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                )

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
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        id_short: Optional[str] = r"GeometryReferenceList",
                        type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0",
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
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
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
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError(
                                "geometryreferencelist_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Geometryreferencelist_item(i)
                                )
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [geometryreferencelist_items]:
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

                class IDList3DModel(aas.SubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0",
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
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        idlist3dmodel_items: Optional[
                            Iterable[Union[str, Idlist3dmodel_item]]
                        ] = None,
                        id_short: Optional[str] = r"IDList3DModel",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0",
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
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
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
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError(
                                "idlist3dmodel_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Idlist3dmodel_item(i)
                                )
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [idlist3dmodel_items]:
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

                class Reference2DList(aas.SubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Page",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0",
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
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Coordinate(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Coordinate",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0",
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
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
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
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0",
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                )

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

                            if page is not None and not isinstance(
                                page, aas.SubmodelElement
                            ):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(
                                coordinate, aas.SubmodelElement
                            ):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [page, coordinate]:
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
                        reference2dlist_items: Optional[
                            Iterable[Reference2dlist_item]
                        ] = None,
                        id_short: Optional[str] = r"Reference2DList",
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0",
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
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
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
                        if isinstance(reference2dlist_items, str):
                            raise TypeError(
                                "reference2dlist_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [reference2dlist_items]:
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

                class DatumField1(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"DatumField1",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/DatumField1/1/0",
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
                                    r"en": r"Information about a geometric reference that is required to define the feature",
                                    r"de": r"Angaben zu einem geometrischen Bezug der für die Definition des Merkmals benötigt wird",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class DatumField2(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"DatumField2",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/DatumField2/1/0",
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
                                    r"en": r"Information about a geometric reference that is required to define the feature",
                                    r"de": r"Angaben zu einem geometrischen Bezug der für die Definition des Merkmals benötigt wird",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class DatumField3(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"DatumField3",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/DatumField3/1/0",
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
                                    r"en": r"Information about a geometric reference that is required to define the feature",
                                    r"de": r"Angaben zu einem geometrischen Bezug der für die Definition des Merkmals benötigt wird",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class AdditionalInformationList(aas.SubmodelElementList):

                    class Additionalinformationlist_item(aas.SubmodelElementCollection):

                        class GPS_Identifier(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"GPS_Identifier",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Identifier/1/0",
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
                                            r"en": r"Identifier of additional GPS field information according to DIN EN 1101",
                                            r"de": r"Bezeichner einer zusätzlichen GPS Feldinformationen gemäß DIN EN 1101",
                                        }
                                    )

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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class GPS_Value(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"GPS_Value",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Value/1/0",
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
                                            r"en": r"Value of additional GPS field information according to DIN EN 1101",
                                            r"de": r"Wert einer zusätzlichen GPS Feldinformation gemäß DIN EN 1101",
                                        }
                                    )

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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
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
                            gPS_Identifier: Optional[
                                Iterable[Union[str, GPS_Identifier]]
                            ] = None,
                            gPS_Value: Optional[Iterable[Union[str, GPS_Value]]] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/AdditionalInformation/1/0",
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
                                        r"en": r"Informationen zu weiteren GPS-Feldern gemäß DIN EN 1101",
                                        r"de": r"Informationen zu weiteren GPS-Feldern gemäß DIN EN 1101",
                                    }
                                )

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

                            # A str would be split into its characters
                            if isinstance(gPS_Identifier, str):
                                raise TypeError(
                                    "gPS_Identifier takes several elements, got a str"
                                )

                            # Build submodel elements from raw values passed in the argument
                            if gPS_Identifier:
                                gPS_Identifier = [
                                    (
                                        i
                                        if isinstance(i, aas.SubmodelElement)
                                        else self.GPS_Identifier(i)
                                    )
                                    for i in gPS_Identifier
                                ]

                            # A str would be split into its characters
                            if isinstance(gPS_Value, str):
                                raise TypeError(
                                    "gPS_Value takes several elements, got a str"
                                )

                            # Build submodel elements from raw values passed in the argument
                            if gPS_Value:
                                gPS_Value = [
                                    (
                                        i
                                        if isinstance(i, aas.SubmodelElement)
                                        else self.GPS_Value(i)
                                    )
                                    for i in gPS_Value
                                ]

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [gPS_Identifier, gPS_Value]:
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
                        additionalinformationlist_items: Optional[
                            Iterable[Additionalinformationlist_item]
                        ] = None,
                        id_short: Optional[str] = r"AdditionalInformationList",
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/AdditionalInformationList/1/0",
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
                                    r"en": r"List with information on other GPS fields in accordance with DIN EN 1101",
                                    r"de": r"Liste mit Informationen zu weiteren GPS-Feldern gemäß DIN EN 1101",
                                }
                            )

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

                        # A str would be split into its characters
                        if isinstance(additionalinformationlist_items, str):
                            raise TypeError(
                                "additionalinformationlist_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [additionalinformationlist_items]:
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

                def __init__(
                    self,
                    gPS_FeatureName: Union[str, GPS_FeatureName],
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    gPS_Type: Union[str, GPS_Type],
                    gPS_ReferenceRequired: Union[bool, GPS_ReferenceRequired],
                    gPS_Description: Optional[Union[str, GPS_Description]] = None,
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    gPS_ToleranceZone: Optional[Iterable[GPS_ToleranceZone]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[
                                Union[
                                    aas.Reference,
                                    GeometryReferenceList.Geometryreferencelist_item,
                                ]
                            ],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[
                            Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]],
                            IDList3DModel,
                        ]
                    ] = None,
                    reference2DList: Optional[
                        Union[
                            Iterable[Reference2DList.Reference2dlist_item],
                            Reference2DList,
                        ]
                    ] = None,
                    datumField1: Optional[Union[str, DatumField1]] = None,
                    datumField2: Optional[Union[str, DatumField2]] = None,
                    datumField3: Optional[Union[str, DatumField3]] = None,
                    additionalInformationList: Optional[
                        Union[
                            Iterable[
                                AdditionalInformationList.Additionalinformationlist_item
                            ],
                            AdditionalInformationList,
                        ]
                    ] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/GeometricFeature/1/0",
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
                                r"en": r"Information on a geometric quality feature according to DIN EN ISO 1101",
                                r"de": r"Angaben zu einem geometrischen Qualitätsmerkmal nach DIN EN ISO 1101",
                            }
                        )

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

                    if gPS_FeatureName is not None and not isinstance(
                        gPS_FeatureName, aas.SubmodelElement
                    ):
                        gPS_FeatureName = self.GPS_FeatureName(gPS_FeatureName)

                    # Build a submodel element if a raw value was passed in the argument

                    if gPS_Description is not None and not isinstance(
                        gPS_Description, aas.SubmodelElement
                    ):
                        gPS_Description = self.GPS_Description(gPS_Description)

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(
                        measurementProcedure, aas.SubmodelElement
                    ):
                        measurementProcedure = self.MeasurementProcedure(
                            measurementProcedure
                        )

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError(
                            "toleranceNorm takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.ToleranceNorm(i)
                            )
                            for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(
                        inspectionRelevant, aas.SubmodelElement
                    ):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # Build a submodel element if a raw value was passed in the argument

                    if gPS_Type is not None and not isinstance(
                        gPS_Type, aas.SubmodelElement
                    ):
                        gPS_Type = self.GPS_Type(gPS_Type)

                    # Build a submodel element if a raw value was passed in the argument

                    if gPS_ReferenceRequired is not None and not isinstance(
                        gPS_ReferenceRequired, aas.SubmodelElement
                    ):
                        gPS_ReferenceRequired = self.GPS_ReferenceRequired(
                            gPS_ReferenceRequired
                        )

                    # A str would be split into its characters
                    if isinstance(gPS_ToleranceZone, str):
                        raise TypeError(
                            "gPS_ToleranceZone takes several elements, got a str"
                        )

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError(
                            "geometryReferenceList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(
                        geometryReferenceList, aas.SubmodelElement
                    ):
                        geometryReferenceList = self.GeometryReferenceList(
                            geometryReferenceList
                        )

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError(
                            "iDList3DModel takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(
                        iDList3DModel, aas.SubmodelElement
                    ):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError(
                            "reference2DList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(
                        reference2DList, aas.SubmodelElement
                    ):
                        reference2DList = self.Reference2DList(reference2DList)

                    # Build a submodel element if a raw value was passed in the argument

                    if datumField1 is not None and not isinstance(
                        datumField1, aas.SubmodelElement
                    ):
                        datumField1 = self.DatumField1(datumField1)

                    # Build a submodel element if a raw value was passed in the argument

                    if datumField2 is not None and not isinstance(
                        datumField2, aas.SubmodelElement
                    ):
                        datumField2 = self.DatumField2(datumField2)

                    # Build a submodel element if a raw value was passed in the argument

                    if datumField3 is not None and not isinstance(
                        datumField3, aas.SubmodelElement
                    ):
                        datumField3 = self.DatumField3(datumField3)

                    # A str would be split into its characters
                    if isinstance(additionalInformationList, str):
                        raise TypeError(
                            "additionalInformationList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if additionalInformationList is not None and not isinstance(
                        additionalInformationList, aas.SubmodelElement
                    ):
                        additionalInformationList = self.AdditionalInformationList(
                            additionalInformationList
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        gPS_FeatureName,
                        gPS_Description,
                        measurementProcedure,
                        toleranceNorm,
                        inspectionRelevant,
                        gPS_Type,
                        gPS_ReferenceRequired,
                        gPS_ToleranceZone,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
                        datumField1,
                        datumField2,
                        datumField3,
                        additionalInformationList,
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
                geometricfeatureslist_items: Optional[
                    Iterable[Geometricfeatureslist_item]
                ] = None,
                id_short: Optional[str] = r"GeometricFeaturesList",
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
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/GeometricFeaturesList/1/0",
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
                            r"en": r"List of geometric quality characteristics according to DIN EN ISO 1101",
                            r"de": r"Liste geometrischer Qualitätsmerkmale gemäß DIN EN ISO 1101",
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
                if isinstance(geometricfeatureslist_items, str):
                    raise TypeError(
                        "geometricfeatureslist_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [geometricfeatureslist_items]:
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

        class ArealSurfaceFeaturesList(aas.SubmodelElementList):

            class Arealsurfacefeatureslist_item(aas.SubmodelElementCollection):

                class ASF_FeatureName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ASF_FeatureName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ASF_FeatureName/1/0",
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
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ASF_Description(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ASF_Description",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ASF_Description/1/0",
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
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class MeasurementProcedure(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"MeasurementProcedure",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0",
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
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ToleranceNorm(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ToleranceNorm",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0",
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
                                        value=r"0173-1#02-AAO933#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            )

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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class InspectionRelevant(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"InspectionRelevant",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0",
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
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ArealSurfaceFeatureType(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ArealSurfaceFeatureType",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ArealSurfaceFeatureType/1/0",
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
                                    r"en": r'Type of surface feature according to DIN EN ISO 25178-1(Value List "S-L" or "S-F")',
                                    r"de": r'Typ der Oberflächenbeschaffenheit gemäß DIN EN ISO 25178-1 (Value-List "S-L" oder "S-F")',
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class GeometryReferenceList(aas.SubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0",
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
                                        r"en": r"Reference to a Geomatry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometry beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                )

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
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        id_short: Optional[str] = r"GeometryReferenceList",
                        type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0",
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
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
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
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError(
                                "geometryreferencelist_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Geometryreferencelist_item(i)
                                )
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [geometryreferencelist_items]:
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

                class IDList3DModel(aas.SubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0",
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
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        idlist3dmodel_items: Optional[
                            Iterable[Union[str, Idlist3dmodel_item]]
                        ] = None,
                        id_short: Optional[str] = r"IDList3DModel",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0",
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
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
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
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError(
                                "idlist3dmodel_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Idlist3dmodel_item(i)
                                )
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [idlist3dmodel_items]:
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

                class Reference2DList(aas.SubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Page",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0",
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
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Coordinate(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Coordinate",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0",
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
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
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

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
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
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0",
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                )

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

                            if page is not None and not isinstance(
                                page, aas.SubmodelElement
                            ):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(
                                coordinate, aas.SubmodelElement
                            ):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [page, coordinate]:
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
                        reference2dlist_items: Optional[
                            Iterable[Reference2dlist_item]
                        ] = None,
                        id_short: Optional[str] = r"Reference2DList",
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0",
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
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
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
                        if isinstance(reference2dlist_items, str):
                            raise TypeError(
                                "reference2dlist_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [reference2dlist_items]:
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

                class SL_Parameters(aas.SubmodelElementCollection):

                    class SL_ASP_Limit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_Limit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Limit/1/0",
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
                                        r"en": r"Either U (upper) or L (lower) specification limit according to ISO 25178-1",
                                        r"de": r"Entweder U (obere) oder L (untere) Spezifikationsgrenze gemäß ISO 25178-1",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_S_FilterType(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_S_FilterType",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_S_FilterType/1/0",
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
                                        r"en": r"Filter type of S-filter",
                                        r"de": r"Filtertyp des S-Filters",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_S_FilterNestingIndex(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_S_FilterNestingIndex",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_S_FilterNestingIndex/1/0",
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
                                        r"en": r"Nesting index of the S-filter",
                                        r"de": r"Nesting-Index des S-Filters",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_L_FilterType(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_L_FilterType",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_L_FilterType/1/0",
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
                                        r"en": r"Filter type of L-filter",
                                        r"de": r"Filtertyp des L-Filters",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_L_FilterNestingIndex(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_L_FilterNestingIndex",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_L_FilterNestingIndex/1/0",
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
                                        r"en": r"Nesting index of the L-filter",
                                        r"de": r"Nesting-Index des L-Filters",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_F_Operator(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_F_Operator",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_F_Operator/1/0",
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
                                        r"en": r"Type of association operator and nesting index",
                                        r"de": r"Typ des Assoziationsoperators und des Nesting-Indexes",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_Indicator(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_Indicator",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Indicator/1/0",
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
                                        r"en": r"Name of the areal parameter. See also ISO 25178-2:2012, 3.2",
                                        r"de": r"Bezeichnung der flächenhaften Kenngröße. Siehe auch ISO 25178-2:2012, 3.2",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_Value(aas.Property):

                        def __init__(
                            self,
                            value: float,
                            id_short: Optional[str] = r"SL_ASP_Value",
                            value_type: aas.DataTypeDefXsd = float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Value/1/0",
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
                                        r"en": r"Specified limit value of the parameter",
                                        r"de": r"Festgelegter Grenzwert der Kenngröße",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_Unit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_Unit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Unit/1/0",
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
                                        r"en": r"Unit of the parameter value, if it is not the default unit",
                                        r"de": r"Einheit des Kenngrößenwertes, sofern es nicht die defaultmäßige Einheit ist.",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SL_ASP_Or(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SL_ASP_Or",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Or/1/0",
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
                                        r"en": r"Symbol for the option to choose other requirements according to DIN EN ISO ISO 25178-2. Additional requirements are specified here.",
                                        r"de": r"Symbol für die Wahlmöglichkeit sonstige Anforderungen gemäß DIN EN ISO 25178-2. An dieser Stelle werden zusätzliche Anforderungen angegeben.",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        sL_ASP_Limit: Union[str, SL_ASP_Limit],
                        sL_ASP_S_FilterType: Union[str, SL_ASP_S_FilterType],
                        sL_ASP_S_FilterNestingIndex: Union[
                            str, SL_ASP_S_FilterNestingIndex
                        ],
                        sL_ASP_L_FilterType: Union[str, SL_ASP_L_FilterType],
                        sL_ASP_L_FilterNestingIndex: Union[
                            str, SL_ASP_L_FilterNestingIndex
                        ],
                        sL_ASP_F_Operator: Union[str, SL_ASP_F_Operator],
                        sL_ASP_Indicator: Union[str, SL_ASP_Indicator],
                        sL_ASP_Value: Union[float, SL_ASP_Value],
                        sL_ASP_Unit: Union[str, SL_ASP_Unit],
                        sL_ASP_Or: Optional[Union[str, SL_ASP_Or]] = None,
                        id_short: Optional[str] = r"SL_Parameters",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/SL_Parameters/1/0",
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
                                    r"en": r"Specification of an S-L surface finish according to DIN EN ISO 25178-1",
                                    r"de": r"Spezifikation einer S-L-Oberflächenbeschaffenheit gemäß DIN EN ISO 25178-1",
                                }
                            )

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

                        if sL_ASP_Limit is not None and not isinstance(
                            sL_ASP_Limit, aas.SubmodelElement
                        ):
                            sL_ASP_Limit = self.SL_ASP_Limit(sL_ASP_Limit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_S_FilterType is not None and not isinstance(
                            sL_ASP_S_FilterType, aas.SubmodelElement
                        ):
                            sL_ASP_S_FilterType = self.SL_ASP_S_FilterType(
                                sL_ASP_S_FilterType
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_S_FilterNestingIndex is not None and not isinstance(
                            sL_ASP_S_FilterNestingIndex, aas.SubmodelElement
                        ):
                            sL_ASP_S_FilterNestingIndex = (
                                self.SL_ASP_S_FilterNestingIndex(
                                    sL_ASP_S_FilterNestingIndex
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_L_FilterType is not None and not isinstance(
                            sL_ASP_L_FilterType, aas.SubmodelElement
                        ):
                            sL_ASP_L_FilterType = self.SL_ASP_L_FilterType(
                                sL_ASP_L_FilterType
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_L_FilterNestingIndex is not None and not isinstance(
                            sL_ASP_L_FilterNestingIndex, aas.SubmodelElement
                        ):
                            sL_ASP_L_FilterNestingIndex = (
                                self.SL_ASP_L_FilterNestingIndex(
                                    sL_ASP_L_FilterNestingIndex
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_F_Operator is not None and not isinstance(
                            sL_ASP_F_Operator, aas.SubmodelElement
                        ):
                            sL_ASP_F_Operator = self.SL_ASP_F_Operator(
                                sL_ASP_F_Operator
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Indicator is not None and not isinstance(
                            sL_ASP_Indicator, aas.SubmodelElement
                        ):
                            sL_ASP_Indicator = self.SL_ASP_Indicator(sL_ASP_Indicator)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Value is not None and not isinstance(
                            sL_ASP_Value, aas.SubmodelElement
                        ):
                            sL_ASP_Value = self.SL_ASP_Value(sL_ASP_Value)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Unit is not None and not isinstance(
                            sL_ASP_Unit, aas.SubmodelElement
                        ):
                            sL_ASP_Unit = self.SL_ASP_Unit(sL_ASP_Unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Or is not None and not isinstance(
                            sL_ASP_Or, aas.SubmodelElement
                        ):
                            sL_ASP_Or = self.SL_ASP_Or(sL_ASP_Or)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            sL_ASP_Limit,
                            sL_ASP_S_FilterType,
                            sL_ASP_S_FilterNestingIndex,
                            sL_ASP_L_FilterType,
                            sL_ASP_L_FilterNestingIndex,
                            sL_ASP_F_Operator,
                            sL_ASP_Indicator,
                            sL_ASP_Value,
                            sL_ASP_Unit,
                            sL_ASP_Or,
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

                class SF_Parameters(aas.SubmodelElementCollection):

                    class SF_ASP_Limit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_Limit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Limit/1/0",
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
                                        r"en": r"Either U (upper) or L (lower) specification limit according to ISO 25178-1",
                                        r"de": r"Entweder U (obere) oder L (untere) Spezifikationsgrenze gemäß ISO 25178-1",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_S_FilterType(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_S_FilterType",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_S_FilterType/1/0",
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
                                        r"en": r"Filter type of S-filter",
                                        r"de": r"Filtertyp des S-Filters",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_S_FilterNestingIndex(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_S_FilterNestingIndex",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_S_FilterNestingIndex/1/0",
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
                                        r"en": r"Nesting index of the S-filter",
                                        r"de": r"Nesting-Index des S-Filters",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_F_Operator(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_F_Operator",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_F_Operator/1/0",
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
                                        r"en": r"Type of association operator and nesting index",
                                        r"de": r"Typ des Assoziationsoperators und des Nesting-Indexes",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_Indicator(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_Indicator",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Indicator/1/0",
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
                                        r"en": r"Name of the areal parameter. See also ISO 25178-2:2012, 3.2",
                                        r"de": r"Bezeichnung der flächenhaften Kenngröße. Siehe auch ISO 25178-2:2012, 3.2",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_Value(aas.Property):

                        def __init__(
                            self,
                            value: float,
                            id_short: Optional[str] = r"SF_ASP_Value",
                            value_type: aas.DataTypeDefXsd = float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Value/1/0",
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
                                        r"en": r"Specified limit value of the parameter",
                                        r"de": r"Festgelegter Grenzwert der Kenngröße",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_Unit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_Unit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Unit/1/0",
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
                                        r"en": r"Unit of the parameter value, if it is not the default unit (the default unit µm does not need to be specified)",
                                        r"de": r"Einheit des Kenngrößenwertes, sofern es nicht die defaultmäßige Einheit ist (die defaultmäßige Einheit µm braucht nicht angegeben zu werden)",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_ES(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_ES",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_ES/1/0",
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
                                        r"en": r"Choice of electromagnetic surface, according to DIN EN 25178-2",
                                        r"de": r"Wahlmöglichkeit elektromagnetische Oberfläche gemäß DIN EN ISO 25178-2",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class SF_ASP_Or(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SF_ASP_Or",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Or/1/0",
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
                                        r"en": r"Symbol for the option to choose other requirements according to DIN EN ISO 25178-2. Additional requirements are specified here.",
                                        r"de": r"Symbol für die Wahlmöglichkeit sonstige Anforderungen gemäß DIN EN ISO 25178-2. An dieser Stelle werden zusätzliche Anforderungen angegeben.",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        sF_ASP_Limit: Union[str, SF_ASP_Limit],
                        sF_ASP_S_FilterType: Union[str, SF_ASP_S_FilterType],
                        sF_ASP_S_FilterNestingIndex: Union[
                            str, SF_ASP_S_FilterNestingIndex
                        ],
                        sF_ASP_F_Operator: Union[str, SF_ASP_F_Operator],
                        sF_ASP_Indicator: Union[str, SF_ASP_Indicator],
                        sF_ASP_Value: Union[float, SF_ASP_Value],
                        sF_ASP_Unit: Optional[Union[str, SF_ASP_Unit]] = None,
                        sF_ASP_ES: Optional[Union[str, SF_ASP_ES]] = None,
                        sF_ASP_Or: Optional[Union[str, SF_ASP_Or]] = None,
                        id_short: Optional[str] = r"SF_Parameters",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/SF_Parameters/1/0",
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
                                    r"en": r"Specification of an S-F surface finish, see ISO 25178-2:2012, 3.1.6",
                                    r"de": r"Spezifikation einer S-F-Oberflächenbeschaffenheit, siehe ISO 25178-2:2012, 3.1.6",
                                }
                            )

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

                        if sF_ASP_Limit is not None and not isinstance(
                            sF_ASP_Limit, aas.SubmodelElement
                        ):
                            sF_ASP_Limit = self.SF_ASP_Limit(sF_ASP_Limit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_S_FilterType is not None and not isinstance(
                            sF_ASP_S_FilterType, aas.SubmodelElement
                        ):
                            sF_ASP_S_FilterType = self.SF_ASP_S_FilterType(
                                sF_ASP_S_FilterType
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_S_FilterNestingIndex is not None and not isinstance(
                            sF_ASP_S_FilterNestingIndex, aas.SubmodelElement
                        ):
                            sF_ASP_S_FilterNestingIndex = (
                                self.SF_ASP_S_FilterNestingIndex(
                                    sF_ASP_S_FilterNestingIndex
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_F_Operator is not None and not isinstance(
                            sF_ASP_F_Operator, aas.SubmodelElement
                        ):
                            sF_ASP_F_Operator = self.SF_ASP_F_Operator(
                                sF_ASP_F_Operator
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Indicator is not None and not isinstance(
                            sF_ASP_Indicator, aas.SubmodelElement
                        ):
                            sF_ASP_Indicator = self.SF_ASP_Indicator(sF_ASP_Indicator)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Value is not None and not isinstance(
                            sF_ASP_Value, aas.SubmodelElement
                        ):
                            sF_ASP_Value = self.SF_ASP_Value(sF_ASP_Value)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Unit is not None and not isinstance(
                            sF_ASP_Unit, aas.SubmodelElement
                        ):
                            sF_ASP_Unit = self.SF_ASP_Unit(sF_ASP_Unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_ES is not None and not isinstance(
                            sF_ASP_ES, aas.SubmodelElement
                        ):
                            sF_ASP_ES = self.SF_ASP_ES(sF_ASP_ES)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Or is not None and not isinstance(
                            sF_ASP_Or, aas.SubmodelElement
                        ):
                            sF_ASP_Or = self.SF_ASP_Or(sF_ASP_Or)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            sF_ASP_Limit,
                            sF_ASP_S_FilterType,
                            sF_ASP_S_FilterNestingIndex,
                            sF_ASP_F_Operator,
                            sF_ASP_Indicator,
                            sF_ASP_Value,
                            sF_ASP_Unit,
                            sF_ASP_ES,
                            sF_ASP_Or,
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

                class Smr_Parameters(aas.SubmodelElementCollection):

                    class Smr_RefCValue(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Smr_RefCValue",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Smr_RefCValue/1/0",
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
                                        r"en": r"Specification of the reference level as a percentage of the material proportion curve, see ISO 25178-2:2012, 4.4.3. The default reference is the highest point 0% of the material proportion curve and does not need to be specified.",
                                        r"de": "Spezifikation des Bezugsniveaus als prozentualer Anteil der Materialanteilskurve, siehe\nISO 25178-2:2012, 4.4.3. Der Default-Bezug ist der höchste Punkt 0 % der Materialanteilskurve und braucht nicht angegeben zu werden.",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Smr_CValue(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Smr_CValue",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Smr_CValue/1/0",
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
                                        r"en": r"Set height distance in relation to the reference c value in µm, see ISO 25178-2:2012, 4.4.2. The c-value is negative if it is below the reference c-value and is positive if it is is above the reference c value",
                                        r"de": "Festgelegter Höhenabstand im Verhältnis zum Bezugs-c-Wert in µm, siehe\nISO 25178-2:2012, 4.4.2.\nDer c-Wert ist negativ, wenn er unter dem Bezugs-c-Wert liegt, und ist positiv, wenn er\nüber dem Bezugs-c-Wert liegt",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Smr_Value(aas.Property):

                        def __init__(
                            self,
                            value: float,
                            id_short: Optional[str] = r"Smr_Value",
                            value_type: aas.DataTypeDefXsd = float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Smr_Value/1/0",
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
                                        r"en": r"Specified limit value of the parameter",
                                        r"de": r"Festgelegter Grenzwert der Kenngröße",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Smr_Unit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Smr_Unit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/Smr_Unit/1/0",
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
                                        r"en": r"Unit, default: %, must always be specified",
                                        r"de": r"Einhheit, default: %, muss immer angegeben werden",
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        smr_CValue: Union[str, Smr_CValue],
                        smr_Value: Union[float, Smr_Value],
                        smr_Unit: Union[str, Smr_Unit],
                        smr_RefCValue: Optional[Union[str, Smr_RefCValue]] = None,
                        id_short: Optional[str] = r"Smr_Parameters",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Smr_Parameters/1/0",
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
                                    r"en": r"Control elements for specifying the parameter value Smr for the material ratio in technical drawings, applies to both S-L and S-F surface finishes, see also ISO 25178-2:2012, 3.1.6",
                                    r"de": r"Steuerelemente für die Angabe des Kenngrößenwertes Smr für das Materialverhältnis in technischen Zeichnungen, gilt sowohl für S-L als auch für S-F Oberflächenbeschaffenheiten, siehe auch ISO 25178-2:2012, 3.1.6",
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

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_RefCValue is not None and not isinstance(
                            smr_RefCValue, aas.SubmodelElement
                        ):
                            smr_RefCValue = self.Smr_RefCValue(smr_RefCValue)

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_CValue is not None and not isinstance(
                            smr_CValue, aas.SubmodelElement
                        ):
                            smr_CValue = self.Smr_CValue(smr_CValue)

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_Value is not None and not isinstance(
                            smr_Value, aas.SubmodelElement
                        ):
                            smr_Value = self.Smr_Value(smr_Value)

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_Unit is not None and not isinstance(
                            smr_Unit, aas.SubmodelElement
                        ):
                            smr_Unit = self.Smr_Unit(smr_Unit)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [smr_RefCValue, smr_CValue, smr_Value, smr_Unit]:
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
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    arealSurfaceFeatureType: Union[str, ArealSurfaceFeatureType],
                    aSF_FeatureName: Optional[Union[str, ASF_FeatureName]] = None,
                    aSF_Description: Optional[Union[str, ASF_Description]] = None,
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[
                                Union[
                                    aas.Reference,
                                    GeometryReferenceList.Geometryreferencelist_item,
                                ]
                            ],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[
                            Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]],
                            IDList3DModel,
                        ]
                    ] = None,
                    reference2DList: Optional[
                        Union[
                            Iterable[Reference2DList.Reference2dlist_item],
                            Reference2DList,
                        ]
                    ] = None,
                    sL_Parameters: Optional[Iterable[SL_Parameters]] = None,
                    sF_Parameters: Optional[Iterable[SF_Parameters]] = None,
                    smr_Parameters: Optional[Smr_Parameters] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/ArealSurfaceFeature/1/0",
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
                                r"en": r"Definition of an areal surface parameter according to DIN EN ISO 25178-1",
                                r"de": r"Definition einer flächenhaften Oberflächenkenngröße gemäß DIN EN ISO 25178-1",
                            }
                        )

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

                    if aSF_FeatureName is not None and not isinstance(
                        aSF_FeatureName, aas.SubmodelElement
                    ):
                        aSF_FeatureName = self.ASF_FeatureName(aSF_FeatureName)

                    # Build a submodel element if a raw value was passed in the argument

                    if aSF_Description is not None and not isinstance(
                        aSF_Description, aas.SubmodelElement
                    ):
                        aSF_Description = self.ASF_Description(aSF_Description)

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(
                        measurementProcedure, aas.SubmodelElement
                    ):
                        measurementProcedure = self.MeasurementProcedure(
                            measurementProcedure
                        )

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError(
                            "toleranceNorm takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.ToleranceNorm(i)
                            )
                            for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(
                        inspectionRelevant, aas.SubmodelElement
                    ):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # Build a submodel element if a raw value was passed in the argument

                    if arealSurfaceFeatureType is not None and not isinstance(
                        arealSurfaceFeatureType, aas.SubmodelElement
                    ):
                        arealSurfaceFeatureType = self.ArealSurfaceFeatureType(
                            arealSurfaceFeatureType
                        )

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError(
                            "geometryReferenceList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(
                        geometryReferenceList, aas.SubmodelElement
                    ):
                        geometryReferenceList = self.GeometryReferenceList(
                            geometryReferenceList
                        )

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError(
                            "iDList3DModel takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(
                        iDList3DModel, aas.SubmodelElement
                    ):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError(
                            "reference2DList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(
                        reference2DList, aas.SubmodelElement
                    ):
                        reference2DList = self.Reference2DList(reference2DList)

                    # A str would be split into its characters
                    if isinstance(sL_Parameters, str):
                        raise TypeError(
                            "sL_Parameters takes several elements, got a str"
                        )

                    # A str would be split into its characters
                    if isinstance(sF_Parameters, str):
                        raise TypeError(
                            "sF_Parameters takes several elements, got a str"
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        aSF_FeatureName,
                        aSF_Description,
                        measurementProcedure,
                        toleranceNorm,
                        inspectionRelevant,
                        arealSurfaceFeatureType,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
                        sL_Parameters,
                        sF_Parameters,
                        smr_Parameters,
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
                arealsurfacefeatureslist_items: Optional[
                    Iterable[Arealsurfacefeatureslist_item]
                ] = None,
                id_short: Optional[str] = r"ArealSurfaceFeaturesList",
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
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/ArealSurfaceFeaturesList/1/0",
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
                            r"en": r"List of areal surface parameters according to EN ISO 25178-1",
                            r"de": r"Liste flächenhafter Oberflächenkenngrößen gemäß EN ISO 25178-1",
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
                if isinstance(arealsurfacefeatureslist_items, str):
                    raise TypeError(
                        "arealsurfacefeatureslist_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [arealsurfacefeatureslist_items]:
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

        def __init__(
            self,
            linearFeaturesList: Optional[
                Union[
                    Iterable[LinearFeaturesList.Linearfeatureslist_item],
                    LinearFeaturesList,
                ]
            ] = None,
            attributiveFeaturesList: Optional[
                Union[
                    Iterable[AttributiveFeaturesList.Attributivefeatureslist_item],
                    AttributiveFeaturesList,
                ]
            ] = None,
            geometricFeaturesList: Optional[
                Union[
                    Iterable[GeometricFeaturesList.Geometricfeatureslist_item],
                    GeometricFeaturesList,
                ]
            ] = None,
            arealSurfaceFeaturesList: Optional[
                Union[
                    Iterable[ArealSurfaceFeaturesList.Arealsurfacefeatureslist_item],
                    ArealSurfaceFeaturesList,
                ]
            ] = None,
            id_short: Optional[str] = r"QualityFeatures",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/QualityControlForMachining/QualityFeatures/1/0",
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
                        r"en": r"Quality criteria of the item and their properties",
                        r"de": r"Qualitätskriterien des Artikels und deren Eigenschaften",
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
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(linearFeaturesList, str):
                raise TypeError("linearFeaturesList takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if linearFeaturesList is not None and not isinstance(
                linearFeaturesList, aas.SubmodelElement
            ):
                linearFeaturesList = self.LinearFeaturesList(linearFeaturesList)

            # A str would be split into its characters
            if isinstance(attributiveFeaturesList, str):
                raise TypeError(
                    "attributiveFeaturesList takes several elements, got a str"
                )

            # Build a submodel element if a raw value was passed in the argument

            if attributiveFeaturesList is not None and not isinstance(
                attributiveFeaturesList, aas.SubmodelElement
            ):
                attributiveFeaturesList = self.AttributiveFeaturesList(
                    attributiveFeaturesList
                )

            # A str would be split into its characters
            if isinstance(geometricFeaturesList, str):
                raise TypeError(
                    "geometricFeaturesList takes several elements, got a str"
                )

            # Build a submodel element if a raw value was passed in the argument

            if geometricFeaturesList is not None and not isinstance(
                geometricFeaturesList, aas.SubmodelElement
            ):
                geometricFeaturesList = self.GeometricFeaturesList(
                    geometricFeaturesList
                )

            # A str would be split into its characters
            if isinstance(arealSurfaceFeaturesList, str):
                raise TypeError(
                    "arealSurfaceFeaturesList takes several elements, got a str"
                )

            # Build a submodel element if a raw value was passed in the argument

            if arealSurfaceFeaturesList is not None and not isinstance(
                arealSurfaceFeaturesList, aas.SubmodelElement
            ):
                arealSurfaceFeaturesList = self.ArealSurfaceFeaturesList(
                    arealSurfaceFeaturesList
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                linearFeaturesList,
                attributiveFeaturesList,
                geometricFeaturesList,
                arealSurfaceFeaturesList,
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

    class ProductionCriteria(aas.SubmodelElementCollection):

        class TechnicalData(aas.ReferenceElement):

            def __init__(
                self,
                value: aas.Reference,
                id_short: Optional[str] = r"TechnicalData",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/TechnicalData/1/0",
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
                            r"en": "Reference to the AAS Submodel Technical Data for Industrial\nEquipment in Manufacturing",
                            r"de": 'Referenz auf das AAS Submodel Technical Data for Industrial\nEquipment in Manufacturing"',
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

        class ProductionJobOrderParameters(aas.SubmodelElementCollection):

            class ProductionStart(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"ProductionStart",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/ProductionStart/1/0",
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
                                    value=r"0112/2///61360_4#ADA031#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Date and time when production started for the production order",
                                r"de": r"Datum und Uhrzeit des Starts der Produktion für den Produktionsauftrag",
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ProductionEnd(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"ProductionEnd",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/ProductionEnd/1/0",
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
                                    value=r"0112/2///61360_4#ADA031#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Date and time when production ended for the production order",
                                r"de": r"Datum und Uhrzeit des Endes der Produktion für den Produktionsauftrag",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class JobName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"JobName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/JobName/1/0",
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
                                r"en": r"Human readable name of the job. Array shall always contain the same text, potentially in different languages.",
                                r"de": r"Für Menschen lesbarer Name des Jobs. Das Array muss immer denselben Text enthalten, möglicherweise in verschiedenen Sprachen.",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class JobOrderNumber(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"JobOrderNumber",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/JobOrderNumber/1/0",
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
                                r"en": r"The OrderNumbers are used to reference company internal ERP orders the job order belongs to. Shall be provided in JobOrderParameters if any planned produced material uses OrderNumber as Identification and shall contain all those OrderNumbers.",
                                r"de": r"Die Bestellnummern werden verwendet, um unternehmensinterne ERP-Bestellungen zu referenzieren, zu denen der Auftrag gehört. Wird in JobOrderParameters angegeben, wenn ein geplantes produziertes Material die Bestellnummer als Identifikation verwendet, und muss alle diese Bestellnummern enthalten.",
                            }
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class PlannedPartsPerRun(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"PlannedPartsPerRun",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/PlannedPartsPerRun/1/0",
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
                                r"en": r"The number of parts produced by one run",
                                r"de": r"Die Anzahl der Teile, die in einem Lauf produziert werden",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class PlannedOrderQuantity(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"PlannedOrderQuantity",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/PlannedOrderQuantity/1/0",
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
                                r"en": r"The planned order quantity shall be the planned quantity of products for a production order (lot size, production order quantity). [Source: ISO 22400]",
                                r"de": r"Die geplante Auftragsmenge ist die geplante Produktmenge für einen Produktionsauftrag (Losgröße, Produktionsauftragsmenge). [Quelle: ISO 22400]",
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ActualPartsInRun(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"ActualPartsInRun",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/ActualPartsInRun/1/0",
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
                                r"en": r"The number of parts actually measuerd by one run",
                                r"de": r"Die Anzahl der Teile, die in einem Lauf tatsächlich gemessen werden",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class JobFinished(aas.Property):

                def __init__(
                    self,
                    value: bool,
                    id_short: Optional[str] = r"JobFinished",
                    value_type: aas.DataTypeDefXsd = bool,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/JobFinished/1/0",
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
                                r"en": r"Status order completed. True: yes, false: no",
                                r"de": r"Status Auftrag beendet. True: ja, false: nein",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
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
                productionStart: Union[xsd.DateTime, ProductionStart],
                jobOrderNumber: Iterable[Union[str, JobOrderNumber]],
                plannedOrderQuantity: Union[int, PlannedOrderQuantity],
                productionEnd: Optional[Union[xsd.DateTime, ProductionEnd]] = None,
                jobName: Optional[Union[str, JobName]] = None,
                plannedPartsPerRun: Optional[Union[int, PlannedPartsPerRun]] = None,
                actualPartsInRun: Optional[Union[int, ActualPartsInRun]] = None,
                jobFinished: Optional[Union[bool, JobFinished]] = None,
                id_short: Optional[str] = r"ProductionJobOrderParameters",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/ProductionJobOrderParameters/1/0",
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
                            r"en": r"Production order information",
                            r"de": r"Informationen zum Produktionsauftrag",
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if productionStart is not None and not isinstance(
                    productionStart, aas.SubmodelElement
                ):
                    productionStart = self.ProductionStart(productionStart)

                # Build a submodel element if a raw value was passed in the argument

                if productionEnd is not None and not isinstance(
                    productionEnd, aas.SubmodelElement
                ):
                    productionEnd = self.ProductionEnd(productionEnd)

                # Build a submodel element if a raw value was passed in the argument

                if jobName is not None and not isinstance(jobName, aas.SubmodelElement):
                    jobName = self.JobName(jobName)

                # A str would be split into its characters
                if isinstance(jobOrderNumber, str):
                    raise TypeError("jobOrderNumber takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if jobOrderNumber:
                    jobOrderNumber = [
                        (
                            i
                            if isinstance(i, aas.SubmodelElement)
                            else self.JobOrderNumber(i)
                        )
                        for i in jobOrderNumber
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if plannedPartsPerRun is not None and not isinstance(
                    plannedPartsPerRun, aas.SubmodelElement
                ):
                    plannedPartsPerRun = self.PlannedPartsPerRun(plannedPartsPerRun)

                # Build a submodel element if a raw value was passed in the argument

                if plannedOrderQuantity is not None and not isinstance(
                    plannedOrderQuantity, aas.SubmodelElement
                ):
                    plannedOrderQuantity = self.PlannedOrderQuantity(
                        plannedOrderQuantity
                    )

                # Build a submodel element if a raw value was passed in the argument

                if actualPartsInRun is not None and not isinstance(
                    actualPartsInRun, aas.SubmodelElement
                ):
                    actualPartsInRun = self.ActualPartsInRun(actualPartsInRun)

                # Build a submodel element if a raw value was passed in the argument

                if jobFinished is not None and not isinstance(
                    jobFinished, aas.SubmodelElement
                ):
                    jobFinished = self.JobFinished(jobFinished)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    productionStart,
                    productionEnd,
                    jobName,
                    jobOrderNumber,
                    plannedPartsPerRun,
                    plannedOrderQuantity,
                    actualPartsInRun,
                    jobFinished,
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
            productionJobOrderParameters: ProductionJobOrderParameters,
            technicalData: Optional[Union[aas.Reference, TechnicalData]] = None,
            id_short: Optional[str] = r"ProductionCriteria",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/QualityControlForMachining/ProductionCriteria/1/0",
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
                        r"en": r"Information on production-relevant criteria in connection with the production of a specific component",
                        r"de": r"Informationen zu produktionsrevelvanten Kriterien im Zusammenhang mit der Fertigung eines konkreten Bauteils",
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

            # Build a submodel element if a raw value was passed in the argument

            if technicalData is not None and not isinstance(
                technicalData, aas.SubmodelElement
            ):
                technicalData = self.TechnicalData(technicalData)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [technicalData, productionJobOrderParameters]:
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

    class PartInformation(aas.SubmodelElementCollection):

        class DigitalNameplate(aas.ReferenceElement):

            def __init__(
                self,
                value: aas.Reference,
                id_short: Optional[str] = r"DigitalNameplate",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/DigitalNameplate/1/0",
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
                            r"en": r"Reference to the component’s Digital Nameplate submodel, including details such as serial number, product family, product type, and manufacturer.",
                            r"de": r"Referenz zum Submodel Digital Nameplate des Bauteils, mit Informationen zur Seriennummer, Produktfamilie, Produkttyp und Hersteller",
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

        class PartIdentifier(aas.Property):

            def __init__(
                self,
                value: xsd.AnyURI,
                id_short: Optional[str] = r"PartIdentifier",
                value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/PartIdentifier/1/0",
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
                            r"en": r"Reference to the AAS of the component: IRDI of the management shell of the component, which is carried in the machine to assign the manufacturing data for the component",
                            r"de": r"Referenz auf die AAS des Bauteils: IRDI der Verwaltungschale des Bauteils, die in der Maschine zur Zuordnung der Fertigungsdaten für das Bauteil mitgeführt wird",
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class PartNumber(aas.Property):

            def __init__(
                self,
                value: int,
                id_short: Optional[str] = r"PartNumber",
                value_type: aas.DataTypeDefXsd = int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/PartNumber/1/0",
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
                                value=r"0112/2///61360_4#ADA029#001",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Consecutive number of the manufactured component in the batch from the CNC",
                            r"de": r"Fortlaufende Nummer des gefertigten Bauteil im Los aus der CNC",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class OrderNumber(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"OrderNumber",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/OrderNumber/1/0",
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
                            r"en": r"Identifier to identify the order. Shall be provided if defined in OutputInfo.",
                            r"de": r"Bezeichner zur Identifizierung der Bestellung. Wird bereitgestellt, wenn in Output Info definiert.",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class LotNumber(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"LotNumber",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/LotNumber/1/0",
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
                            r"en": r"Identifier to identify the production lot. Shall be provided if defined in OutputInfo.",
                            r"de": r"Bezeichner zur Identifizierung des Fertigungsloses. Wird bereitgestellt, wenn in Output Info definiert.",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class SubmodelReference3D(aas.ReferenceElement):

            def __init__(
                self,
                value: aas.Reference,
                id_short: Optional[str] = r"SubmodelReference3D",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/3DSubmodelReference/1/0",
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
                            r"en": r"Reference to IDTA Submodel Provision of 3D Models",
                            r"de": r"Reference auf IDTA Submodel Provision of 3D Models",
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

        class DrawingReference2D(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"DrawingReference2D",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/DrawingReference2D/1/0",
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
                            r"en": r"Reference to a pdf-file containing the 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed. All drawings referenced in the submodel have to be included in a single PDF document.",
                            r"de": r"Referenz zum pdf-Dokument einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann. Es wird vorausgesetzt, dass alle im Submodel referenzierten Zeichnungen in einem pdf Dokument enthalten sind.",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class CADFileReference3D(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CADFileReference3D",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/CADFileReference3D/1/0",
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
                            r"en": r"Reference to a file which contains a §D CAD  model, elg. STL-file",
                            r"de": r"Referenz auf eine Datei die ein §D CAD Modell enthält, z.B. STL-file",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
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
            partIdentifier: Union[xsd.AnyURI, PartIdentifier],
            digitalNameplate: Optional[Union[aas.Reference, DigitalNameplate]] = None,
            partNumber: Optional[Union[int, PartNumber]] = None,
            orderNumber: Optional[Union[str, OrderNumber]] = None,
            lotNumber: Optional[Union[str, LotNumber]] = None,
            submodelReference3D: Optional[
                Union[aas.Reference, SubmodelReference3D]
            ] = None,
            drawingReference2D: Optional[Union[str, DrawingReference2D]] = None,
            cADFileReference3D: Optional[Union[str, CADFileReference3D]] = None,
            id_short: Optional[str] = r"PartInformation",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/QualityControlForMachining/PartInformation/1/0",
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
                        r"en": r"Production information about the component",
                        r"de": r"Produktionsinformationen zu dem Bauteil",
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
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if digitalNameplate is not None and not isinstance(
                digitalNameplate, aas.SubmodelElement
            ):
                digitalNameplate = self.DigitalNameplate(digitalNameplate)

            # Build a submodel element if a raw value was passed in the argument

            if partIdentifier is not None and not isinstance(
                partIdentifier, aas.SubmodelElement
            ):
                partIdentifier = self.PartIdentifier(partIdentifier)

            # Build a submodel element if a raw value was passed in the argument

            if partNumber is not None and not isinstance(
                partNumber, aas.SubmodelElement
            ):
                partNumber = self.PartNumber(partNumber)

            # Build a submodel element if a raw value was passed in the argument

            if orderNumber is not None and not isinstance(
                orderNumber, aas.SubmodelElement
            ):
                orderNumber = self.OrderNumber(orderNumber)

            # Build a submodel element if a raw value was passed in the argument

            if lotNumber is not None and not isinstance(lotNumber, aas.SubmodelElement):
                lotNumber = self.LotNumber(lotNumber)

            # Build a submodel element if a raw value was passed in the argument

            if submodelReference3D is not None and not isinstance(
                submodelReference3D, aas.SubmodelElement
            ):
                submodelReference3D = self.SubmodelReference3D(submodelReference3D)

            # Build a submodel element if a raw value was passed in the argument

            if drawingReference2D is not None and not isinstance(
                drawingReference2D, aas.SubmodelElement
            ):
                drawingReference2D = self.DrawingReference2D(drawingReference2D)

            # Build a submodel element if a raw value was passed in the argument

            if cADFileReference3D is not None and not isinstance(
                cADFileReference3D, aas.SubmodelElement
            ):
                cADFileReference3D = self.CADFileReference3D(cADFileReference3D)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                digitalNameplate,
                partIdentifier,
                partNumber,
                orderNumber,
                lotNumber,
                submodelReference3D,
                drawingReference2D,
                cADFileReference3D,
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

    class QualityResponsibilityList(aas.SubmodelElementList):

        class Qualityresponsibilitylist_item(aas.SubmodelElementCollection):

            class DepartmentName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DepartmentName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/DepartmentName/1/0",
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
                                r"en": r"Name of the institution/testing body",
                                r"de": r"Bezeichnung der Institution/Prüfstelle",
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Role(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Role",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/Role/1/0",
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
                                r"en": r"Role of the QS testing body (e.g. external quality testing laboratory)",
                                r"de": r"Rolle der QS-Prüfstelle (z.B. externes Qualitätsprüflabor)",
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ContactInformation(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"ContactInformation",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/ContactInformation/1/0",
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
                                r"en": r"Reference to the AAS submodel “Contact Information”",
                                r"de": r'Referenz auf das AAS Submodel "Contact Information"',
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
                departmentName: Union[str, DepartmentName],
                role: Union[str, Role],
                contactInformation: Optional[
                    Union[aas.Reference, ContactInformation]
                ] = None,
                id_short: Optional[str] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/QualityResponsibility/1/0",
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
                            r"en": r"Information about an organizational unit responsible for quality assurance",
                            r"de": r"Informationen zu einer für Qualitätssicherung verantwortlichen Organisationseinheiten",
                        }
                    )

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

                if departmentName is not None and not isinstance(
                    departmentName, aas.SubmodelElement
                ):
                    departmentName = self.DepartmentName(departmentName)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if contactInformation is not None and not isinstance(
                    contactInformation, aas.SubmodelElement
                ):
                    contactInformation = self.ContactInformation(contactInformation)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [departmentName, role, contactInformation]:
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
            qualityresponsibilitylist_items: Optional[
                Iterable[Qualityresponsibilitylist_item]
            ] = None,
            id_short: Optional[str] = r"QualityResponsibilityList",
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
                        value=r"https://admin-shell.io/idta/QualityControlForMachining/QualityResponsibilityList/1/0",
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
                        r"en": r"List of organizational units responsible for quality assurance",
                        r"de": r"Liste der für die Qualitätssicherung verantwortlichen Organisationseinheiten",
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
            if isinstance(qualityresponsibilitylist_items, str):
                raise TypeError(
                    "qualityresponsibilitylist_items takes several elements, got a str"
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [qualityresponsibilitylist_items]:
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

    class TestingDevicesList(aas.SubmodelElementList):

        class Testingdeviceslist_item(aas.SubmodelElementCollection):

            class Responsibility(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"Responsibility",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/Responsibility/1/0",
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
                                r"en": r"Reference to SMC QualityResponsibility",
                                r"de": r"Referenz auf SMC QualityResponsibility",
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

            class DigitalNameplateTestingDevice(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"DigitalNameplateTestingDevice",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/DigitalNameplateTestingDevice/1/0",
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
                                r"en": r"Reference to the testing device’s Digital Nameplate submodel, including details such as serial number, product family, product type, and manufacturer.",
                                r"de": r"Referenz zum Submodel Digital Nameplate des Prüfgeräts, mit Informationen zur Seriennummer, Produktfamilie, Produkttyp und Hersteller",
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

            class DeviceName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DeviceName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/DeviceName/1/0",
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
                                r"en": r"Name of the test device",
                                r"de": r"Bezeichnung des Prüfgeräts",
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class MeasuringType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MeasuringType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasuringType/1/0",
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
                                r"en": r"Type of measurement method, e.g. according to DIN EN ISO 25178-6, DIN EN ISO 25178-601, DIN EN ISO 25178-602",
                                r"de": r"Art der Messmethode, z.B. nach DIN EN ISO 25178-6, DIN EN ISO 25178-601, DIN EN ISO 25178-602",
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class MeasuringUnit(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"MeasuringUnit",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasuringUnit/1/0",
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
                                r"en": r"Unit in which the information on the measuring range and resolution is given",
                                r"de": r"Einheit, in der die Angaben zum Messbereich und Auflösung erfolgen",
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class MeasuringRange(aas.Range):

                def __init__(
                    self,
                    min: float,
                    max: float,
                    id_short: Optional[str] = r"MeasuringRange",
                    value_type: aas.DataTypeDefXsd = float,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasuringRange/1/0",
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
                                    value=r"0173-1#02-AAN807#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"range defined by two values of the measurand, or quantity to be supplied, within which the limits of uncertainty of the measuring instrument are specified",
                                r"de": r"Bereich in dem die Messabweichungen oder Messgeräteabweichungen innerhalb festgelegter Grenzen bleiben",
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

            class Resolution(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"Resolution",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/Resolution/1/0",
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
                                r"en": r"Physical resolution of the measuring instrument",
                                r"de": r"Physikalische Auflösung des Messinstruments",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Accuracy(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"Accuracy",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/Accuracy/1/0",
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
                                    value=r"0173-1#02-AAQ616#009",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Accuracy expressed as a percentage. Containing the parameters referring to percentage measuring accuracy",
                                r"de": r"Genauigkeit ausgedrückt in Prozent. Enthält die Parameter, die sich auf die prozentuale Messgenauigkeit beziehen",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Norm(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Norm",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/Norm/1/0",
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
                                r"en": r"Reference to the relevant standard in which the measuring method is described, e.g. DIN EN ISO 25178-601",
                                r"de": r"Verweis auf entsprechende Norm in der die Messmethode beschrieben ist, z.B. DIN EN ISO 25178-601",
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

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class CalibrationCertificate(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"CalibrationCertificate",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/CalibrationCertificate/1/0",
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
                                r"en": r"Reference to AAS Submodel Digital Quality Document",
                                r"de": r"Referenz auf AAS Submodel Digital Quality Document",
                            }
                        )

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
                deviceName: Union[str, DeviceName],
                measuringType: Union[str, MeasuringType],
                measuringUnit: Union[str, MeasuringUnit],
                measuringRange: Union[Tuple[float, float], MeasuringRange],
                responsibility: Optional[Union[aas.Reference, Responsibility]] = None,
                digitalNameplateTestingDevice: Optional[
                    Union[aas.Reference, DigitalNameplateTestingDevice]
                ] = None,
                resolution: Optional[Union[float, Resolution]] = None,
                accuracy: Optional[Union[float, Accuracy]] = None,
                norm: Optional[Union[str, Norm]] = None,
                calibrationCertificate: Optional[
                    Iterable[Union[aas.Reference, CalibrationCertificate]]
                ] = None,
                id_short: Optional[str] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/TestingDeviceProperties/1/0",
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
                            r"en": r"QS relevant information about the test device",
                            r"de": r"QS relelvante Informationen über das Prüfgerät",
                        }
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if responsibility is not None and not isinstance(
                    responsibility, aas.SubmodelElement
                ):
                    responsibility = self.Responsibility(responsibility)

                # Build a submodel element if a raw value was passed in the argument

                if digitalNameplateTestingDevice is not None and not isinstance(
                    digitalNameplateTestingDevice, aas.SubmodelElement
                ):
                    digitalNameplateTestingDevice = self.DigitalNameplateTestingDevice(
                        digitalNameplateTestingDevice
                    )

                # Build a submodel element if a raw value was passed in the argument

                if deviceName is not None and not isinstance(
                    deviceName, aas.SubmodelElement
                ):
                    deviceName = self.DeviceName(deviceName)

                # Build a submodel element if a raw value was passed in the argument

                if measuringType is not None and not isinstance(
                    measuringType, aas.SubmodelElement
                ):
                    measuringType = self.MeasuringType(measuringType)

                # Build a submodel element if a raw value was passed in the argument

                if measuringUnit is not None and not isinstance(
                    measuringUnit, aas.SubmodelElement
                ):
                    measuringUnit = self.MeasuringUnit(measuringUnit)

                # Build a submodel element if a raw value was passed in the argument

                if measuringRange is not None and not isinstance(
                    measuringRange, aas.SubmodelElement
                ):
                    measuringRange = self.MeasuringRange(
                        min=measuringRange[0], max=measuringRange[1]
                    )

                # Build a submodel element if a raw value was passed in the argument

                if resolution is not None and not isinstance(
                    resolution, aas.SubmodelElement
                ):
                    resolution = self.Resolution(resolution)

                # Build a submodel element if a raw value was passed in the argument

                if accuracy is not None and not isinstance(
                    accuracy, aas.SubmodelElement
                ):
                    accuracy = self.Accuracy(accuracy)

                # Build a submodel element if a raw value was passed in the argument

                if norm is not None and not isinstance(norm, aas.SubmodelElement):
                    norm = self.Norm(norm)

                # A str would be split into its characters
                if isinstance(calibrationCertificate, str):
                    raise TypeError(
                        "calibrationCertificate takes several elements, got a str"
                    )

                # Build submodel elements from raw values passed in the argument
                if calibrationCertificate:
                    calibrationCertificate = [
                        (
                            i
                            if isinstance(i, aas.SubmodelElement)
                            else self.CalibrationCertificate(i)
                        )
                        for i in calibrationCertificate
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    responsibility,
                    digitalNameplateTestingDevice,
                    deviceName,
                    measuringType,
                    measuringUnit,
                    measuringRange,
                    resolution,
                    accuracy,
                    norm,
                    calibrationCertificate,
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
            testingdeviceslist_items: Iterable[Testingdeviceslist_item],
            id_short: Optional[str] = r"TestingDevicesList",
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
                        value=r"https://admin-shell.io/idta/QualityControlForMachining/TestingDevicesList/1/0",
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
                        r"en": r"List of testing devices used",
                        r"de": r"Liste der verwendeten Prüfgeräte",
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
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(testingdeviceslist_items, str):
                raise TypeError(
                    "testingdeviceslist_items takes several elements, got a str"
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [testingdeviceslist_items]:
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

    class MetrologyJobResults(aas.SubmodelElementCollection):

        class JobStart(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"JobStart",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/JobStart/1/0",
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
                            r"en": r"Date time of job start",
                            r"de": r"Datum und Zeit des Starts des Auftrags",
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class JobEnd(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"JobEnd",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/JobEnd/1/0",
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
                            r"en": r"Date time of job end",
                            r"de": r"Datum und Zeit des Endes des Auftrags",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class JobName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"JobName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/JobName/1/0",
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
                            r"en": r"Human readable name of the job. Array shall always contain the same text, potentially in different languages.",
                            r"de": r"Für Menschen lesbarer Name des Jobs. Das Array muss immer denselben Text enthalten, möglicherweise in verschiedenen Sprachen.",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class JobOrderNumber(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"JobOrderNumber",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/JobOrderNumber/1/0",
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
                            r"en": r"The OrderNumbers are used to reference company internal ERP orders the job order belongs to. Shall be provided in JobOrderParameters if any planned produced material uses OrderNumber as Identification and shall contain all those OrderNumbers.",
                            r"de": r"Die Bestellnummern werden verwendet, um unternehmensinterne ERP-Bestellungen zu referenzieren, zu denen der Auftrag gehört. Wird in JobOrderParameters angegeben, wenn ein geplantes produziertes Material die Bestellnummer als Identifikation verwendet, und muss alle diese Bestellnummern enthalten.",
                        }
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class PlannedPartsPerRun(aas.Property):

            def __init__(
                self,
                value: int,
                id_short: Optional[str] = r"PlannedPartsPerRun",
                value_type: aas.DataTypeDefXsd = int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/PlannedPartsPerRun/1/0",
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
                            r"en": r"The number of parts planned to be measured by one run",
                            r"de": r"Die Anzahl der Teile, die in einem Lauf gemessen werden sollen",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ActualPartsInRun(aas.Property):

            def __init__(
                self,
                value: int,
                id_short: Optional[str] = r"ActualPartsInRun",
                value_type: aas.DataTypeDefXsd = int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/ActualPartsInRun/1/0",
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
                            r"en": r"The number of parts actually measuerd by one run",
                            r"de": r"Die Anzahl der Teile, die in einem Lauf tatsächlich gemessen werden",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class JobFinished(aas.Property):

            def __init__(
                self,
                value: bool,
                id_short: Optional[str] = r"JobFinished",
                value_type: aas.DataTypeDefXsd = bool,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/JobFinished/1/0",
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
                            r"en": r"Status order completed. True: yes, false: no",
                            r"de": r"Status Auftrag beendet. True: ja, false: nein",
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

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class MetrologyResultsList(aas.SubmodelElementList):

            class Metrologyresultslist_item(aas.SubmodelElementCollection):

                class QualityFeatureReference(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = r"QualityFeatureReference",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/QualityFeatureReference/1/0",
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
                                    r"en": r"Reference to QualityFeature in SMC QualityFeaturesList",
                                    r"de": r"Referenz auf QualityFeature in SMC QualityFeaturesList",
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

                class TestingDeviceReference(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = r"TestingDeviceReference",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/TestingDeviceReference/1/0",
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
                                    r"en": r"Reference to the test device used in SMC TestingDeviceList",
                                    r"de": r"Referenz auf das verwendete Prüfgerät in SMC TestingDeviceList",
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

                class PartReference(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = r"PartReference",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/PartReference/1/0",
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
                                    r"en": r"Reference to the AAS of the component if the SMC MetrologyData is not within this AAS",
                                    r"de": r"Referenz auf die AAS des Bauteils, falls sich die SMC MetrologyData nicht innerhalb dieser AAS befindet",
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

                class ID(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ID",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/ID/1/0",
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
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Description(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Description",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Description/1/0",
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
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class EngineeringUnit(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"EngineeringUnit",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/EngineeringUnit/1/0",
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
                                    r"en": r"Physical unit of feature",
                                    r"de": r"Physikalische Einheit des Merkmals",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class QualityActualValue(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"QualityActualValue",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/QualityActualValue/1/0",
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
                                    r"en": r"Value or values (with several repeated measurements) for the specific quality feature of the component",
                                    r"de": r"Wert oder Werte (bei mehreren Wiederholungsmessungen) für das bestimmte Qualitätsmerkmal des Bauteils",
                                }
                            )

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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class QualityActualAttribute(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"QualityActualAttribute",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/QualityActualAttribute/1/0",
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
                                    r"en": r"For attributive characteristics: attribute or attributes in the case of several repeat determinations) for the specific quality characteristic of the component",
                                    r"de": r"Bei attributiven Qualitätsmerkmalen: Attribut oder Attibute bei mehreren Wiederholungsbestimmungen für das bestimmte Qualitätsmerkmal des Bauteils",
                                }
                            )

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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class QualityInSpec(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"QualityInSpec",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/QualityInSpec/1/0",
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
                                    r"en": r"Indication whether the feature is within the tolerance, i.e. OK.",
                                    r"de": r"Angabe, ob das Merkmal innerhalb der Toleranz liegt, also i.O. ist.",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Deviation(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"Deviation",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Deviation/1/0",
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
                                    r"en": r"Deviation from nominal value",
                                    r"de": r"Abweichung vom Sollwert",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class AverageValue(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"AverageValue",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/AverageValue/1/0",
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
                                    r"en": r"Average value, if several values ​​are measured when determining the characteristic",
                                    r"de": r"Arithmetischer Mittelwert, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class MinValue(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"MinValue",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MinValue/1/0",
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
                                    r"en": r"Minimum value if several values ​​are measured when determining the characteristic",
                                    r"de": r"Minimaler Wert, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class MaxValue(aas.Property):

                    def __init__(
                        self,
                        value: float,
                        id_short: Optional[str] = r"MaxValue",
                        value_type: aas.DataTypeDefXsd = float,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MaxValue/1/0",
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
                                    r"en": r"Maximum value if several values ​​are measured when determining the characteristic",
                                    r"de": r"Maximaler Wert, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
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
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/Standarddeviation/1/0",
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
                                    r"en": r"Standarddeviation of measuring results if several values ​​are measured when determining the characteristic",
                                    r"de": r"Standardabweichung der Messergebnisse, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
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

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class DataAggregatedFromSeries(aas.Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"DataAggregatedFromSeries",
                        value_type: aas.DataTypeDefXsd = bool,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/DataAggregatedFromSeries/1/0",
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
                                    r"en": r"Boolean variable which indicates that the measured quality data is provided as aggregated value for a series of parts (e.g. as an average value for a lot or batch). Has to be set on false, if the measuring data is provided part specific.",
                                    r"de": r"Boolesche Variable, die angibt, dass die gemessenen Qualitätsdaten als aggregierter Wert, z.B. als Mittelwert für eine Reihe von Teilen (z. B. Los oder Charge) bereitgestellt werden. Muss auf false gesetzt werden, wenn die Messdaten teilespezifisch bereitgestellt werden.",
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
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class MeasuredValuesList(aas.SubmodelElementList):

                    class Measuredvalueslist_item(aas.Property):

                        def __init__(
                            self,
                            value: float,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasuredValue/1/0",
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
                                        r"en": r"Measured value",
                                        r"de": r"Gemessener Wert",
                                    }
                                )

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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        measuredvalueslist_items: Optional[
                            Iterable[Union[float, Measuredvalueslist_item]]
                        ] = None,
                        id_short: Optional[str] = r"MeasuredValuesList",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = float,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MeasuredValuesList/1/0",
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
                                    r"en": r"Optional list of measured values",
                                    r"de": r"Optionale Liste gemessener Werte",
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
                        if isinstance(measuredvalueslist_items, str):
                            raise TypeError(
                                "measuredvalueslist_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if measuredvalueslist_items:
                            measuredvalueslist_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Measuredvalueslist_item(i)
                                )
                                for i in measuredvalueslist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [measuredvalueslist_items]:
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

                class MetrologyDataFile(aas.SubmodelElementCollection):

                    class FileLink(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"FileLink",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/File/1/0",
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
                                            value=r"0173-1#02-ABK126#001",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Link to the file",
                                        r"de": r"Link zu der Datei",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class MimeType(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"MimeType",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/QualityControlForMachining/MimeType/1/0",
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
                                            value=r"0112/2///61360_4#ACB113#001",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"MIME type of the file",
                                        r"de": r"MIME-typ der Datei",
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

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
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
                        fileLink: Optional[Union[xsd.AnyURI, FileLink]] = None,
                        mimeType: Optional[Union[str, MimeType]] = None,
                        id_short: Optional[str] = r"MetrologyDataFile",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyDataFile/1/0",
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
                                    r"en": r"Optional measurement data file with the original measurement protocol",
                                    r"de": r"Optionale Messdatendatei mit dem original Messprotokoll",
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

                        # Build a submodel element if a raw value was passed in the argument

                        if fileLink is not None and not isinstance(
                            fileLink, aas.SubmodelElement
                        ):
                            fileLink = self.FileLink(fileLink)

                        # Build a submodel element if a raw value was passed in the argument

                        if mimeType is not None and not isinstance(
                            mimeType, aas.SubmodelElement
                        ):
                            mimeType = self.MimeType(mimeType)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [fileLink, mimeType]:
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
                    qualityFeatureReference: Union[
                        aas.Reference, QualityFeatureReference
                    ],
                    testingDeviceReference: Union[
                        aas.Reference, TestingDeviceReference
                    ],
                    partReference: Union[aas.Reference, PartReference],
                    qualityInSpec: Union[bool, QualityInSpec],
                    dataAggregatedFromSeries: Union[bool, DataAggregatedFromSeries],
                    iD: Optional[Union[str, ID]] = None,
                    description_: Optional[Union[str, Description]] = None,
                    engineeringUnit: Optional[Union[str, EngineeringUnit]] = None,
                    qualityActualValue: Optional[
                        Iterable[Union[float, QualityActualValue]]
                    ] = None,
                    qualityActualAttribute: Optional[
                        Iterable[Union[str, QualityActualAttribute]]
                    ] = None,
                    deviation: Optional[Union[float, Deviation]] = None,
                    averageValue: Optional[Union[float, AverageValue]] = None,
                    minValue: Optional[Union[float, MinValue]] = None,
                    maxValue: Optional[Union[float, MaxValue]] = None,
                    standarddeviation: Optional[Union[float, Standarddeviation]] = None,
                    measuredValuesList: Optional[
                        Union[
                            Iterable[
                                Union[float, MeasuredValuesList.Measuredvalueslist_item]
                            ],
                            MeasuredValuesList,
                        ]
                    ] = None,
                    metrologyDataFile: Optional[MetrologyDataFile] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyData/1/0",
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
                                r"en": r"Measurement results a quality feature",
                                r"de": r"Messergebnisse einem Qualitätsmerkmal",
                            }
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
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if qualityFeatureReference is not None and not isinstance(
                        qualityFeatureReference, aas.SubmodelElement
                    ):
                        qualityFeatureReference = self.QualityFeatureReference(
                            qualityFeatureReference
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if testingDeviceReference is not None and not isinstance(
                        testingDeviceReference, aas.SubmodelElement
                    ):
                        testingDeviceReference = self.TestingDeviceReference(
                            testingDeviceReference
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if partReference is not None and not isinstance(
                        partReference, aas.SubmodelElement
                    ):
                        partReference = self.PartReference(partReference)

                    # Build a submodel element if a raw value was passed in the argument

                    if iD is not None and not isinstance(iD, aas.SubmodelElement):
                        iD = self.ID(iD)

                    # Build a submodel element if a raw value was passed in the argument

                    if description_ is not None and not isinstance(
                        description_, aas.SubmodelElement
                    ):
                        description_ = self.Description(description_)

                    # Build a submodel element if a raw value was passed in the argument

                    if engineeringUnit is not None and not isinstance(
                        engineeringUnit, aas.SubmodelElement
                    ):
                        engineeringUnit = self.EngineeringUnit(engineeringUnit)

                    # A str would be split into its characters
                    if isinstance(qualityActualValue, str):
                        raise TypeError(
                            "qualityActualValue takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if qualityActualValue:
                        qualityActualValue = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.QualityActualValue(i)
                            )
                            for i in qualityActualValue
                        ]

                    # A str would be split into its characters
                    if isinstance(qualityActualAttribute, str):
                        raise TypeError(
                            "qualityActualAttribute takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if qualityActualAttribute:
                        qualityActualAttribute = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.QualityActualAttribute(i)
                            )
                            for i in qualityActualAttribute
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if qualityInSpec is not None and not isinstance(
                        qualityInSpec, aas.SubmodelElement
                    ):
                        qualityInSpec = self.QualityInSpec(qualityInSpec)

                    # Build a submodel element if a raw value was passed in the argument

                    if deviation is not None and not isinstance(
                        deviation, aas.SubmodelElement
                    ):
                        deviation = self.Deviation(deviation)

                    # Build a submodel element if a raw value was passed in the argument

                    if averageValue is not None and not isinstance(
                        averageValue, aas.SubmodelElement
                    ):
                        averageValue = self.AverageValue(averageValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if minValue is not None and not isinstance(
                        minValue, aas.SubmodelElement
                    ):
                        minValue = self.MinValue(minValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if maxValue is not None and not isinstance(
                        maxValue, aas.SubmodelElement
                    ):
                        maxValue = self.MaxValue(maxValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if standarddeviation is not None and not isinstance(
                        standarddeviation, aas.SubmodelElement
                    ):
                        standarddeviation = self.Standarddeviation(standarddeviation)

                    # Build a submodel element if a raw value was passed in the argument

                    if dataAggregatedFromSeries is not None and not isinstance(
                        dataAggregatedFromSeries, aas.SubmodelElement
                    ):
                        dataAggregatedFromSeries = self.DataAggregatedFromSeries(
                            dataAggregatedFromSeries
                        )

                    # A str would be split into its characters
                    if isinstance(measuredValuesList, str):
                        raise TypeError(
                            "measuredValuesList takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if measuredValuesList is not None and not isinstance(
                        measuredValuesList, aas.SubmodelElement
                    ):
                        measuredValuesList = self.MeasuredValuesList(measuredValuesList)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        qualityFeatureReference,
                        testingDeviceReference,
                        partReference,
                        iD,
                        description_,
                        engineeringUnit,
                        qualityActualValue,
                        qualityActualAttribute,
                        qualityInSpec,
                        deviation,
                        averageValue,
                        minValue,
                        maxValue,
                        standarddeviation,
                        dataAggregatedFromSeries,
                        measuredValuesList,
                        metrologyDataFile,
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
                metrologyresultslist_items: Iterable[Metrologyresultslist_item],
                id_short: Optional[str] = r"MetrologyResultsList",
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
                            value=r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyResultsList/1/0",
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
                            r"en": r"List of measurement results for the quality characteristics",
                            r"de": r"Liste der Messergebnisse zu den Qualitätsmerkmalen",
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
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(metrologyresultslist_items, str):
                    raise TypeError(
                        "metrologyresultslist_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [metrologyresultslist_items]:
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

        def __init__(
            self,
            jobStart: Union[xsd.DateTime, JobStart],
            jobOrderNumber: Iterable[Union[str, JobOrderNumber]],
            metrologyResultsList: Union[
                Iterable[MetrologyResultsList.Metrologyresultslist_item],
                MetrologyResultsList,
            ],
            jobEnd: Optional[Union[xsd.DateTime, JobEnd]] = None,
            jobName: Optional[Union[str, JobName]] = None,
            plannedPartsPerRun: Optional[Union[int, PlannedPartsPerRun]] = None,
            actualPartsInRun: Optional[Union[int, ActualPartsInRun]] = None,
            jobFinished: Optional[Union[bool, JobFinished]] = None,
            id_short: Optional[str] = r"MetrologyJobResults",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyJobResults/1/0",
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
                        r"en": r"Information and measurements on the results of a quality assessment order",
                        r"de": r"Informationen und Messwerte zu Ergebnissen eines Qualitätsbewertungsauftrag",
                    }
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
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if jobStart is not None and not isinstance(jobStart, aas.SubmodelElement):
                jobStart = self.JobStart(jobStart)

            # Build a submodel element if a raw value was passed in the argument

            if jobEnd is not None and not isinstance(jobEnd, aas.SubmodelElement):
                jobEnd = self.JobEnd(jobEnd)

            # Build a submodel element if a raw value was passed in the argument

            if jobName is not None and not isinstance(jobName, aas.SubmodelElement):
                jobName = self.JobName(jobName)

            # A str would be split into its characters
            if isinstance(jobOrderNumber, str):
                raise TypeError("jobOrderNumber takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if jobOrderNumber:
                jobOrderNumber = [
                    i if isinstance(i, aas.SubmodelElement) else self.JobOrderNumber(i)
                    for i in jobOrderNumber
                ]

            # Build a submodel element if a raw value was passed in the argument

            if plannedPartsPerRun is not None and not isinstance(
                plannedPartsPerRun, aas.SubmodelElement
            ):
                plannedPartsPerRun = self.PlannedPartsPerRun(plannedPartsPerRun)

            # Build a submodel element if a raw value was passed in the argument

            if actualPartsInRun is not None and not isinstance(
                actualPartsInRun, aas.SubmodelElement
            ):
                actualPartsInRun = self.ActualPartsInRun(actualPartsInRun)

            # Build a submodel element if a raw value was passed in the argument

            if jobFinished is not None and not isinstance(
                jobFinished, aas.SubmodelElement
            ):
                jobFinished = self.JobFinished(jobFinished)

            # A str would be split into its characters
            if isinstance(metrologyResultsList, str):
                raise TypeError(
                    "metrologyResultsList takes several elements, got a str"
                )

            # Build a submodel element if a raw value was passed in the argument

            if metrologyResultsList is not None and not isinstance(
                metrologyResultsList, aas.SubmodelElement
            ):
                metrologyResultsList = self.MetrologyResultsList(metrologyResultsList)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                jobStart,
                jobEnd,
                jobName,
                jobOrderNumber,
                plannedPartsPerRun,
                actualPartsInRun,
                jobFinished,
                metrologyResultsList,
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
        qualityFeatures: QualityFeatures,
        partInformation: PartInformation,
        testingDevicesList: Union[
            Iterable[TestingDevicesList.Testingdeviceslist_item], TestingDevicesList
        ],
        metrologyJobResults: Iterable[MetrologyJobResults],
        productionCriteria: Optional[ProductionCriteria] = None,
        qualityResponsibilityList: Optional[
            Union[
                Iterable[QualityResponsibilityList.Qualityresponsibilitylist_item],
                QualityResponsibilityList,
            ]
        ] = None,
        id_short: Optional[str] = r"QualityControlForMachining",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = None,
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.TEMPLATE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel Quality Control for Machining allows the collection of quality relevant information about parts produced in cyclical manufacturing processes. The focus is on looking at the production result and on machining manufacturing processes of milling, turning and drilling. However, the Submodel can also be used for other manufacturing processes.",
                    r"de": r"Das Teilmodell Quality Control for Machining erlaubt die Erfassung von qualitätsrelevanten Informationen über in zyklischen Fertigungsprozessen produzierte Bauteile. Der Fokus liegt auf der Betrachtung des Produktionsresultats und auf den zerspanenden Fertigungsverfahren Fräsen, Drehen, Bohren. Das Teilmodell kann jedoch auch für andere Fertigungsverfahren verwendet werden.",
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02049",
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # A str would be split into its characters
        if isinstance(qualityResponsibilityList, str):
            raise TypeError(
                "qualityResponsibilityList takes several elements, got a str"
            )

        # Build a submodel element if a raw value was passed in the argument

        if qualityResponsibilityList is not None and not isinstance(
            qualityResponsibilityList, aas.SubmodelElement
        ):
            qualityResponsibilityList = self.QualityResponsibilityList(
                qualityResponsibilityList
            )

        # A str would be split into its characters
        if isinstance(testingDevicesList, str):
            raise TypeError("testingDevicesList takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if testingDevicesList is not None and not isinstance(
            testingDevicesList, aas.SubmodelElement
        ):
            testingDevicesList = self.TestingDevicesList(testingDevicesList)

        # A str would be split into its characters
        if isinstance(metrologyJobResults, str):
            raise TypeError("metrologyJobResults takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            qualityFeatures,
            productionCriteria,
            partInformation,
            qualityResponsibilityList,
            testingDevicesList,
            metrologyJobResults,
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
