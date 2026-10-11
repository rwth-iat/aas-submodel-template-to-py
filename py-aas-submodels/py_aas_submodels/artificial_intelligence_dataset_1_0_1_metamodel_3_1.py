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


class AIDataset(aas.Submodel):

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
                    dict_={r"de": r"Version des Datensatzes", r"en": r"Version of the dataset"}
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
                        r"en": r"Refernce to the Contact Information IDTA Submodel to describe the responsible person for the Submodel"
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/ContactInformation/1/0"),
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
                    dict_={r"en": r"Path to the dataset (e.g. local path, serverpath,...)"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/Storage/1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Labeled(aas.SubmodelElementCollection):

        class Classification(aas.SubmodelElementCollection):

            class NumberLables(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NumberLables",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Number of the different labels in the dataset"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Classification/NumberLabels/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Labels(aas.SubmodelElementCollection):

                class ExampleLabel(aas.SubmodelElementCollection):

                    class ClassName(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ClassName",
                                "value_type": str,
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the class"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/Label/ClassName/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class NumberOfSamples(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"NumberOfSamples",
                                "value_type": str,
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Number of occurrences of the label in the dataset"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/Label/NumberOfSamples/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ExampleLabel",
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Additional information about one label"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/Label/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        className: Union[str, ClassName],
                        numberOfSamples: Optional[Union[str, NumberOfSamples]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if className is not None and not isinstance(className, aas.SubmodelElement):
                            className = self.ClassName(className)

                        # Build a submodel element if a raw value was passed in the argument

                        if numberOfSamples is not None and not isinstance(numberOfSamples, aas.SubmodelElement):
                            numberOfSamples = self.NumberOfSamples(numberOfSamples)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(className, numberOfSamples)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Labels",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Every label as a property and the number of samples"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/1/0"
                        ),
                    }

                def __init__(
                    self, exampleLabel: Iterable[ExampleLabel], **kwargs: Unpack[SubmodelElementCollectionMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(exampleLabel, str):
                        raise TypeError("exampleLabel takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(exampleLabel)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SingleFiles(aas.SubmodelElementCollection):

                class ExampleSingleFile(aas.SubmodelElementCollection):

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Name",
                                "value_type": str,
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the file"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Name/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Labels(aas.SubmodelElementCollection):

                        class NumberLabels(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"NumberLabels",
                                    "value_type": str,
                                    "category": r"PARAMETER",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Number of labels in this dataset element"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Labels/NumberLabels/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Label(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Label",
                                    "value_type": str,
                                    "category": r"PARAMETER",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Example label, this property should be existing for every label with the labelname as value"
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Labels/Label/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"Labels",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Collection containing all the labels within the dataset element"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Labels/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            numberLabels: Union[str, NumberLabels],
                            label: Optional[Iterable[Union[str, Label]]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if numberLabels is not None and not isinstance(numberLabels, aas.SubmodelElement):
                                numberLabels = self.NumberLabels(numberLabels)

                            # A str would be split into its characters
                            if isinstance(label, str):
                                raise TypeError("label takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if label:
                                label = [i if isinstance(i, aas.SubmodelElement) else self.Label(i) for i in label]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(numberLabels, label)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class SingleFilePath(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SingleFilePath",
                                "value_type": str,
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Path to the dataset element"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/SingleFilePath/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class AnnotationFile(aas.File):

                        @staticmethod
                        def template_defaults() -> FileMetadata:
                            return {
                                "id_short": r"AnnotationFile",
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Annotation file with labeling information about the dataset element"
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/AnnotationFile/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            value: str,
                            content_type: Optional[str] = r"application/json",
                            **kwargs: Unpack[FileMetadata],
                        ):

                            super().__init__(
                                value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                            )

                    class SingleFileDetails(aas.SubmodelElementCollection):

                        class ExampleSingleFileDetail(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ExampleSingleFileDetail",
                                    "value_type": str,
                                    "category": r"PARAMETER",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"additional information about the dataset element"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/SingleFileDetails/SingleFileDetail/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"SingleFileDetails",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Collection to add addtional information about the dataset element (e.g. speaker information for audio data)"
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/SingleFileDetails/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            exampleSingleFileDetail: Union[str, ExampleSingleFileDetail],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if exampleSingleFileDetail is not None and not isinstance(
                                exampleSingleFileDetail, aas.SubmodelElement
                            ):
                                exampleSingleFileDetail = self.ExampleSingleFileDetail(exampleSingleFileDetail)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(exampleSingleFileDetail)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ExampleSingleFile",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Collection for features and the annotatin file for a single dataset element"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        name: Union[str, Name],
                        labels: Labels,
                        singleFilePath: Union[str, SingleFilePath],
                        annotationFile: Optional[AnnotationFile] = None,
                        singleFileDetails: Optional[SingleFileDetails] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if singleFilePath is not None and not isinstance(singleFilePath, aas.SubmodelElement):
                            singleFilePath = self.SingleFilePath(singleFilePath)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            name, labels, singleFilePath, annotationFile, singleFileDetails
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"SingleFiles",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection containing every dataset element individuallly"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/1/0"
                        ),
                    }

                def __init__(
                    self,
                    exampleSingleFile: Iterable[ExampleSingleFile],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(exampleSingleFile, str):
                        raise TypeError("exampleSingleFile takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(exampleSingleFile)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Balance(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Balance",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Balance between the classes"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Balance/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AnnotationFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"AnnotationFile",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Annotation file of the dataset (e.g. CSV,JSON,Path...)"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Classification/AnnotationFile/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Classification",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about labeled data for classification"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/Labeled/Classification/1/0"),
                }

            def __init__(
                self,
                numberLables: Union[str, NumberLables],
                labels: Optional[Labels] = None,
                singleFiles: Optional[SingleFiles] = None,
                balance: Optional[Union[str, Balance]] = None,
                annotationFile: Optional[AnnotationFile] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if numberLables is not None and not isinstance(numberLables, aas.SubmodelElement):
                    numberLables = self.NumberLables(numberLables)

                # Build a submodel element if a raw value was passed in the argument

                if balance is not None and not isinstance(balance, aas.SubmodelElement):
                    balance = self.Balance(balance)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    numberLables, labels, singleFiles, balance, annotationFile
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Regression(aas.SubmodelElementCollection):

            class Labeledescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"labeledescription",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"The meaning of the label"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Regression/labeledescription/1/0"
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AnnotationFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"AnnotationFile",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Annotation file of the labeled data"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Regression/AnnotationFile/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class SingleFiles(aas.SubmodelElementCollection):

                class ExampleAnnotation(aas.SubmodelElementCollection):

                    class AnnotationFile(aas.File):

                        @staticmethod
                        def template_defaults() -> FileMetadata:
                            return {
                                "id_short": r"AnnotationFile",
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Annotation file with labeling information about the dataset element"
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/AnnotationFile/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            value: str,
                            content_type: Optional[str] = r"text/plain",
                            **kwargs: Unpack[FileMetadata],
                        ):

                            super().__init__(
                                value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                            )

                    class SingleFileDetails(aas.SubmodelElementCollection):

                        class ExampleDetails(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ExampleDetails",
                                    "value_type": str,
                                    "category": r"PARAMETER",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"This is a property for a specific metainformation for single regressionfiles"
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/SingleFileDetails/Detail/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"SingleFileDetails",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Collection to add addtional information about the dataset element"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/SingleFileDetails/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            exampleDetails: Optional[Iterable[Union[str, ExampleDetails]]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(exampleDetails, str):
                                raise TypeError("exampleDetails takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if exampleDetails:
                                exampleDetails = [
                                    i if isinstance(i, aas.SubmodelElement) else self.ExampleDetails(i)
                                    for i in exampleDetails
                                ]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(exampleDetails)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ExampleAnnotation",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Collection for a single annotation of a dataset element"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        annotationFile: Optional[AnnotationFile] = None,
                        singleFileDetails: Optional[SingleFileDetails] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(annotationFile, singleFileDetails)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"SingleFiles",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection containing every dataset element individually"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/1/0"
                        ),
                    }

                def __init__(
                    self,
                    exampleAnnotation: Iterable[ExampleAnnotation],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(exampleAnnotation, str):
                        raise TypeError("exampleAnnotation takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(exampleAnnotation)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Regression",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about labeled data for regression"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/Labeled/Regression/1/0"),
                }

            def __init__(
                self,
                labeledescription: Union[aas.LangStringSet, Labeledescription],
                annotationFile: Optional[AnnotationFile] = None,
                singleFiles: Optional[SingleFiles] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if labeledescription is not None and not isinstance(labeledescription, aas.SubmodelElement):
                    labeledescription = self.Labeledescription(labeledescription)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(labeledescription, annotationFile, singleFiles)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Labeled",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Additional Information typical for labeled datasets"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/labeled/1/0"),
            }

        def __init__(
            self,
            classification: Optional[Iterable[Classification]] = None,
            regression: Optional[Iterable[Regression]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(classification, str):
                raise TypeError("classification takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(regression, str):
                raise TypeError("regression takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(classification, regression)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SizeInformation(aas.SubmodelElementCollection):

        class CompleteSize(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CompleteSize",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Number of all samples in the dataset"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDataset//SizeInformation/CompleteSize/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TrainSize(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TrainSize",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Number of all dataset elements in the training subset"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/SizeInformation/TrainSize/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ValSize(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ValSize",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Number of all dataset elements in the validation subset"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/SizeInformationValSize/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TestSize(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TestSize",
                    "value_type": str,
                    "category": r"VARIABLE",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Number of all dataset elements in the test subset"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/SizeInformation/TestSize/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SplitRatio(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SplitRatio",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Splitratio between the sets, notate as value1:value2:value3 if all three exist, else value1:value2"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/SizeInformation/SplitRatio/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SizeInformation",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection about the number of dataset elements in the dataset and subsets"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/SizeInformation/1/0"),
            }

        def __init__(
            self,
            completeSize: Union[str, CompleteSize],
            trainSize: Optional[Union[str, TrainSize]] = None,
            valSize: Optional[Union[str, ValSize]] = None,
            testSize: Optional[Union[str, TestSize]] = None,
            splitRatio: Optional[Union[str, SplitRatio]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if completeSize is not None and not isinstance(completeSize, aas.SubmodelElement):
                completeSize = self.CompleteSize(completeSize)

            # Build a submodel element if a raw value was passed in the argument

            if trainSize is not None and not isinstance(trainSize, aas.SubmodelElement):
                trainSize = self.TrainSize(trainSize)

            # Build a submodel element if a raw value was passed in the argument

            if valSize is not None and not isinstance(valSize, aas.SubmodelElement):
                valSize = self.ValSize(valSize)

            # Build a submodel element if a raw value was passed in the argument

            if testSize is not None and not isinstance(testSize, aas.SubmodelElement):
                testSize = self.TestSize(testSize)

            # Build a submodel element if a raw value was passed in the argument

            if splitRatio is not None and not isinstance(splitRatio, aas.SubmodelElement):
                splitRatio = self.SplitRatio(splitRatio)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                completeSize, trainSize, valSize, testSize, splitRatio
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MetaData(aas.SubmodelElementCollection):

        class FileType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FileType",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Data type of the dataset elements (e.g. .WAV, .JPEG, ... )"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/MetaData/FileType/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AdditionalInformation(aas.SubmodelElementCollection):

            class ExampleInfo(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExampleInfo",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Meta data information of the dataset"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/MetaData/AdditionalInformation/Info/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"AdditionalInformation",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection of additional meta information of the dataset"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDataset/MetaData/AdditionalInformation/1/0"
                    ),
                }

            def __init__(
                self,
                exampleInfo: Iterable[Union[str, ExampleInfo]],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(exampleInfo, str):
                    raise TypeError("exampleInfo takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if exampleInfo:
                    exampleInfo = [
                        i if isinstance(i, aas.SubmodelElement) else self.ExampleInfo(i) for i in exampleInfo
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(exampleInfo)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MetaData",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of meta data information about the dataset"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/MetaData/1/0"),
            }

        def __init__(
            self,
            fileType: Iterable[Union[str, FileType]],
            additionalInformation: Optional[AdditionalInformation] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(fileType, str):
                raise TypeError("fileType takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if fileType:
                fileType = [i if isinstance(i, aas.SubmodelElement) else self.FileType(i) for i in fileType]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(fileType, additionalInformation)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Metrics(aas.SubmodelElementCollection):

        class ExampleMetric(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ExampleMetric",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"metric of the dataset"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/MetaData/Metrics/Metric/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Metrics",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Collection of different metrics"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/Metrics/1/0"),
            }

        def __init__(
            self,
            exampleMetric: Optional[Union[str, ExampleMetric]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if exampleMetric is not None and not isinstance(exampleMetric, aas.SubmodelElement):
                exampleMetric = self.ExampleMetric(exampleMetric)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(exampleMetric)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class BoundaryConditions(aas.SubmodelElementCollection):

        class DataCollectors(aas.SubmodelElementCollection):

            class Collector(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"Collector",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Reference to the data collector"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/DataCollectors/CollectorDescription/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DataCollectors",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about the datacollector (e.g. a sensor)."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/DataCollectors/1/0"
                    ),
                }

            def __init__(
                self,
                collector: Optional[Iterable[Union[aas.Reference, Collector]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(collector, str):
                    raise TypeError("collector takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if collector:
                    collector = [i if isinstance(i, aas.SubmodelElement) else self.Collector(i) for i in collector]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(collector)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class EnviromentConditions(aas.SubmodelElementCollection):

            class ExampleCondition(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExampleCondition",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Condition about the enviroment"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/EnviromentConditions/Condition/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"EnviromentConditions",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection about environmental conditions the dataset was created with"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/EnviromentConditions/1/0"
                    ),
                }

            def __init__(
                self,
                exampleCondition: Optional[Union[str, ExampleCondition]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if exampleCondition is not None and not isinstance(exampleCondition, aas.SubmodelElement):
                    exampleCondition = self.ExampleCondition(exampleCondition)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(exampleCondition)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class SyntheticData(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"SyntheticData",
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Information, if the dataset is synthetic, real or mixed"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/SyntheticData/1/0"
                    ),
                }

            def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"BoundaryConditions",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Boundary conditions in which the dataset was created"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/1/0"),
            }

        def __init__(
            self,
            dataCollectors: Optional[DataCollectors] = None,
            enviromentConditions: Optional[EnviromentConditions] = None,
            syntheticData: Optional[Union[aas.LangStringSet, SyntheticData]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if syntheticData is not None and not isinstance(syntheticData, aas.SubmodelElement):
                syntheticData = self.SyntheticData(syntheticData)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(dataCollectors, enviromentConditions, syntheticData)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"AIDataset",
            "description": aas.MultiLanguageTextType(dict_={r"en": r"Categories and Information of the aidataset@en "}),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/SubmodelTemplate/AIDataset/1/0"),
        }

    def __init__(
        self,
        id_: str,
        uRIOfTheProduct: Union[str, URIOfTheProduct],
        version: Union[str, Version],
        contactInformation: Union[aas.Reference, ContactInformation],
        storage: Union[str, Storage],
        sizeInformation: SizeInformation,
        metaData: MetaData,
        labeled: Optional[Labeled] = None,
        metrics: Optional[Metrics] = None,
        boundaryConditions: Optional[BoundaryConditions] = None,
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

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            uRIOfTheProduct,
            version,
            contactInformation,
            storage,
            labeled,
            sizeInformation,
            metaData,
            metrics,
            boundaryConditions,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
