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


class AIModelNameplate(aas.Submodel):

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
                    dict_={r"de": r"Version des Nameplates", r"en": r"Version of the nameplate"}
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
                        r"en": r"Reference to the Contact Information IDTA Submodel to describe the responsible person for the Submodel"
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Contactinformation/1/0"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Storage(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"Storage",
                "value_type": str,
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Path to the model (e.g. local path, serverpath,...)"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Storage/1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class KindOfLearning(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"KindOfLearning",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"This property describes the learningmethod of the model (supervised, unsupervised, reinforcement, ....)"
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/KindOfLearning/1/0"),
            }

        def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Inputs(aas.SubmodelElementCollection):

        class KindOfInput(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"KindOfInput",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Type of data (e.g. Images, Audio)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Inputs/KindOfInput/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DimensionN(aas.SubmodelElementCollection):

            class Size(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Size",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Size of the output dimension"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/Inputs/DimensionN/Size/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Information(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Information",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Information about the usage of this dimension"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/Inputs/DimensionN/Information/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DimensionN",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection of information about a single input dimension"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Inputs/DimensionN/1/0"),
                }

            def __init__(
                self,
                size: Union[str, Size],
                information: Optional[Union[str, Information]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if size is not None and not isinstance(size, aas.SubmodelElement):
                    size = self.Size(size)

                # Build a submodel element if a raw value was passed in the argument

                if information is not None and not isinstance(information, aas.SubmodelElement):
                    information = self.Information(information)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(size, information)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Preprocessing(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"Preprocessing",
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Preprocessing pipeline as a file"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Inputs/Preprocessing/1/0"),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Inputs",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of necessary information about the model input"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Inputs/1/0"),
            }

        def __init__(
            self,
            kindOfInput: Union[str, KindOfInput],
            dimensionN: Optional[Iterable[DimensionN]] = None,
            preprocessing: Optional[Preprocessing] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if kindOfInput is not None and not isinstance(kindOfInput, aas.SubmodelElement):
                kindOfInput = self.KindOfInput(kindOfInput)

            # A str would be split into its characters
            if isinstance(dimensionN, str):
                raise TypeError("dimensionN takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(kindOfInput, dimensionN, preprocessing)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Outputs(aas.SubmodelElementCollection):

        class DimensionN(aas.SubmodelElementCollection):

            class Size(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Size",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Size of the output dimension"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/Outputs/DimensionN/Size/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Result(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Result",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Meaning of the output dimension (e.g. class)"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/Outputs/DimensionN/Result/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DimensionN",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection of information about a single output dimension"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Outputs/DimensionN/1/0"),
                }

            def __init__(
                self,
                size: Union[str, Size],
                result: Union[aas.MultiLanguageTextType, Result],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if size is not None and not isinstance(size, aas.SubmodelElement):
                    size = self.Size(size)

                # Build a submodel element if a raw value was passed in the argument

                if result is not None and not isinstance(result, aas.SubmodelElement):
                    result = self.Result(result)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(size, result)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Outputs",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of necessary information about the model output"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Outputs/1/0"),
            }

        def __init__(self, dimensionN: Iterable[DimensionN], **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # A str would be split into its characters
            if isinstance(dimensionN, str):
                raise TypeError("dimensionN takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(dimensionN)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class TrainingResults(aas.SubmodelElementCollection):

        class ExampleResult(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ExampleResult",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Result of the trained AI"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIModelNameplate/TrainingResults/Result/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"TrainingResults",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of different training results of the model"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/TrainingResults/1/0"),
            }

        def __init__(
            self,
            exampleResult: Optional[Union[str, ExampleResult]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if exampleResult is not None and not isinstance(exampleResult, aas.SubmodelElement):
                exampleResult = self.ExampleResult(exampleResult)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(exampleResult)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Plots(aas.SubmodelElementCollection):

        class TrainingTesting(aas.SubmodelElementCollection):

            class ExamplePlot(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"ExamplePlot",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Training or test result plot"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/Plots/TrainingTesting/Plot/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/jpeg", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"TrainingTesting",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection of plots about training results and test results"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIModelNameplate/Plots/TrainingTesting/1/0"
                    ),
                }

            def __init__(self, examplePlot: Iterable[ExamplePlot], **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # A str would be split into its characters
                if isinstance(examplePlot, str):
                    raise TypeError("examplePlot takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(examplePlot)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Structure(aas.SubmodelElementCollection):

            class ExampleStructurePlot(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"ExampleStructurePlot",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Image of a model architecture"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/Plots/Structure/StructurePlot/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/jpeg", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Structure",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection describing the model architecture (e.g. of a neural net)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Plots/Structure/1/0"),
                }

            def __init__(
                self,
                exampleStructurePlot: Iterable[ExampleStructurePlot],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(exampleStructurePlot, str):
                    raise TypeError("exampleStructurePlot takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(exampleStructurePlot)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class GeneralPlots(aas.SubmodelElementCollection):

            class ExamplePlot(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"ExamplePlot",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Image of an model related plot"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/Plots/GeneralPlots/Plot/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/jpeg", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"GeneralPlots",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection of plots not fitting in existing collections"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Plots/GeneralPlots/1/0"),
                }

            def __init__(self, examplePlot: Iterable[ExamplePlot], **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # A str would be split into its characters
                if isinstance(examplePlot, str):
                    raise TypeError("examplePlot takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(examplePlot)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Plots",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Collection of different plots "}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Plots/1/0"),
            }

        def __init__(
            self,
            trainingTesting: Optional[TrainingTesting] = None,
            structure: Optional[Structure] = None,
            generalPlots: Optional[GeneralPlots] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(trainingTesting, structure, generalPlots)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Details(aas.SubmodelElementCollection):

        class FileExtension(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FileExtension",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"File extension of the model (e.g. .pth)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Details/DataEnding/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AIFramework(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AIFramework",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"AI framework and its version (e.g. pytorch 11.3)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Details/AIFramework/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProgramLanguage(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProgramLanguage",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Programming language and version (e.g. python 3.9)"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIModelNameplate/Details/ProgramLanguage/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Requirements(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"Requirements",
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Requirements file containing the required software dependencies (e.g. Python Requirements.txt file)"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Details/Requirements/1/0"),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Details",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of additional details about the model"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/Details/1/0"),
            }

        def __init__(
            self,
            fileExtension: Union[str, FileExtension],
            aIFramework: Union[str, AIFramework],
            programLanguage: Union[str, ProgramLanguage],
            requirements: Optional[Requirements] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if fileExtension is not None and not isinstance(fileExtension, aas.SubmodelElement):
                fileExtension = self.FileExtension(fileExtension)

            # Build a submodel element if a raw value was passed in the argument

            if aIFramework is not None and not isinstance(aIFramework, aas.SubmodelElement):
                aIFramework = self.AIFramework(aIFramework)

            # Build a submodel element if a raw value was passed in the argument

            if programLanguage is not None and not isinstance(programLanguage, aas.SubmodelElement):
                programLanguage = self.ProgramLanguage(programLanguage)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                fileExtension, aIFramework, programLanguage, requirements
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class AIDataset(aas.SubmodelElementCollection):

        class AIDatasetReference(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"AIDatasetReference",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Reference to the used AIDataset-Submodel"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIModelNameplate/AIDataset/DatasetReference/1/0"
                    ),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TimeStamp(aas.Range):

            @staticmethod
            def template_defaults() -> RangeMetadata:
                return {
                    "id_short": r"TimeStamp",
                    "value_type": xsd.DateTime,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Determining the used data, when dataset differs over time"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/AIDataset/TimeStamp/1/0"),
                }

            def __init__(self, min: xsd.DateTime, max: xsd.DateTime, **kwargs: Unpack[RangeMetadata]):

                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AIDataset",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of additional details about the model"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIModelNameplate/AIDataset/1/0"),
            }

        def __init__(
            self,
            aIDatasetReference: Union[aas.Reference, AIDatasetReference],
            timeStamp: Optional[Union[Tuple[xsd.DateTime, xsd.DateTime], TimeStamp]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if aIDatasetReference is not None and not isinstance(aIDatasetReference, aas.SubmodelElement):
                aIDatasetReference = self.AIDatasetReference(aIDatasetReference)

            # Build a submodel element if a raw value was passed in the argument

            if timeStamp is not None and not isinstance(timeStamp, aas.SubmodelElement):
                timeStamp = self.TimeStamp(min=timeStamp[0], max=timeStamp[1])

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(aIDatasetReference, timeStamp)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class AITypeSpecificInformation(aas.SubmodelElementCollection):

        class TransferLearning(aas.SubmodelElementCollection):

            class Name(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Name",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Name of the origin neural network (e.g. resnet18)"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/NeuralNetwork/TransferLearning/Name/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TimeStamp(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TimeStamp",
                        "value_type": xsd.DateTime,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Date of access of the origin neural network"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/NeuralNetwork/TransferLearning/TimeStamp/1/0"
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Weights(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"Weights",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"File containing the weights of the origin model (e.g. .txt)"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/NeuralNetwork/TransferLearning/Weights/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class AIModelNameplate(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"AIModelNameplate",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Reference to the AI Modelnameplate submodel of the origin neural network"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/NeuralNetwork/TransferLearning/ModelnameplateRef/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"TransferLearning",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Collection containing information of the origin model, if the model is a result of transfer learning"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/TransferLearning/1/0"
                    ),
                }

            def __init__(
                self,
                name: Optional[Union[str, Name]] = None,
                timeStamp: Optional[Union[xsd.DateTime, TimeStamp]] = None,
                weights: Optional[Weights] = None,
                aIModelNameplate: Optional[Union[aas.Reference, AIModelNameplate]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if name is not None and not isinstance(name, aas.SubmodelElement):
                    name = self.Name(name)

                # Build a submodel element if a raw value was passed in the argument

                if timeStamp is not None and not isinstance(timeStamp, aas.SubmodelElement):
                    timeStamp = self.TimeStamp(timeStamp)

                # Build a submodel element if a raw value was passed in the argument

                if aIModelNameplate is not None and not isinstance(aIModelNameplate, aas.SubmodelElement):
                    aIModelNameplate = self.AIModelNameplate(aIModelNameplate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(name, timeStamp, weights, aIModelNameplate)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Hyperparameter(aas.SubmodelElementCollection):

            class Example(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Example",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Example hyperparameter (e.g. learning rate of the model)"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/Hyperparameter/LearningRate/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Hyperparameter",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection containing relevant hyperparamter"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/Hyperparameter/1/0"
                    ),
                }

            def __init__(
                self, example: Optional[Union[str, Example]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
            ):

                # Build a submodel element if a raw value was passed in the argument

                if example is not None and not isinstance(example, aas.SubmodelElement):
                    example = self.Example(example)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(example)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Type(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"Type",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Type of  the AI(e.g. CNN, RNN, LSTM, ...)"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/Type/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AITypeSpecificInformation",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection containing different kinds of AI method specific parameters"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/AIModelNameplate/AITypeSpecificInformation/1/0"
                ),
            }

        def __init__(
            self,
            type: Union[aas.MultiLanguageTextType, Type],
            transferLearning: Optional[TransferLearning] = None,
            hyperparameter: Optional[Hyperparameter] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if type is not None and not isinstance(type, aas.SubmodelElement):
                type = self.Type(type)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(transferLearning, hyperparameter, type)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"AIModelNameplate",
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/AIModelNameplate/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        uRIOfTheProduct: Union[str, URIOfTheProduct],
        version: Union[str, Version],
        contactInformation: Union[aas.Reference, ContactInformation],
        storage: Union[str, Storage],
        kindOfLearning: Union[aas.MultiLanguageTextType, KindOfLearning],
        inputs: Inputs,
        outputs: Outputs,
        trainingResults: TrainingResults,
        details: Details,
        aITypeSpecificInformation: AITypeSpecificInformation,
        plots: Optional[Plots] = None,
        aIDataset: Optional[Iterable[AIDataset]] = None,
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

        if storage is not None and not isinstance(storage, aas.SubmodelElement):
            storage = self.Storage(storage)

        # Build a submodel element if a raw value was passed in the argument

        if kindOfLearning is not None and not isinstance(kindOfLearning, aas.SubmodelElement):
            kindOfLearning = self.KindOfLearning(kindOfLearning)

        # A str would be split into its characters
        if isinstance(aIDataset, str):
            raise TypeError("aIDataset takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            uRIOfTheProduct,
            version,
            contactInformation,
            storage,
            kindOfLearning,
            inputs,
            outputs,
            trainingResults,
            plots,
            details,
            aIDataset,
            aITypeSpecificInformation,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
