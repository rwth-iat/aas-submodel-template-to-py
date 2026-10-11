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


class EntityMetadata(TypedDict, total=False):
    """Metadata of aas.Entity, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    entity_type: Optional[aas.EntityType]
    global_asset_id: Optional[str]
    specific_asset_id: Iterable[aas.SpecificAssetId]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


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


class HandoverDocumentation(aas.Submodel):

    class Documents(GeneratedSubmodelElementList):

        class Documents_item(aas.SubmodelElementCollection):

            class DocumentIds(GeneratedSubmodelElementList):

                class Documentids_item(aas.SubmodelElementCollection):

                    class DocumentDomainId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DocumentDomainId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"document domain identificator",
                                        r"de": r"Document Domain Identifikator",
                                    }
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH994#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH994-003"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DocumentIdentifier(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DocumentIdentifier",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Document Identifyer", r"de": r"Dokumentennummer"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-AAO099#004"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO099-004"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DocumentIsPrimary(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DocumentIsPrimary",
                                "value_type": bool,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Document is primary", r"de": r"Dokument ist primär"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH995#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH995-003"),
                                ),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Document identificator", r"de": r"Dokumentidentifikator"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"This SubmodelElementCollection holds the information for a VDI 2770 Document entity"
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABI501#003/0173-1#01-AHF580#003"),
                            "supplemental_semantic_id": (
                                aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"0173-1#02-ABI501#003~0/0173-1#01-AHF580#003",
                                        ),
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI501-003/0173-1-01-AHF580-003",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
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
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABI501#003/0173-1#01-AHF580#003"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Document identifyers", r"de": r"Dokumentidentifikatoren"}
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
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Class identificator", r"de": r"Klassenidentifikator"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH996#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH996-003"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ClassName(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"ClassName",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Klassenname"}),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABJ219#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABJ219-002"),
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ClassificationSystem(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ClassificationSystem",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Classification system", r"de": r"Klassifizierungssystem"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH997#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH997-003"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Document classification", r"de": r"Dokumentklassifikation"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Set of information for describing the classification of the Document according to a ClassificationSystem"
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABI502#003/0173-1#01-AHF581#003"),
                            "supplemental_semantic_id": (
                                aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"0173-1#02-ABI502#003~0/0173-1#01-AHF581#003",
                                        ),
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI502-003/0173-1-01-AHF581-003",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                        }

                    def __init__(
                        self,
                        classId: Union[str, ClassId],
                        className: Union[aas.LangStringSet, ClassName],
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

                        if classificationSystem is not None and not isinstance(
                            classificationSystem, aas.SubmodelElement
                        ):
                            classificationSystem = self.ClassificationSystem(classificationSystem)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(classId, className, classificationSystem)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"DocumentClassifications",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABI502#003/0173-1#01-AHF581#003"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Document classifications", r"de": r"Dokumentklassifikationen"}
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

                    embedded_submodel_elements = collect_submodel_elements(
                        documentclassifications_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class DocumentVersions(GeneratedSubmodelElementList):

                class Documentversions_item(aas.SubmodelElementCollection):

                    class Language(GeneratedSubmodelElementList):

                        class Language_item(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": None,
                                    "value_type": str,
                                    "value_id": global_ref(r"0173-1#07-AAS045#003"),
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"en (English)", r"de": r"en (Englisch)"}
                                    ),
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
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Language", r"de": r"Sprache"}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAN468#008"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAN468-008"),
                                ),
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
                                    i if isinstance(i, aas.SubmodelElement) else self.Language_item(i)
                                    for i in language_items
                                ]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                language_items, number_repeated=False
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class Version(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Version",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Document version", r"de": r"Dokumentenversion"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-AAP003#005"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAP003-005"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Title(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Title",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Document title", r"de": r"Dokumententitel"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABG940#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABG940-003"),
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Subtitle(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Subtitle",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Subtitle", r"de": r"Untertitel"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH998#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH998-003"),
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Description(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Description",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Document description", r"de": r"Dokumentenbeschreibung"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-AAN466#004"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAN466-004"),
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class KeyWords(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"KeyWords",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Keywords", r"de": r"Stichworte"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH999#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH999-003"),
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class StatusSetDate(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StatusSetDate",
                                "value_type": xsd.Date,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document status set date",
                                        r"de": r"Datum der Einstellung des Dokumentenstatus",
                                    }
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABI000#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI000-003"),
                                ),
                            }

                        def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class StatusValue(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StatusValue",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Document status", r"de": r"Dokumentstatus"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABI001#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI001-003"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class OrganizationShortName(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"OrganizationShortName",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Organization short name", r"de": r"Kurzname der Organisation"}
                                ),
                                "category": r"PARAMETER",
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
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Organization official name",
                                        r"de": r"Offizieller Name der Organisation",
                                    }
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABI004#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI004-003"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class RefersToEntities(GeneratedSubmodelElementList):

                        class Referstoentities_item(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": None,
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(r"0173-1#02-ABK288#002"),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"RefersToEntities",
                                "type_value_list_element": aas.ReferenceElement,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Reference to other documents",
                                        r"de": r"Referenz zu anderen Dokumenten",
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABK288#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK288-002"),
                                ),
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
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(r"0173-1#02-ABK289#002"),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"BasedOnReferences",
                                "type_value_list_element": aas.ReferenceElement,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Based on other documents", r"de": r"Basiert auf anderen Dokumenten"}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABK289#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK289-002"),
                                ),
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

                    class TranslationOfEntities(GeneratedSubmodelElementList):

                        class Translationofentities_item(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": None,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={
                                            r"en": r"Translation of documents",
                                            r"de": r"Übersetzung von anderen Elementen",
                                        }
                                    ),
                                    "category": r"PARAMETER",
                                    "semantic_id": global_ref(r"0173-1#02-ABK290#002"),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"TranslationOfEntities",
                                "type_value_list_element": aas.ReferenceElement,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Translation of other documents",
                                        r"de": r"Übersetzung von anderen Elementen",
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABK290#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK290-002"),
                                ),
                            }

                        def __init__(
                            self,
                            translationofentities_items: Iterable[Union[aas.Reference, Translationofentities_item]],
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(translationofentities_items, str):
                                raise TypeError("translationofentities_items takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if translationofentities_items:
                                translationofentities_items = [
                                    i if isinstance(i, aas.SubmodelElement) else self.Translationofentities_item(i)
                                    for i in translationofentities_items
                                ]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                translationofentities_items, number_repeated=False
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class DigitalFiles(GeneratedSubmodelElementList):

                        class Digitalfiles_item(aas.File):

                            @staticmethod
                            def template_defaults() -> FileMetadata:
                                return {
                                    "id_short": None,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={
                                            r"en": r"Name of the specific digital file@en",
                                            r"de": r"Name der spezifischen digitalen Datei@de",
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABK126#002"),
                                }

                            def __init__(
                                self,
                                value: str,
                                content_type: Optional[str] = r"application/pdf",
                                **kwargs: Unpack[FileMetadata],
                            ):

                                super().__init__(
                                    value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"DigitalFiles",
                                "type_value_list_element": aas.File,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Digital files", r"de": r"Digitale Dateien"}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABK126#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK126-002"),
                                ),
                            }

                        def __init__(
                            self,
                            digitalfiles_items: Iterable[Digitalfiles_item],
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(digitalfiles_items, str):
                                raise TypeError("digitalfiles_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                digitalfiles_items, number_repeated=False
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class PreviewFile(aas.File):

                        @staticmethod
                        def template_defaults() -> FileMetadata:
                            return {
                                "id_short": r"PreviewFile",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Preview file", r"de": r"Vorschaudatei"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABK127#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK127-002"),
                                ),
                            }

                        def __init__(
                            self,
                            value: str,
                            content_type: Optional[str] = r"image/jpeg",
                            **kwargs: Unpack[FileMetadata],
                        ):

                            super().__init__(
                                value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                            )

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Document version", r"de": r"Document version"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABI503#003/0173-1#01-AHF582#003"),
                            "supplemental_semantic_id": (
                                aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"0173-1#02-ABI503#003~0/0173-1#01-AHF582#003",
                                        ),
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI503-003",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                        }

                    def __init__(
                        self,
                        language: Union[Iterable[Union[str, Language.Language_item]], Language],
                        version: Union[str, Version],
                        title: Union[aas.LangStringSet, Title],
                        description_: Union[aas.LangStringSet, Description],
                        statusSetDate: Union[xsd.Date, StatusSetDate],
                        statusValue: Union[str, StatusValue],
                        organizationShortName: Union[str, OrganizationShortName],
                        organizationOfficialName: Union[str, OrganizationOfficialName],
                        digitalFiles: Union[Iterable[DigitalFiles.Digitalfiles_item], DigitalFiles],
                        subtitle: Optional[Union[aas.LangStringSet, Subtitle]] = None,
                        keyWords: Optional[Union[aas.LangStringSet, KeyWords]] = None,
                        refersToEntities: Optional[
                            Union[
                                Iterable[Union[aas.Reference, RefersToEntities.Referstoentities_item]], RefersToEntities
                            ]
                        ] = None,
                        basedOnReferences: Optional[
                            Union[
                                Iterable[Union[aas.Reference, BasedOnReferences.Basedonreferences_item]],
                                BasedOnReferences,
                            ]
                        ] = None,
                        translationOfEntities: Optional[
                            Union[
                                Iterable[Union[aas.Reference, TranslationOfEntities.Translationofentities_item]],
                                TranslationOfEntities,
                            ]
                        ] = None,
                        previewFile: Optional[PreviewFile] = None,
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

                        if subtitle is not None and not isinstance(subtitle, aas.SubmodelElement):
                            subtitle = self.Subtitle(subtitle)

                        # Build a submodel element if a raw value was passed in the argument

                        if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                            description_ = self.Description(description_)

                        # Build a submodel element if a raw value was passed in the argument

                        if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                            keyWords = self.KeyWords(keyWords)

                        # Build a submodel element if a raw value was passed in the argument

                        if statusSetDate is not None and not isinstance(statusSetDate, aas.SubmodelElement):
                            statusSetDate = self.StatusSetDate(statusSetDate)

                        # Build a submodel element if a raw value was passed in the argument

                        if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                            statusValue = self.StatusValue(statusValue)

                        # Build a submodel element if a raw value was passed in the argument

                        if organizationShortName is not None and not isinstance(
                            organizationShortName, aas.SubmodelElement
                        ):
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
                        if isinstance(translationOfEntities, str):
                            raise TypeError("translationOfEntities takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if translationOfEntities is not None and not isinstance(
                            translationOfEntities, aas.SubmodelElement
                        ):
                            translationOfEntities = self.TranslationOfEntities(translationOfEntities)

                        # A str would be split into its characters
                        if isinstance(digitalFiles, str):
                            raise TypeError("digitalFiles takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if digitalFiles is not None and not isinstance(digitalFiles, aas.SubmodelElement):
                            digitalFiles = self.DigitalFiles(digitalFiles)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            language,
                            version,
                            title,
                            subtitle,
                            description_,
                            keyWords,
                            statusSetDate,
                            statusValue,
                            organizationShortName,
                            organizationOfficialName,
                            refersToEntities,
                            basedOnReferences,
                            translationOfEntities,
                            digitalFiles,
                            previewFile,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"DocumentVersions",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABI503#003/0173-1#01-AHF582#003"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Document versions", r"de": r"Dokumentenversionen"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI503#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI503-003"),),
                    }

                def __init__(
                    self,
                    documentversions_items: Iterable[Documentversions_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(documentversions_items, str):
                        raise TypeError("documentversions_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        documentversions_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class DocumentedEntities(GeneratedSubmodelElementList):

                class Documentedentities_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": None,
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"DocumentedEntities",
                        "type_value_list_element": aas.ReferenceElement,
                        "semantic_id": global_ref(r"https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities"),
                    }

                def __init__(
                    self,
                    documentedentities_items: Iterable[Union[aas.Reference, Documentedentities_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(documentedentities_items, str):
                        raise TypeError("documentedentities_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if documentedentities_items:
                        documentedentities_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Documentedentities_item(i)
                            for i in documentedentities_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        documentedentities_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"This SubmodelElementCollection holds the information for a VDI 2770 Document entity"
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI500#003/0173-1#01-AHF579#003"),
                    "supplemental_semantic_id": (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABI500#003~0/0173-1#01-AHF579#003",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABI500-003/0173-1-01-AHF579-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                }

            def __init__(
                self,
                documentIds: Union[Iterable[DocumentIds.Documentids_item], DocumentIds],
                documentClassifications: Union[
                    Iterable[DocumentClassifications.Documentclassifications_item], DocumentClassifications
                ],
                documentVersions: Union[Iterable[DocumentVersions.Documentversions_item], DocumentVersions],
                documentedEntities: Optional[
                    Union[
                        Iterable[Union[aas.Reference, DocumentedEntities.Documentedentities_item]], DocumentedEntities
                    ]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
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
                if isinstance(documentVersions, str):
                    raise TypeError("documentVersions takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if documentVersions is not None and not isinstance(documentVersions, aas.SubmodelElement):
                    documentVersions = self.DocumentVersions(documentVersions)

                # A str would be split into its characters
                if isinstance(documentedEntities, str):
                    raise TypeError("documentedEntities takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if documentedEntities is not None and not isinstance(documentedEntities, aas.SubmodelElement):
                    documentedEntities = self.DocumentedEntities(documentedEntities)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    documentIds, documentClassifications, documentVersions, documentedEntities
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"Documents",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#02-ABI500#003/0173-1#01-AHF579#003"),
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Documents (handover documentation)", r"de": r"Dokumente (Übergabedokumentation)"}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABI500#003"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI500-003"),),
            }

        def __init__(self, documents_items: Iterable[Documents_item], **kwargs: Unpack[SubmodelElementListMetadata]):

            # A str would be split into its characters
            if isinstance(documents_items, str):
                raise TypeError("documents_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(documents_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Entities(GeneratedSubmodelElementList):

        class Entities_item(aas.Entity):

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": None,
                    "entity_type": aas.EntityType.CO_MANAGED_ENTITY,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation"),
                }

            def __init__(self, **kwargs: Unpack[EntityMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"Entities",
                "type_value_list_element": aas.Entity,
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2770/1/0/EntitiesForDocumentation"),
            }

        def __init__(self, entities_items: Iterable[Entities_item], **kwargs: Unpack[SubmodelElementListMetadata]):

            # A str would be split into its characters
            if isinstance(entities_items, str):
                raise TypeError("entities_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(entities_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"HandoverDocumentation",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel defines a set meta data for the handover of documentation from the manufacturer to the operator for industrial equipment"
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"2",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02004-2-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AHF578#003"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
            "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-01-AHF578-003"),),
        }

    def __init__(
        self,
        id_: str,
        documents: Union[Iterable[Documents.Documents_item], Documents],
        entities: Optional[Union[Iterable[Entities.Entities_item], Entities]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(documents, str):
            raise TypeError("documents takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documents is not None and not isinstance(documents, aas.SubmodelElement):
            documents = self.Documents(documents)

        # A str would be split into its characters
        if isinstance(entities, str):
            raise TypeError("entities takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if entities is not None and not isinstance(entities, aas.SubmodelElement):
            entities = self.Entities(entities)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(documents, entities)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
