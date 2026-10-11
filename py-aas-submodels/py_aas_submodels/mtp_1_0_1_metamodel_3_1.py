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


class RelationshipElementMetadata(TypedDict, total=False):
    """Metadata of aas.RelationshipElement, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    first: Optional[aas.Reference]
    second: Optional[aas.Reference]
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


class AssetIdentification(aas.Submodel):

    class Manufacturer(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"Manufacturer",
                "value_type": str,
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"0173-1#02-AAO677#002"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {"id_short": r"AssetIdentification"}

    def __init__(self, id_: str, manufacturer: Union[str, Manufacturer], **kwargs: Unpack[SubmodelMetadata]):

        # Build a submodel element if a raw value was passed in the argument

        if manufacturer is not None and not isinstance(manufacturer, aas.SubmodelElement):
            manufacturer = self.Manufacturer(manufacturer)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(manufacturer)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))


class Documentation(aas.Submodel):

    class Document01(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/jpeg", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document01",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document02(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document02",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document03(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document03",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document04(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document04",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document05(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document05",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document06(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document06",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document07(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Language02(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language02",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                language02: Union[str, Language02],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if language02 is not None and not isinstance(language02, aas.SubmodelElement):
                    language02 = self.Language02(language02)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    language02,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document07",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document08(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document08",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document09(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document09",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"Documentation",
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"http://admin-shell.io/vdi/2770/1/0/Documentation"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        document01: Document01,
        document02: Document02,
        document03: Document03,
        document04: Document04,
        document05: Document05,
        document06: Document06,
        document07: Document07,
        document08: Document08,
        document09: Document09,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            document01, document02, document03, document04, document05, document06, document07, document08, document09
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))


class AssetIdentification(aas.Submodel):

    class SerialNumber(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"SerialNumber",
                "value_type": str,
                "semantic_id": global_ref(r"http://opcfoundation.org/UA/DI/1.1/DeviceType/Serialnumber"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Manufacturer(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"Manufacturer",
                "value_type": str,
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"0173-1#02-AAO677#002"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {"id_short": r"AssetIdentification"}

    def __init__(
        self,
        id_: str,
        serialNumber: Union[str, SerialNumber],
        manufacturer: Union[str, Manufacturer],
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if serialNumber is not None and not isinstance(serialNumber, aas.SubmodelElement):
            serialNumber = self.SerialNumber(serialNumber)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturer is not None and not isinstance(manufacturer, aas.SubmodelElement):
            manufacturer = self.Manufacturer(manufacturer)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(serialNumber, manufacturer)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))


class ModuleTypePackage(aas.Submodel):

    class MTPFile(aas.File):

        @staticmethod
        def template_defaults() -> FileMetadata:
            return {
                "id_short": r"MTPFile",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPSUCLib/ModuleTypePackage"),
            }

        def __init__(
            self, value: str, content_type: Optional[str] = r"application/mtp", **kwargs: Unpack[FileMetadata]
        ):

            super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

    class DocumentationReferences(aas.SubmodelElementCollection):

        class M0013_Datasheet(aas.RelationshipElement):

            @staticmethod
            def template_defaults() -> RelationshipElementMetadata:
                return {
                    "id_short": r"M0013_Datasheet",
                    "first": aas.ModelReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"www.vendor.com/ids/sm/6233_9041_1002_7102"),
                            aas.Key(type_=aas.KeyTypes.FILE, value=r"MTPFile"),
                            aas.Key(
                                type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                value=r"CAEX@ModuleTypePackage/BPXX_Freelance/CommunicationSet/InstanceList/M0013",
                            ),
                        ),
                        type_=type(None),
                        referred_semantic_id=None,
                    ),
                    "second": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.SUBMODEL,
                                value=r"http://example.com/id/instance/99920200206160529000012810",
                            ),
                            aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document01"),
                        ),
                        type_=aas.SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPReference"),
                }

            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                super().__init__(**(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DocumentationReferences",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPReferences"),
            }

        def __init__(
            self, m0013_Datasheet: Iterable[M0013_Datasheet], **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(m0013_Datasheet, str):
                raise TypeError("m0013_Datasheet takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(m0013_Datasheet)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class BOMReferences(aas.SubmodelElementCollection):

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"BOMReferences",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPReferences"),
            }

        def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements()

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ModuleTypePackage",
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/vdi/2658/1/0/MTPSubmodel"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        mTPFile: MTPFile,
        documentationReferences: Optional[Iterable[DocumentationReferences]] = None,
        bOMReferences: Optional[Iterable[BOMReferences]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(documentationReferences, str):
            raise TypeError("documentationReferences takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(bOMReferences, str):
            raise TypeError("bOMReferences takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(mTPFile, documentationReferences, bOMReferences)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))


class ProcessEquipmentAssembly(aas.Submodel):

    class MTPFile(aas.File):

        @staticmethod
        def template_defaults() -> FileMetadata:
            return {
                "id_short": r"MTPFile",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPSUCLib/ModuleTypePackage"),
            }

        def __init__(
            self, value: str, content_type: Optional[str] = r"application/mtp", **kwargs: Unpack[FileMetadata]
        ):

            super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

    class SourceList(aas.SubmodelElementCollection):

        class FreelanceOPCUA(aas.SubmodelElementCollection):

            class DiscoveryUrl(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DiscoveryUrl",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/opcua-server-datasheet/1/0/discovery-url"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ApplicationUri(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ApplicationUri",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/opcua-server-datasheet/1/0/application-uri"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"FreelanceOPCUA",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/vdi/2658/1/0/MTPCommunicationSUCLib/ServerAssembly/OPCUAServer"
                    ),
                }

            def __init__(
                self,
                discoveryUrl: Iterable[Union[str, DiscoveryUrl]],
                applicationUri: Optional[Iterable[Union[str, ApplicationUri]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(discoveryUrl, str):
                    raise TypeError("discoveryUrl takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if discoveryUrl:
                    discoveryUrl = [
                        i if isinstance(i, aas.SubmodelElement) else self.DiscoveryUrl(i) for i in discoveryUrl
                    ]

                # A str would be split into its characters
                if isinstance(applicationUri, str):
                    raise TypeError("applicationUri takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if applicationUri:
                    applicationUri = [
                        i if isinstance(i, aas.SubmodelElement) else self.ApplicationUri(i) for i in applicationUri
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(discoveryUrl, applicationUri)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SourceList",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPSUCLib/CommunicationSet/SourceList"),
            }

        def __init__(
            self, freelanceOPCUA: Iterable[FreelanceOPCUA], **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(freelanceOPCUA, str):
                raise TypeError("freelanceOPCUA takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(freelanceOPCUA)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DisplayName(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"DisplayName",
                "category": r"PARAMETER",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/PEASubmodel/DisplayName"),
            }

        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Description(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"Description",
                "category": r"PARAMETER",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/PEASubmodel/Description"),
            }

        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class DocumentationReferences(aas.SubmodelElementCollection):

        class M0013_FAT_Protocol(aas.RelationshipElement):

            @staticmethod
            def template_defaults() -> RelationshipElementMetadata:
                return {
                    "id_short": r"M0013_FAT_Protocol",
                    "first": aas.ModelReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"www.vendor.com/ids/sm/6233_9041_1002_7102"),
                            aas.Key(type_=aas.KeyTypes.FILE, value=r"MTPFile"),
                            aas.Key(
                                type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                value=r"CAEX@ModuleTypePackage/BPXX_Freelance/CommunicationSet/InstanceList/M0013",
                            ),
                        ),
                        type_=type(None),
                        referred_semantic_id=None,
                    ),
                    "second": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/0455_7003_3012_9891"
                            ),
                            aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document03"),
                        ),
                        type_=aas.SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPReference"),
                }

            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                super().__init__(**(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DocumentationReferences",
                "semantic_id": global_ref(r"https://admin-shell.io/vdi/2658/1/0/MTPReferences"),
            }

        def __init__(
            self, m0013_FAT_Protocol: Iterable[M0013_FAT_Protocol], **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(m0013_FAT_Protocol, str):
                raise TypeError("m0013_FAT_Protocol takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(m0013_FAT_Protocol)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ProcessEquipmentAssembly",
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/vdi/2658/1/0/PEASubmodel"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        mTPFile: Optional[MTPFile] = None,
        sourceList: Optional[SourceList] = None,
        displayName: Optional[Union[aas.LangStringSet, DisplayName]] = None,
        description_: Optional[Union[aas.LangStringSet, Description]] = None,
        documentationReferences: Optional[DocumentationReferences] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if displayName is not None and not isinstance(displayName, aas.SubmodelElement):
            displayName = self.DisplayName(displayName)

        # Build a submodel element if a raw value was passed in the argument

        if description_ is not None and not isinstance(description_, aas.SubmodelElement):
            description_ = self.Description(description_)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            mTPFile, sourceList, displayName, description_, documentationReferences
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))


class Documentation(aas.Submodel):

    class Document01(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/jpeg", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document01",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document02(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document02",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document03(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document03",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document04(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document04",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document05(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document05",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document06(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document06",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document07(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Language02(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language02",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                language02: Union[str, Language02],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if language02 is not None and not isinstance(language02, aas.SubmodelElement):
                    language02 = self.Language02(language02)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    language02,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document07",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document08(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document08",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Document09(aas.SubmodelElementCollection):

        class DocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/Id"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPrimaryDocumentId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPrimaryDocumentId",
                    "value_type": bool,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentId/isPrimary"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassId",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassId"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassName",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentClassificationSystem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DocumentClassificationSystem",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(
                        r"http://admin-shell.io/vdi/2770/1/0/DocumentClassification/ClassificationSystem"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DocumentVersion01(aas.SubmodelElementCollection):

            class Language01(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language01",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/Language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersionId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersionId",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion/DocumentVersionId"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Description/Title"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Summary(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Summary",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/Summary"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class KeyWords(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"KeyWords",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentDescription/KeyWords"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SetDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SetDate",
                        "value_type": xsd.Date,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/SetDate"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusValue",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/LifeCycleStatus/StatusValue"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Party/Role"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationName"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrganizationOfficialName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OrganizationOfficialName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/Organization/OrganizationOfficialName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DigitalFile",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(
                            r"http://admin-shell.io/vdi/2770/1/0/StoredDocumentRepresentation/DigitalFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentVersion01",
                    "category": r"CONSTANT",
                    "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/DocumentVersion"),
                }

            def __init__(
                self,
                language01: Union[str, Language01],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[aas.LangStringSet, Title],
                summary: Union[aas.LangStringSet, Summary],
                keyWords: Union[aas.LangStringSet, KeyWords],
                setDate: Union[xsd.Date, SetDate],
                statusValue: Union[str, StatusValue],
                role: Union[str, Role],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: DigitalFile,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if language01 is not None and not isinstance(language01, aas.SubmodelElement):
                    language01 = self.Language01(language01)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersionId is not None and not isinstance(documentVersionId, aas.SubmodelElement):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if summary is not None and not isinstance(summary, aas.SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument

                if keyWords is not None and not isinstance(keyWords, aas.SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument

                if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                    setDate = self.SetDate(setDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if organizationName is not None and not isinstance(organizationName, aas.SubmodelElement):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    language01,
                    documentVersionId,
                    title,
                    summary,
                    keyWords,
                    setDate,
                    statusValue,
                    role,
                    organizationName,
                    organizationOfficialName,
                    digitalFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Document09",
                "category": r"CONSTANT",
                "semantic_id": global_ref(r"http://admin-shell.io/vdi/2770/1/0/Document"),
            }

        def __init__(
            self,
            documentId: Union[str, DocumentId],
            isPrimaryDocumentId: Union[bool, IsPrimaryDocumentId],
            documentClassId: Union[str, DocumentClassId],
            documentClassName: Union[str, DocumentClassName],
            documentClassificationSystem: Union[str, DocumentClassificationSystem],
            documentVersion01: DocumentVersion01,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if documentId is not None and not isinstance(documentId, aas.SubmodelElement):
                documentId = self.DocumentId(documentId)

            # Build a submodel element if a raw value was passed in the argument

            if isPrimaryDocumentId is not None and not isinstance(isPrimaryDocumentId, aas.SubmodelElement):
                isPrimaryDocumentId = self.IsPrimaryDocumentId(isPrimaryDocumentId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassId is not None and not isinstance(documentClassId, aas.SubmodelElement):
                documentClassId = self.DocumentClassId(documentClassId)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassName is not None and not isinstance(documentClassName, aas.SubmodelElement):
                documentClassName = self.DocumentClassName(documentClassName)

            # Build a submodel element if a raw value was passed in the argument

            if documentClassificationSystem is not None and not isinstance(
                documentClassificationSystem, aas.SubmodelElement
            ):
                documentClassificationSystem = self.DocumentClassificationSystem(documentClassificationSystem)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                documentId,
                isPrimaryDocumentId,
                documentClassId,
                documentClassName,
                documentClassificationSystem,
                documentVersion01,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"Documentation",
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"http://admin-shell.io/vdi/2770/1/0/Documentation"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        document01: Document01,
        document02: Document02,
        document03: Document03,
        document04: Document04,
        document05: Document05,
        document06: Document06,
        document07: Document07,
        document08: Document08,
        document09: Document09,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            document01, document02, document03, document04, document05, document06, document07, document08, document09
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
