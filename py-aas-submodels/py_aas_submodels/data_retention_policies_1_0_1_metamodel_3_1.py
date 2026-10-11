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


class DataRetentionPolicies(aas.Submodel):

    class InheritedFrom(aas.ReferenceElement):

        @staticmethod
        def template_defaults() -> ReferenceElementMetadata:
            return {
                "id_short": r"InheritedFrom",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference to a DataRetentionPolicies Submodel whose policies are extended or changed by the policies defined in this Submodel."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/InheritedFrom/1/0"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Policies(aas.SubmodelElementCollection):

        class Policy(aas.SubmodelElementCollection):

            class RetentionTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RetentionTime",
                        "value_type": xsd.Duration,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies how long an element must be retained before it can be deleted."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/DataRetentionPolicies/RetentionTime/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Duration, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SemanticIds(GeneratedSubmodelElementList):

                class Semanticids_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to a semantic identifier of an element that this policy shall apply to."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/SemanticId/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"SemanticIds",
                        "type_value_list_element": aas.ReferenceElement,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/DataRetentionPolicies/SemanticId/1/0"
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"References to semantic identifiers of elements that this policy shall apply to."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/SemanticIds/1/0"),
                    }

                def __init__(
                    self,
                    semanticids_items: Iterable[Union[aas.Reference, Semanticids_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(semanticids_items, str):
                        raise TypeError("semanticids_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if semanticids_items:
                        semanticids_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Semanticids_item(i)
                            for i in semanticids_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(semanticids_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Overrides(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"Overrides",
                        "first": aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DataRetentionPolicies/Overrides/1/0",
                                ),
                            ),
                            referred_semantic_id=global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/Overrides/1/0"
                            ),
                        ),
                        "second": aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DataRetentionPolicies/Overrides/1/0",
                                ),
                            ),
                            referred_semantic_id=global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/Overrides/1/0"
                            ),
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Establishes a relationship with a policy that is being overridden by this policy."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/Overrides/1/0"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class Immutable(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Immutable",
                        "value_type": bool,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies whether the policy is immutable."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/Immutable/1/0"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CreatedBy(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CreatedBy",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Legal name of the entity who created the policy."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/CreatedBy/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CreationTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CreationTime",
                        "value_type": xsd.DateTime,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Timestamp of when the policy was created."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/DataRetentionPolicies/CreationTime/1/0"
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Issuer(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Issuer",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Legal name of the entity that issued the policy."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/Issuer/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Source(aas.SubmodelElementCollection):

                class Identifier(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Identifier",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Identifier of the source."}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/SourceIdentifier/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Document(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"Document",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Reference to an external file representing the policy source."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/SourceDocument/1/0"
                            ),
                        }

                    def __init__(
                        self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class Link(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Link",
                            "value_type": xsd.AnyURI,
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Link to an external source."}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/SourceLink/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Reference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"Reference",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to a source in the same or an external Asset Administration Shell."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/SourceReference/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Source",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Describes the source of a policy."}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/Source/1/0"),
                    }

                def __init__(
                    self,
                    identifier: Union[str, Identifier],
                    document: Optional[Document] = None,
                    link: Optional[Union[xsd.AnyURI, Link]] = None,
                    reference: Optional[Union[aas.Reference, Reference]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if identifier is not None and not isinstance(identifier, aas.SubmodelElement):
                        identifier = self.Identifier(identifier)

                    # Build a submodel element if a raw value was passed in the argument

                    if link is not None and not isinstance(link, aas.SubmodelElement):
                        link = self.Link(link)

                    # Build a submodel element if a raw value was passed in the argument

                    if reference is not None and not isinstance(reference, aas.SubmodelElement):
                        reference = self.Reference(reference)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(identifier, document, link, reference)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class EffectiveFrom(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EffectiveFrom",
                        "value_type": xsd.DateTime,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Date and time that the policy is valid from."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/DataRetentionPolicies/EffectiveFrom/1/0"
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EffectiveUntil(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EffectiveUntil",
                        "value_type": xsd.DateTime,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Date and time until when the policy is valid."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/DataRetentionPolicies/EffectiveUntil/1/0"
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AuditLog(GeneratedSubmodelElementList):

                class Auditlog_item(aas.SubmodelElementCollection):

                    class Timestamp(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Timestamp",
                                "value_type": xsd.DateTime,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Time when the change was made."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DataRetentionPolicies/Timestamp/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Identity(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Identity",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Username or legal name of the entity that made the change."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DataRetentionPolicies/Identity/1/0"
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Operation(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Operation",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Description of the action taken."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DataRetentionPolicies/Operation/1/0"
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Reason(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Reason",
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Reason for the change."}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DataRetentionPolicies/Reason/1/0"
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Signature(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Signature",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Signature of the Policy after the change was made."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/DataRetentionPolicies/Signature/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"An activity related to the policy."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/DataRetentionPolicies/Activity/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        timestamp: Union[xsd.DateTime, Timestamp],
                        identity: Union[aas.LangStringSet, Identity],
                        operation: Union[aas.LangStringSet, Operation],
                        reason: Union[aas.LangStringSet, Reason],
                        signature: Union[str, Signature],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if timestamp is not None and not isinstance(timestamp, aas.SubmodelElement):
                            timestamp = self.Timestamp(timestamp)

                        # Build a submodel element if a raw value was passed in the argument

                        if identity is not None and not isinstance(identity, aas.SubmodelElement):
                            identity = self.Identity(identity)

                        # Build a submodel element if a raw value was passed in the argument

                        if operation is not None and not isinstance(operation, aas.SubmodelElement):
                            operation = self.Operation(operation)

                        # Build a submodel element if a raw value was passed in the argument

                        if reason is not None and not isinstance(reason, aas.SubmodelElement):
                            reason = self.Reason(reason)

                        # Build a submodel element if a raw value was passed in the argument

                        if signature is not None and not isinstance(signature, aas.SubmodelElement):
                            signature = self.Signature(signature)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            timestamp, identity, operation, reason, signature
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"AuditLog",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/DataRetentionPolicies/Activity/1/0"
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Activity log of changes to the policy."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/AuditLog/1/0"),
                    }

                def __init__(
                    self, auditlog_items: Iterable[Auditlog_item], **kwargs: Unpack[SubmodelElementListMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(auditlog_items, str):
                        raise TypeError("auditlog_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(auditlog_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Policy",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Describes a single data retention policy."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/Policy/1/0"),
                }

            def __init__(
                self,
                retentionTime: Union[xsd.Duration, RetentionTime],
                semanticIds: Union[Iterable[Union[aas.Reference, SemanticIds.Semanticids_item]], SemanticIds],
                immutable: Union[bool, Immutable],
                createdBy: Union[str, CreatedBy],
                creationTime: Union[xsd.DateTime, CreationTime],
                issuer: Union[str, Issuer],
                source: Source,
                effectiveFrom: Union[xsd.DateTime, EffectiveFrom],
                auditLog: Union[Iterable[AuditLog.Auditlog_item], AuditLog],
                overrides: Optional[Overrides] = None,
                effectiveUntil: Optional[Union[xsd.DateTime, EffectiveUntil]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if retentionTime is not None and not isinstance(retentionTime, aas.SubmodelElement):
                    retentionTime = self.RetentionTime(retentionTime)

                # A str would be split into its characters
                if isinstance(semanticIds, str):
                    raise TypeError("semanticIds takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if semanticIds is not None and not isinstance(semanticIds, aas.SubmodelElement):
                    semanticIds = self.SemanticIds(semanticIds)

                # Build a submodel element if a raw value was passed in the argument

                if immutable is not None and not isinstance(immutable, aas.SubmodelElement):
                    immutable = self.Immutable(immutable)

                # Build a submodel element if a raw value was passed in the argument

                if createdBy is not None and not isinstance(createdBy, aas.SubmodelElement):
                    createdBy = self.CreatedBy(createdBy)

                # Build a submodel element if a raw value was passed in the argument

                if creationTime is not None and not isinstance(creationTime, aas.SubmodelElement):
                    creationTime = self.CreationTime(creationTime)

                # Build a submodel element if a raw value was passed in the argument

                if issuer is not None and not isinstance(issuer, aas.SubmodelElement):
                    issuer = self.Issuer(issuer)

                # Build a submodel element if a raw value was passed in the argument

                if effectiveFrom is not None and not isinstance(effectiveFrom, aas.SubmodelElement):
                    effectiveFrom = self.EffectiveFrom(effectiveFrom)

                # Build a submodel element if a raw value was passed in the argument

                if effectiveUntil is not None and not isinstance(effectiveUntil, aas.SubmodelElement):
                    effectiveUntil = self.EffectiveUntil(effectiveUntil)

                # A str would be split into its characters
                if isinstance(auditLog, str):
                    raise TypeError("auditLog takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if auditLog is not None and not isinstance(auditLog, aas.SubmodelElement):
                    auditLog = self.AuditLog(auditLog)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    retentionTime,
                    semanticIds,
                    overrides,
                    immutable,
                    createdBy,
                    creationTime,
                    issuer,
                    source,
                    effectiveFrom,
                    effectiveUntil,
                    auditLog,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Policies",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Defines the set of policies."}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/DataRetentionPolicies/Policies/1/0"),
            }

        def __init__(
            self, policy: Optional[Iterable[Policy]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(policy, str):
                raise TypeError("policy takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(policy)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"DataRetentionPolicies",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel containing data retention policies for data elements in the Asset Administration Shell."
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/DataRetentionPolicies/1/0"
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        policies: Policies,
        inheritedFrom: Optional[Union[aas.Reference, InheritedFrom]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if inheritedFrom is not None and not isinstance(inheritedFrom, aas.SubmodelElement):
            inheritedFrom = self.InheritedFrom(inheritedFrom)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(inheritedFrom, policies)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
