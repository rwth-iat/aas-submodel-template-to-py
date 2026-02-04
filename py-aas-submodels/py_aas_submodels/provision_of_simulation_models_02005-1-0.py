from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class SimulationModels(Submodel):
    class SimulationModel(SubmodelElementCollectionUnordered):
        class Summary(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "Summary",
                value_id: Optional[Reference] = None,
                category: Optional[str] = "CONSTANT",
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/Summary/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Summary of the contents of the simulation model in text form. ",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="summary",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="summary",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_id=value_id,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class SimPurpose(SubmodelElementCollectionUnordered):
            class PosSimPurpose(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "PosSimPurpose",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/PosSimPurpose/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="posSimPurpose'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormChoices",
                                value_type=str,
                                value="Concept evaluation; Sizing; Energy consumption; Control design; Behaviour in fault condition; Validation and testing; Virtual commissioning; Condition monitoring; Predictive maintenance; Operator Training; Teaching",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="List of simulation purposes for which the model is intended.",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="OneToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="posSimPurpose",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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

            class NegSimPurpose(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "NegSimPurpose",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/NegSimPurpose/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="negSimPurpose",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="negSimPurpose'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormChoices",
                                value_type=str,
                                value="Concept evaluation; Sizing; Energy consumption; Control design; Behaviour in fault condition; Validation and testing; Virtual commissioning; Condition monitoring; Predictive maintenance; Operator Training; Teaching",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="List of simulation purposes for which the model is explicitly not suitable. ",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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
                posSimPurpose: Iterable[Union[str, PosSimPurpose]],
                negSimPurpose: Optional[Iterable[Union[str, NegSimPurpose]]] = None,
                id_short: str = "SimPurpose",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/SimPurpose/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="simPurpose",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="This characteristic describes the simulation purpose or suitability for different simulation goals.",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="simPurpose",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="One",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                # Build a list of submodel elements if a raw values were passed in the argument
                if posSimPurpose and all([isinstance(i, str) for i in posSimPurpose]):
                    posSimPurpose = [self.PosSimPurpose(i) for i in posSimPurpose]

                # Build a list of submodel elements if a raw values were passed in the argument
                if negSimPurpose and all([isinstance(i, str) for i in negSimPurpose]):
                    negSimPurpose = [self.NegSimPurpose(i) for i in negSimPurpose]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [posSimPurpose, negSimPurpose]:
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

        class TypeOfModel(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "TypeOfModel",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/TypeOfModel/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="List of modeling approaches used for the model.",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormChoices",
                            value_type=str,
                            value="Linear model; Nonlinear model; Data-driven model; Lumped element model; Fixed causality model; Acausal model ",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="typeOfModelDesc",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="typeOfModel",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

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

        class ScopeOfModel(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "ScopeOfModel",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/ScopeOfModel/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="List of basic physical characteristics which are represented by the model.",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormChoices",
                            value_type=str,
                            value="Logic and timing behaviour; Geometry; Kinematics; Dynamics; Distribution networks; Network communication; Visualization",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="scopeOfModel",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="OneToMany",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="scopeOfModel",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

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

        class LicenseModel(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "LicenseModel",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/LicenseModel/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormChoices",
                            value_type=str,
                            value="free; perpetual; subscription; volume-based",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="licenseModel",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="licenseModel",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="If a simulation model usage will be charged and how it will be charged.",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

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

        class EngineeringDomain(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "EngineeringDomain",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/EngineeringDomain/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="engineeringDomainList'{0:00}'",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="engineeringDomainList",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormChoices",
                            value_type=str,
                            value="Hydraulic Engineering; Electrical Engineering; Pneumatic Engineering; Mechanical Engineering; Material Flow; Robotics; Image Processing; Data Engineering; Process Engineering; Workflow Engineering; HMI Engineering; Control Engineering",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="List of engineering disciplines supported or mapped with the model. ",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

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

        class Environment(SubmodelElementCollectionUnordered):
            class OperatingSystem(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "OperatingSystem",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/OperatingSystem/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="operatingSystem",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="operatingSystem'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="Name of the operating system including version and architecture (e.g. Windows 10 64bit)",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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

            class ToolEnvironment(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "ToolEnvironment",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/ToolEnvironment/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="toolEnvironment",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="toolEnvironment'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="List with required simulation tools, interpreters, model libraries or runtime libraries. In each case the exact designation of the software producer is given as free text.",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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

            class DependencyEnvironment(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "DependencyEnvironment",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "CONSTANT",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/DependencyEnvironment/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="dependencyEnvironment",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="Description of dependencies to associated hardware and software. ",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="dependencyEnvironment",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class VisualizationInformation(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "VisualizationInformation",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/VisualizationInformation/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormChoices",
                                value_type=str,
                                value="separately; integrated; none",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="visualizationInformation",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="Ability to use a visualization. This can be integrated in a model or the model offers capabilities for connection. The connection can be described in more detail under ports.",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="visualizationInformation",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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

            class SimulationTool(SubmodelElementCollectionUnordered):
                class SimToolName(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "SimToolName",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = "CONSTANT",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModel/SimToolName/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="simToolName",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="simToolName",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Name of the simulation tool including version.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class DependencySimTool(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "DependencySimTool",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = "CONSTANT",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/DependencySimTool/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Dependencies of Simulation Tools",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="dependencySimTool'{0:00}'",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="dependencySimTool",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToMany",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class Compiler(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "Compiler",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = "CONSTANT",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/Compiler/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToMany",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="compiler",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Name of necessary compiler including version",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="compiler'{0:00}'",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class SolverAndTolerances(SubmodelElementCollectionUnordered):
                    class StepSizeControlNeeded(Property):
                        def __init__(
                            self,
                            value: bool,
                            id_short: str = "StepSizeControlNeeded",
                            value_type: DataTypeDef = bool,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/StepSizeControlNeeded/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="stepSizeControlNeeded",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormChoices",
                                        value_type=str,
                                        value="True; False",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="stepSizeControlNeeded",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Solver with step size control recommended.",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class FixedStepSize(Property):
                        def __init__(
                            self,
                            value: Float,
                            id_short: str = "FixedStepSize",
                            value_type: DataTypeDef = Float,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/FixedStepSize/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Fixed integration step size, if there is no adaptive step size ",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="fixedStepSize",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="fixedStepSize",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="ZeroToOne",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class StiffSolverNeeded(Property):
                        def __init__(
                            self,
                            value: bool,
                            id_short: str = "StiffSolverNeeded",
                            value_type: DataTypeDef = bool,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/StiffSolverNeeded/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="stiffSolverNeeded",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormChoices",
                                        value_type=str,
                                        value="True; False",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="stiffSolverNeeded",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Stiff solver needed.",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class SolverIncluded(Property):
                        def __init__(
                            self,
                            value: bool,
                            id_short: str = "SolverIncluded",
                            value_type: DataTypeDef = bool,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/SolverIncluded/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="solverIncluded",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Solver is integrated in the model (e.g. FMU for co-simulation)",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormChoices",
                                        value_type=str,
                                        value="True; False",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="solverIncluded",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class TestedToolSolverAlgorithm(SubmodelElementCollectionUnordered):
                        class SolverAlgorithm(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "SolverAlgorithm",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/idta/SimulationModels/SolverAlgorithm/1/0",
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
                                    qualifier = {
                                        Qualifier(
                                            type_="PresetIdShort",
                                            value_type=str,
                                            value="solverAlgorithm",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="Multiplicity",
                                            value_type=str,
                                            value="One",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="FormTitle",
                                            value_type=str,
                                            value="solverAlgorithm",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="FormInfo",
                                            value_type=str,
                                            value="validated solver",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                    }

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

                        class ToolSolverFurtherDescription(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "ToolSolverFurtherDescription",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/idta/SimulationModels/ToolSolverFurtherDescription/1/0",
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
                                    qualifier = {
                                        Qualifier(
                                            type_="FormTitle",
                                            value_type=str,
                                            value="toolSolverFurtherDescription",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="FormInfo",
                                            value_type=str,
                                            value="Further tool- and solver-specific information",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="Multiplicity",
                                            value_type=str,
                                            value="ZeroToOne",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="PresetIdShort",
                                            value_type=str,
                                            value="toolSolverFurtherDescription",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                    }

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

                        class Tolerance(Property):
                            def __init__(
                                self,
                                value: Float,
                                id_short: str = "Tolerance",
                                value_type: DataTypeDef = Float,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/idta/SimulationModels/Tolerance/1/0",
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
                                    qualifier = {
                                        Qualifier(
                                            type_="PresetIdShort",
                                            value_type=str,
                                            value="tolerance",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="FormInfo",
                                            value_type=str,
                                            value="(relative) tolerance for theadaptive step size ",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="FormTitle",
                                            value_type=str,
                                            value="tolerance",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                        Qualifier(
                                            type_="Multiplicity",
                                            value_type=str,
                                            value="ZeroToOne",
                                            value_id=None,
                                            semantic_id=None,
                                        ),
                                    }

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
                            solverAlgorithm: Union[str, SolverAlgorithm],
                            toolSolverFurtherDescription: Optional[
                                Union[str, ToolSolverFurtherDescription]
                            ] = None,
                            tolerance: Optional[Union[Float, Tolerance]] = None,
                            id_short: str = "TestedToolSolverAlgorithm",
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/TestedToolSolverAlgorithm/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="testedToolSolverAlgorithm",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="testedToolSolverAlgorithm'{0:00}'",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="List of validated tool-solver combinations",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="ZeroToMany",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

                            # Build a submodel element if a raw value was passed in the argument
                            if solverAlgorithm and not isinstance(
                                solverAlgorithm, SubmodelElement
                            ):
                                solverAlgorithm = self.SolverAlgorithm(solverAlgorithm)

                            # Build a submodel element if a raw value was passed in the argument
                            if toolSolverFurtherDescription and not isinstance(
                                toolSolverFurtherDescription, SubmodelElement
                            ):
                                toolSolverFurtherDescription = (
                                    self.ToolSolverFurtherDescription(
                                        toolSolverFurtherDescription
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if tolerance and not isinstance(tolerance, SubmodelElement):
                                tolerance = self.Tolerance(tolerance)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                solverAlgorithm,
                                toolSolverFurtherDescription,
                                tolerance,
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
                        stepSizeControlNeeded: Union[bool, StepSizeControlNeeded],
                        stiffSolverNeeded: Union[bool, StiffSolverNeeded],
                        solverIncluded: Union[bool, SolverIncluded],
                        fixedStepSize: Optional[Union[Float, FixedStepSize]] = None,
                        testedToolSolverAlgorithm: Optional[
                            Iterable[TestedToolSolverAlgorithm]
                        ] = None,
                        id_short: str = "SolverAndTolerances",
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/SolverAndTolerances/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="solverAndTolerances",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Useful settings of the simulation environment. Includes e.g. solver settings. ",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="solverAndTolerances",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        # Build a submodel element if a raw value was passed in the argument
                        if stepSizeControlNeeded and not isinstance(
                            stepSizeControlNeeded, SubmodelElement
                        ):
                            stepSizeControlNeeded = self.StepSizeControlNeeded(
                                stepSizeControlNeeded
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if fixedStepSize and not isinstance(
                            fixedStepSize, SubmodelElement
                        ):
                            fixedStepSize = self.FixedStepSize(fixedStepSize)

                        # Build a submodel element if a raw value was passed in the argument
                        if stiffSolverNeeded and not isinstance(
                            stiffSolverNeeded, SubmodelElement
                        ):
                            stiffSolverNeeded = self.StiffSolverNeeded(
                                stiffSolverNeeded
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if solverIncluded and not isinstance(
                            solverIncluded, SubmodelElement
                        ):
                            solverIncluded = self.SolverIncluded(solverIncluded)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            stepSizeControlNeeded,
                            fixedStepSize,
                            stiffSolverNeeded,
                            solverIncluded,
                            testedToolSolverAlgorithm,
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
                    simToolName: Union[str, SimToolName],
                    solverAndTolerances: SolverAndTolerances,
                    dependencySimTool: Optional[
                        Iterable[Union[str, DependencySimTool]]
                    ] = None,
                    compiler: Optional[Iterable[Union[str, Compiler]]] = None,
                    id_short: str = "SimulationTool",
                    category: Optional[str] = "CONSTANT",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/SimulationTool/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="simulationTool",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="OneToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="simulationTool'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="Eigenschaften des Modells bezüglich konkreter Simulationswerkzeuge.",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if simToolName and not isinstance(simToolName, SubmodelElement):
                        simToolName = self.SimToolName(simToolName)

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if dependencySimTool and all(
                        [isinstance(i, str) for i in dependencySimTool]
                    ):
                        dependencySimTool = [
                            self.DependencySimTool(i) for i in dependencySimTool
                        ]

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if compiler and all([isinstance(i, str) for i in compiler]):
                        compiler = [self.Compiler(i) for i in compiler]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        simToolName,
                        dependencySimTool,
                        compiler,
                        solverAndTolerances,
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
                operatingSystem: Union[str, OperatingSystem],
                simulationTool: Iterable[SimulationTool],
                toolEnvironment: Optional[Iterable[Union[str, ToolEnvironment]]] = None,
                dependencyEnvironment: Optional[
                    Union[LangStringSet, DependencyEnvironment]
                ] = None,
                visualizationInformation: Optional[
                    Union[str, VisualizationInformation]
                ] = None,
                id_short: str = "Environment",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/Environment/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Information about prerequisite environments or dependencies of underlying components on the target system.",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="environment",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="environment",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                # Build a submodel element if a raw value was passed in the argument
                if operatingSystem and not isinstance(operatingSystem, SubmodelElement):
                    operatingSystem = self.OperatingSystem(operatingSystem)

                # Build a list of submodel elements if a raw values were passed in the argument
                if toolEnvironment and all(
                    [isinstance(i, str) for i in toolEnvironment]
                ):
                    toolEnvironment = [self.ToolEnvironment(i) for i in toolEnvironment]

                # Build a submodel element if a raw value was passed in the argument
                if dependencyEnvironment and not isinstance(
                    dependencyEnvironment, SubmodelElement
                ):
                    dependencyEnvironment = self.DependencyEnvironment(
                        dependencyEnvironment
                    )

                # Build a submodel element if a raw value was passed in the argument
                if visualizationInformation and not isinstance(
                    visualizationInformation, SubmodelElement
                ):
                    visualizationInformation = self.VisualizationInformation(
                        visualizationInformation
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    operatingSystem,
                    toolEnvironment,
                    dependencyEnvironment,
                    visualizationInformation,
                    simulationTool,
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

        class RefSimDocumentation(File):
            def __init__(
                self,
                value: str,
                mime_type: str,
                id_short: str = "RefSimDocumentation",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/RefSimDocumentation/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="refSimDocumentation",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="refSimDocumentation'{0:00}'",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Documentation of example simulations of the model can be supplied. This includes a solver setup and sample circuit and sample results. e.g. zip file, PDF, html, ...",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                super().__init__(
                    value=value,
                    mime_type=mime_type,
                    id_short=id_short,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class ModelFile(SubmodelElementCollectionUnordered):
            class ModelFileType(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "ModelFileType",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/ModelFileType/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value='"Designation of the exchange format of the model. E.G.: FMI 1.0, Co-Simulation, Platform / Source - Code. FMI 2.0.2, Model Exchange, Source - Code. S-function, Version 2, 64bit, mex - Format / or C-Code. Modelica 3, encoded. VHDL',
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="modelFileType",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="modelFileType",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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

            class ModelFileVersion(SubmodelElementCollectionUnordered):
                class ModelVersionId(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "ModelVersionId",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/ModelVersionId/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Version number of the model from the vendor.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="modelVersionId",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="modelVersionId",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class ModelPreviewImage(File):
                    def __init__(
                        self,
                        value: str,
                        mime_type: str,
                        id_short: str = "ModelPreviewImage",
                        category: Optional[str] = "CONSTANT",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/ModelPreviewImage/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Image file to represent the model in user interfaces, e.g. in a search.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="modelPreviewImage",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="modelPreviewImage",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            mime_type=mime_type,
                            id_short=id_short,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                class DigitalFile(File):
                    def __init__(
                        self,
                        value: str,
                        mime_type: str,
                        id_short: str = "DigitalFile",
                        category: Optional[str] = "CONSTANT",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/DigitalFile/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Deployment of the model file.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="digitalFile",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="digitalFile",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            mime_type=mime_type,
                            id_short=id_short,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                class ModelFileReleaseNotesTxt(MultiLanguageProperty):
                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: str = "ModelFileReleaseNotesTxt",
                        value_id: Optional[Reference] = Reference(key=()),
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/ModelFileReleaseNotesTxt/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="contains information about this release",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="modelFileReleaseNotesTxt",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="modelFileReleaseNotesTxt",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                class ModelFileReleaseNotesFile(File):
                    def __init__(
                        self,
                        value: str,
                        mime_type: str,
                        id_short: str = "ModelFileReleaseNotesFile",
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/ModelFileReleaseNotesFile/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="release notes link or file",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="modelFileReleaseNotesFile",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="modelFileReleaseNotesFile",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            mime_type=mime_type,
                            id_short=id_short,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                def __init__(
                    self,
                    modelVersionId: Union[str, ModelVersionId],
                    digitalFile: DigitalFile,
                    modelPreviewImage: Optional[ModelPreviewImage] = None,
                    modelFileReleaseNotesTxt: Optional[
                        Union[LangStringSet, ModelFileReleaseNotesTxt]
                    ] = None,
                    modelFileReleaseNotesFile: Optional[
                        ModelFileReleaseNotesFile
                    ] = None,
                    id_short: str = "ModelFileVersion",
                    category: Optional[str] = "CONSTANT",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/ModelFileVersion/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="OneToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="Provision of a version of the simulation model with information to distinguish the versions. The versions are primarily intended for bug fixes without content changes.",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="modelFileVersion'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="modelFileVersion",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if modelVersionId and not isinstance(
                        modelVersionId, SubmodelElement
                    ):
                        modelVersionId = self.ModelVersionId(modelVersionId)

                    # Build a submodel element if a raw value was passed in the argument
                    if modelFileReleaseNotesTxt and not isinstance(
                        modelFileReleaseNotesTxt, SubmodelElement
                    ):
                        modelFileReleaseNotesTxt = self.ModelFileReleaseNotesTxt(
                            modelFileReleaseNotesTxt
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        modelVersionId,
                        modelPreviewImage,
                        digitalFile,
                        modelFileReleaseNotesTxt,
                        modelFileReleaseNotesFile,
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
                modelFileVersion: Iterable[ModelFileVersion],
                modelFileType: Optional[Union[str, ModelFileType]] = None,
                id_short: str = "ModelFile",
                category: Optional[str] = "CONSTANT",
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/ModelFile/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="modelFile",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="One",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Providing versions of the simulation model and with characteristics to distinguish them.",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="modelFile",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                # Build a submodel element if a raw value was passed in the argument
                if modelFileType and not isinstance(modelFileType, SubmodelElement):
                    modelFileType = self.ModelFileType(modelFileType)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [modelFileType, modelFileVersion]:
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

        class ParamMethod(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "ParamMethod",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/ParamMethod/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="paramMethod",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="One",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Indicates whether the model must be parameterized and if so, which method is required.",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormChoices",
                            value_type=str,
                            value='by using "technical data" of asset; by using "technical data" and user; by user interface; by setting file; not necessary; by documentation file; pre-parametrized',
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="paramMethod",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

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

        class ParamFile(File):
            def __init__(
                self,
                value: str,
                mime_type: str,
                id_short: str = "ParamFile",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/ParamFile/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="paramFile",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="paramFile",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="File for parameterization of the model. As parameter file or parameter documentation (e.g. pdf). ",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                super().__init__(
                    value=value,
                    mime_type=mime_type,
                    id_short=id_short,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class InitStateMethod(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "InitStateMethod",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/InitStateMethod/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="initStateMethod",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value='" Describes the state variables of the simulation model that must be initialized to start the simulation. For initial value problems, these quantities describe the system state at the start of the simulation. In this case, the system is in a state of equilibrium. Alternatively, a simulation model may include a method to determine consistent initial values at this step, e.g., at an operating point. ',
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormChoices",
                            value_type=str,
                            value="not necessary, by user interface; by setting file; set states within simulation environment; integrated in model; by documentation file",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="initStateMethod",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="One",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

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

        class InitStateFile(File):
            def __init__(
                self,
                value: str,
                mime_type: str,
                id_short: str = "InitStateFile",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/InitStateFile/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="initStateFile",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="File for parameterizing the initial states of the model. As parameter file or parameter documentation (e.g. pdf). ",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="initStateFile",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                super().__init__(
                    value=value,
                    mime_type=mime_type,
                    id_short=id_short,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class DefaultSimTime(Property):
            def __init__(
                self,
                value: Float,
                id_short: str = "DefaultSimTime",
                value_type: DataTypeDef = Float,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/DefaultSimTime/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="defaultSimTime",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Predefined simulation period in seconds ",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="defaultSimTime",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

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

        class SimModManufacturerInformation(SubmodelElementCollectionUnordered):
            class Company(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "Company",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAW001#001",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="company",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="company",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="name of the company",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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

            class Language(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "Language",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO895#003",
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
                        qualifier = {
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="language'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="available language",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="language",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="OneToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

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

            class Email(SubmodelElementCollectionUnordered):
                class TypeOfEmailAddress(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "TypeOfEmailAddress",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO199#003",
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
                            qualifier = {
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="typeOfEmailAddress",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="characterization of an e-mail address according to its location or usage",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="typeOfEmailAddress",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class EmailAddress(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "EmailAddress",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO198#002",
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
                            qualifier = {
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="emailAddress",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="emailAddress",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="electronic mail address of a business partner",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class TypeOfPublicKey(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "TypeOfPublicKey",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO201#002",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="typeOfPublicKey",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="typeOfPublicKey",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="characterization of a public key according to its encryption process",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class PublicKey(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "PublicKey",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO200#002",
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
                            qualifier = {
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="publicKey",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="public part of an unsymmetrical key pair to sign or encrypt text or messages",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="publicKey",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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
                    emailAddress: Union[str, EmailAddress],
                    typeOfEmailAddress: Optional[Union[str, TypeOfEmailAddress]] = None,
                    typeOfPublicKey: Optional[Union[str, TypeOfPublicKey]] = None,
                    publicKey: Optional[Union[str, PublicKey]] = None,
                    id_short: str = "Email",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAQ836#005",
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
                        qualifier = {
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="E-mail address and encryption method",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="email",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="email",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if typeOfEmailAddress and not isinstance(
                        typeOfEmailAddress, SubmodelElement
                    ):
                        typeOfEmailAddress = self.TypeOfEmailAddress(typeOfEmailAddress)

                    # Build a submodel element if a raw value was passed in the argument
                    if emailAddress and not isinstance(emailAddress, SubmodelElement):
                        emailAddress = self.EmailAddress(emailAddress)

                    # Build a submodel element if a raw value was passed in the argument
                    if typeOfPublicKey and not isinstance(
                        typeOfPublicKey, SubmodelElement
                    ):
                        typeOfPublicKey = self.TypeOfPublicKey(typeOfPublicKey)

                    # Build a submodel element if a raw value was passed in the argument
                    if publicKey and not isinstance(publicKey, SubmodelElement):
                        publicKey = self.PublicKey(publicKey)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        typeOfEmailAddress,
                        emailAddress,
                        typeOfPublicKey,
                        publicKey,
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

            class Phone(SubmodelElementCollectionUnordered):
                class TypeOfTelephone(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "TypeOfTelephone",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO137#003",
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
                            qualifier = {
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="typeOfTelephone",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="typeOfTelephone",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="characterization of a telephone according to its location or usage",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class TelephoneNumber(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "TelephoneNumber",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO136#002",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="telephoneNumber",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="telephoneNumber",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="complete telephone number to be called to reach a business partner",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class AvailableTime(MultiLanguageProperty):
                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: str = "AvailableTime",
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Specification of the available time window",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="availableTime",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="availableTime",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                def __init__(
                    self,
                    telephoneNumber: Union[str, TelephoneNumber],
                    typeOfTelephone: Optional[Union[str, TypeOfTelephone]] = None,
                    availableTime: Optional[Union[LangStringSet, AvailableTime]] = None,
                    id_short: str = "Phone",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Phone",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="phone",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="Phone number including type",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="phone",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if typeOfTelephone and not isinstance(
                        typeOfTelephone, SubmodelElement
                    ):
                        typeOfTelephone = self.TypeOfTelephone(typeOfTelephone)

                    # Build a submodel element if a raw value was passed in the argument
                    if telephoneNumber and not isinstance(
                        telephoneNumber, SubmodelElement
                    ):
                        telephoneNumber = self.TelephoneNumber(telephoneNumber)

                    # Build a submodel element if a raw value was passed in the argument
                    if availableTime and not isinstance(availableTime, SubmodelElement):
                        availableTime = self.AvailableTime(availableTime)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [typeOfTelephone, telephoneNumber, availableTime]:
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
                company: Union[str, Company],
                language: Iterable[Union[str, Language]],
                email: Optional[Email] = None,
                phone: Optional[Phone] = None,
                id_short: str = "SimModManufacturerInformation",
                category: Optional[str] = "CONSTANT",
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/SimModManufacturerInformation/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="simModManufacturerInformation",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Provide access to  simulation support service provided by the distributor via mail or phone",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="simModManufacturerInformation'{0:00}'",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                # Build a submodel element if a raw value was passed in the argument
                if company and not isinstance(company, SubmodelElement):
                    company = self.Company(company)

                # Build a list of submodel elements if a raw values were passed in the argument
                if language and all([isinstance(i, str) for i in language]):
                    language = [self.Language(i) for i in language]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [company, language, email, phone]:
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

        class Ports(SubmodelElementCollectionUnordered):
            class PortsConnector(SubmodelElementCollectionUnordered):
                class PortConnectorName(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "PortConnectorName",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/PortsConnectorName/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="portConnectorName",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="portConnectorName",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Name of the Connector Port.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class PortConDescription(MultiLanguageProperty):
                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: str = "PortConDescription",
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModel/portConDescription/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="portConDescription",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="portConDescription",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Description of the Connector Port.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                class Variable(SubmodelElementCollectionUnordered):
                    class VariableName(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "VariableName",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/VariableName/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="variableName",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="variableName",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Name of the variable.",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class Range(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "Range",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/Range/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="range",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="ZeroToOne",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Range of values for the variable (e.g. [min, max], [min, max[, ]min, max], ]min, max[, {val1, val2, ...}).",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="range",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class VariableType(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "VariableType",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/VariableType/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="variableType",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="variableType",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Type of the variable (e.g. Real, Integer, Boolean, String or Enum).",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormChoices",
                                        value_type=str,
                                        value="Real; Integer; Boolean; String; ENUM",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class VariableDescription(MultiLanguageProperty):
                        def __init__(
                            self,
                            value: LangStringSet,
                            id_short: str = "VariableDescription",
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/VariableDescription/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="variableDescription",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="variableDescription",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="ZeroToOne",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Description of the variable.",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_id=value_id,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                kind=kind,
                            )

                    class UnitList(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "UnitList",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/UnitList/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value='The most common units can be selected here. .. If "others" is selected, a free text can be entered.',
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="unitList",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormChoices",
                                        value_type=str,
                                        value="s; m; kg; N; m/s; m/s^2; V; A; K; none",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="unitList",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class UnitDescription(MultiLanguageProperty):
                        def __init__(
                            self,
                            value: LangStringSet,
                            id_short: str = "UnitDescription",
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/UnitDescription/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="unitDescription",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="ZeroToOne",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="unitDescription",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="Text field for missing units of the list.",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_id=value_id,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                kind=kind,
                            )

                    class VariableCausality(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "VariableCausality",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/VariableCausality/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormChoices",
                                        value_type=str,
                                        value="input; output; acausal",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value="The causality of the variable: input to inputs, output to ouputs, acausal connections (e.g. mechanical connection) do not have causality.",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="variableCausality",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="variableCausality",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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

                    class VariablePrefix(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "VariablePrefix",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/SimulationModels/VariablePrefix/1/0",
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
                                qualifier = {
                                    Qualifier(
                                        type_="FormChoices",
                                        value_type=str,
                                        value="Flow; Stream",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="ZeroToOne",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="PresetIdShort",
                                        value_type=str,
                                        value="variablePrefix",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormTitle",
                                        value_type=str,
                                        value="variablePrefix",
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                    Qualifier(
                                        type_="FormInfo",
                                        value_type=str,
                                        value='Prefix for acausal variable. Potential variables are set equal when connecting (no prefix). Stream variables are connected according to Kirchhoff\'s law, i.e. the sum of the variables equals zero. The bi-directional flow of matter is described with "stream" (e.g. for enthalpy).',
                                        value_id=None,
                                        semantic_id=None,
                                    ),
                                }

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
                        variableName: Union[str, VariableName],
                        variableType: Union[str, VariableType],
                        unitList: Union[str, UnitList],
                        variableCausality: Union[str, VariableCausality],
                        range: Optional[Union[str, Range]] = None,
                        variableDescription: Optional[
                            Union[LangStringSet, VariableDescription]
                        ] = None,
                        unitDescription: Optional[
                            Union[LangStringSet, UnitDescription]
                        ] = None,
                        variablePrefix: Optional[Union[str, VariablePrefix]] = None,
                        id_short: str = "Variable",
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/Variable/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="List of variables of the port.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToMany",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="variable{0:00}",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="variable",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        # Build a submodel element if a raw value was passed in the argument
                        if variableName and not isinstance(
                            variableName, SubmodelElement
                        ):
                            variableName = self.VariableName(variableName)

                        # Build a submodel element if a raw value was passed in the argument
                        if range and not isinstance(range, SubmodelElement):
                            range = self.Range(range)

                        # Build a submodel element if a raw value was passed in the argument
                        if variableType and not isinstance(
                            variableType, SubmodelElement
                        ):
                            variableType = self.VariableType(variableType)

                        # Build a submodel element if a raw value was passed in the argument
                        if variableDescription and not isinstance(
                            variableDescription, SubmodelElement
                        ):
                            variableDescription = self.VariableDescription(
                                variableDescription
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if unitList and not isinstance(unitList, SubmodelElement):
                            unitList = self.UnitList(unitList)

                        # Build a submodel element if a raw value was passed in the argument
                        if unitDescription and not isinstance(
                            unitDescription, SubmodelElement
                        ):
                            unitDescription = self.UnitDescription(unitDescription)

                        # Build a submodel element if a raw value was passed in the argument
                        if variableCausality and not isinstance(
                            variableCausality, SubmodelElement
                        ):
                            variableCausality = self.VariableCausality(
                                variableCausality
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if variablePrefix and not isinstance(
                            variablePrefix, SubmodelElement
                        ):
                            variablePrefix = self.VariablePrefix(variablePrefix)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            variableName,
                            range,
                            variableType,
                            variableDescription,
                            unitList,
                            unitDescription,
                            variableCausality,
                            variablePrefix,
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
                    portConnectorName: Union[str, PortConnectorName],
                    portConDescription: Optional[
                        Union[LangStringSet, PortConDescription]
                    ] = None,
                    variable: Optional[Iterable[Variable]] = None,
                    id_short: str = "PortsConnector",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/PortsConnector/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value="List of ports of the model. These include a name, a description, a list of variables, and a list of ports.",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="portsConnector",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="portsConnector'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if portConnectorName and not isinstance(
                        portConnectorName, SubmodelElement
                    ):
                        portConnectorName = self.PortConnectorName(portConnectorName)

                    # Build a submodel element if a raw value was passed in the argument
                    if portConDescription and not isinstance(
                        portConDescription, SubmodelElement
                    ):
                        portConDescription = self.PortConDescription(portConDescription)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [portConnectorName, portConDescription, variable]:
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

            class BinaryConnector(SubmodelElementCollectionUnordered):
                class BinaryConName(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "BinaryConName",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/BinaryConnectorName/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="binConName",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Binary interface name.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="binaryConName",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

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

                class BinaryConDescription(MultiLanguageProperty):
                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: str = "BinaryConDescription",
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/SimulationModels/BinaryConDescription/1/0",
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
                            qualifier = {
                                Qualifier(
                                    type_="FormTitle",
                                    value_type=str,
                                    value="binaryConDescription",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="binaryConDescription",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToOne",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="FormInfo",
                                    value_type=str,
                                    value="Binary interface description.",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                def __init__(
                    self,
                    binaryConName: Union[str, BinaryConName],
                    binaryConDescription: Optional[
                        Union[LangStringSet, BinaryConDescription]
                    ] = None,
                    id_short: str = "BinaryConnector",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/SimulationModels/BinaryConnector/1/0",
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
                        qualifier = {
                            Qualifier(
                                type_="FormTitle",
                                value_type=str,
                                value="binaryConnector",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="FormInfo",
                                value_type=str,
                                value='Binary interfaces (binaryType) based on the FMI 3.0 standard (https://fmi-standard.org/docs/3.0-dev/#definition-of-types). At this point the name (e.g. "Binary interface visualization") and the description (e.g. "Interface for binary transfer of visualization information") are specified.',
                                value_id=None,
                                semantic_id=None,
                            ),
                            Qualifier(
                                type_="PresetIdShort",
                                value_type=str,
                                value="binaryConnector'{0:00}'",
                                value_id=None,
                                semantic_id=None,
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if binaryConName and not isinstance(binaryConName, SubmodelElement):
                        binaryConName = self.BinaryConName(binaryConName)

                    # Build a submodel element if a raw value was passed in the argument
                    if binaryConDescription and not isinstance(
                        binaryConDescription, SubmodelElement
                    ):
                        binaryConDescription = self.BinaryConDescription(
                            binaryConDescription
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [binaryConName, binaryConDescription]:
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
                portsConnector: Optional[Iterable[PortsConnector]] = None,
                binaryConnector: Optional[Iterable[BinaryConnector]] = None,
                id_short: str = "Ports",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/SimulationModels/Ports/1/0",
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
                    qualifier = {
                        Qualifier(
                            type_="FormInfo",
                            value_type=str,
                            value="Interfaces of the model. This includes inputs, outputs as well as acausal connections (e.g. mechanical connections). In addition, it is specified here whether the model provides binary interfaces (e.g. for visualization).",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="ports",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="FormTitle",
                            value_type=str,
                            value="ports",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [portsConnector, binaryConnector]:
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
            simPurpose: SimPurpose,
            scopeOfModel: Iterable[Union[str, ScopeOfModel]],
            modelFile: ModelFile,
            paramMethod: Union[str, ParamMethod],
            initStateMethod: Union[str, InitStateMethod],
            summary: Optional[Union[LangStringSet, Summary]] = None,
            typeOfModel: Optional[Iterable[Union[str, TypeOfModel]]] = None,
            licenseModel: Optional[Union[str, LicenseModel]] = None,
            engineeringDomain: Optional[Iterable[Union[str, EngineeringDomain]]] = None,
            environment: Optional[Iterable[Environment]] = None,
            refSimDocumentation: Optional[Iterable[RefSimDocumentation]] = None,
            paramFile: Optional[ParamFile] = None,
            initStateFile: Optional[InitStateFile] = None,
            defaultSimTime: Optional[Union[Float, DefaultSimTime]] = None,
            simModManufacturerInformation: Optional[
                Iterable[SimModManufacturerInformation]
            ] = None,
            ports: Optional[Ports] = None,
            id_short: str = "SimulationModel",
            category: Optional[str] = "CONSTANT",
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="https://admin-shell.io/idta/SimulationModels/SimulationModel/1/0",
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
                qualifier = {
                    Qualifier(
                        type_="FormInfo",
                        value_type=str,
                        value="Merkmalssammlung zur Bereitstellung oder Anfrage von Simulationsmodellen. Die Modelle können von der Zielstellung und inhaltlich beschrieben werden.",
                        value_id=None,
                        semantic_id=None,
                    ),
                    Qualifier(
                        type_="Multiplicity",
                        value_type=str,
                        value="ZeroToMany",
                        value_id=None,
                        semantic_id=None,
                    ),
                    Qualifier(
                        type_="FormTitle",
                        value_type=str,
                        value="SimulationModel",
                        value_id=None,
                        semantic_id=None,
                    ),
                    Qualifier(
                        type_="PresetIdShort",
                        value_type=str,
                        value="To be filleSimulationModel'{0:00}'",
                        value_id=None,
                        semantic_id=None,
                    ),
                }

            # Build a submodel element if a raw value was passed in the argument
            if summary and not isinstance(summary, SubmodelElement):
                summary = self.Summary(summary)

            # Build a list of submodel elements if a raw values were passed in the argument
            if typeOfModel and all([isinstance(i, str) for i in typeOfModel]):
                typeOfModel = [self.TypeOfModel(i) for i in typeOfModel]

            # Build a list of submodel elements if a raw values were passed in the argument
            if scopeOfModel and all([isinstance(i, str) for i in scopeOfModel]):
                scopeOfModel = [self.ScopeOfModel(i) for i in scopeOfModel]

            # Build a submodel element if a raw value was passed in the argument
            if licenseModel and not isinstance(licenseModel, SubmodelElement):
                licenseModel = self.LicenseModel(licenseModel)

            # Build a list of submodel elements if a raw values were passed in the argument
            if engineeringDomain and all(
                [isinstance(i, str) for i in engineeringDomain]
            ):
                engineeringDomain = [
                    self.EngineeringDomain(i) for i in engineeringDomain
                ]

            # Build a submodel element if a raw value was passed in the argument
            if paramMethod and not isinstance(paramMethod, SubmodelElement):
                paramMethod = self.ParamMethod(paramMethod)

            # Build a submodel element if a raw value was passed in the argument
            if initStateMethod and not isinstance(initStateMethod, SubmodelElement):
                initStateMethod = self.InitStateMethod(initStateMethod)

            # Build a submodel element if a raw value was passed in the argument
            if defaultSimTime and not isinstance(defaultSimTime, SubmodelElement):
                defaultSimTime = self.DefaultSimTime(defaultSimTime)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                summary,
                simPurpose,
                typeOfModel,
                scopeOfModel,
                licenseModel,
                engineeringDomain,
                environment,
                refSimDocumentation,
                modelFile,
                paramMethod,
                paramFile,
                initStateMethod,
                initStateFile,
                defaultSimTime,
                simModManufacturerInformation,
                ports,
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
        simulationModel: Optional[Iterable[SimulationModel]] = None,
        id_short: str = "SimulationModels",
        category: Optional[str] = "CONSTANT",
        description: Optional[LangStringSet] = None,
        administration: Optional[AdministrativeInformation] = None,
        semantic_id: Optional[Reference] = Reference(
            key=(
                Key(
                    type_=KeyElements.SUBMODEL,
                    local=True,
                    value="https://admin-shell.io/idta/SimulationModels/SimulationModels/1/0",
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
            qualifier = {
                Qualifier(
                    type_="FormTitle",
                    value_type=str,
                    value="Simulation Submodel v008",
                    value_id=None,
                    semantic_id=None,
                ),
                Qualifier(
                    type_="FormInfo",
                    value_type=str,
                    value="Das Submodel kann ein oder meherer Simulationsmodelle bereitstellen, einen Service zur Generierung eines spezifischen Modells oder einen Zugang zu einer offenen oder spezifischen Anfrage.",
                    value_id=None,
                    semantic_id=None,
                ),
            }

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [simulationModel]:
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
