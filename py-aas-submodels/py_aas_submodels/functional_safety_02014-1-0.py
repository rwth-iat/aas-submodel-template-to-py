from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class FunctionalSafety(Submodel):
    class NumberOfFunctionalSafetySetsOfCharacteristics(Property):
        def __init__(
            self,
            value: Int,
            id_short: str = "NumberOfFunctionalSafetySetsOfCharacteristics",
            value_type: DataTypeDef = Int,
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0112/2///62683#ACE005#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "number of functional safety sets of characteristics",
                    "fr": "nombre d'ensembles de caractéristiques de sécurité fonctionnelle",
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

    class OperatingConditionsOfFunctionalSafetyCharacteristics(
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
            id_short: str = "OperatingConditionsOfFunctionalSafetyCharacteristics",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0112/2///62683#ACG057#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "operating conditions of functional safety characteristics",
                    "fr": "conditions de fonctionnement des caractéristiques de sécurité fonctionnelle",
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

    class SafetyDeviceTypes(SubmodelElementCollectionUnordered):
        class FunctionalSafetyDeviceType(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "FunctionalSafetyDeviceType",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH687",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH688",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH689",
                            id_type=KeyType.IRDI,
                        ),
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="0112/2///62683#ACH690",
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
                            value="0112/2///62683#ACE071#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "functional safety device type",
                        "fr": "type de dispositif de sécurité fonctionnelle",
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

        class SafetySubsystem(SubmodelElementCollectionUnordered):
            class SIL(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "SIL",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH670#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH671#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH672#001",
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
                                value="0112/2///62683#ACE051#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "safety integrity level",
                            "fr": "niveau d'intégrité de sécurité",
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

            class PFH(Property):
                def __init__(
                    self,
                    value: float,
                    id_short: str = "PFH",
                    value_type: DataTypeDef = float,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///62683#ACE052#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "probability of dangerous failure within one hour",
                            "fr": "fréquence de défaillance dangereuse par heure",
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

            class ProofTestInterval(Property):
                def __init__(
                    self,
                    value: float,
                    id_short: str = "ProofTestInterval",
                    value_type: DataTypeDef = float,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///62683#ACE058#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "proof test interval",
                            "fr": "intervalle entre essai périodique",
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

            class PL(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "PL",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH677#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH678#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH679#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH680#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH681#001",
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
                                value="0112/2///62683#ACE060#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "performance level",
                            "fr": "niveau de performance",
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

            class Category(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "Category",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH682#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH683#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH684#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH685#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH686#001",
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
                                value="0112/2///62683#ACE063#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {"en": "category", "fr": "catégory"}

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
                sIL: Union[str, SIL],
                pFH: Union[float, PFH],
                proofTestInterval: Union[float, ProofTestInterval],
                pL: Union[str, PL],
                category_se: Union[str, Category],
                id_short: str = "SafetySubsystem",
                category: str = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACG065#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Safety subsystem",
                        "fr": "Sous-système de sécurité",
                    }

                if qualifier is None:
                    qualifier = set()

                # Build a submodel element if a raw value was passed in the argument
                if sIL and not isinstance(sIL, SubmodelElement):
                    sIL = self.SIL(sIL)

                # Build a submodel element if a raw value was passed in the argument
                if pFH and not isinstance(pFH, SubmodelElement):
                    pFH = self.PFH(pFH)

                # Build a submodel element if a raw value was passed in the argument
                if proofTestInterval and not isinstance(
                    proofTestInterval, SubmodelElement
                ):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Build a submodel element if a raw value was passed in the argument
                if pL and not isinstance(pL, SubmodelElement):
                    pL = self.PL(pL)

                # Build a submodel element if a raw value was passed in the argument
                if category_se and not isinstance(category_se, SubmodelElement):
                    category_se = self.Category(category_se)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [sIL, pFH, proofTestInterval, pL, category_se]:
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

        class ElectronicElement(SubmodelElementCollectionUnordered):
            class MTTFD(Property):
                def __init__(
                    self,
                    value: Int,
                    id_short: str = "MTTFD",
                    value_type: DataTypeDef = Int,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///62683#ACE057#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "mean time to dangerous failure",
                            "fr": "durée moyenne de fonctionnement avant défaillance dangereuse",
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

            class RDF(Property):
                def __init__(
                    self,
                    value: Int,
                    id_short: str = "RDF",
                    value_type: DataTypeDef = Int,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/FunctionalSafety/RDF/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {"en": "ratio of dangerous failure"}

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

            class ProofTestInterval(Property):
                def __init__(
                    self,
                    value: float,
                    id_short: str = "ProofTestInterval",
                    value_type: DataTypeDef = float,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///62683#ACE058#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "proof test interval",
                            "fr": "intervalle entre essai périodique",
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
                mTTFD: Union[Int, MTTFD],
                rDF: Union[Int, RDF],
                proofTestInterval: Union[float, ProofTestInterval],
                id_short: str = "ElectronicElement",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACG066#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Electronic element",
                        "fr": "Elément électronique",
                    }

                if qualifier is None:
                    qualifier = set()

                # Build a submodel element if a raw value was passed in the argument
                if mTTFD and not isinstance(mTTFD, SubmodelElement):
                    mTTFD = self.MTTFD(mTTFD)

                # Build a submodel element if a raw value was passed in the argument
                if rDF and not isinstance(rDF, SubmodelElement):
                    rDF = self.RDF(rDF)

                # Build a submodel element if a raw value was passed in the argument
                if proofTestInterval and not isinstance(
                    proofTestInterval, SubmodelElement
                ):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [mTTFD, rDF, proofTestInterval]:
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

        class ElectromechanicalElement(SubmodelElementCollectionUnordered):
            class B10D(Property):
                def __init__(
                    self,
                    value: float,
                    id_short: str = "B10D",
                    value_type: DataTypeDef = float,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///62683#ACE056#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "number of operations until ten percent dangerous failure",
                            "fr": "nombre de cycles jusqu'à dix pour cent de défaillances dangereuses",
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

            class ProofTestInterval(Property):
                def __init__(
                    self,
                    value: float,
                    id_short: str = "ProofTestInterval",
                    value_type: DataTypeDef = float,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///62683#ACE058#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "proof test interval",
                            "fr": "intervalle entre essai périodique",
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
                b10D: Union[float, B10D],
                proofTestInterval: Union[float, ProofTestInterval],
                id_short: str = "ElectromechanicalElement",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACG067#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Electromechanical element",
                        "fr": "Elément électromécanique de sous-système",
                    }

                if qualifier is None:
                    qualifier = set()

                # Build a submodel element if a raw value was passed in the argument
                if b10D and not isinstance(b10D, SubmodelElement):
                    b10D = self.B10D(b10D)

                # Build a submodel element if a raw value was passed in the argument
                if proofTestInterval and not isinstance(
                    proofTestInterval, SubmodelElement
                ):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [b10D, proofTestInterval]:
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

        class InherentlySafeSubsystem(SubmodelElementCollectionUnordered):
            class SIL(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "SIL",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH670#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH671#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH672#001",
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
                                value="0112/2///62683#ACE051#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "safety integrity level",
                            "fr": "niveau d'intégrité de sécurité",
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

            class ProofTestInterval(Property):
                def __init__(
                    self,
                    value: float,
                    id_short: str = "ProofTestInterval",
                    value_type: DataTypeDef = float,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///62683#ACE058#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "proof test interval",
                            "fr": "intervalle entre essai périodique",
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

            class PL(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "PL",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH677#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH678#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH679#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH680#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH681#001",
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
                                value="0112/2///62683#ACE060#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "performance level",
                            "fr": "niveau de performance",
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

            class Category(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "Category",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH682#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH683#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH684#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH685#001",
                                id_type=KeyType.IRDI,
                            ),
                            Key(
                                type_=KeyElements.GLOBAL_REFERENCE,
                                local=False,
                                value="0112/2///62683#ACH686#001",
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
                                value="0112/2///62683#ACE063#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {"en": "category", "fr": "catégory"}

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
                sIL: Union[str, SIL],
                proofTestInterval: Union[float, ProofTestInterval],
                pL: Union[str, PL],
                category_se: Union[str, Category],
                id_short: str = "InherentlySafeSubsystem",
                category: str = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0112/2///62683#ACG069#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Inherently safe subsystem",
                        "fr": "Sous-système intrinsèquement sûr",
                    }

                if qualifier is None:
                    qualifier = set()

                # Build a submodel element if a raw value was passed in the argument
                if sIL and not isinstance(sIL, SubmodelElement):
                    sIL = self.SIL(sIL)

                # Build a submodel element if a raw value was passed in the argument
                if proofTestInterval and not isinstance(
                    proofTestInterval, SubmodelElement
                ):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Build a submodel element if a raw value was passed in the argument
                if pL and not isinstance(pL, SubmodelElement):
                    pL = self.PL(pL)

                # Build a submodel element if a raw value was passed in the argument
                if category_se and not isinstance(category_se, SubmodelElement):
                    category_se = self.Category(category_se)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [sIL, proofTestInterval, pL, category_se]:
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
            functionalSafetyDeviceType: Union[str, FunctionalSafetyDeviceType],
            safetySubsystem: SafetySubsystem,
            electronicElement: ElectronicElement,
            electromechanicalElement: ElectromechanicalElement,
            inherentlySafeSubsystem: InherentlySafeSubsystem,
            id_short: str = "SafetyDeviceTypes",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0112/2///62683#ACG070#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {"en": "safety device", "fr": "dispositif de sécurité"}

            if qualifier is None:
                qualifier = set()

            # Build a submodel element if a raw value was passed in the argument
            if functionalSafetyDeviceType and not isinstance(
                functionalSafetyDeviceType, SubmodelElement
            ):
                functionalSafetyDeviceType = self.FunctionalSafetyDeviceType(
                    functionalSafetyDeviceType
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                functionalSafetyDeviceType,
                safetySubsystem,
                electronicElement,
                electromechanicalElement,
                inherentlySafeSubsystem,
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

    def __init__(
        self,
        identification: Identifier,
        numberOfFunctionalSafetySetsOfCharacteristics: Union[
            Int, NumberOfFunctionalSafetySetsOfCharacteristics
        ],
        operatingConditionsOfFunctionalSafetyCharacteristics: OperatingConditionsOfFunctionalSafetyCharacteristics,
        safetyDeviceTypes: SafetyDeviceTypes,
        id_short: str = "FunctionalSafety",
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
                    value="https://admin-shell.io/idta/iec62683/1/0/FunctionalSafety",
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
        if numberOfFunctionalSafetySetsOfCharacteristics and not isinstance(
            numberOfFunctionalSafetySetsOfCharacteristics, SubmodelElement
        ):
            numberOfFunctionalSafetySetsOfCharacteristics = (
                self.NumberOfFunctionalSafetySetsOfCharacteristics(
                    numberOfFunctionalSafetySetsOfCharacteristics
                )
            )

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            numberOfFunctionalSafetySetsOfCharacteristics,
            operatingConditionsOfFunctionalSafetyCharacteristics,
            safetyDeviceTypes,
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
