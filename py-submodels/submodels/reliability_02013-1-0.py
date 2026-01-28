from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class Reliability(Submodel):
    class NumberOfReliabilitySets(Property):
        def __init__(
            self,
            value: Int,
            id_short: str = "NumberOfReliabilitySets",
            value_type: DataTypeDef = Int,
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0112/2///62683#ACE006#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "number of reliability sets of characteristics",
                    "fr": "nombre d'ensembles de caractéristiques de fiabilité",
                }

            if qualifier is None:
                qualifier = set()

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class OperatingConditionsOfReliabilityCharacteristics(
        SubmodelElementCollectionUnordered
    ):
        class TypeOfVoltage(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "TypeOfVoltage",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///61987#ABL837#001",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///61987#ABL838#001",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///61987#ABI407#004",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///61987#ABA969#007",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "type of voltage",
                        "fr": "type de tension",
                        "de": "Spannungsart",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class RatedVoltage(Property):
            def __init__(
                self,
                value: float,
                id_short: str = "RatedVoltage",
                value_type: DataTypeDef = float,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///61987#ABA588#004",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "rated voltage",
                        "fr": "tension assignée",
                        "de": "Bemessungsspannung",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class MinimumRatedVoltage(Property):
            def __init__(
                self,
                value: float,
                id_short: str = "MinimumRatedVoltage",
                value_type: DataTypeDef = float,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///61987#ABD461#004",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "minimum rated voltage",
                        "fr": "tension assignée minimale",
                        "de": "minimale Bemessungsspannung",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class MaximumRatedVoltage(Property):
            def __init__(
                self,
                value: float,
                id_short: str = "MaximumRatedVoltage",
                value_type: DataTypeDef = float,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///61987#ABD462#004",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "maximum rated voltage",
                        "fr": "tension assignée maximale",
                        "de": "maximale Bemessungsspannung",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class RatedOperationalCurrent(Property):
            def __init__(
                self,
                value: float,
                id_short: str = "RatedOperationalCurrent",
                value_type: DataTypeDef = float,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/FunctionalSafety/RatedOperationalCurrent/1/0",
                            id_type=KeyType.IRI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {"en": "rated operational current"}

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class TypeOfInterlockingDevice(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "TypeOfInterlockingDevice",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH673#001",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH674#001",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH675#001",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH676#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACE053#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "type of interlocking device",
                        "fr": "type de dispositif de verrouillage",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class OtherOperatingConditions(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "OtherOperatingConditions",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACE070#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "other operating conditions",
                        "fr": "autres conditions de fonctionnement",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class UsefulLifeInNumberOfOperations(Property):
            def __init__(
                self,
                value: float,
                id_short: str = "UsefulLifeInNumberOfOperations",
                value_type: DataTypeDef = float,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACE055#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "useful life in number of operations",
                        "fr": "durée de vie utile en cycle de fonctionnement",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class UsefulLifeInTimeInterval(Property):
            def __init__(
                self,
                value: float,
                id_short: str = "UsefulLifeInTimeInterval",
                value_type: DataTypeDef = float,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACE054#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "useful life in time interval",
                        "fr": "durée de vie utile en intervalle de temps",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        def __init__(
            self,
            typeOfVoltage: Union[str, TypeOfVoltage],
            ratedVoltage: Union[float, RatedVoltage],
            minimumRatedVoltage: Union[float, MinimumRatedVoltage],
            maximumRatedVoltage: Union[float, MaximumRatedVoltage],
            ratedOperationalCurrent: Union[float, RatedOperationalCurrent],
            typeOfInterlockingDevice: Union[str, TypeOfInterlockingDevice],
            otherOperatingConditions: Union[str, OtherOperatingConditions],
            usefulLifeInNumberOfOperations: Union[
                float, UsefulLifeInNumberOfOperations
            ],
            usefulLifeInTimeInterval: Union[float, UsefulLifeInTimeInterval],
            id_short: str = "OperatingConditionsOfReliabilityCharacteristics",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0112/2///62683#ACG071#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "operating conditions of reliability characteristics",
                    "fr": "conditions de fonctionnement des caractéristiques de fiabilité et de sécurité fonctionnelle",
                }

            if qualifier is None:
                qualifier = set()

            # Build a submodel element if a raw value was passed in the argument
            if typeOfVoltage and not isinstance(typeOfVoltage, SubmodelElement):
                typeOfVoltage = self.TypeOfVoltage(typeOfVoltage)

            # Build a submodel element if a raw value was passed in the argument
            if ratedVoltage and not isinstance(ratedVoltage, SubmodelElement):
                ratedVoltage = self.RatedVoltage(ratedVoltage)

            # Build a submodel element if a raw value was passed in the argument
            if minimumRatedVoltage and not isinstance(
                minimumRatedVoltage, SubmodelElement
            ):
                minimumRatedVoltage = self.MinimumRatedVoltage(minimumRatedVoltage)

            # Build a submodel element if a raw value was passed in the argument
            if maximumRatedVoltage and not isinstance(
                maximumRatedVoltage, SubmodelElement
            ):
                maximumRatedVoltage = self.MaximumRatedVoltage(maximumRatedVoltage)

            # Build a submodel element if a raw value was passed in the argument
            if ratedOperationalCurrent and not isinstance(
                ratedOperationalCurrent, SubmodelElement
            ):
                ratedOperationalCurrent = self.RatedOperationalCurrent(
                    ratedOperationalCurrent
                )

            # Build a submodel element if a raw value was passed in the argument
            if typeOfInterlockingDevice and not isinstance(
                typeOfInterlockingDevice, SubmodelElement
            ):
                typeOfInterlockingDevice = self.TypeOfInterlockingDevice(
                    typeOfInterlockingDevice
                )

            # Build a submodel element if a raw value was passed in the argument
            if otherOperatingConditions and not isinstance(
                otherOperatingConditions, SubmodelElement
            ):
                otherOperatingConditions = self.OtherOperatingConditions(
                    otherOperatingConditions
                )

            # Build a submodel element if a raw value was passed in the argument
            if usefulLifeInNumberOfOperations and not isinstance(
                usefulLifeInNumberOfOperations, SubmodelElement
            ):
                usefulLifeInNumberOfOperations = self.UsefulLifeInNumberOfOperations(
                    usefulLifeInNumberOfOperations
                )

            # Build a submodel element if a raw value was passed in the argument
            if usefulLifeInTimeInterval and not isinstance(
                usefulLifeInTimeInterval, SubmodelElement
            ):
                usefulLifeInTimeInterval = self.UsefulLifeInTimeInterval(
                    usefulLifeInTimeInterval
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                typeOfVoltage,
                ratedVoltage,
                minimumRatedVoltage,
                maximumRatedVoltage,
                ratedOperationalCurrent,
                typeOfInterlockingDevice,
                otherOperatingConditions,
                usefulLifeInNumberOfOperations,
                usefulLifeInTimeInterval,
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
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class ReliabilityCharacteristics(SubmodelElementCollectionUnordered):
        class MTTF(Property):
            def __init__(
                self,
                value: Int,
                id_short: str = "MTTF",
                value_type: DataTypeDef = Int,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACE061#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "mean operating time to failure",
                        "fr": "durée moyenne de fonctionnement avant défaillance",
                        "de": "mittlere Betriebszeit bis zum Ausfall",
                        "jp": "平均故障間動作時間",
                        "cn": "平均失效前工作时间",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class MTBF(Property):
            def __init__(
                self,
                value: Int,
                id_short: str = "MTBF",
                value_type: DataTypeDef = Int,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACE062#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "mean operating time between failure",
                        "fr": "moyenne des temps de bon fonctionnement",
                        "de": "mittlere Betriebszeit zwischen Ausfällen",
                        "cn": "平均失效间隔工作时间",
                    }

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class B(Property):
            def __init__(
                self,
                value: Int,
                id_short: str = "B",
                value_type: DataTypeDef = Int,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/Reliability/B10/1/0",
                            id_type=KeyType.IRI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = set()

                if qualifier is None:
                    qualifier = set()

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        def __init__(
            self,
            mTTF: Union[Int, MTTF],
            mTBF: Union[Int, MTBF],
            b: Union[Int, B],
            id_short: str = "ReliabilityCharacteristics",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0112/2///62683#ACG080#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Reliability characteristics",
                    "fr": "Caractéristiques de fiabilité",
                }

            if qualifier is None:
                qualifier = set()

            # Build a submodel element if a raw value was passed in the argument
            if mTTF and not isinstance(mTTF, SubmodelElement):
                mTTF = self.MTTF(mTTF)

            # Build a submodel element if a raw value was passed in the argument
            if mTBF and not isinstance(mTBF, SubmodelElement):
                mTBF = self.MTBF(mTBF)

            # Build a submodel element if a raw value was passed in the argument
            if b and not isinstance(b, SubmodelElement):
                b = self.B(b)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [mTTF, mTBF, b]:
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
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    def __init__(
        self,
        identification: Identifier,
        numberOfReliabilitySets: Union[Int, NumberOfReliabilitySets],
        operatingConditionsOfReliabilityCharacteristics: OperatingConditionsOfReliabilityCharacteristics,
        reliabilityCharacteristics: ReliabilityCharacteristics,
        id_short: str = "Reliability",
        category: Optional[str] = None,
        description: Optional[LangStringSet] = None,
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version="1", revision="0"
        ),
        semantic_id: Optional[Reference] = Reference(
            key=(
                Key(
                    type_=KeyElements.SUBMODEL,
                    local=True,
                    value="https://admin-shell.io/idta/iec62683/1/0/Reliability",
                    id_type=KeyType.IRI,
                ),
            )
        ),
        qualifier: Optional[Set[Constraint]] = None,
        kind: ModelingKind = ModelingKind.INSTANCE,
    ):
        if description is None:
            description = set()

        if qualifier is None:
            qualifier = set()

        # Build a submodel element if a raw value was passed in the argument
        if numberOfReliabilitySets and not isinstance(
            numberOfReliabilitySets, SubmodelElement
        ):
            numberOfReliabilitySets = self.NumberOfReliabilitySets(
                numberOfReliabilitySets
            )

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            numberOfReliabilitySets,
            operatingConditionsOfReliabilityCharacteristics,
            reliabilityCharacteristics,
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
            identification=identification,
            id_short=id_short,
            category=category,
            description=description,
            administration=administration,
            semantic_id=semantic_id,
            qualifier=qualifier,
            kind=kind,
        )
