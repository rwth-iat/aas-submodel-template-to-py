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


class HierarchicalStructures(aas.Submodel):

    class EntryNode(aas.Entity):

        class Node(aas.Entity):

            class Node(aas.Entity):

                @staticmethod
                def template_defaults() -> EntityMetadata:
                    return {
                        "id_short": r"Node",
                        "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                        "global_asset_id": r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Can be a Co-managed or Self-managed entity. A Node reflects an element in the hierarchical model is set into relation with one or more defined relations. The name of a node can be picked freely but it must be unique in its hierarchical (sub-)level."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/Node/1/0"),
                    }

                def __init__(self, **kwargs: Unpack[EntityMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SameAs(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"SameAs",
                        "first": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                        "second": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Reference between two Entities in the same Submodel or across Submodels."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class IsPartOf(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"IsPartOf",
                        "first": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                        "second": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'Modeling of logical connections between components and sub-components. Either this or "HasPart" must be used, not both.'
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasPart(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasPart",
                        "first": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                        "second": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'Modeling of logical connections between components and sub-components. Either this or "IsPartOf" must be used, not both.'
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class BulkCount(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BulkCount",
                        "value_type": xsd.UnsignedLong,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"To be used if bulk components are referenced, e.g., a 10x M4x30 screw."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0"),
                    }

                def __init__(self, value: xsd.UnsignedLong, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"Node",
                    "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                    "global_asset_id": r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the Asset Administration Shell this Submodel is part of. The idShort of the EntryNode can be picked freely and may reflect a name of the asset."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/Node/1/0"),
                }

            def __init__(
                self,
                node: Optional[Iterable[Node]] = None,
                sameAs: Optional[Iterable[SameAs]] = None,
                isPartOf: Optional[Iterable[IsPartOf]] = None,
                hasPart: Optional[Iterable[HasPart]] = None,
                bulkCount: Optional[Union[xsd.UnsignedLong, BulkCount]] = None,
                **kwargs: Unpack[EntityMetadata],
            ):

                # A str would be split into its characters
                if isinstance(node, str):
                    raise TypeError("node takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(sameAs, str):
                    raise TypeError("sameAs takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(isPartOf, str):
                    raise TypeError("isPartOf takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasPart, str):
                    raise TypeError("hasPart takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if bulkCount is not None and not isinstance(bulkCount, aas.SubmodelElement):
                    bulkCount = self.BulkCount(bulkCount)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(node, sameAs, isPartOf, hasPart, bulkCount)

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class SameAs(aas.RelationshipElement):

            @staticmethod
            def template_defaults() -> RelationshipElementMetadata:
                return {
                    "id_short": r"SameAs",
                    "first": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                    "second": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Reference between two Entities in the same Submodel or across Submodels."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0"),
                }

            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                super().__init__(**(self.template_defaults() | kwargs))

        class IsPartOf(aas.RelationshipElement):

            @staticmethod
            def template_defaults() -> RelationshipElementMetadata:
                return {
                    "id_short": r"IsPartOf",
                    "first": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                    "second": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r'Modeling of logical connections between asset and sub-asset. Either this or "HasPart" must be used, not both.'
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0"),
                }

            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                super().__init__(**(self.template_defaults() | kwargs))

        class HasPart(aas.RelationshipElement):

            @staticmethod
            def template_defaults() -> RelationshipElementMetadata:
                return {
                    "id_short": r"HasPart",
                    "first": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                    "second": global_ref(r"https://admin-shell.io/SMT/General/IntentionallyEmpty"),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r'Modeling of logical connections between components and sub-components. Either this or "IsPartOf" must be used, not both.'
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0"),
                }

            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                super().__init__(**(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> EntityMetadata:
            return {
                "id_short": r"EntryNode",
                "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                "global_asset_id": r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the AAS this Submodel is part of."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"),
            }

        def __init__(
            self,
            node: Iterable[Node],
            sameAs: Optional[Iterable[SameAs]] = None,
            isPartOf: Optional[Iterable[IsPartOf]] = None,
            hasPart: Optional[Iterable[HasPart]] = None,
            **kwargs: Unpack[EntityMetadata],
        ):

            # A str would be split into its characters
            if isinstance(node, str):
                raise TypeError("node takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(sameAs, str):
                raise TypeError("sameAs takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(isPartOf, str):
                raise TypeError("isPartOf takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(hasPart, str):
                raise TypeError("hasPart takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(node, sameAs, isPartOf, hasPart)

            super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ArcheType(aas.Property):

        ALLOWED_VALUES = (r"Full", r"OneDown", r"OneUp")

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"ArcheType",
                "value_type": str,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"ArcheType of the Submodel, there are three allowed enumeration entries: 1. “Full”, 2. “OneDown” and 3. “OneUp”. "
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/HierarchicalStructures/ArcheType/1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            if value is not None and value not in self.ALLOWED_VALUES:
                raise ValueError(
                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                )

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"HierarchicalStructures",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel HierarchicalStructures identified by its semanticId. The Submodel idShort can be picked freely."
                }
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/HierarchicalStructures/1/1/Submodel",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self, id_: str, entryNode: EntryNode, archeType: Union[str, ArcheType], **kwargs: Unpack[SubmodelMetadata]
    ):

        # Build a submodel element if a raw value was passed in the argument

        if archeType is not None and not isinstance(archeType, aas.SubmodelElement):
            archeType = self.ArcheType(archeType)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(entryNode, archeType)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
