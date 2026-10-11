from typing import Any, ForwardRef, Iterable, Optional, Tuple, TypedDict, Union, Unpack
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


def global_ref(value: str) -> aas.ExternalReference:
    """External reference to the global identifier `value`, e.g. a semantic ID"""
    return aas.ExternalReference((aas.Key(aas.KeyTypes.GLOBAL_REFERENCE, value),))


def collect_submodel_elements(*elements: Any, number_repeated: bool = True) -> list[aas.SubmodelElement]:
    """Collect the submodel elements passed to an init in one list: single elements, unless None,
    and the elements of iterables, whose idShorts get an index if `number_repeated` (e.g. Keyword00)"""
    collected = []
    for element in elements:
        if element is None:
            continue
        elif isinstance(element, aas.SubmodelElement):
            collected.append(element)
        elif isinstance(element, Iterable):
            for n, item in enumerate(element):
                if number_repeated:
                    # Number with two digits at least, as the placeholders {00} and __00__ of templates
                    item.id_short = f"{item.id_short}{n:02d}"
                collected.append(item)
        else:
            raise TypeError(f"Expected a submodel element or an iterable of them, got {element.__class__}")
    return collected


class GeneratedSubmodelElementList(aas.SubmodelElementList):
    """SubmodelElementList, whose items may be instances of subclasses of type_value_list_element,
    such as the generated classes of its items"""

    def _check_constraints(self, new, existing) -> None:
        # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
        # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
        saved_id_short = new.id_short
        new.id_short = None

        # We relax constraint AASd-108 here: It is allowed to add subclasses of the specified in type_value_list_element
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
                if item.semantic_id is not None and new.semantic_id != item.semantic_id:
                    raise aas.AASConstraintViolation(
                        114,
                        f"Element to be added {new!r} has semantic_id "
                        f"{new.semantic_id!r}, while already contained element "
                        f"{item!r} has semantic_id {item.semantic_id!r}, which "
                        "aren't equal.",
                    )

        # Re-assign id_short
        new.id_short = saved_id_short


class FileMetadata(TypedDict, total=False):
    """Metadata of aas.File, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class MultiLanguagePropertyMetadata(TypedDict, total=False):
    """Metadata of aas.MultiLanguageProperty, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_id: Optional[aas.Reference]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class PropertyMetadata(TypedDict, total=False):
    """Metadata of aas.Property, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_type: aas.DataTypeDefXsd
    value_id: Optional[aas.Reference]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelElementCollectionMetadata(TypedDict, total=False):
    """Metadata of aas.SubmodelElementCollection, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelMetadata(TypedDict, total=False):
    """Metadata of aas.Submodel, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    administration: Optional[aas.AdministrativeInformation]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    kind: aas.ModellingKind
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SimulationModels(aas.Submodel):

    class SimulationModel(aas.SubmodelElementCollection):

        class Summary(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"Summary",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Summary"}),
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Specifies Summary."}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Summary/1/0"),
                }

            def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SimPurpose(aas.SubmodelElementCollection):

            class PosSimPurpose(aas.Property):

                ALLOWED_VALUES = (
                    r"Concept evaluation",
                    r"Sizing",
                    r"Energy consumption",
                    r"Control design",
                    r"Behaviour in fault condition",
                    r"Validation and testing",
                    r"Virtual commissioning",
                    r"Condition monitoring",
                    r"Predictive maintenance",
                    r"Operator Training",
                    r"Teaching",
                )

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PosSimPurpose",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Pos Sim Purpose"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"List of simulation purposes for which the model is intended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/PosSimPurpose/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NegSimPurpose(aas.Property):

                ALLOWED_VALUES = (
                    r"Concept evaluation",
                    r"Sizing",
                    r"Energy consumption",
                    r"Control design",
                    r"Behaviour in fault condition",
                    r"Validation and testing",
                    r"Virtual commissioning",
                    r"Condition monitoring",
                    r"Predictive maintenance",
                    r"Operator Training",
                    r"Teaching",
                )

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NegSimPurpose",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Neg Sim Purpose"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List of simulation purposes for which the model is explicitly not suitable."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/NegSimPurpose/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"SimPurpose",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sim Purpose"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"This characteristic describes the simulation purpose or suitability for different simulation goals."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/SimPurpose/1/0"),
                }

            def __init__(
                self,
                posSimPurpose: Iterable[Union[str, PosSimPurpose]],
                negSimPurpose: Optional[Iterable[Union[str, NegSimPurpose]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(posSimPurpose, str):
                    raise TypeError("posSimPurpose takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if posSimPurpose:
                    posSimPurpose = [
                        i if isinstance(i, aas.SubmodelElement) else self.PosSimPurpose(i) for i in posSimPurpose
                    ]

                # A str would be split into its characters
                if isinstance(negSimPurpose, str):
                    raise TypeError("negSimPurpose takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if negSimPurpose:
                    negSimPurpose = [
                        i if isinstance(i, aas.SubmodelElement) else self.NegSimPurpose(i) for i in negSimPurpose
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(posSimPurpose, negSimPurpose)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class TypeOfModel(aas.Property):

            ALLOWED_VALUES = (
                r"Linear model",
                r"Nonlinear model",
                r"Data-driven model",
                r"Lumped element model",
                r"Fixed causality model",
                r"Acausal model",
            )

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TypeOfModel",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Type Of Model"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"List of modeling approaches used for the model."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/TypeOfModel/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ScopeOfModel(aas.Property):

            ALLOWED_VALUES = (
                r"Logic and timing behaviour",
                r"Geometry",
                r"Kinematics",
                r"Dynamics",
                r"Distribution networks",
                r"Network communication",
                r"Visualization",
            )

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ScopeOfModel",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Scope Of Model"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"List of basic physical characteristics which are represented by the model."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/ScopeOfModel/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LicenseModel(aas.Property):

            ALLOWED_VALUES = (r"free", r"perpetual", r"subscription", r"volume-based")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LicenseModel",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"License Model"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"If a simulation model usage will be charged and how it will be charged."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/LicenseModel/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EngineeringDomain(aas.Property):

            ALLOWED_VALUES = (
                r"Hydraulic Engineering",
                r"Electrical Engineering",
                r"Pneumatic Engineering",
                r"Mechanical Engineering",
                r"Material Flow",
                r"Robotics",
                r"Image Processing",
                r"Data Engineering",
                r"Process Engineering",
                r"Workflow Engineering",
                r"HMI Engineering",
                r"Control Engineering",
            )

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EngineeringDomain",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Engineering Domain"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"List of engineering disciplines supported or mapped with the model."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/EngineeringDomain/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Environment(aas.SubmodelElementCollection):

            class OperatingSystem(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OperatingSystem",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Operating System"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Name of the operating system including version and architecture (e.g. Windows 10 64bit)"
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/OperatingSystem/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ToolEnvironment(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ToolEnvironment",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Tool Environment"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List with required simulation tools, interpreters, model libraries or runtime libraries. In each case the exact designation of the software producer is given as free text."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/ToolEnvironment/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DependencyEnvironment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"DependencyEnvironment",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependency Environment"}),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Description of dependencies to associated hardware and software."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/SimulationModels/DependencyEnvironment/1/0"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class VisualizationInformation(aas.Property):

                ALLOWED_VALUES = (r"separately", r"integrated", r"none")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"VisualizationInformation",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Visualization Information"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Ability to use a visualization. This can be integrated in a model or the model offers capabilities for connection. The connection can be described in more detail under Ports."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/SimulationModels/VisualizationInformation/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SimulationTool(aas.SubmodelElementCollection):

                class SimToolName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SimToolName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sim Tool Name"}),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Specifies Sim Tool Name."}),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/SimToolName/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DependencySimTool(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DependencySimTool",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Dependency Sim Tool"}),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Dependencies of Simulation Tools"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/DependencySimTool/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Compiler(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Compiler",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Compiler"}),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Name of necessary compiler including version"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Compiler/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SolverAndTolerances(aas.SubmodelElementCollection):

                    class StepSizeControlNeeded(aas.Property):

                        ALLOWED_VALUES = (True, False)

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StepSizeControlNeeded",
                                "value_type": bool,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Step Size Control Needed"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Solver with step size control recommended."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/StepSizeControlNeeded/1/0"
                                ),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class FixedStepSize(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"FixedStepSize",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fixed Step Size"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Fixed integration step size, if there is no adaptive step size"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/FixedStepSize/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class StiffSolverNeeded(aas.Property):

                        ALLOWED_VALUES = (True, False)

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StiffSolverNeeded",
                                "value_type": bool,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Stiff Solver Needed"}),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Stiff solver needed."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/StiffSolverNeeded/1/0"
                                ),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SolverIncluded(aas.Property):

                        ALLOWED_VALUES = (True, False)

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SolverIncluded",
                                "value_type": bool,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Solver Included"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Solver is integrated in the model (e.g. FMU for co-simulation)"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/SolverIncluded/1/0"
                                ),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TestedToolSolverAlgorithm(aas.SubmodelElementCollection):

                        class SolverAlgorithm(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"SolverAlgorithm",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Solver Algorithm"}),
                                    "description": aas.MultiLanguageTextType(dict_={r"en": r"validated solver"}),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/SimulationModels/SolverAlgorithm/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ToolSolverFurtherDescription(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ToolSolverFurtherDescription",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Tool Solver Further Description"}
                                    ),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Further tool- and solver-specific information"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/SimulationModels/ToolSolverFurtherDescription/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Tolerance(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Tolerance",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Tolerance"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"(relative) tolerance for theadaptive step size"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/SimulationModels/Tolerance/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"TestedToolSolverAlgorithm",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Tested Tool Solver Algorithm"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"List of validated tool-solver combinations"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/TestedToolSolverAlgorithm/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            solverAlgorithm: Union[str, SolverAlgorithm],
                            toolSolverFurtherDescription: Optional[Union[str, ToolSolverFurtherDescription]] = None,
                            tolerance: Optional[Union[xsd.Float, Tolerance]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if solverAlgorithm is not None and not isinstance(solverAlgorithm, aas.SubmodelElement):
                                solverAlgorithm = self.SolverAlgorithm(solverAlgorithm)

                            # Build a submodel element if a raw value was passed in the argument

                            if toolSolverFurtherDescription is not None and not isinstance(
                                toolSolverFurtherDescription, aas.SubmodelElement
                            ):
                                toolSolverFurtherDescription = self.ToolSolverFurtherDescription(
                                    toolSolverFurtherDescription
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if tolerance is not None and not isinstance(tolerance, aas.SubmodelElement):
                                tolerance = self.Tolerance(tolerance)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                solverAlgorithm, toolSolverFurtherDescription, tolerance
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"SolverAndTolerances",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Solver And Tolerances"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Useful settings of the simulation environment. Includes e.g. solver settings."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/SolverAndTolerances/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        stepSizeControlNeeded: Union[bool, StepSizeControlNeeded],
                        stiffSolverNeeded: Union[bool, StiffSolverNeeded],
                        solverIncluded: Union[bool, SolverIncluded],
                        fixedStepSize: Optional[Union[xsd.Float, FixedStepSize]] = None,
                        testedToolSolverAlgorithm: Optional[Iterable[TestedToolSolverAlgorithm]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if stepSizeControlNeeded is not None and not isinstance(
                            stepSizeControlNeeded, aas.SubmodelElement
                        ):
                            stepSizeControlNeeded = self.StepSizeControlNeeded(stepSizeControlNeeded)

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedStepSize is not None and not isinstance(fixedStepSize, aas.SubmodelElement):
                            fixedStepSize = self.FixedStepSize(fixedStepSize)

                        # Build a submodel element if a raw value was passed in the argument

                        if stiffSolverNeeded is not None and not isinstance(stiffSolverNeeded, aas.SubmodelElement):
                            stiffSolverNeeded = self.StiffSolverNeeded(stiffSolverNeeded)

                        # Build a submodel element if a raw value was passed in the argument

                        if solverIncluded is not None and not isinstance(solverIncluded, aas.SubmodelElement):
                            solverIncluded = self.SolverIncluded(solverIncluded)

                        # A str would be split into its characters
                        if isinstance(testedToolSolverAlgorithm, str):
                            raise TypeError("testedToolSolverAlgorithm takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            stepSizeControlNeeded,
                            fixedStepSize,
                            stiffSolverNeeded,
                            solverIncluded,
                            testedToolSolverAlgorithm,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"SimulationTool",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Simulation Tool"}),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Properties of the model with regarding to concrete simulation tools"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/SimulationTool/1/0"),
                    }

                def __init__(
                    self,
                    simToolName: Union[str, SimToolName],
                    solverAndTolerances: SolverAndTolerances,
                    dependencySimTool: Optional[Iterable[Union[str, DependencySimTool]]] = None,
                    compiler: Optional[Iterable[Union[str, Compiler]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if simToolName is not None and not isinstance(simToolName, aas.SubmodelElement):
                        simToolName = self.SimToolName(simToolName)

                    # A str would be split into its characters
                    if isinstance(dependencySimTool, str):
                        raise TypeError("dependencySimTool takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if dependencySimTool:
                        dependencySimTool = [
                            i if isinstance(i, aas.SubmodelElement) else self.DependencySimTool(i)
                            for i in dependencySimTool
                        ]

                    # A str would be split into its characters
                    if isinstance(compiler, str):
                        raise TypeError("compiler takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if compiler:
                        compiler = [i if isinstance(i, aas.SubmodelElement) else self.Compiler(i) for i in compiler]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        simToolName, dependencySimTool, compiler, solverAndTolerances
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Environment",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Environment"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Information about prerequisite environments or dependencies of underlying components on the target system."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Environment/1/0"),
                }

            def __init__(
                self,
                operatingSystem: Union[str, OperatingSystem],
                simulationTool: Iterable[SimulationTool],
                toolEnvironment: Optional[Iterable[Union[str, ToolEnvironment]]] = None,
                dependencyEnvironment: Optional[Union[aas.LangStringSet, DependencyEnvironment]] = None,
                visualizationInformation: Optional[Union[str, VisualizationInformation]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if operatingSystem is not None and not isinstance(operatingSystem, aas.SubmodelElement):
                    operatingSystem = self.OperatingSystem(operatingSystem)

                # A str would be split into its characters
                if isinstance(toolEnvironment, str):
                    raise TypeError("toolEnvironment takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if toolEnvironment:
                    toolEnvironment = [
                        i if isinstance(i, aas.SubmodelElement) else self.ToolEnvironment(i) for i in toolEnvironment
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if dependencyEnvironment is not None and not isinstance(dependencyEnvironment, aas.SubmodelElement):
                    dependencyEnvironment = self.DependencyEnvironment(dependencyEnvironment)

                # Build a submodel element if a raw value was passed in the argument

                if visualizationInformation is not None and not isinstance(
                    visualizationInformation, aas.SubmodelElement
                ):
                    visualizationInformation = self.VisualizationInformation(visualizationInformation)

                # A str would be split into its characters
                if isinstance(simulationTool, str):
                    raise TypeError("simulationTool takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    operatingSystem, toolEnvironment, dependencyEnvironment, visualizationInformation, simulationTool
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RefSimDocumentation(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"RefSimDocumentation",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ref Sim Documentation"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Documentation of example simulations of the model can be supplied. This includes a solver setup and sample circuit and sample results. e.g. zip file, PDF, html, ..."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/RefSimDocumentation/1/0"),
                }

            def __init__(
                self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class ModelFile(aas.SubmodelElementCollection):

            class ModelFileType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ModelFileType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Model File Type"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'"Designation of the exchange format of the model. E.G.: FMI 1.0, Co-Simulation, Platform / Source - Code. FMI 2.0.2, Model Exchange, Source - Code, S-function, Version 2, 64bit, mex - Format / or C-Code, Modelica 3, encoded, VHDL'
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/ModelFileType/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ModelFileVersion(aas.SubmodelElementCollection):

                class ModelVersionId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ModelVersionId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Model Version Id"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Version number of the model from the vendor."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/ModelVersionId/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ModelPreviewImage(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"ModelPreviewImage",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Model Preview Image"}),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Image file to represent the model in user interfaces, e.g. in a search."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/ModelPreviewImage/1/0"
                            ),
                        }

                    def __init__(
                        self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class DigitalFile(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"DigitalFile",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Digital File"}),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Deployment of the model file."}),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/DigitalFile/1/0"),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/octet-stream",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class ModelFileReleaseNotesTxt(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ModelFileReleaseNotesTxt",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Model File Release Notes Txt"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"contains information about this release"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/ModelFileReleaseNotesTxt/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ModelFileReleaseNotesFile(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"ModelFileReleaseNotesFile",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Model File Release Notes File"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"release notes link or file"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/ModelFileReleaseNotesFile/1/0"
                            ),
                        }

                    def __init__(
                        self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ModelFileVersion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Model File Version"}),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Provision of a version of the simulation model with information to distinguish the versions. The versions are primarily intended for bug fixes without content changes."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/ModelFileVersion/1/0"),
                    }

                def __init__(
                    self,
                    modelVersionId: Union[str, ModelVersionId],
                    digitalFile: DigitalFile,
                    modelPreviewImage: Optional[ModelPreviewImage] = None,
                    modelFileReleaseNotesTxt: Optional[Union[aas.LangStringSet, ModelFileReleaseNotesTxt]] = None,
                    modelFileReleaseNotesFile: Optional[ModelFileReleaseNotesFile] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if modelVersionId is not None and not isinstance(modelVersionId, aas.SubmodelElement):
                        modelVersionId = self.ModelVersionId(modelVersionId)

                    # Build a submodel element if a raw value was passed in the argument

                    if modelFileReleaseNotesTxt is not None and not isinstance(
                        modelFileReleaseNotesTxt, aas.SubmodelElement
                    ):
                        modelFileReleaseNotesTxt = self.ModelFileReleaseNotesTxt(modelFileReleaseNotesTxt)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        modelVersionId,
                        modelPreviewImage,
                        digitalFile,
                        modelFileReleaseNotesTxt,
                        modelFileReleaseNotesFile,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ModelFile",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Model File"}),
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Providing versions of the simulation model and with characteristics to distinguish them."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/ModelFile/1/0"),
                }

            def __init__(
                self,
                modelFileVersion: Iterable[ModelFileVersion],
                modelFileType: Optional[Union[str, ModelFileType]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if modelFileType is not None and not isinstance(modelFileType, aas.SubmodelElement):
                    modelFileType = self.ModelFileType(modelFileType)

                # A str would be split into its characters
                if isinstance(modelFileVersion, str):
                    raise TypeError("modelFileVersion takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(modelFileType, modelFileVersion)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ParamMethod(aas.Property):

            ALLOWED_VALUES = (
                r'by using "technical data" of asset',
                r'by using "technical data" and user',
                r"by user interface",
                r"by setting file",
                r"not necessary",
                r"by documentation file",
                r"pre-parametrized",
            )

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ParamMethod",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Param Method"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates whether the model must be parameterized and if so, which method is required."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/ParamMethod/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ParamFile(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"ParamFile",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Param File"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"File for parameterization of the model. As parameter file or parameter documentation (e.g. pdf)."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/ParamFile/1/0"),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class InitStateMethod(aas.Property):

            ALLOWED_VALUES = (
                r"not necessary",
                r"by user interface",
                r"by setting file",
                r"set states within simulation environment",
                r"integrated in model",
                r"by documentation file",
            )

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"InitStateMethod",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Init State Method"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r'" Describes the state variables of the simulation model that must be initialized to start the simulation. For initial value problems, these quantities describe the system state at the start of the simulation. In this case, the system is in a state of equilibrium. Alternatively, a simulation model may include a method to determine consistent initial values at this step, e.g., at an operating point.'
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/InitStateMethod/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class InitStateFile(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"InitStateFile",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Init State File"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"File for parameterizing the initial states of the model. As parameter file or parameter documentation (e.g. pdf)."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/InitStateFile/1/0"),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class DefaultSimTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DefaultSimTime",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Default Sim Time"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Predefined simulation period in seconds"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/DefaultSimTime/1/0"),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SimModManufacturerInformation(aas.SubmodelElementCollection):

            class Company(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Company",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Company"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"name of the company"}),
                        "semantic_id": global_ref(r"0173-1#02-AAW001#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Language(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Language"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"available language"}),
                        "semantic_id": global_ref(r"0173-1#02-AAO895#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Email(aas.SubmodelElementCollection):

                class TypeOfEmailAddress(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TypeOfEmailAddress",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Type Of Email Address"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"characterization of an e-mail address according to its location or usage"
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAO199#003"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EmailAddress(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EmailAddress",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Email Address"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"electronic mail address of a business partner"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAO198#002"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TypeOfPublicKey(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TypeOfPublicKey",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Type Of Public Key"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"characterization of a public key according to its encryption process"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAO201#002"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PublicKey(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PublicKey",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Public Key"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"public part of an unsymmetrical key pair to sign or encrypt text or messages"
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAO200#002"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Email",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Email"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"E-mail address and encryption method"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAQ836#005"),
                    }

                def __init__(
                    self,
                    emailAddress: Union[str, EmailAddress],
                    typeOfEmailAddress: Optional[Union[str, TypeOfEmailAddress]] = None,
                    typeOfPublicKey: Optional[Union[str, TypeOfPublicKey]] = None,
                    publicKey: Optional[Union[str, PublicKey]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfEmailAddress is not None and not isinstance(typeOfEmailAddress, aas.SubmodelElement):
                        typeOfEmailAddress = self.TypeOfEmailAddress(typeOfEmailAddress)

                    # Build a submodel element if a raw value was passed in the argument

                    if emailAddress is not None and not isinstance(emailAddress, aas.SubmodelElement):
                        emailAddress = self.EmailAddress(emailAddress)

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfPublicKey is not None and not isinstance(typeOfPublicKey, aas.SubmodelElement):
                        typeOfPublicKey = self.TypeOfPublicKey(typeOfPublicKey)

                    # Build a submodel element if a raw value was passed in the argument

                    if publicKey is not None and not isinstance(publicKey, aas.SubmodelElement):
                        publicKey = self.PublicKey(publicKey)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        typeOfEmailAddress, emailAddress, typeOfPublicKey, publicKey
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Phone(aas.SubmodelElementCollection):

                class TypeOfTelephone(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TypeOfTelephone",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Type Of Telephone"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"characterization of a telephone according to its location or usage"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAO137#003"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TelephoneNumber(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TelephoneNumber",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Telephone Number"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"complete telephone number to be called to reach a business partner"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAO136#002"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AvailableTime(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AvailableTime",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Available Time"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Specification of the available time window"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Phone",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Phone"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Phone number including type"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Phone"
                        ),
                    }

                def __init__(
                    self,
                    telephoneNumber: Union[str, TelephoneNumber],
                    typeOfTelephone: Optional[Union[str, TypeOfTelephone]] = None,
                    availableTime: Optional[Union[str, AvailableTime]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfTelephone is not None and not isinstance(typeOfTelephone, aas.SubmodelElement):
                        typeOfTelephone = self.TypeOfTelephone(typeOfTelephone)

                    # Build a submodel element if a raw value was passed in the argument

                    if telephoneNumber is not None and not isinstance(telephoneNumber, aas.SubmodelElement):
                        telephoneNumber = self.TelephoneNumber(telephoneNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if availableTime is not None and not isinstance(availableTime, aas.SubmodelElement):
                        availableTime = self.AvailableTime(availableTime)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        typeOfTelephone, telephoneNumber, availableTime
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"SimModManufacturerInformation",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sim Mod Manufacturer Information"}),
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Provide access to  simulation support service provided by the distributor via mail or phone"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/SimulationModels/SimModManufacturerInformation/1/0"
                    ),
                }

            def __init__(
                self,
                company: Union[str, Company],
                language: Iterable[Union[str, Language]],
                email: Optional[Email] = None,
                phone: Optional[Phone] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if company is not None and not isinstance(company, aas.SubmodelElement):
                    company = self.Company(company)

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if language:
                    language = [i if isinstance(i, aas.SubmodelElement) else self.Language(i) for i in language]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(company, language, email, phone)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Ports(aas.SubmodelElementCollection):

            class PortsConnector(aas.SubmodelElementCollection):

                class PortConnectorName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PortConnectorName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Port Connector Name"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the Connector Port."}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/PortsConnectorName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PortConDescription(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"PortConDescription",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Port Con Description"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Specifies Port Con Description."}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/portConDescription/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Variable(aas.SubmodelElementCollection):

                    class VariableName(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"VariableName",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Name"}),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the variable."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/VariableName/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Range(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Range",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Range"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Range of values for the variable (e.g. [min, max], [min, max[, ]min, max], ]min, max[, {val1, val2, ...})."
                                    }
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Range/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VariableType(aas.Property):

                        ALLOWED_VALUES = (r"Real", r"Integer", r"Boolean", r"String", r"ENUM")

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"VariableType",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Type"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Type of the variable (e.g. Real, Integer, Boolean, String or Enum)."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/VariableType/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VariableDescription(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"VariableDescription",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Description"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Description of the variable."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/VariableDescription/1/0"
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class UnitList(aas.Property):

                        ALLOWED_VALUES = (r"s", r"m", r"kg", r"N", r"m/s", r"m/s^2", r"V", r"A", r"K", r"none")

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"UnitList",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit List"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r'The most common units can be selected here. .. If "others" is selected, a free text can be entered.'
                                    }
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/UnitList/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class UnitDescription(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"UnitDescription",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit Description"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Text field for missing units of the list"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/UnitDescription/1/0"
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VariableCausality(aas.Property):

                        ALLOWED_VALUES = (r"input", r"output", r"acausal")

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"VariableCausality",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Causality"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The causality of the variable: input to inputs, output to ouputs, acausal connections (e.g. mechanical connection) do not have causality."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/VariableCausality/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class VariablePrefix(aas.Property):

                        ALLOWED_VALUES = (r"Flow", r"Stream")

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"VariablePrefix",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable Prefix"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": 'Prefix for acausal variable. Potential variables are set equal when connecting (no prefix). Stream variables are connected according to Kirchhoff\'s law, i.e. the sum of the variables equals zero. The bi-directional flow of matter is described with "stream" (e.g. for enthalpy).'
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/SimulationModels/VariablePrefix/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Variable",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Variable"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"List of variables of the port."}),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Variable/1/0"),
                        }

                    def __init__(
                        self,
                        variableName: Union[str, VariableName],
                        variableType: Union[str, VariableType],
                        unitList: Union[str, UnitList],
                        variableCausality: Union[str, VariableCausality],
                        range: Optional[Union[str, Range]] = None,
                        variableDescription: Optional[Union[aas.LangStringSet, VariableDescription]] = None,
                        unitDescription: Optional[Union[aas.LangStringSet, UnitDescription]] = None,
                        variablePrefix: Optional[Union[str, VariablePrefix]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if variableName is not None and not isinstance(variableName, aas.SubmodelElement):
                            variableName = self.VariableName(variableName)

                        # Build a submodel element if a raw value was passed in the argument

                        if range is not None and not isinstance(range, aas.SubmodelElement):
                            range = self.Range(range)

                        # Build a submodel element if a raw value was passed in the argument

                        if variableType is not None and not isinstance(variableType, aas.SubmodelElement):
                            variableType = self.VariableType(variableType)

                        # Build a submodel element if a raw value was passed in the argument

                        if variableDescription is not None and not isinstance(variableDescription, aas.SubmodelElement):
                            variableDescription = self.VariableDescription(variableDescription)

                        # Build a submodel element if a raw value was passed in the argument

                        if unitList is not None and not isinstance(unitList, aas.SubmodelElement):
                            unitList = self.UnitList(unitList)

                        # Build a submodel element if a raw value was passed in the argument

                        if unitDescription is not None and not isinstance(unitDescription, aas.SubmodelElement):
                            unitDescription = self.UnitDescription(unitDescription)

                        # Build a submodel element if a raw value was passed in the argument

                        if variableCausality is not None and not isinstance(variableCausality, aas.SubmodelElement):
                            variableCausality = self.VariableCausality(variableCausality)

                        # Build a submodel element if a raw value was passed in the argument

                        if variablePrefix is not None and not isinstance(variablePrefix, aas.SubmodelElement):
                            variablePrefix = self.VariablePrefix(variablePrefix)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            variableName,
                            range,
                            variableType,
                            variableDescription,
                            unitList,
                            unitDescription,
                            variableCausality,
                            variablePrefix,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"PortsConnector",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ports Connector"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List of ports of the model. These include a name, a description, a list of variables, and a list of ports."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/PortsConnector/1/0"),
                    }

                def __init__(
                    self,
                    portConnectorName: Union[str, PortConnectorName],
                    portConDescription: Optional[Union[aas.LangStringSet, PortConDescription]] = None,
                    variable: Optional[Iterable[Variable]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if portConnectorName is not None and not isinstance(portConnectorName, aas.SubmodelElement):
                        portConnectorName = self.PortConnectorName(portConnectorName)

                    # Build a submodel element if a raw value was passed in the argument

                    if portConDescription is not None and not isinstance(portConDescription, aas.SubmodelElement):
                        portConDescription = self.PortConDescription(portConDescription)

                    # A str would be split into its characters
                    if isinstance(variable, str):
                        raise TypeError("variable takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        portConnectorName, portConDescription, variable
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class BinaryConnector(aas.SubmodelElementCollection):

                class BinaryConName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"BinaryConName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Binary Con Name"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Binary interface name."}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/BinaryConnectorName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class BinaryConDescription(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"BinaryConDescription",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Binary Con Description"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Binary interface description."}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SimulationModels/BinaryConDescription/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"BinaryConnector",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Binary Connector"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'Binary interfaces (binaryType) based on the FMI 3.0 standard (https://fmi-standard.org/docs/3.0-dev/#definition-of-types). At this point the name (e.g. "Binary interface visualization") and the description (e.g. "Interface for binary transfer of visualization information") are specified.'
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/BinaryConnector/1/0"),
                    }

                def __init__(
                    self,
                    binaryConName: Union[str, BinaryConName],
                    binaryConDescription: Optional[Union[aas.LangStringSet, BinaryConDescription]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if binaryConName is not None and not isinstance(binaryConName, aas.SubmodelElement):
                        binaryConName = self.BinaryConName(binaryConName)

                    # Build a submodel element if a raw value was passed in the argument

                    if binaryConDescription is not None and not isinstance(binaryConDescription, aas.SubmodelElement):
                        binaryConDescription = self.BinaryConDescription(binaryConDescription)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(binaryConName, binaryConDescription)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Ports",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ports"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Interfaces of the model. This includes inputs, outputs as well as acausal connections (e.g. mechanical connections). In addition, it is specified here whether the model provides binary interfaces (e.g. for visualization)."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Ports/1/0"),
                }

            def __init__(
                self,
                portsConnector: Optional[Iterable[PortsConnector]] = None,
                binaryConnector: Optional[Iterable[BinaryConnector]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(portsConnector, str):
                    raise TypeError("portsConnector takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(binaryConnector, str):
                    raise TypeError("binaryConnector takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(portsConnector, binaryConnector)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Quality(aas.SubmodelElementCollection):

            class Usability(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Usability",
                        "value_type": xsd.PositiveInteger,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Usability"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "The model's ease of use, adaptability, and user-friendliness, ensuring it is accessible and manageable for intended roles."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Usability/1/1"),
                    }

                def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Architecture(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Architecture",
                        "value_type": xsd.PositiveInteger,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Architecture"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The structural design and organization of the model, defining how its components interact to support accurate and efficient simulation."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Architecture/1/1"),
                    }

                def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Validation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Validation",
                        "value_type": xsd.PositiveInteger,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Validation"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The process of confirming that the model accurately replicates real-world processes or behaviors, meeting specified requirements for its intended application."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Validation/1/1"),
                    }

                def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class QualityMetricFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"QualityMetricFile",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Quality Metric File"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"AML File containing the complete quality evaluation of the simulation model with all factors, criteria and attributes."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/SimulationModels/QualityMetricFile/1/1"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class EvaluationPerspective(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"EvaluationPerspective",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Evaluation Perspective"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Role description indicating from which point of view the simulation model’s quality was evaluated (e.g., Model Provider, Model User, Model Consumer, Model Developer, etc.)."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/SimulationModels/EvaluationPerspective/1/1"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Quality",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Quality"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "The overall measure of a simulation model's ability to meet predefined standards and functional expectations, ensuring it accurately represents the intended system."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/Quality/1/1"),
                }

            def __init__(
                self,
                usability: Union[xsd.PositiveInteger, Usability],
                architecture: Union[xsd.PositiveInteger, Architecture],
                validation: Union[xsd.PositiveInteger, Validation],
                qualityMetricFile: QualityMetricFile,
                evaluationPerspective: Union[aas.LangStringSet, EvaluationPerspective],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if usability is not None and not isinstance(usability, aas.SubmodelElement):
                    usability = self.Usability(usability)

                # Build a submodel element if a raw value was passed in the argument

                if architecture is not None and not isinstance(architecture, aas.SubmodelElement):
                    architecture = self.Architecture(architecture)

                # Build a submodel element if a raw value was passed in the argument

                if validation is not None and not isinstance(validation, aas.SubmodelElement):
                    validation = self.Validation(validation)

                # Build a submodel element if a raw value was passed in the argument

                if evaluationPerspective is not None and not isinstance(evaluationPerspective, aas.SubmodelElement):
                    evaluationPerspective = self.EvaluationPerspective(evaluationPerspective)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    usability, architecture, validation, qualityMetricFile, evaluationPerspective
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SimulationModel",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Simulation Model"}),
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Specifies Simulation Model."}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/SimulationModels/SimulationModel/1/1"),
            }

        def __init__(
            self,
            simPurpose: SimPurpose,
            scopeOfModel: Iterable[Union[str, ScopeOfModel]],
            modelFile: ModelFile,
            paramMethod: Union[str, ParamMethod],
            initStateMethod: Union[str, InitStateMethod],
            summary: Optional[Union[aas.LangStringSet, Summary]] = None,
            typeOfModel: Optional[Iterable[Union[str, TypeOfModel]]] = None,
            licenseModel: Optional[Union[str, LicenseModel]] = None,
            engineeringDomain: Optional[Iterable[Union[str, EngineeringDomain]]] = None,
            environment: Optional[Iterable[Environment]] = None,
            refSimDocumentation: Optional[Iterable[RefSimDocumentation]] = None,
            paramFile: Optional[ParamFile] = None,
            initStateFile: Optional[InitStateFile] = None,
            defaultSimTime: Optional[Union[xsd.Float, DefaultSimTime]] = None,
            simModManufacturerInformation: Optional[Iterable[SimModManufacturerInformation]] = None,
            ports: Optional[Ports] = None,
            quality: Optional[Iterable[Quality]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if summary is not None and not isinstance(summary, aas.SubmodelElement):
                summary = self.Summary(summary)

            # A str would be split into its characters
            if isinstance(typeOfModel, str):
                raise TypeError("typeOfModel takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if typeOfModel:
                typeOfModel = [i if isinstance(i, aas.SubmodelElement) else self.TypeOfModel(i) for i in typeOfModel]

            # A str would be split into its characters
            if isinstance(scopeOfModel, str):
                raise TypeError("scopeOfModel takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if scopeOfModel:
                scopeOfModel = [i if isinstance(i, aas.SubmodelElement) else self.ScopeOfModel(i) for i in scopeOfModel]

            # Build a submodel element if a raw value was passed in the argument

            if licenseModel is not None and not isinstance(licenseModel, aas.SubmodelElement):
                licenseModel = self.LicenseModel(licenseModel)

            # A str would be split into its characters
            if isinstance(engineeringDomain, str):
                raise TypeError("engineeringDomain takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if engineeringDomain:
                engineeringDomain = [
                    i if isinstance(i, aas.SubmodelElement) else self.EngineeringDomain(i) for i in engineeringDomain
                ]

            # A str would be split into its characters
            if isinstance(environment, str):
                raise TypeError("environment takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(refSimDocumentation, str):
                raise TypeError("refSimDocumentation takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if paramMethod is not None and not isinstance(paramMethod, aas.SubmodelElement):
                paramMethod = self.ParamMethod(paramMethod)

            # Build a submodel element if a raw value was passed in the argument

            if initStateMethod is not None and not isinstance(initStateMethod, aas.SubmodelElement):
                initStateMethod = self.InitStateMethod(initStateMethod)

            # Build a submodel element if a raw value was passed in the argument

            if defaultSimTime is not None and not isinstance(defaultSimTime, aas.SubmodelElement):
                defaultSimTime = self.DefaultSimTime(defaultSimTime)

            # A str would be split into its characters
            if isinstance(simModManufacturerInformation, str):
                raise TypeError("simModManufacturerInformation takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(quality, str):
                raise TypeError("quality takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
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
                quality,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"SimulationModels",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Simulation Models"}),
            "description": aas.MultiLanguageTextType(dict_={r"en": r"Specifies Simulation Models."}),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/SimulationModels/1/1",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self, id_: str, simulationModel: Optional[Iterable[SimulationModel]] = None, **kwargs: Unpack[SubmodelMetadata]
    ):

        # A str would be split into its characters
        if isinstance(simulationModel, str):
            raise TypeError("simulationModel takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(simulationModel)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
