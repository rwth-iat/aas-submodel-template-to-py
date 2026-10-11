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


class ExecutedProcesses(aas.Submodel):

    class Run(aas.SubmodelElementCollection):

        class RunResult(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RunResult",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Indicates the outcome of a run."}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/RunResult/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Process(aas.SubmodelElementCollection):

            class ProcessId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProcessId",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Describes the ID of the process"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ProcessParameters/ProcessId/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProcessName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProcessName",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Describes the Name of the Process "}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ProcessParameters/ProcessName/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProcessDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ProcessDescription",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Describes the process."}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ProcessParameters/ProcessDescription/1/0"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PlannedProcessTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PlannedProcessTime",
                        "value_type": xsd.Duration,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Planned processing time for process execution (without set-up time)"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ProcessParameters/PlannedProcessTime/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Duration, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProductParameters(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProductParameters",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Mandatory product parameters for process execution"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0"
                        ),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ProcessParameters(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessParameters",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Mandatory process parameters for process execution"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0"
                        ),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ResourceParameters(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ResourceParameters",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Mandatory resource parameters for process execution"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0"
                        ),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ProcessBoM(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessBoM",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"describes the products or semi-finished products to be involved in the process"
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ProcessStatus(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProcessStatus",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Describes the process status."}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStatus/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProcessResult(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProcessResult",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Result of the process."}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/ProcessResult/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OperatorRole(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OperatorRole",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Role of the operator in the process."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/OperatorRole/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProcessStartTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProcessStartTime",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Start time of the process."}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStartTime/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProcessEndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProcessEndTime",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"End time of the process."}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/ProcessEndTime/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProcessStages(aas.SubmodelElementCollection):

                class ProcessStage(aas.SubmodelElementCollection):

                    class StageId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StageId",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"ID of the stage."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStage/StageId/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class StartTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StartTime",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Time when the stage started."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStage/StartTime/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class EndTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"EndTime",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Time when the stage ended."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStage/EndTime/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Result(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Result",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Stage result."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStage/Result/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ProcessStage",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"A stage that the process went through."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStage/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        stageId: Union[str, StageId],
                        startTime: Union[str, StartTime],
                        endTime: Union[str, EndTime],
                        result: Union[str, Result],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if stageId is not None and not isinstance(stageId, aas.SubmodelElement):
                            stageId = self.StageId(stageId)

                        # Build a submodel element if a raw value was passed in the argument

                        if startTime is not None and not isinstance(startTime, aas.SubmodelElement):
                            startTime = self.StartTime(startTime)

                        # Build a submodel element if a raw value was passed in the argument

                        if endTime is not None and not isinstance(endTime, aas.SubmodelElement):
                            endTime = self.EndTime(endTime)

                        # Build a submodel element if a raw value was passed in the argument

                        if result is not None and not isinstance(result, aas.SubmodelElement):
                            result = self.Result(result)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(stageId, startTime, endTime, result)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessStages",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"List of stages that the process went through."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/ProcessStages/1/0"),
                    }

                def __init__(
                    self,
                    processStage: Optional[Iterable[ProcessStage]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(processStage, str):
                        raise TypeError("processStage takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(processStage)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ProcessErrors(aas.SubmodelElementCollection):

                class ProcessError(aas.SubmodelElementCollection):

                    class ErrorCode(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ErrorCode",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Error code."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ExecutedProcesses/ProcessError/ErrorCode/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ErrorDescription(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ErrorDescription",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Error description."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ExecutedProcesses/ProcessError/ErrorDescription/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ProcessError",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"An error that caused the process to fail."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ExecutedProcesses/ProcessError/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        errorCode: Union[str, ErrorCode],
                        errorDescription: Union[str, ErrorDescription],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if errorCode is not None and not isinstance(errorCode, aas.SubmodelElement):
                            errorCode = self.ErrorCode(errorCode)

                        # Build a submodel element if a raw value was passed in the argument

                        if errorDescription is not None and not isinstance(errorDescription, aas.SubmodelElement):
                            errorDescription = self.ErrorDescription(errorDescription)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(errorCode, errorDescription)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessErrors",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"List of errors that caused the process to fail."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/ProcessErrors/1/0"),
                    }

                def __init__(
                    self,
                    processError: Optional[Iterable[ProcessError]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(processError, str):
                        raise TypeError("processError takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(processError)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Process",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Describes the values of a process that was executed."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/Process/1/0"),
                }

            def __init__(
                self,
                processId: Union[str, ProcessId],
                processName: Union[str, ProcessName],
                processDescription: Union[aas.LangStringSet, ProcessDescription],
                plannedProcessTime: Union[xsd.Duration, PlannedProcessTime],
                productParameters: ProductParameters,
                processParameters: ProcessParameters,
                resourceParameters: ResourceParameters,
                processBoM: ProcessBoM,
                processStatus: Union[str, ProcessStatus],
                processResult: Union[str, ProcessResult],
                processStartTime: Union[str, ProcessStartTime],
                processEndTime: Union[str, ProcessEndTime],
                processStages: ProcessStages,
                processErrors: ProcessErrors,
                operatorRole: Optional[Union[str, OperatorRole]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if processId is not None and not isinstance(processId, aas.SubmodelElement):
                    processId = self.ProcessId(processId)

                # Build a submodel element if a raw value was passed in the argument

                if processName is not None and not isinstance(processName, aas.SubmodelElement):
                    processName = self.ProcessName(processName)

                # Build a submodel element if a raw value was passed in the argument

                if processDescription is not None and not isinstance(processDescription, aas.SubmodelElement):
                    processDescription = self.ProcessDescription(processDescription)

                # Build a submodel element if a raw value was passed in the argument

                if plannedProcessTime is not None and not isinstance(plannedProcessTime, aas.SubmodelElement):
                    plannedProcessTime = self.PlannedProcessTime(plannedProcessTime)

                # Build a submodel element if a raw value was passed in the argument

                if processStatus is not None and not isinstance(processStatus, aas.SubmodelElement):
                    processStatus = self.ProcessStatus(processStatus)

                # Build a submodel element if a raw value was passed in the argument

                if processResult is not None and not isinstance(processResult, aas.SubmodelElement):
                    processResult = self.ProcessResult(processResult)

                # Build a submodel element if a raw value was passed in the argument

                if operatorRole is not None and not isinstance(operatorRole, aas.SubmodelElement):
                    operatorRole = self.OperatorRole(operatorRole)

                # Build a submodel element if a raw value was passed in the argument

                if processStartTime is not None and not isinstance(processStartTime, aas.SubmodelElement):
                    processStartTime = self.ProcessStartTime(processStartTime)

                # Build a submodel element if a raw value was passed in the argument

                if processEndTime is not None and not isinstance(processEndTime, aas.SubmodelElement):
                    processEndTime = self.ProcessEndTime(processEndTime)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    processId,
                    processName,
                    processDescription,
                    plannedProcessTime,
                    productParameters,
                    processParameters,
                    resourceParameters,
                    processBoM,
                    processStatus,
                    processResult,
                    operatorRole,
                    processStartTime,
                    processEndTime,
                    processStages,
                    processErrors,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Run",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Represents a single execution of the processes defined in the bill-of-process."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/Run/1/0"),
            }

        def __init__(
            self,
            runResult: Union[str, RunResult],
            process: Optional[Iterable[Process]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if runResult is not None and not isinstance(runResult, aas.SubmodelElement):
                runResult = self.RunResult(runResult)

            # A str would be split into its characters
            if isinstance(process, str):
                raise TypeError("process takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(runResult, process)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ExecutedProcesses",
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"The Submodel describes the input and output parameters for the execution of processes."}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell-io/IDTA-02031-2",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/ExecutedProcesses/1/0"),
        }

    def __init__(self, id_: str, run: Iterable[Run], **kwargs: Unpack[SubmodelMetadata]):

        # A str would be split into its characters
        if isinstance(run, str):
            raise TypeError("run takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(run)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
