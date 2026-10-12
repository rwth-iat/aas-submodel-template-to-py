from typing import Any, Iterable, Optional, Tuple, TypedDict, Union, Unpack, cast
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


class SubmodelElementListMetadata(TypedDict, total=False):
    """Metadata of aas.SubmodelElementList, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    type_value_list_element: type[aas.SubmodelElement]
    semantic_id_list_element: Optional[aas.Reference]
    value_type_list_element: Optional[aas.DataTypeDefXsd]
    order_relevant: bool
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


class DigitalQualityDocuments(aas.Submodel):

    class DocumentIds(GeneratedSubmodelElementList):

        class Documentids_item(aas.SubmodelElementCollection):

            class DocumentDomainId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentDomainId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Domain Id"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Identification of the domain in which the given DocumentId is unique. The domain ID can, e.g., be the name or acronym of the providing organisation"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABH994#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH994-003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentIdentifier(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentIdentifier",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Identifier"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Alphanumeric character sequence uniquely identifying a document"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAO099#004"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO099-004"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentIsPrimary(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentIsPrimary",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Is Primary"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Flag indicating whether a DocumentId within a collection of at least two DocumentIds is the ‘primary’ identifier for the document. This is the preferred ID of the document (commonly from the point of view of the owner of the asset)"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABH995#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH995-003"),),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Id"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about a document identification entity"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI501#003/0173-1#01-AHF580#003"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI501-003"),),
                }

            def __init__(
                self,
                documentDomainId: Union[str, DocumentDomainId],
                documentIdentifier: Union[str, DocumentIdentifier],
                documentIsPrimary: Optional[Union[bool, DocumentIsPrimary]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if documentDomainId is not None and not isinstance(documentDomainId, aas.SubmodelElement):
                    documentDomainId = self.DocumentDomainId(documentDomainId)

                # Build a submodel element if a raw value was passed in the argument

                if documentIdentifier is not None and not isinstance(documentIdentifier, aas.SubmodelElement):
                    documentIdentifier = self.DocumentIdentifier(documentIdentifier)

                # Build a submodel element if a raw value was passed in the argument

                if documentIsPrimary is not None and not isinstance(documentIsPrimary, aas.SubmodelElement):
                    documentIsPrimary = self.DocumentIsPrimary(documentIsPrimary)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    documentDomainId, documentIdentifier, documentIsPrimary
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"DocumentIds",
                "type_value_list_element": aas.SubmodelElementCollection,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Ids"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Set of document identifiers for the document. One ID in this collection should be used as a preferred ID"
                    }
                ),
                "semantic_id": global_ref(r"0173-1#02-ABI501#003"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI501-003"),),
            }

        def __init__(
            self, documentids_items: Iterable[Documentids_item], **kwargs: Unpack[SubmodelElementListMetadata]
        ):

            # A str would be split into its characters
            if isinstance(documentids_items, str):
                raise TypeError("documentids_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(documentids_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DocumentClassifications(GeneratedSubmodelElementList):

        class Documentclassifications_item(aas.SubmodelElementCollection):

            class ClassId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ClassId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Class Id"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Unique ID of the document class within a classficationsystem"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABH996#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH996-003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ClassName(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ClassName",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Class Name"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Name of the class in the classification system"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABJ219#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABJ219-002"),),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ClassificationSystem(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ClassificationSystem",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Classification System"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identification of the classification system "}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABH997#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH997-003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Classification"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Set of information for describing the classification of the Document according to a ClassificationSystem"
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI502#003/0173-1#01-AHF581#003"),
                }

            def __init__(
                self,
                classId: Union[str, ClassId],
                className: Union[aas.MultiLanguageTextType, ClassName],
                classificationSystem: Union[str, ClassificationSystem],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if classId is not None and not isinstance(classId, aas.SubmodelElement):
                    classId = self.ClassId(classId)

                # Build a submodel element if a raw value was passed in the argument

                if className is not None and not isinstance(className, aas.SubmodelElement):
                    className = self.ClassName(className)

                # Build a submodel element if a raw value was passed in the argument

                if classificationSystem is not None and not isinstance(classificationSystem, aas.SubmodelElement):
                    classificationSystem = self.ClassificationSystem(classificationSystem)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(classId, className, classificationSystem)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"DocumentClassifications",
                "type_value_list_element": aas.SubmodelElementCollection,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Classifications"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Set of information for describing the classification of the Document according to ClassificationSystems"
                    }
                ),
                "semantic_id": global_ref(r"0173-1#02-ABI502#003"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI502-003"),),
            }

        def __init__(
            self,
            documentclassifications_items: Iterable[Documentclassifications_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(documentclassifications_items, str):
                raise TypeError("documentclassifications_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(documentclassifications_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DocumentInstances(GeneratedSubmodelElementList):

        class Documentinstances_item(aas.SubmodelElementCollection):

            class Language(GeneratedSubmodelElementList):

                class Language_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Language"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Language of the document"}),
                            "semantic_id": global_ref(r"0173-1#02-AAN468#008"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"Language",
                        "type_value_list_element": aas.Property,
                        "value_type_list_element": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Language"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Language of the document instance."}),
                        "semantic_id": global_ref(r" 0173-1#02-AAN468#008"),
                    }

                def __init__(
                    self,
                    language_items: Iterable[Union[str, Language_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(language_items, str):
                        raise TypeError("language_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if language_items:
                        language_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Language_item(i) for i in language_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(language_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Version(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Version",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Version"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Version of the document"}),
                        "semantic_id": global_ref(r"0173-1#02-AAP003#005"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAP003-005"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Title"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the document"}),
                        "semantic_id": global_ref(r"0173-1#02-ABG940#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABG940-003"),),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Description"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Plain text characterizing the content of the document, e.g., the context of the quality document and its conformity statement."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAN466#004"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAN466-004"),),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusSetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusSetDate",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Status Set Date"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Date when the document status was set. Usually, the date when the quality document was issued"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI000#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI000-003"),),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Status Value"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Each document instance represents a point in time in the asset life cycle. This status value refers to the milestones in the asset life cycle. "
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI001#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI001-003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationShortName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationShortName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Organization Short Name"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Short name of the organization that issued the quality document instance"}
                        ),
                        "semantic_id": global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI002-003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Organization Official Name"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Official name of the organization that issued the document"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI004#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI004-003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RefersToEntities(GeneratedSubmodelElementList):

                class Referstoentities_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Refers To Entity"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Forms a generic refers to-relationship to another document or document instance"
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABK288#002"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"RefersToEntities",
                        "type_value_list_element": aas.ReferenceElement,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Refers To Entities"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Forms a generic refers to-relationship to another document or document instance. "
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABK288#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK288-002"),),
                    }

                def __init__(
                    self,
                    referstoentities_items: Iterable[Union[aas.Reference, Referstoentities_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(referstoentities_items, str):
                        raise TypeError("referstoentities_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if referstoentities_items:
                        referstoentities_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Referstoentities_item(i)
                            for i in referstoentities_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        referstoentities_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class BasedOnReferences(GeneratedSubmodelElementList):

                class Basedonreferences_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Based On Reference"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"BasedOnReference"}),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"BasedOnReferences",
                        "type_value_list_element": aas.ReferenceElement,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Based On References"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Forms a based on-relationship to another document or document instance"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABK289#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK289-002"),),
                    }

                def __init__(
                    self,
                    basedonreferences_items: Iterable[Union[aas.Reference, Basedonreferences_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(basedonreferences_items, str):
                        raise TypeError("basedonreferences_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if basedonreferences_items:
                        basedonreferences_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Basedonreferences_item(i)
                            for i in basedonreferences_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        basedonreferences_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class DigitalFiles(GeneratedSubmodelElementList):

                class Digitalfiles_item(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Digital File"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"MIME-Type, file name and file contents given by the file"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABK126#002"),
                        }

                    def __init__(
                        self, value: str, content_type: Optional[str] = r"text/xml", **kwargs: Unpack[FileMetadata]
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"DigitalFiles",
                        "type_value_list_element": aas.File,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Digital Files"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"MIME-Type, file name and file contents given by the file SubmodelElement. This holds the actual quality document, e.g., the DCC XML file."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABK126#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK126-002"),),
                    }

                def __init__(
                    self, digitalfiles_items: Iterable[Digitalfiles_item], **kwargs: Unpack[SubmodelElementListMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(digitalfiles_items, str):
                        raise TypeError("digitalfiles_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(digitalfiles_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class PreviewFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"PreviewFile",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Preview File"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Provides a preview of the Document Instance, e.g., the human-readable PDF version of the XML file"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABK127#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK127-002"),),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class AdministrativeData(aas.SubmodelElementCollection):

                class CoreData(aas.SubmodelElementCollection):

                    class UniqueIdentifier(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"UniqueIdentifier",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unique Identifier"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"A worldwide unique identifier for the DQD (e.g., calibration certificate number) "
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABI501#001/0173-1#01-AHF580#001*01"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Identifications(GeneratedSubmodelElementList):

                        class Identifications_item(aas.SubmodelElementCollection):

                            class IdentificationName(aas.MultiLanguageProperty):

                                @staticmethod
                                def template_defaults() -> MultiLanguagePropertyMetadata:
                                    return {
                                        "id_short": r"IdentificationName",
                                        "display_name": aas.MultiLanguageNameType(
                                            dict_={r"en": r"Identification Name"}
                                        ),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={r"en": r"Name of the identification"}
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    value: aas.MultiLanguageTextType,
                                    **kwargs: Unpack[MultiLanguagePropertyMetadata],
                                ):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class IdentificationIssuer(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"IdentificationIssuer",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(
                                            dict_={r"en": r"Identification Issuer"}
                                        ),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class IdentificationValue(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"IdentificationValue",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(
                                            dict_={r"en": r"Identification Value"}
                                        ),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class ID(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"ID",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"ID"}),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Attribute for which the value is unique within the quality document"
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class RefID(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"RefID",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ref ID"}),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={r"en": r"Reference to an existing ID within the quality document"}
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class RefType(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"RefType",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ref Type"}),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": None,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Identification"}),
                                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Identification"}),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification"
                                    ),
                                }

                            def __init__(
                                self,
                                identificationName: Optional[
                                    Union[aas.MultiLanguageTextType, IdentificationName]
                                ] = None,
                                identificationIssuer: Optional[Union[str, IdentificationIssuer]] = None,
                                identificationValue: Optional[Union[str, IdentificationValue]] = None,
                                iD: Optional[Union[str, ID]] = None,
                                refID: Optional[Iterable[Union[str, RefID]]] = None,
                                refType: Optional[Union[str, RefType]] = None,
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationName is not None and not isinstance(
                                    identificationName, aas.SubmodelElement
                                ):
                                    identificationName = self.IdentificationName(identificationName)

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationIssuer is not None and not isinstance(
                                    identificationIssuer, aas.SubmodelElement
                                ):
                                    identificationIssuer = self.IdentificationIssuer(identificationIssuer)

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationValue is not None and not isinstance(
                                    identificationValue, aas.SubmodelElement
                                ):
                                    identificationValue = self.IdentificationValue(identificationValue)

                                # Build a submodel element if a raw value was passed in the argument

                                if iD is not None and not isinstance(iD, aas.SubmodelElement):
                                    iD = self.ID(iD)

                                # A str would be split into its characters
                                if isinstance(refID, str):
                                    raise TypeError("refID takes several elements, got a str")

                                # Build submodel elements from raw values passed in the argument
                                if refID:
                                    refID = [i if isinstance(i, aas.SubmodelElement) else self.RefID(i) for i in refID]

                                # Build a submodel element if a raw value was passed in the argument

                                if refType is not None and not isinstance(refType, aas.SubmodelElement):
                                    refType = self.RefType(refType)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    identificationName, identificationIssuer, identificationValue, iD, refID, refType
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"Identifications",
                                "type_value_list_element": aas.SubmodelElementCollection,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Identifications"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Identifications contains identifiers which exactly describe the content of the parent element"
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications"
                                ),
                            }

                        def __init__(
                            self,
                            identifications_items: Iterable[Identifications_item],
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(identifications_items, str):
                                raise TypeError("identifications_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                identifications_items, number_repeated=False
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class IssueDate(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"IssueDate",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Issue Date"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Date when the document has been officially issued"}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABI000#001"),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"CoreData",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Core Data"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Contains essential administrative information for the quality document"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData"
                            ),
                        }

                    def __init__(
                        self,
                        uniqueIdentifier: Union[str, UniqueIdentifier],
                        identifications: Optional[
                            Union[Iterable[Identifications.Identifications_item], Identifications]
                        ] = None,
                        issueDate: Optional[Union[xsd.DateTime, IssueDate]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if uniqueIdentifier is not None and not isinstance(uniqueIdentifier, aas.SubmodelElement):
                            uniqueIdentifier = self.UniqueIdentifier(uniqueIdentifier)

                        # A str would be split into its characters
                        if isinstance(identifications, str):
                            raise TypeError("identifications takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if identifications is not None and not isinstance(identifications, aas.SubmodelElement):
                            identifications = self.Identifications(identifications)

                        # Build a submodel element if a raw value was passed in the argument

                        if issueDate is not None and not isinstance(issueDate, aas.SubmodelElement):
                            issueDate = self.IssueDate(issueDate)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            uniqueIdentifier, identifications, issueDate
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Items(aas.SubmodelElementCollection):

                    class Identifications(GeneratedSubmodelElementList):

                        class Identifications_item(aas.SubmodelElementCollection):

                            class IdentificationName(aas.MultiLanguageProperty):

                                @staticmethod
                                def template_defaults() -> MultiLanguagePropertyMetadata:
                                    return {
                                        "id_short": r"IdentificationName",
                                        "display_name": aas.MultiLanguageNameType(
                                            dict_={r"en": r"Identification Name"}
                                        ),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={r"en": r"Name of the identification"}
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    value: aas.MultiLanguageTextType,
                                    **kwargs: Unpack[MultiLanguagePropertyMetadata],
                                ):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class IdentificationIssuer(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"IdentificationIssuer",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(
                                            dict_={r"en": r"Identification Issuer"}
                                        ),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class IdentificationValue(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"IdentificationValue",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(
                                            dict_={r"en": r"Identification Value"}
                                        ),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class ID(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"ID",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"ID"}),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Attribute for which the value is unique within the quality document"
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class RefID(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"RefID",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ref ID"}),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={r"en": r"Reference to an existing ID within the quality document"}
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class RefType(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"RefType",
                                        "value_type": str,
                                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ref Type"}),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": None,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Identification"}),
                                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Identification"}),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification"
                                    ),
                                }

                            def __init__(
                                self,
                                identificationName: Optional[
                                    Union[aas.MultiLanguageTextType, IdentificationName]
                                ] = None,
                                identificationIssuer: Optional[Union[str, IdentificationIssuer]] = None,
                                identificationValue: Optional[Union[str, IdentificationValue]] = None,
                                iD: Optional[Union[str, ID]] = None,
                                refID: Optional[Iterable[Union[str, RefID]]] = None,
                                refType: Optional[Union[str, RefType]] = None,
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationName is not None and not isinstance(
                                    identificationName, aas.SubmodelElement
                                ):
                                    identificationName = self.IdentificationName(identificationName)

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationIssuer is not None and not isinstance(
                                    identificationIssuer, aas.SubmodelElement
                                ):
                                    identificationIssuer = self.IdentificationIssuer(identificationIssuer)

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationValue is not None and not isinstance(
                                    identificationValue, aas.SubmodelElement
                                ):
                                    identificationValue = self.IdentificationValue(identificationValue)

                                # Build a submodel element if a raw value was passed in the argument

                                if iD is not None and not isinstance(iD, aas.SubmodelElement):
                                    iD = self.ID(iD)

                                # A str would be split into its characters
                                if isinstance(refID, str):
                                    raise TypeError("refID takes several elements, got a str")

                                # Build submodel elements from raw values passed in the argument
                                if refID:
                                    refID = [i if isinstance(i, aas.SubmodelElement) else self.RefID(i) for i in refID]

                                # Build a submodel element if a raw value was passed in the argument

                                if refType is not None and not isinstance(refType, aas.SubmodelElement):
                                    refType = self.RefType(refType)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    identificationName, identificationIssuer, identificationValue, iD, refID, refType
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"Identifications",
                                "type_value_list_element": aas.SubmodelElementCollection,
                                "value_type_list_element": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Identifications"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Identifications contains identifiers which exactly describe the content of the parent element."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification"
                                ),
                            }

                        def __init__(
                            self,
                            identifications_items: Iterable[Identifications_item],
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(identifications_items, str):
                                raise TypeError("identifications_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                identifications_items, number_repeated=False
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class Item(GeneratedSubmodelElementList):

                        class Item_item(aas.SubmodelElementCollection):

                            class Identifications(GeneratedSubmodelElementList):

                                class Identifications_item(aas.SubmodelElementCollection):

                                    class IdentificationName(aas.MultiLanguageProperty):

                                        @staticmethod
                                        def template_defaults() -> MultiLanguagePropertyMetadata:
                                            return {
                                                "id_short": r"IdentificationName",
                                                "display_name": aas.MultiLanguageNameType(
                                                    dict_={r"en": r"Identification Name"}
                                                ),
                                                "description": aas.MultiLanguageTextType(
                                                    dict_={r"en": r"Name of the identification"}
                                                ),
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName"
                                                ),
                                            }

                                        def __init__(
                                            self,
                                            value: aas.MultiLanguageTextType,
                                            **kwargs: Unpack[MultiLanguagePropertyMetadata],
                                        ):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class IdentificationIssuer(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"IdentificationIssuer",
                                                "value_type": str,
                                                "display_name": aas.MultiLanguageNameType(
                                                    dict_={r"en": r"Identification Issuer"}
                                                ),
                                                "description": aas.MultiLanguageTextType(
                                                    dict_={
                                                        r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                                    }
                                                ),
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class IdentificationValue(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"IdentificationValue",
                                                "value_type": str,
                                                "display_name": aas.MultiLanguageNameType(
                                                    dict_={r"en": r"Identification Value"}
                                                ),
                                                "description": aas.MultiLanguageTextType(
                                                    dict_={
                                                        r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                                    }
                                                ),
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class ID(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"ID",
                                                "value_type": str,
                                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"ID"}),
                                                "description": aas.MultiLanguageTextType(
                                                    dict_={
                                                        r"en": r"Attribute for which the value is unique within the quality document"
                                                    }
                                                ),
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class RefID(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"RefID",
                                                "value_type": str,
                                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ref ID"}),
                                                "description": aas.MultiLanguageTextType(
                                                    dict_={
                                                        r"en": r"Reference to an existing ID within the quality document"
                                                    }
                                                ),
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class RefType(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"RefType",
                                                "value_type": str,
                                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ref Type"}),
                                                "description": aas.MultiLanguageTextType(
                                                    dict_={
                                                        r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                                    }
                                                ),
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    @staticmethod
                                    def template_defaults() -> SubmodelElementCollectionMetadata:
                                        return {
                                            "id_short": None,
                                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Identification"}),
                                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Identification"}),
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification"
                                            ),
                                        }

                                    def __init__(
                                        self,
                                        identificationName: Optional[
                                            Union[aas.MultiLanguageTextType, IdentificationName]
                                        ] = None,
                                        identificationIssuer: Optional[Union[str, IdentificationIssuer]] = None,
                                        identificationValue: Optional[Union[str, IdentificationValue]] = None,
                                        iD: Optional[Union[str, ID]] = None,
                                        refID: Optional[Iterable[Union[str, RefID]]] = None,
                                        refType: Optional[Union[str, RefType]] = None,
                                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                    ):

                                        # Build a submodel element if a raw value was passed in the argument

                                        if identificationName is not None and not isinstance(
                                            identificationName, aas.SubmodelElement
                                        ):
                                            identificationName = self.IdentificationName(identificationName)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if identificationIssuer is not None and not isinstance(
                                            identificationIssuer, aas.SubmodelElement
                                        ):
                                            identificationIssuer = self.IdentificationIssuer(identificationIssuer)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if identificationValue is not None and not isinstance(
                                            identificationValue, aas.SubmodelElement
                                        ):
                                            identificationValue = self.IdentificationValue(identificationValue)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if iD is not None and not isinstance(iD, aas.SubmodelElement):
                                            iD = self.ID(iD)

                                        # A str would be split into its characters
                                        if isinstance(refID, str):
                                            raise TypeError("refID takes several elements, got a str")

                                        # Build submodel elements from raw values passed in the argument
                                        if refID:
                                            refID = [
                                                i if isinstance(i, aas.SubmodelElement) else self.RefID(i)
                                                for i in refID
                                            ]

                                        # Build a submodel element if a raw value was passed in the argument

                                        if refType is not None and not isinstance(refType, aas.SubmodelElement):
                                            refType = self.RefType(refType)

                                        # Add all passed/initialized submodel elements to a single list

                                        embedded_submodel_elements = collect_submodel_elements(
                                            identificationName,
                                            identificationIssuer,
                                            identificationValue,
                                            iD,
                                            refID,
                                            refType,
                                        )

                                        super().__init__(
                                            value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                        )

                                @staticmethod
                                def template_defaults() -> SubmodelElementListMetadata:
                                    return {
                                        "id_short": r"Identifications",
                                        "type_value_list_element": aas.SubmodelElementCollection,
                                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Identifications"}),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Identifications contains identifiers which exactly describe the content of the parent element."
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    identifications_items: Iterable[Identifications_item],
                                    **kwargs: Unpack[SubmodelElementListMetadata],
                                ):

                                    # A str would be split into its characters
                                    if isinstance(identifications_items, str):
                                        raise TypeError("identifications_items takes several elements, got a str")

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        identifications_items, number_repeated=False
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": None,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Item"}),
                                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Item"}),
                                    "semantic_id": global_ref(r"https://dccwiki.ptb.de/en/dccitems"),
                                }

                            def __init__(
                                self,
                                identifications: Union[Iterable[Identifications.Identifications_item], Identifications],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(identifications, str):
                                    raise TypeError("identifications takes several elements, got a str")

                                # Build a submodel element if a raw value was passed in the argument

                                if identifications is not None and not isinstance(identifications, aas.SubmodelElement):
                                    identifications = self.Identifications(identifications)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(identifications)

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"Item",
                                "type_value_list_element": aas.SubmodelElementCollection,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Item"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Item of calibration, conformity assessment or other"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Items"
                                ),
                            }

                        def __init__(
                            self, item_items: Iterable[Item_item], **kwargs: Unpack[SubmodelElementListMetadata]
                        ):

                            # A str would be split into its characters
                            if isinstance(item_items, str):
                                raise TypeError("item_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(item_items, number_repeated=False)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Items",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Items"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Contains unique identification, description and if applicable, conditions of the item"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/items"
                            ),
                        }

                    def __init__(
                        self,
                        identifications: Union[Iterable[Identifications.Identifications_item], Identifications],
                        item: Union[Iterable[Item.Item_item], Item],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(identifications, str):
                            raise TypeError("identifications takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if identifications is not None and not isinstance(identifications, aas.SubmodelElement):
                            identifications = self.Identifications(identifications)

                        # A str would be split into its characters
                        if isinstance(item, str):
                            raise TypeError("item takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if item is not None and not isinstance(item, aas.SubmodelElement):
                            item = self.Item(item)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(identifications, item)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Statements(GeneratedSubmodelElementList):

                    class Statements_item(aas.SubmodelElementCollection):

                        class DateOfStatement(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"DateOfStatement",
                                    "value_type": xsd.DateTime,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Date Of Statement"}),
                                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Date of statement"}),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statements/Date"
                                    ),
                                }

                            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class StatementReference(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"StatementReference",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Statement Reference"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Normative or other reference in accordance which the statement is made"
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statement/StatementReference"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Declaration(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {
                                    "id_short": r"Declaration",
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Declaration"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Additional information providing context for the statement"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statement/Declaration"
                                    ),
                                }

                            def __init__(
                                self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Statement"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"statement records regarding the quality assessment"}
                                ),
                            }

                        def __init__(
                            self,
                            dateOfStatement: Optional[Union[xsd.DateTime, DateOfStatement]] = None,
                            statementReference: Optional[Union[str, StatementReference]] = None,
                            declaration: Optional[Union[aas.MultiLanguageTextType, Declaration]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if dateOfStatement is not None and not isinstance(dateOfStatement, aas.SubmodelElement):
                                dateOfStatement = self.DateOfStatement(dateOfStatement)

                            # Build a submodel element if a raw value was passed in the argument

                            if statementReference is not None and not isinstance(
                                statementReference, aas.SubmodelElement
                            ):
                                statementReference = self.StatementReference(statementReference)

                            # Build a submodel element if a raw value was passed in the argument

                            if declaration is not None and not isinstance(declaration, aas.SubmodelElement):
                                declaration = self.Declaration(declaration)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                dateOfStatement, statementReference, declaration
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"Statements",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Statements"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Contains list of statement records regarding the quality assessment"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/statements"
                            ),
                        }

                    def __init__(
                        self, statements_items: Iterable[Statements_item], **kwargs: Unpack[SubmodelElementListMetadata]
                    ):

                        # A str would be split into its characters
                        if isinstance(statements_items, str):
                            raise TypeError("statements_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(statements_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"AdministrativeData",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Administrative Data"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"This submodel element collection contains essential administrative information about the document."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData"
                        ),
                    }

                def __init__(
                    self,
                    coreData: CoreData,
                    items: Optional[Items] = None,
                    statements: Optional[Union[Iterable[Statements.Statements_item], Statements]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(statements, str):
                        raise TypeError("statements takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if statements is not None and not isinstance(statements, aas.SubmodelElement):
                        statements = self.Statements(statements)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(coreData, items, statements)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class DocumentSignature(aas.SubmodelElementCollection):

                class SignedInfo(aas.SubmodelElementCollection):

                    class CanonicalizationMethod(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"CanonicalizationMethod",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Canonicalization Method"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Information about the signature and the algorithms used"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/CanonicalizationMethod"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SignatureMethod(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SignatureMethod",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Signature Method"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Information about the method used for creating the signature"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureMethod"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SignatureReference(aas.SubmodelElementCollection):

                        class Transforms(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Transforms",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Transforms"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Contains the transformations applied to the resource prior to signing"
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/Transforms"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class DigestMethod(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"DigestMethod",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Digest Method"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Specifies the hash algorithm before applying the hash"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/DigestMethod"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class DigestValue(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"DigestValue",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Digest Value"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Contains the Base64 encoded result of applying the hash algorithm to the transformed resource"
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/DigestValue"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"SignatureReference",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Signature Reference"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Additional information for processing the signature"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference"
                                ),
                            }

                        def __init__(
                            self,
                            transforms: Union[str, Transforms],
                            digestMethod: Union[str, DigestMethod],
                            digestValue: Union[str, DigestValue],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if transforms is not None and not isinstance(transforms, aas.SubmodelElement):
                                transforms = self.Transforms(transforms)

                            # Build a submodel element if a raw value was passed in the argument

                            if digestMethod is not None and not isinstance(digestMethod, aas.SubmodelElement):
                                digestMethod = self.DigestMethod(digestMethod)

                            # Build a submodel element if a raw value was passed in the argument

                            if digestValue is not None and not isinstance(digestValue, aas.SubmodelElement):
                                digestValue = self.DigestValue(digestValue)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                transforms, digestMethod, digestValue
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"SignedInfo",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Signed Info"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Information about the signature and the algorithms used"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo"
                            ),
                        }

                    def __init__(
                        self,
                        canonicalizationMethod: Union[str, CanonicalizationMethod],
                        signatureMethod: Union[str, SignatureMethod],
                        signatureReference: Iterable[SignatureReference],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if canonicalizationMethod is not None and not isinstance(
                            canonicalizationMethod, aas.SubmodelElement
                        ):
                            canonicalizationMethod = self.CanonicalizationMethod(canonicalizationMethod)

                        # Build a submodel element if a raw value was passed in the argument

                        if signatureMethod is not None and not isinstance(signatureMethod, aas.SubmodelElement):
                            signatureMethod = self.SignatureMethod(signatureMethod)

                        # A str would be split into its characters
                        if isinstance(signatureReference, str):
                            raise TypeError("signatureReference takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            canonicalizationMethod, signatureMethod, signatureReference
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class SignatureValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SignatureValue",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Signature Value"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Contains the Base64 encoded result of the hash algorithm, i.e., the signature generated with the parameters specified in the SignatureMethod defined in SignedInfo after applying the algorithm specified by the CanonicalizationMethod"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignatureValue"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class KeyInfo(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"KeyInfo",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Key Info"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information to allow the signer to provide recipients with the key that validates the signature, usually in the form of one or more X.509 digital certificates"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/KeyInfo"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"DocumentSignature",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Signature"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about the electronic signature of the quality document. The semantic structure is based on the W3C schema xmldsig"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature"
                        ),
                        "supplemental_semantic_id": (global_ref(r"http://www.w3.org/TR/xmldsig-core1/"),),
                    }

                def __init__(
                    self,
                    signedInfo: SignedInfo,
                    signatureValue: Union[str, SignatureValue],
                    keyInfo: Union[str, KeyInfo],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if signatureValue is not None and not isinstance(signatureValue, aas.SubmodelElement):
                        signatureValue = self.SignatureValue(signatureValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if keyInfo is not None and not isinstance(keyInfo, aas.SubmodelElement):
                        keyInfo = self.KeyInfo(keyInfo)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(signedInfo, signatureValue, keyInfo)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Instance"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Information about a document instance. This SMC inherits from “DocumentVersion” of IDTA 02004-2-0 “Handover Documentation”"
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI503#003/0173-1#01-AHF582#003"),
                }

            def __init__(
                self,
                language: Union[Iterable[Union[str, Language.Language_item]], Language],
                version: Union[str, Version],
                title: Union[aas.MultiLanguageTextType, Title],
                description_: Union[aas.MultiLanguageTextType, Description],
                statusSetDate: Union[xsd.DateTime, StatusSetDate],
                statusValue: Union[str, StatusValue],
                organizationShortName: Union[str, OrganizationShortName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFiles: Union[Iterable[DigitalFiles.Digitalfiles_item], DigitalFiles],
                administrativeData: AdministrativeData,
                refersToEntities: Optional[
                    Union[Iterable[Union[aas.Reference, RefersToEntities.Referstoentities_item]], RefersToEntities]
                ] = None,
                basedOnReferences: Optional[
                    Union[Iterable[Union[aas.Reference, BasedOnReferences.Basedonreferences_item]], BasedOnReferences]
                ] = None,
                previewFile: Optional[PreviewFile] = None,
                documentSignature: Optional[Iterable[DocumentSignature]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if language is not None and not isinstance(language, aas.SubmodelElement):
                    language = self.Language(language)

                # Build a submodel element if a raw value was passed in the argument

                if version is not None and not isinstance(version, aas.SubmodelElement):
                    version = self.Version(version)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if statusSetDate is not None and not isinstance(statusSetDate, aas.SubmodelElement):
                    statusSetDate = self.StatusSetDate(statusSetDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if organizationShortName is not None and not isinstance(organizationShortName, aas.SubmodelElement):
                    organizationShortName = self.OrganizationShortName(organizationShortName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # A str would be split into its characters
                if isinstance(refersToEntities, str):
                    raise TypeError("refersToEntities takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if refersToEntities is not None and not isinstance(refersToEntities, aas.SubmodelElement):
                    refersToEntities = self.RefersToEntities(refersToEntities)

                # A str would be split into its characters
                if isinstance(basedOnReferences, str):
                    raise TypeError("basedOnReferences takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if basedOnReferences is not None and not isinstance(basedOnReferences, aas.SubmodelElement):
                    basedOnReferences = self.BasedOnReferences(basedOnReferences)

                # A str would be split into its characters
                if isinstance(digitalFiles, str):
                    raise TypeError("digitalFiles takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if digitalFiles is not None and not isinstance(digitalFiles, aas.SubmodelElement):
                    digitalFiles = self.DigitalFiles(digitalFiles)

                # A str would be split into its characters
                if isinstance(documentSignature, str):
                    raise TypeError("documentSignature takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language,
                    version,
                    title,
                    description_,
                    statusSetDate,
                    statusValue,
                    organizationShortName,
                    organizationOfficialName,
                    refersToEntities,
                    basedOnReferences,
                    digitalFiles,
                    previewFile,
                    administrativeData,
                    documentSignature,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"DocumentInstances",
                "type_value_list_element": aas.SubmodelElementCollection,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Instances"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Information elements of individual document instances, which can be different versions of each other"
                    }
                ),
                "semantic_id": global_ref(r"0173-1#02-ABI503#003"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI503-003"),),
            }

        def __init__(
            self,
            documentinstances_items: Iterable[Documentinstances_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(documentinstances_items, str):
                raise TypeError("documentinstances_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(documentinstances_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"DigitalQualityDocuments",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Digital Quality Documents"}),
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"Template submodel for Digital Quality Documents."}
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/SubmodelTemplate/DigitalQualityDocument/1/0"),
        }

    def __init__(
        self,
        id_: str,
        documentIds: Union[Iterable[DocumentIds.Documentids_item], DocumentIds],
        documentClassifications: Union[
            Iterable[DocumentClassifications.Documentclassifications_item], DocumentClassifications
        ],
        documentInstances: Union[Iterable[DocumentInstances.Documentinstances_item], DocumentInstances],
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(documentIds, str):
            raise TypeError("documentIds takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documentIds is not None and not isinstance(documentIds, aas.SubmodelElement):
            documentIds = self.DocumentIds(documentIds)

        # A str would be split into its characters
        if isinstance(documentClassifications, str):
            raise TypeError("documentClassifications takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documentClassifications is not None and not isinstance(documentClassifications, aas.SubmodelElement):
            documentClassifications = self.DocumentClassifications(documentClassifications)

        # A str would be split into its characters
        if isinstance(documentInstances, str):
            raise TypeError("documentInstances takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documentInstances is not None and not isinstance(documentInstances, aas.SubmodelElement):
            documentInstances = self.DocumentInstances(documentInstances)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(documentIds, documentClassifications, documentInstances)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
