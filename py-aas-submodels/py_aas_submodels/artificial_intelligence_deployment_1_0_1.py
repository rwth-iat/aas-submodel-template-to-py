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


class RangeMetadata(TypedDict, total=False):
    """Metadata of aas.Range, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_type: aas.DataTypeDefXsd
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class ReferenceElementMetadata(TypedDict, total=False):
    """Metadata of aas.ReferenceElement, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
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


class AIDeployment(aas.Submodel):

    class URIOfTheProduct(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"URIOfTheProduct",
                "value_type": str,
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"de": r"eindeutige globale Identifizierung der Produktinstanz unter Verwendung eines universellen Ressourcenbezeichners (URI)",
                        r"en": r"unique global identification of the product instance using an universal resource identifier (URI)",
                    }
                ),
                "semantic_id": global_ref(r"0112/2///61987#ABN590#002 "),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Version(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"Version",
                "value_type": str,
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={r"de": r"Version of the deployment ", r"en": r"Version des Deployments"}
                ),
                "semantic_id": global_ref(r"0173-1#02-AAS354#002"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ContactInformation(aas.ReferenceElement):

        @staticmethod
        def template_defaults() -> ReferenceElementMetadata:
            return {
                "id_short": r"ContactInformation",
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference to the Contact Information IDTA Submodel to describe the responsible person for the Submodel."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Contactinformation/1/0"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ModelNameplateRef(aas.ReferenceElement):

        @staticmethod
        def template_defaults() -> ReferenceElementMetadata:
            return {
                "id_short": r"ModelNameplateRef",
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Reference to the ModelNameplate-Submodel of the deployed model"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/ModelNameplateRef/1/0"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Storage(aas.SubmodelElementCollection):

        class Format(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Format",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Data format of the deployable model (e.g. onnx, docker-image ,...)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Storage/Format/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DeployedModel(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"DeployedModel",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"The deployable model"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Storage/DeployedModel/1/0"),
                }

            def __init__(
                self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Storage",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of storage information about the deployable AI-model"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Storage/1/0"),
            }

        def __init__(
            self,
            format: Union[str, Format],
            deployedModel: Optional[DeployedModel] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if format is not None and not isinstance(format, aas.SubmodelElement):
                format = self.Format(format)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(format, deployedModel)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Input(aas.SubmodelElementCollection):

        class ExampleInput(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ExampleInput",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"This is an example inputinformation placeholder"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Input/InputProperty/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Input",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of information about the input data for deployment"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Input/1/0"),
            }

        def __init__(
            self, exampleInput: Iterable[Union[str, ExampleInput]], **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(exampleInput, str):
                raise TypeError("exampleInput takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if exampleInput:
                exampleInput = [i if isinstance(i, aas.SubmodelElement) else self.ExampleInput(i) for i in exampleInput]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(exampleInput)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Output(aas.SubmodelElementCollection):

        class ExampleOutput(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ExampleOutput",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"This is an example inputinformation placeholder"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Output/OutputProperty/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Output",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of information about the output data for deployment"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/Output/1/0"),
            }

        def __init__(
            self,
            exampleOutput: Iterable[Union[str, ExampleOutput]],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(exampleOutput, str):
                raise TypeError("exampleOutput takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if exampleOutput:
                exampleOutput = [
                    i if isinstance(i, aas.SubmodelElement) else self.ExampleOutput(i) for i in exampleOutput
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(exampleOutput)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SoftwareRequirements(aas.SubmodelElementCollection):

        class ExampleFile(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"ExampleFile",
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Requirement file for software requirements"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/SoftwareRequirements/RequirementsFile/1/0"
                    ),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SoftwareRequirements",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection about required software for deployment"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/SoftwareRequirements/1/0"),
            }

        def __init__(
            self, exampleFile: Optional[ExampleFile] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(exampleFile)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class HardwareRequirements(aas.SubmodelElementCollection):

        class ExampleHardware(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"ExampleHardware",
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"This is an example requirement placeholder"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/HardwareRequirements/HardwareDescription/1/0"
                    ),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"HardwareRequirements",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection about required hardware for deployment"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/HardwareRequirements/1/0"),
            }

        def __init__(
            self, exampleHardware: Optional[ExampleHardware] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(exampleHardware)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class PerformanceInformation(aas.SubmodelElementCollection):

        class InferenceTime(aas.SubmodelElementCollection):

            class Time(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Time",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Measured inference time"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/PerformanceInformation/InferenceTime/Time/1/0"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Hardware(aas.SubmodelElementCollection):

                class CPU(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"CPU",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Information about the CPU."}),
                            "semantic_id": global_ref(r"0173-1#01-ACL481#008"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GPU(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"GPU",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Information about the GPU."}),
                            "semantic_id": global_ref(r"0173-1#01-ACL476#008"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TPU(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TPU",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Information about the TPU."}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AIDeployment/PerformanceInformation/InferenceTime/Hardware/TPU/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class RAM(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"RAM",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Information about the RAM."}),
                            "semantic_id": global_ref(r"0173-1#01-ACL340#008"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Hardware",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection of hardware used for the measurement"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/PerformanceInformation/InferenceTime/Hardware/1/0"
                        ),
                    }

                def __init__(
                    self,
                    cPU: Optional[Union[str, CPU]] = None,
                    gPU: Optional[Union[str, GPU]] = None,
                    tPU: Optional[Union[str, TPU]] = None,
                    rAM: Optional[Union[str, RAM]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if cPU is not None and not isinstance(cPU, aas.SubmodelElement):
                        cPU = self.CPU(cPU)

                    # Build a submodel element if a raw value was passed in the argument

                    if gPU is not None and not isinstance(gPU, aas.SubmodelElement):
                        gPU = self.GPU(gPU)

                    # Build a submodel element if a raw value was passed in the argument

                    if tPU is not None and not isinstance(tPU, aas.SubmodelElement):
                        tPU = self.TPU(tPU)

                    # Build a submodel element if a raw value was passed in the argument

                    if rAM is not None and not isinstance(rAM, aas.SubmodelElement):
                        rAM = self.RAM(rAM)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(cPU, gPU, tPU, rAM)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InferenceTime",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Collection of information about the measured inference time and the used equipment to achieve it"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/PerformanceInformation/InferenceTime/1/0"
                    ),
                }

            def __init__(
                self,
                time: Union[aas.LangStringSet, Time],
                hardware: Hardware,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if time is not None and not isinstance(time, aas.SubmodelElement):
                    time = self.Time(time)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(time, hardware)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"PerformanceInformation",
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Collection of performance measurements"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/PerformanceInformation/1/0"),
            }

        def __init__(
            self,
            inferenceTime: Optional[Iterable[InferenceTime]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(inferenceTime, str):
                raise TypeError("inferenceTime takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(inferenceTime)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class LiveMonitoring(aas.SubmodelElementCollection):

        class Confidence(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Confidence",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Live confidence"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/Confidence/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TimeIntervall(aas.Range):

            @staticmethod
            def template_defaults() -> RangeMetadata:
                return {
                    "id_short": r"TimeIntervall",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Time intervall for calculating the average confidence"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/TimeIntervall/1/0"
                    ),
                }

            def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

        class AverageConfidenceOverTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AverageConfidenceOverTime",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"confidence over a definded time intervall"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/AverageConfidence/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RunTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RunTime",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Time the deployed model is running without a break or downtime"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/RunTime/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class HardwareWorkload(aas.SubmodelElementCollection):

            class GPUWorkload(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"GPUWorkload",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Live GPU workload."}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/HardwareWorkload/GPUWorkload/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CPUWorkload(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CPUWorkload",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Llive CPU workload."}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/HardwareWorkload/CPUWorkload/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TPUWorkload(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TPUWorkload",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Live TPU workload."}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/HardwareWorkload/TPUWorkload/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RAMWorkload(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RAMWorkload",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Live RAM workload."}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/HardwareWorkload/RAMWorkload/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"HardwareWorkload",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection containing the live hardware workload"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/HardwareWorkload/1/0"
                    ),
                }

            def __init__(
                self,
                gPUWorkload: Optional[Union[str, GPUWorkload]] = None,
                cPUWorkload: Optional[Union[str, CPUWorkload]] = None,
                tPUWorkload: Optional[Union[str, TPUWorkload]] = None,
                rAMWorkload: Optional[Union[str, RAMWorkload]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if gPUWorkload is not None and not isinstance(gPUWorkload, aas.SubmodelElement):
                    gPUWorkload = self.GPUWorkload(gPUWorkload)

                # Build a submodel element if a raw value was passed in the argument

                if cPUWorkload is not None and not isinstance(cPUWorkload, aas.SubmodelElement):
                    cPUWorkload = self.CPUWorkload(cPUWorkload)

                # Build a submodel element if a raw value was passed in the argument

                if tPUWorkload is not None and not isinstance(tPUWorkload, aas.SubmodelElement):
                    tPUWorkload = self.TPUWorkload(tPUWorkload)

                # Build a submodel element if a raw value was passed in the argument

                if rAMWorkload is not None and not isinstance(rAMWorkload, aas.SubmodelElement):
                    rAMWorkload = self.RAMWorkload(rAMWorkload)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    gPUWorkload, cPUWorkload, tPUWorkload, rAMWorkload
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class DriftMetrics(aas.SubmodelElementCollection):

            class DataDrift(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DataDrift",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Live data drift"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/DriftMetrics/DataDrift/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ConceptDrift(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ConceptDrift",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Live concept drift"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/DriftMetrics/ConceptDrift/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PerformanceDrift(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PerformanceDrift",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Live performance drift"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/DriftMetrics/PerformanceDrift/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DriftMetrics",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection of live monitoring of different drift metrics"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/DriftMetrics/1/0"
                    ),
                }

            def __init__(
                self,
                dataDrift: Optional[Union[str, DataDrift]] = None,
                conceptDrift: Optional[Union[str, ConceptDrift]] = None,
                performanceDrift: Optional[Union[str, PerformanceDrift]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if dataDrift is not None and not isinstance(dataDrift, aas.SubmodelElement):
                    dataDrift = self.DataDrift(dataDrift)

                # Build a submodel element if a raw value was passed in the argument

                if conceptDrift is not None and not isinstance(conceptDrift, aas.SubmodelElement):
                    conceptDrift = self.ConceptDrift(conceptDrift)

                # Build a submodel element if a raw value was passed in the argument

                if performanceDrift is not None and not isinstance(performanceDrift, aas.SubmodelElement):
                    performanceDrift = self.PerformanceDrift(performanceDrift)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(dataDrift, conceptDrift, performanceDrift)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"LiveMonitoring",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection containing live values for monitoring"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/LiveMonitoring/1/0"),
            }

        def __init__(
            self,
            confidence: Optional[Union[str, Confidence]] = None,
            timeIntervall: Optional[Union[Tuple[str, str], TimeIntervall]] = None,
            averageConfidenceOverTime: Optional[Union[str, AverageConfidenceOverTime]] = None,
            runTime: Optional[Union[str, RunTime]] = None,
            hardwareWorkload: Optional[HardwareWorkload] = None,
            driftMetrics: Optional[DriftMetrics] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if confidence is not None and not isinstance(confidence, aas.SubmodelElement):
                confidence = self.Confidence(confidence)

            # Build a submodel element if a raw value was passed in the argument

            if timeIntervall is not None and not isinstance(timeIntervall, aas.SubmodelElement):
                timeIntervall = self.TimeIntervall(min=timeIntervall[0], max=timeIntervall[1])

            # Build a submodel element if a raw value was passed in the argument

            if averageConfidenceOverTime is not None and not isinstance(averageConfidenceOverTime, aas.SubmodelElement):
                averageConfidenceOverTime = self.AverageConfidenceOverTime(averageConfidenceOverTime)

            # Build a submodel element if a raw value was passed in the argument

            if runTime is not None and not isinstance(runTime, aas.SubmodelElement):
                runTime = self.RunTime(runTime)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                confidence, timeIntervall, averageConfidenceOverTime, runTime, hardwareWorkload, driftMetrics
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class RiskAssessment(aas.ReferenceElement):

        @staticmethod
        def template_defaults() -> ReferenceElementMetadata:
            return {
                "id_short": r"RiskAssessment",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"risk assessment based on regulation(EU) 2024/1689 of the european parliament and of the council",
                        r"de": r"Risikobewertung auf der Grundlage der Verordnung (EU) 2024/1689 des Europäischen Parlaments und des Rates",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDeployment/RiskAssessment/1/0"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"AIDeployment",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Contains the information for AI deployment ",
                    r"de": r"Enthält die Informationen für das AI-Deployment",
                }
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/SubmodelTemplate/AIDeployment/1/0"),
        }

    def __init__(
        self,
        id_: str,
        uRIOfTheProduct: Union[str, URIOfTheProduct],
        version: Union[str, Version],
        contactInformation: Union[aas.Reference, ContactInformation],
        modelNameplateRef: Union[aas.Reference, ModelNameplateRef],
        storage: Storage,
        input: Input,
        output: Output,
        softwareRequirements: Optional[SoftwareRequirements] = None,
        hardwareRequirements: Optional[HardwareRequirements] = None,
        performanceInformation: Optional[PerformanceInformation] = None,
        liveMonitoring: Optional[LiveMonitoring] = None,
        riskAssessment: Optional[Union[aas.Reference, RiskAssessment]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if uRIOfTheProduct is not None and not isinstance(uRIOfTheProduct, aas.SubmodelElement):
            uRIOfTheProduct = self.URIOfTheProduct(uRIOfTheProduct)

        # Build a submodel element if a raw value was passed in the argument

        if version is not None and not isinstance(version, aas.SubmodelElement):
            version = self.Version(version)

        # Build a submodel element if a raw value was passed in the argument

        if contactInformation is not None and not isinstance(contactInformation, aas.SubmodelElement):
            contactInformation = self.ContactInformation(contactInformation)

        # Build a submodel element if a raw value was passed in the argument

        if modelNameplateRef is not None and not isinstance(modelNameplateRef, aas.SubmodelElement):
            modelNameplateRef = self.ModelNameplateRef(modelNameplateRef)

        # Build a submodel element if a raw value was passed in the argument

        if riskAssessment is not None and not isinstance(riskAssessment, aas.SubmodelElement):
            riskAssessment = self.RiskAssessment(riskAssessment)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            uRIOfTheProduct,
            version,
            contactInformation,
            modelNameplateRef,
            storage,
            input,
            output,
            softwareRequirements,
            hardwareRequirements,
            performanceInformation,
            liveMonitoring,
            riskAssessment,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
