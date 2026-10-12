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

            class DocumentClassifications(GeneratedSubmodelElementList):

                class Documentclassifications_item(aas.SubmodelElementCollection):

                    class ClassName(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"ClassName",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"class name", r"de": r"Klassenname"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABJ219#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABJ219-002"),
                                    global_ref(r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#className"),
                                ),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ClassId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ClassId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"class ID", r"de": r"Klassenidentifikator"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH996#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH996-003"),
                                    global_ref(r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#classId"),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ClassificationSystem(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ClassificationSystem",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"classification system", r"de": r"Klassifizierungssystem"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH997#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH997-003"),
                                    global_ref(
                                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#classificationSystem"
                                    ),
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"document classification", r"de": r"Dokumentklassifikation"}
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
                                global_ref(
                                    r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentClassification"
                                ),
                            ),
                        }

                    def __init__(
                        self,
                        className: Union[aas.MultiLanguageTextType, ClassName],
                        classId: Union[str, ClassId],
                        classificationSystem: Union[str, ClassificationSystem],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if className is not None and not isinstance(className, aas.SubmodelElement):
                            className = self.ClassName(className)

                        # Build a submodel element if a raw value was passed in the argument

                        if classId is not None and not isinstance(classId, aas.SubmodelElement):
                            classId = self.ClassId(classId)

                        # Build a submodel element if a raw value was passed in the argument

                        if classificationSystem is not None and not isinstance(
                            classificationSystem, aas.SubmodelElement
                        ):
                            classificationSystem = self.ClassificationSystem(classificationSystem)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(className, classId, classificationSystem)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"DocumentClassifications",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABI502#003/0173-1#01-AHF581#003"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"document classifications", r"de": r"Dokumentklassifikationen"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI502#003"),
                        "supplemental_semantic_id": (
                            global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI502-003"),
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#documentClassifications"
                            ),
                        ),
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

            class DocumentIds(GeneratedSubmodelElementList):

                class Documentids_item(aas.SubmodelElementCollection):

                    class DocumentDomainId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DocumentDomainId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"document domain ID", r"de": r"Document Domain Identifikator"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH994#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH994-003"),
                                    global_ref(
                                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#documentDomainId"
                                    ),
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
                                    dict_={r"en": r"document identifier", r"de": r"Dokumentennummer"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-AAO099#004"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO099-004"),
                                    global_ref(
                                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#documentIdentifier"
                                    ),
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
                                    dict_={r"en": r"document is primary", r"de": r"Dokument ist primär"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABH995#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABH995-003"),
                                    global_ref(
                                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#documentIsPrimary"
                                    ),
                                ),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"document ID", r"de": r"Dokumentidentifikator"}
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
                                global_ref(r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentId"),
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
                            dict_={r"en": r"document IDs", r"de": r"Dokumentidentifikatoren"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI501#003"),
                        "supplemental_semantic_id": (
                            global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI501-003"),
                            global_ref(r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#documentIds"),
                        ),
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
                                        dict_={r"en": r"language", r"de": r"en (Englisch)"}
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAN468#008"),
                                    "supplemental_semantic_id": (
                                        global_ref(r"urn:samm:org.eclipse.esmf.samm:characteristic:2.1.0#Locale"),
                                    ),
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
                                    global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#languages"),
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
                                    dict_={r"en": r"Version", r"de": r"Dokumentenversion"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-AAP003#005"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAP003-005"),
                                    global_ref(r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#version"),
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
                                    dict_={r"en": r"Title", r"de": r"Dokumententitel"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABG940#003"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABG940-003"),
                                    global_ref(r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#title"),
                                ),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

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
                                    global_ref(r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#subtitle"),
                                ),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Description(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Description",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Description", r"de": r"Dokumentenbeschreibung"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-AAN466#004"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAN466-004"),
                                    global_ref(
                                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#description"
                                    ),
                                ),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DigitalFiles(GeneratedSubmodelElementList):

                        class Digitalfiles_item(aas.File):

                            @staticmethod
                            def template_defaults() -> FileMetadata:
                                return {
                                    "id_short": None,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={
                                            r"en": r"digital files",
                                            r"de": r"Name der spezifischen digitalen Datei@de",
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-ABK126#002"),
                                    "supplemental_semantic_id": (
                                        global_ref(
                                            r"urn:samm:io.admin-shell.idta.shared:3.1.0#ResourceWithContentType"
                                        ),
                                    ),
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
                                    dict_={r"en": r"digital files", r"de": r"Digitale Dateien"}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABK126#002"),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK126-002"),
                                    global_ref(
                                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#digtialFiles"
                                    ),
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

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"document version", r"de": r"Document version"}
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
                                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI503-003/0173-1-01-AHF582-003",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                global_ref(
                                    r"urn:samm:io.admin-shell.idta.batterypass.handover_documentation:1.0.0#DocumentVersion"
                                ),
                            ),
                        }

                    def __init__(
                        self,
                        language: Union[Iterable[Union[str, Language.Language_item]], Language],
                        title: Union[aas.MultiLanguageTextType, Title],
                        digitalFiles: Union[Iterable[DigitalFiles.Digitalfiles_item], DigitalFiles],
                        version: Optional[Union[str, Version]] = None,
                        subtitle: Optional[Union[aas.MultiLanguageTextType, Subtitle]] = None,
                        description_: Optional[Union[aas.MultiLanguageTextType, Description]] = None,
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

                        # A str would be split into its characters
                        if isinstance(digitalFiles, str):
                            raise TypeError("digitalFiles takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if digitalFiles is not None and not isinstance(digitalFiles, aas.SubmodelElement):
                            digitalFiles = self.DigitalFiles(digitalFiles)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            language, version, title, subtitle, description_, digitalFiles
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"DocumentVersions",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(r"0173-1#02-ABI503#003/0173-1#01-AHF582#003"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"document versions", r"de": r"Dokumentenversionen"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI503#003"),
                        "supplemental_semantic_id": (
                            global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI503-003"),
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.handover_documentation:1.0.0#documentVersions"
                            ),
                        ),
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

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"document"}),
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
                        global_ref(r"urn:samm:io.admin-shell.idta.batterypass.handover_documentation:1.0.0#Document"),
                    ),
                }

            def __init__(
                self,
                documentClassifications: Union[
                    Iterable[DocumentClassifications.Documentclassifications_item], DocumentClassifications
                ],
                documentIds: Union[Iterable[DocumentIds.Documentids_item], DocumentIds],
                documentVersions: Union[Iterable[DocumentVersions.Documentversions_item], DocumentVersions],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(documentClassifications, str):
                    raise TypeError("documentClassifications takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if documentClassifications is not None and not isinstance(documentClassifications, aas.SubmodelElement):
                    documentClassifications = self.DocumentClassifications(documentClassifications)

                # A str would be split into its characters
                if isinstance(documentIds, str):
                    raise TypeError("documentIds takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if documentIds is not None and not isinstance(documentIds, aas.SubmodelElement):
                    documentIds = self.DocumentIds(documentIds)

                # A str would be split into its characters
                if isinstance(documentVersions, str):
                    raise TypeError("documentVersions takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if documentVersions is not None and not isinstance(documentVersions, aas.SubmodelElement):
                    documentVersions = self.DocumentVersions(documentVersions)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    documentClassifications, documentIds, documentVersions
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"Documents",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#02-ABI500#003/0173-1#01-AHF579#003"),
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Documents", r"de": r"Dokumente (Übergabedokumentation)"}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABI500#003"),
                "supplemental_semantic_id": (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI500-003"),
                    global_ref(r"urn:samm:io.admin-shell.idta.batterypass.handover_documentation:1.0.0#documents"),
                ),
            }

        def __init__(self, documents_items: Iterable[Documents_item], **kwargs: Unpack[SubmodelElementListMetadata]):

            # A str would be split into its characters
            if isinstance(documents_items, str):
                raise TypeError("documents_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(documents_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"HandoverDocumentation",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"handover documentation"}),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel defines a set meta data for the handover of documentation from the manufacturer to the operator for industrial equipment"
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02035-2",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AHF578#003"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
            "supplemental_semantic_id": (
                global_ref(r"https://api.eclass-cdp.com/0173-1-01-AHF578-003"),
                global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.handover_documentation:1.0.0#HandoverDocumentation"
                ),
            ),
        }

    def __init__(
        self,
        id_: str,
        documents: Union[Iterable[Documents.Documents_item], Documents],
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(documents, str):
            raise TypeError("documents takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documents is not None and not isinstance(documents, aas.SubmodelElement):
            documents = self.Documents(documents)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(documents)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
