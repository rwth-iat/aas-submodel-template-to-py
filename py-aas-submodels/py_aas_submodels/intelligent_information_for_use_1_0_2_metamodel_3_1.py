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


class IntelligentInformationforUse(aas.Submodel):

    class ResourceIRI(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"ResourceIRI",
                "value_type": xsd.AnyURI,
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                ),
                "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
            }

        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class FormatRestriction(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"FormatRestriction",
                "value_type": str,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"restriction of media formats allowed in an iiRDS package"}
                ),
                "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#formatRestriction"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class IirdsVersion(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"IirdsVersion",
                "value_type": str,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"iiRDS version with which the iiRDS package complies"}
                ),
                "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#iiRDSVersion"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class InformationUnitCollection(aas.SubmodelElementCollection):

        class Document(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Title(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"name of the information unit"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#title"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfCreation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfCreation",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"date of creation of the resource"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfCreation"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfLastModification(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfLastModification",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "date and time of an information unit's last change "}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfLastModification"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Language(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": "identifier of the content's language"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Revision(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Revision",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"version of an information unit"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#revision"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Rights(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Rights",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"declaration of specific rights regarding the usage of the information"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#rights"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasRendition(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasRendition",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Rendition"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its rendition"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-rendition"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasContentLifecycleStatus(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasContentLifecycleStatus",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ContentLifecycleStatus"
                                ),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its content lifecycle status"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-content-lifecycle-status"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class IsReplacementOf(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsReplacementOf",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing the information unit to be replaced"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#is-replacement-of"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IsVersionOf(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"IsVersionOf",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationObjectCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationObject"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its information object"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#is-version-of"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToEvent(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToEvent",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Event"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing an event"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-event"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToSupply(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToSupply",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Supply"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a supply"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-supply"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToQualification(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToQualification",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"SkillLevel"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a qualification "}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-qualification"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasIdentity(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasIdentity",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Identity"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing an identifier"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-identity"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToParty(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToParty",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing a party"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-party"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasDocumentType(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasDocumentType",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#InstallationInstructions",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "document's property referencing its document type"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-document-type"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToComponent(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToComponent",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Component"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a component"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-component"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasSubject(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasSubject",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#GenericTechnicalOverview",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its subject"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-subject"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToAction(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToAction",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Action"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing an action"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-action"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductFeature(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductFeature",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductFeature"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a product feature"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-product-feature"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductLifecyclePhase(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductLifecyclePhase",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductLifeCyclePhase"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-product-lifecycle-phase"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductVariant(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductVariant",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductVariant"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a product variant"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ProductVariant"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasPlanningTime(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasPlanningTime",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"WorkingTime"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-planning-time"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Document",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"information unit consisting of an ordered set of information intended by the sender to be regarded as an entity"
                        }
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Document"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                title: Optional[Union[str, Title]] = None,
                dateOfCreation: Optional[Union[str, DateOfCreation]] = None,
                dateOfLastModification: Optional[Union[str, DateOfLastModification]] = None,
                language: Optional[Iterable[Union[str, Language]]] = None,
                revision: Optional[Union[str, Revision]] = None,
                rights: Optional[Iterable[Union[aas.MultiLanguageTextType, Rights]]] = None,
                hasRendition: Optional[Iterable[HasRendition]] = None,
                hasContentLifecycleStatus: Optional[Iterable[HasContentLifecycleStatus]] = None,
                isReplacementOf: Optional[Union[str, IsReplacementOf]] = None,
                isVersionOf: Optional[IsVersionOf] = None,
                relatesToEvent: Optional[Iterable[RelatesToEvent]] = None,
                relatesToSupply: Optional[Iterable[RelatesToSupply]] = None,
                relatesToQualification: Optional[Iterable[RelatesToQualification]] = None,
                hasIdentity: Optional[Iterable[HasIdentity]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                hasDocumentType: Optional[Iterable[HasDocumentType]] = None,
                relatesToComponent: Optional[Iterable[RelatesToComponent]] = None,
                hasSubject: Optional[Iterable[HasSubject]] = None,
                relatesToAction: Optional[Iterable[RelatesToAction]] = None,
                relatesToProductFeature: Optional[Iterable[RelatesToProductFeature]] = None,
                relatesToProductLifecyclePhase: Optional[Iterable[RelatesToProductLifecyclePhase]] = None,
                relatesToProductVariant: Optional[Iterable[RelatesToProductVariant]] = None,
                hasPlanningTime: Optional[Iterable[HasPlanningTime]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfCreation is not None and not isinstance(dateOfCreation, aas.SubmodelElement):
                    dateOfCreation = self.DateOfCreation(dateOfCreation)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfLastModification is not None and not isinstance(dateOfLastModification, aas.SubmodelElement):
                    dateOfLastModification = self.DateOfLastModification(dateOfLastModification)

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if language:
                    language = [i if isinstance(i, aas.SubmodelElement) else self.Language(i) for i in language]

                # Build a submodel element if a raw value was passed in the argument

                if revision is not None and not isinstance(revision, aas.SubmodelElement):
                    revision = self.Revision(revision)

                # A str would be split into its characters
                if isinstance(rights, str):
                    raise TypeError("rights takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if rights:
                    rights = [i if isinstance(i, aas.SubmodelElement) else self.Rights(i) for i in rights]

                # A str would be split into its characters
                if isinstance(hasRendition, str):
                    raise TypeError("hasRendition takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasContentLifecycleStatus, str):
                    raise TypeError("hasContentLifecycleStatus takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if isReplacementOf is not None and not isinstance(isReplacementOf, aas.SubmodelElement):
                    isReplacementOf = self.IsReplacementOf(isReplacementOf)

                # A str would be split into its characters
                if isinstance(relatesToEvent, str):
                    raise TypeError("relatesToEvent takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToSupply, str):
                    raise TypeError("relatesToSupply takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToQualification, str):
                    raise TypeError("relatesToQualification takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasIdentity, str):
                    raise TypeError("hasIdentity takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToParty, str):
                    raise TypeError("relatesToParty takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasDocumentType, str):
                    raise TypeError("hasDocumentType takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToComponent, str):
                    raise TypeError("relatesToComponent takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasSubject, str):
                    raise TypeError("hasSubject takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToAction, str):
                    raise TypeError("relatesToAction takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductFeature, str):
                    raise TypeError("relatesToProductFeature takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductLifecyclePhase, str):
                    raise TypeError("relatesToProductLifecyclePhase takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductVariant, str):
                    raise TypeError("relatesToProductVariant takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasPlanningTime, str):
                    raise TypeError("hasPlanningTime takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    resourceIRI,
                    title,
                    dateOfCreation,
                    dateOfLastModification,
                    language,
                    revision,
                    rights,
                    hasRendition,
                    hasContentLifecycleStatus,
                    isReplacementOf,
                    isVersionOf,
                    relatesToEvent,
                    relatesToSupply,
                    relatesToQualification,
                    hasIdentity,
                    relatesToParty,
                    hasDocumentType,
                    relatesToComponent,
                    hasSubject,
                    relatesToAction,
                    relatesToProductFeature,
                    relatesToProductLifecyclePhase,
                    relatesToProductVariant,
                    hasPlanningTime,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Topic(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasTopicType(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasTopicType",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#GenericConcept",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its topic type"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-topic-type"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class IsVersionOf(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"IsVersionOf",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationObjectCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationObject"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its information object"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#is-version-of"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToQualification(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToQualification",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Role"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a qualification "}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-qualification"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductVariant(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductVariant",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductVariant"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a product variant"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ProductVariant"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class Title(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"name of the information unit"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#title"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfCreation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfCreation",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"date of creation of the resource"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfCreation"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfLastModification(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfLastModification",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "date and time of an information unit's last change "}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfLastModification"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Language(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": "identifier of the content's language"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Revision(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Revision",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"version of an information unit"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#revision"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Rights(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Rights",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"declaration of specific rights regarding the usage of the information"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#rights"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasRendition(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasRendition",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Rendition"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its rendition"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-rendition"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasContentLifecycleStatus(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasContentLifecycleStatus",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ContentLifecycleStatus"
                                ),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its content lifecycle status"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-content-lifecycle-status"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class IsReplacementOf(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsReplacementOf",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing the information unit to be replaced"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#is-replacement-of"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RelatesToEvent(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToEvent",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Event"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing an event"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-event"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToSupply(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToSupply",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Supply"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a supply"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-supply"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasIdentity(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasIdentity",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Identity"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing an identifier"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-identity"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToParty(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToParty",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing a party"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-party"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToComponent(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToComponent",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Component"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a component"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-component"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasSubject(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasSubject",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#GenericTechnicalOverview",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its subject"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-subject"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToAction(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToAction",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Action"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing an action"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-action"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductFeature(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductFeature",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductFeature"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a product feature"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-product-feature"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductLifecyclePhase(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductLifecyclePhase",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductLifeCyclePhase"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-product-lifecycle-phase"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class IsApplicableForDocumentType(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"IsApplicableForDocumentType",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#OperatingInstructions",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#is-applicable-for-document-type"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasPlanningTime(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasPlanningTime",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Topic"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"MaintenanceInterval"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-planning-time"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Topic",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"information unit covering a single subject"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Topic"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                hasTopicType: Optional[Iterable[HasTopicType]] = None,
                isVersionOf: Optional[IsVersionOf] = None,
                relatesToQualification: Optional[Iterable[RelatesToQualification]] = None,
                relatesToProductVariant: Optional[Iterable[RelatesToProductVariant]] = None,
                title: Optional[Union[str, Title]] = None,
                dateOfCreation: Optional[Union[str, DateOfCreation]] = None,
                dateOfLastModification: Optional[Union[str, DateOfLastModification]] = None,
                language: Optional[Iterable[Union[str, Language]]] = None,
                revision: Optional[Union[str, Revision]] = None,
                rights: Optional[Iterable[Union[aas.MultiLanguageTextType, Rights]]] = None,
                hasRendition: Optional[Iterable[HasRendition]] = None,
                hasContentLifecycleStatus: Optional[Iterable[HasContentLifecycleStatus]] = None,
                isReplacementOf: Optional[Union[str, IsReplacementOf]] = None,
                relatesToEvent: Optional[Iterable[RelatesToEvent]] = None,
                relatesToSupply: Optional[Iterable[RelatesToSupply]] = None,
                hasIdentity: Optional[Iterable[HasIdentity]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                relatesToComponent: Optional[Iterable[RelatesToComponent]] = None,
                hasSubject: Optional[Iterable[HasSubject]] = None,
                relatesToAction: Optional[Iterable[RelatesToAction]] = None,
                relatesToProductFeature: Optional[Iterable[RelatesToProductFeature]] = None,
                relatesToProductLifecyclePhase: Optional[Iterable[RelatesToProductLifecyclePhase]] = None,
                isApplicableForDocumentType: Optional[Iterable[IsApplicableForDocumentType]] = None,
                hasPlanningTime: Optional[Iterable[HasPlanningTime]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # A str would be split into its characters
                if isinstance(hasTopicType, str):
                    raise TypeError("hasTopicType takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToQualification, str):
                    raise TypeError("relatesToQualification takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductVariant, str):
                    raise TypeError("relatesToProductVariant takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfCreation is not None and not isinstance(dateOfCreation, aas.SubmodelElement):
                    dateOfCreation = self.DateOfCreation(dateOfCreation)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfLastModification is not None and not isinstance(dateOfLastModification, aas.SubmodelElement):
                    dateOfLastModification = self.DateOfLastModification(dateOfLastModification)

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if language:
                    language = [i if isinstance(i, aas.SubmodelElement) else self.Language(i) for i in language]

                # Build a submodel element if a raw value was passed in the argument

                if revision is not None and not isinstance(revision, aas.SubmodelElement):
                    revision = self.Revision(revision)

                # A str would be split into its characters
                if isinstance(rights, str):
                    raise TypeError("rights takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if rights:
                    rights = [i if isinstance(i, aas.SubmodelElement) else self.Rights(i) for i in rights]

                # A str would be split into its characters
                if isinstance(hasRendition, str):
                    raise TypeError("hasRendition takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasContentLifecycleStatus, str):
                    raise TypeError("hasContentLifecycleStatus takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if isReplacementOf is not None and not isinstance(isReplacementOf, aas.SubmodelElement):
                    isReplacementOf = self.IsReplacementOf(isReplacementOf)

                # A str would be split into its characters
                if isinstance(relatesToEvent, str):
                    raise TypeError("relatesToEvent takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToSupply, str):
                    raise TypeError("relatesToSupply takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasIdentity, str):
                    raise TypeError("hasIdentity takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToParty, str):
                    raise TypeError("relatesToParty takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToComponent, str):
                    raise TypeError("relatesToComponent takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasSubject, str):
                    raise TypeError("hasSubject takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToAction, str):
                    raise TypeError("relatesToAction takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductFeature, str):
                    raise TypeError("relatesToProductFeature takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductLifecyclePhase, str):
                    raise TypeError("relatesToProductLifecyclePhase takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(isApplicableForDocumentType, str):
                    raise TypeError("isApplicableForDocumentType takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasPlanningTime, str):
                    raise TypeError("hasPlanningTime takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    resourceIRI,
                    hasTopicType,
                    isVersionOf,
                    relatesToQualification,
                    relatesToProductVariant,
                    title,
                    dateOfCreation,
                    dateOfLastModification,
                    language,
                    revision,
                    rights,
                    hasRendition,
                    hasContentLifecycleStatus,
                    isReplacementOf,
                    relatesToEvent,
                    relatesToSupply,
                    hasIdentity,
                    relatesToParty,
                    relatesToComponent,
                    hasSubject,
                    relatesToAction,
                    relatesToProductFeature,
                    relatesToProductLifecyclePhase,
                    isApplicableForDocumentType,
                    hasPlanningTime,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Fragment(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RelatesToProductVariant(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductVariant",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductVariant"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a product variant"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ProductVariant"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class Title(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Title",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"name of the information unit"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#title"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfCreation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfCreation",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"date of creation of the resource"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfCreation"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfLastModification(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfLastModification",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "date and time of an information unit's last change "}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfLastModification"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Language(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Language",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": "identifier of the content's language"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#language"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Revision(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Revision",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"version of an information unit"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#revision"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Rights(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Rights",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"declaration of specific rights regarding the usage of the information"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#rights"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasRendition(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasRendition",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Rendition"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its rendition"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-rendition"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasContentLifecycleStatus(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasContentLifecycleStatus",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ContentLifecycleStatus"
                                ),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its content lifecycle status"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-content-lifecycle-status"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class IsReplacementOf(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsReplacementOf",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing the information unit to be replaced"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#is-replacement-of"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IsVersionOf(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"IsVersionOf",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationObjectCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationObject"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its information object"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#is-version-of"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToEvent(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToEvent",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Event"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing an event"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-event"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToQualification(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToQualification",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"SkillLevel"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a qualification "}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-qualification"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToSupply(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToSupply",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Supply"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a supply"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-supply"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasIdentity(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasIdentity",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Identity"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing an identifier"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-identity"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToParty(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToParty",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing a party"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-party"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToComponent(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToComponent",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Component"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a component"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-component"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasSubject(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasSubject",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#GenericTechnicalOverview",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing its subject"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-subject"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToAction(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToAction",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Action"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing an action"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-action"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductFeature(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductFeature",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductFeature"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "information unit's property referencing a product feature"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-product-feature"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToProductLifecyclePhase(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToProductLifecyclePhase",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Fragment"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductLifeCyclePhase"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-product-lifecycle-phase"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Fragment",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"information unit that requires additional context"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Fragment"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                relatesToProductVariant: Optional[Iterable[RelatesToProductVariant]] = None,
                title: Optional[Union[str, Title]] = None,
                dateOfCreation: Optional[Union[str, DateOfCreation]] = None,
                dateOfLastModification: Optional[Union[str, DateOfLastModification]] = None,
                language: Optional[Iterable[Union[str, Language]]] = None,
                revision: Optional[Union[str, Revision]] = None,
                rights: Optional[Iterable[Union[aas.MultiLanguageTextType, Rights]]] = None,
                hasRendition: Optional[Iterable[HasRendition]] = None,
                hasContentLifecycleStatus: Optional[Iterable[HasContentLifecycleStatus]] = None,
                isReplacementOf: Optional[Union[str, IsReplacementOf]] = None,
                isVersionOf: Optional[IsVersionOf] = None,
                relatesToEvent: Optional[Iterable[RelatesToEvent]] = None,
                relatesToQualification: Optional[Iterable[RelatesToQualification]] = None,
                relatesToSupply: Optional[Iterable[RelatesToSupply]] = None,
                hasIdentity: Optional[Iterable[HasIdentity]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                relatesToComponent: Optional[Iterable[RelatesToComponent]] = None,
                hasSubject: Optional[Iterable[HasSubject]] = None,
                relatesToAction: Optional[Iterable[RelatesToAction]] = None,
                relatesToProductFeature: Optional[Iterable[RelatesToProductFeature]] = None,
                relatesToProductLifecyclePhase: Optional[Iterable[RelatesToProductLifecyclePhase]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # A str would be split into its characters
                if isinstance(relatesToProductVariant, str):
                    raise TypeError("relatesToProductVariant takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfCreation is not None and not isinstance(dateOfCreation, aas.SubmodelElement):
                    dateOfCreation = self.DateOfCreation(dateOfCreation)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfLastModification is not None and not isinstance(dateOfLastModification, aas.SubmodelElement):
                    dateOfLastModification = self.DateOfLastModification(dateOfLastModification)

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if language:
                    language = [i if isinstance(i, aas.SubmodelElement) else self.Language(i) for i in language]

                # Build a submodel element if a raw value was passed in the argument

                if revision is not None and not isinstance(revision, aas.SubmodelElement):
                    revision = self.Revision(revision)

                # A str would be split into its characters
                if isinstance(rights, str):
                    raise TypeError("rights takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if rights:
                    rights = [i if isinstance(i, aas.SubmodelElement) else self.Rights(i) for i in rights]

                # A str would be split into its characters
                if isinstance(hasRendition, str):
                    raise TypeError("hasRendition takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasContentLifecycleStatus, str):
                    raise TypeError("hasContentLifecycleStatus takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if isReplacementOf is not None and not isinstance(isReplacementOf, aas.SubmodelElement):
                    isReplacementOf = self.IsReplacementOf(isReplacementOf)

                # A str would be split into its characters
                if isinstance(relatesToEvent, str):
                    raise TypeError("relatesToEvent takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToQualification, str):
                    raise TypeError("relatesToQualification takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToSupply, str):
                    raise TypeError("relatesToSupply takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasIdentity, str):
                    raise TypeError("hasIdentity takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToParty, str):
                    raise TypeError("relatesToParty takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToComponent, str):
                    raise TypeError("relatesToComponent takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasSubject, str):
                    raise TypeError("hasSubject takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToAction, str):
                    raise TypeError("relatesToAction takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductFeature, str):
                    raise TypeError("relatesToProductFeature takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(relatesToProductLifecyclePhase, str):
                    raise TypeError("relatesToProductLifecyclePhase takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    resourceIRI,
                    relatesToProductVariant,
                    title,
                    dateOfCreation,
                    dateOfLastModification,
                    language,
                    revision,
                    rights,
                    hasRendition,
                    hasContentLifecycleStatus,
                    isReplacementOf,
                    isVersionOf,
                    relatesToEvent,
                    relatesToQualification,
                    relatesToSupply,
                    hasIdentity,
                    relatesToParty,
                    relatesToComponent,
                    hasSubject,
                    relatesToAction,
                    relatesToProductFeature,
                    relatesToProductLifecyclePhase,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"InformationUnitCollection",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"collection of instances of iirds:topic, iirds:document and iirds:fragment, which are subclasses of iirds:informationunit"
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/IntelligentInformationForUse/InformationUnitCollection/1/0"
                ),
            }

        def __init__(
            self,
            document: Optional[Iterable[Document]] = None,
            topic: Optional[Iterable[Topic]] = None,
            fragment: Optional[Iterable[Fragment]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(document, str):
                raise TypeError("document takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(topic, str):
                raise TypeError("topic takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(fragment, str):
                raise TypeError("fragment takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(document, topic, fragment)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class InformationObjectCollection(aas.SubmodelElementCollection):

        class InformationObject(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InformationObject",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"version- and language-independent abstraction of an information unit"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#InformationObject"),
                }

            def __init__(
                self, resourceIRI: Union[xsd.AnyURI, ResourceIRI], **kwargs: Unpack[SubmodelElementCollectionMetadata]
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"InformationObjectCollection",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"collection of iirds:InformationObject instances"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/IntelligentInformationForUse/InformationObjectCollection/1/0"
                ),
            }

        def __init__(
            self,
            informationObject: Optional[Iterable[InformationObject]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(informationObject, str):
                raise TypeError("informationObject takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(informationObject)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DirectoryNodeCollection(aas.SubmodelElementCollection):

        class DirectoryNode(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r'http://iirds.tekom.de/iirds#ResourceIRI">'),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RelatesToInformationUnit(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToInformationUnit",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"DirectoryNodeCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"DirectoryNode"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"InformationUnitCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Document"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "directory node's property referencing the corresponding information unit"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-information-unit"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasNextSibling(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"HasNextSibling",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "directory node's property referencing the following directory node on the same hierarchy level in a directory structure Verweist auf den folgenden Verzeichniseintrag einer Verzeichnisstruktur auf gleicher Ebene."
                            }
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-next-sibling"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class HasFirstChild(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"HasFirstChild",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "directory node's property referencing the first directory node on the next subordinate level in a directory structure"
                            }
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-first-child"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class HasDirectoryStructureType(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasDirectoryStructureType",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"DirectoryNodeCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"DirectoryNode"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#TableOfContents",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "directory node's property referencing its node type"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-directory-structure-type"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human- readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DirectoryNode",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"node in a tree-like, ordered collection"}),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#DirectoryNode"),
                }

            def __init__(
                self,
                resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                relatesToInformationUnit: Optional[RelatesToInformationUnit] = None,
                hasNextSibling: Optional[HasNextSibling] = None,
                hasFirstChild: Optional[HasFirstChild] = None,
                hasDirectoryStructureType: Optional[HasDirectoryStructureType] = None,
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    resourceIRI,
                    relatesToInformationUnit,
                    hasNextSibling,
                    hasFirstChild,
                    hasDirectoryStructureType,
                    label,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DirectoryNodeCollection",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"collection of iirds:DirectoryNode instances"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/IntelligentInformationForUse/DirectoryNodeCollection/1/0"
                ),
            }

        def __init__(
            self,
            directoryNode: Optional[Iterable[DirectoryNode]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(directoryNode, str):
                raise TypeError("directoryNode takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(directoryNode)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class RenditionCollection(aas.SubmodelElementCollection):

        class Rendition(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Format(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Format",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"media type of the rendition"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#format"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Source(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"Source",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"relative path of a file in the iiRDS package, containing the content of a rendition"
                            }
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#source"),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class HasSelector(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasSelector",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Rendition"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"FragmentSelector"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "rendition's property referencing a selector"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-selector"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RangeSelector(aas.SubmodelElementCollection):

                class ResourceIRI(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ResourceIRI",
                            "value_type": xsd.AnyURI,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                            ),
                            "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                        }

                    def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class HasStartSelector(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"HasStartSelector",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RangeSelector"),
                                    aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                                ),
                                type_=aas.Property,
                                referred_semantic_id=None,
                            ),
                            "second": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"FragmentSelector"),
                                    aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                                ),
                                type_=aas.Property,
                                referred_semantic_id=None,
                            ),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": "range selector's property referencing the start of its range"}
                            ),
                            "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-start-selector"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                class HasEndSelector(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"HasEndSelector",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RangeSelector"),
                                    aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                                ),
                                type_=aas.Property,
                                referred_semantic_id=None,
                            ),
                            "second": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"RenditionCollection"
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"FragmentSelector"),
                                    aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                                ),
                                type_=aas.Property,
                                referred_semantic_id=None,
                            ),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": "range selector's property referencing the end of its range"}
                            ),
                            "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-end-selector"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"RangeSelector",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"selector defining the start point and the end point of a part of content"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#RangeSelector"),
                    }

                def __init__(
                    self,
                    hasStartSelector: HasStartSelector,
                    hasEndSelector: HasEndSelector,
                    resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                        resourceIRI = self.ResourceIRI(resourceIRI)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        resourceIRI, hasStartSelector, hasEndSelector
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class FragmentSelector(aas.SubmodelElementCollection):

                class ResourceIRI(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ResourceIRI",
                            "value_type": xsd.AnyURI,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                            ),
                            "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                        }

                    def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ConformsTo(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ConformsTo",
                            "value_type": str,
                            "category": r"CONSTANT",
                            "semantic_id": global_ref(r"http://purl.org/dc/terms/conformsTo"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Value(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Value",
                            "value_type": str,
                            "category": r"CONSTANT",
                            "semantic_id": global_ref(r"https://www.w3.org/TR/rdf12-schema/#ch_value"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"FragmentSelector",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"selector defining a part of content by a single identifier"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#FragmentSelector"),
                    }

                def __init__(
                    self,
                    conformsTo: Union[str, ConformsTo],
                    value_: Union[str, Value],
                    resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                        resourceIRI = self.ResourceIRI(resourceIRI)

                    # Build a submodel element if a raw value was passed in the argument

                    if conformsTo is not None and not isinstance(conformsTo, aas.SubmodelElement):
                        conformsTo = self.ConformsTo(conformsTo)

                    # Build a submodel element if a raw value was passed in the argument

                    if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                        value_ = self.Value(value_)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(resourceIRI, conformsTo, value_)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Rendition",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"content of an information unit in a specific format"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Rendition"),
                }

            def __init__(
                self,
                format: Union[str, Format],
                source: Source,
                resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                hasSelector: Optional[HasSelector] = None,
                rangeSelector: Optional[Iterable[RangeSelector]] = None,
                fragmentSelector: Optional[Iterable[FragmentSelector]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if format is not None and not isinstance(format, aas.SubmodelElement):
                    format = self.Format(format)

                # A str would be split into its characters
                if isinstance(rangeSelector, str):
                    raise TypeError("rangeSelector takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(fragmentSelector, str):
                    raise TypeError("fragmentSelector takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    resourceIRI, format, source, hasSelector, rangeSelector, fragmentSelector
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"RenditionCollection",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"collection of iirds:Rendition instances"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/IntelligentInformationForUse/RenditionCollection/1/0"
                ),
            }

        def __init__(
            self, rendition: Optional[Iterable[Rendition]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(rendition, str):
                raise TypeError("rendition takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(rendition)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class AdministrativeMetadataCollection(aas.SubmodelElementCollection):

        class ContentLifecycleStatus(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfEffect(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfEffect",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"date and time on which the given content"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfEffect"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfExpiry(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfExpiry",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"date and time on which the given content lifecycle status becomes invalid"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfExpiry"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DateOfStatus(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DateOfStatus",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "date and time of a lifecycle status's last change"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#dateOfStatus"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StatusComment(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusComment",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"note on a content lifecycle status"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#statusComment"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Purpose(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Purpose",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "reason for an information unit's lifecycle status"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#purpose"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasContentLifecycleStatusValue(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasContentLifecycleStatusValue",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ContentLifecycleStatus"
                                ),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#Approved",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "content lifecycle status's property referencing its value"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-content-lifecycle-status-value"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToParty(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToParty",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ContentLifecycleStatus"
                                ),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing a party"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-party"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ContentLifecycleStatus",
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ContentLifeCycleStatus"),
                }

            def __init__(
                self,
                hasContentLifecycleStatusValue: HasContentLifecycleStatusValue,
                resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                dateOfEffect: Optional[Union[str, DateOfEffect]] = None,
                dateOfExpiry: Optional[Union[str, DateOfExpiry]] = None,
                dateOfStatus: Optional[Union[str, DateOfStatus]] = None,
                statusComment: Optional[Iterable[Union[str, StatusComment]]] = None,
                purpose: Optional[Union[str, Purpose]] = None,
                relatesToParty: Optional[RelatesToParty] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfEffect is not None and not isinstance(dateOfEffect, aas.SubmodelElement):
                    dateOfEffect = self.DateOfEffect(dateOfEffect)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfExpiry is not None and not isinstance(dateOfExpiry, aas.SubmodelElement):
                    dateOfExpiry = self.DateOfExpiry(dateOfExpiry)

                # Build a submodel element if a raw value was passed in the argument

                if dateOfStatus is not None and not isinstance(dateOfStatus, aas.SubmodelElement):
                    dateOfStatus = self.DateOfStatus(dateOfStatus)

                # A str would be split into its characters
                if isinstance(statusComment, str):
                    raise TypeError("statusComment takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if statusComment:
                    statusComment = [
                        i if isinstance(i, aas.SubmodelElement) else self.StatusComment(i) for i in statusComment
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if purpose is not None and not isinstance(purpose, aas.SubmodelElement):
                    purpose = self.Purpose(purpose)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    resourceIRI,
                    dateOfEffect,
                    dateOfExpiry,
                    dateOfStatus,
                    statusComment,
                    purpose,
                    hasContentLifecycleStatusValue,
                    relatesToParty,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Identity(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Identifier(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Identifier",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"unique name of the resource within a given domain"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#identifier"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasIdentityDomain(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasIdentityDomain",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Identity"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"IdentityDomain"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "identifier's property referencing the domain in which it is unique"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-identity-domain"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Identity",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"complex identifier of a resource in an external system"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Identity"),
                }

            def __init__(
                self,
                identifier: Union[str, Identifier],
                hasIdentityDomain: HasIdentityDomain,
                resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if identifier is not None and not isinstance(identifier, aas.SubmodelElement):
                    identifier = self.Identifier(identifier)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, identifier, hasIdentityDomain)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Party(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasPartyRole(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasPartyRole",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"http://iirds.tekom.de/iirds#Manufacturer",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "party's property referencing its role"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-party-role"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToVcard(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToVcard",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"VCard"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "party's property referencing an organization or person"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-vcard"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Party",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"person, organization or system"}),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Party"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                hasPartyRole: Optional[HasPartyRole] = None,
                relatesToVcard: Optional[RelatesToVcard] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, hasPartyRole, relatesToVcard)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class IdentityDomain(aas.SubmodelElementCollection):

            class HasIdentityType(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasIdentityType",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"IdentityDomain"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"IdentityType "),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"distinguished set of identifiers that are assigned to an iiRDS identity"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#IdentityType"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class RelatesToParty(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToParty",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"IdentityDomain"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing a party"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-party"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"IdentityDomain",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"organizational origin of an identifier that is assigned to an iiRDS identity"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#IdentityDomain"),
                }

            def __init__(
                self,
                hasIdentityType: Optional[HasIdentityType] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(relatesToParty, str):
                    raise TypeError("relatesToParty takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(hasIdentityType, relatesToParty)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class IdentityType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IdentityType",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"distinguished set of identifiers that are assigned to an iiRDS identity"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#IdentityType"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class VCard(aas.SubmodelElementCollection):

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"VCard",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"vCard is a file format standard for electronic business cards"}
                    ),
                    "semantic_id": global_ref(r"http://www.w3.org/2006/vcard/ns#Kind"),
                }

            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AdministrativeMetadataCollection",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"collection of instances of the subclasses of iirds:AdministrativeMetadata"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/IntelligentInformationForUse/AdministrativeMetadataCollection/1/0"
                ),
            }

        def __init__(
            self,
            contentLifecycleStatus: Optional[Iterable[ContentLifecycleStatus]] = None,
            identity: Optional[Iterable[Identity]] = None,
            party: Optional[Iterable[Party]] = None,
            identityDomain: Optional[Iterable[IdentityDomain]] = None,
            identityType: Optional[Iterable[Union[str, IdentityType]]] = None,
            vCard: Optional[Iterable[VCard]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(contentLifecycleStatus, str):
                raise TypeError("contentLifecycleStatus takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(identity, str):
                raise TypeError("identity takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(party, str):
                raise TypeError("party takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(identityDomain, str):
                raise TypeError("identityDomain takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(identityType, str):
                raise TypeError("identityType takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if identityType:
                identityType = [i if isinstance(i, aas.SubmodelElement) else self.IdentityType(i) for i in identityType]

            # A str would be split into its characters
            if isinstance(vCard, str):
                raise TypeError("vCard takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                contentLifecycleStatus, identity, party, identityDomain, identityType, vCard
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FunctionalMetadataCollection(aas.SubmodelElementCollection):

        class Supply(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Supply",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"physical object used by an actor performing work tasks described in technical documentation"
                        }
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Supply"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Event(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HasEventCode(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasEventCode",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Event"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"EventCode"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"property to identify an event"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-event-code"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class HasEventType(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"HasEventType",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Event"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FunctionalMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"EventType"),
                            ),
                            type_=aas.SubmodelElementCollection,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "event's property referencing its type"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#has-event-type"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Event",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"something noticeable that takes place at a given location and point in time"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Event"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                hasEventCode: HasEventCode,
                hasEventType: HasEventType,
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, hasEventCode, hasEventType, label)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class EventCode(aas.SubmodelElementCollection):

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"EventCode",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"property to identify an event"}),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#EventCode"),
                }

            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class EventType(aas.SubmodelElementCollection):

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"EventType",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": "event's property referencing its type"}),
                    "semantic_id": global_ref("event's property referencing its type"),
                }

            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Role(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Role",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"set of connected behaviors, privileges and obligations associated with a party"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Role"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class SkillLevel(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"SkillLevel",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"degree of qualification of an individual"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#SkillLevel"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Action(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Action",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"atomic manipulation of an object by a participant"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Action"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class WorkingTime(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Duration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Duration",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"span of time"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#duration"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"WorkingTime",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"period of time that is required for conducting a specific task"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#WorkingTime"),
                }

            def __init__(
                self,
                duration: Union[str, Duration],
                resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Build a submodel element if a raw value was passed in the argument

                if duration is not None and not isinstance(duration, aas.SubmodelElement):
                    duration = self.Duration(duration)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label, duration)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class MaintenanceInterval(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Frequency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Frequency",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"intended interval between recurring maintanance tasks"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#frequency"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Duration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Duration",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"span of time"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#duration"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"MaintenanceInterval",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"period of time between scheduled maintenance operations"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#MaintenanceInterval"),
                }

            def __init__(
                self,
                frequency: Union[str, Frequency],
                duration: Union[str, Duration],
                resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Build a submodel element if a raw value was passed in the argument

                if frequency is not None and not isinstance(frequency, aas.SubmodelElement):
                    frequency = self.Frequency(frequency)

                # Build a submodel element if a raw value was passed in the argument

                if duration is not None and not isinstance(duration, aas.SubmodelElement):
                    duration = self.Duration(duration)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label, frequency, duration)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class DownTime(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Duration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Duration",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"span of time"}),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#duration"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DownTime",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"period of time during which an item is not in condition to perform its intended function"
                        }
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#DownTime"),
                }

            def __init__(
                self,
                duration: Union[str, Duration],
                resourceIRI: Optional[Union[xsd.AnyURI, ResourceIRI]] = None,
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Build a submodel element if a raw value was passed in the argument

                if duration is not None and not isinstance(duration, aas.SubmodelElement):
                    duration = self.Duration(duration)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label, duration)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"FunctionalMetadataCollection",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"collection of instances of the subclasses of iirds:FunctionalMetadata"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/IntelligentInformationForUse/FunctionalMetadataCollection/1/0"
                ),
            }

        def __init__(
            self,
            supply: Optional[Iterable[Supply]] = None,
            event: Optional[Iterable[Event]] = None,
            eventCode: Optional[Iterable[EventCode]] = None,
            eventType: Optional[Iterable[EventType]] = None,
            role: Optional[Iterable[Role]] = None,
            skillLevel: Optional[Iterable[SkillLevel]] = None,
            action: Optional[Iterable[Action]] = None,
            workingTime: Optional[Iterable[WorkingTime]] = None,
            maintenanceInterval: Optional[Iterable[MaintenanceInterval]] = None,
            downTime: Optional[Iterable[DownTime]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(supply, str):
                raise TypeError("supply takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(event, str):
                raise TypeError("event takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(eventCode, str):
                raise TypeError("eventCode takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(eventType, str):
                raise TypeError("eventType takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(role, str):
                raise TypeError("role takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(skillLevel, str):
                raise TypeError("skillLevel takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(action, str):
                raise TypeError("action takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(workingTime, str):
                raise TypeError("workingTime takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(maintenanceInterval, str):
                raise TypeError("maintenanceInterval takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(downTime, str):
                raise TypeError("downTime takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                supply,
                event,
                eventCode,
                eventType,
                role,
                skillLevel,
                action,
                workingTime,
                maintenanceInterval,
                downTime,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ProductMetadataCollection(aas.SubmodelElementCollection):

        class Component(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Asset(aas.Entity):

                @staticmethod
                def template_defaults() -> EntityMetadata:
                    return {
                        "id_short": r"Asset",
                        "entity_type": aas.EntityType.SELF_MANAGED_ENTITY,
                        "global_asset_id": r"externalAsset",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Entity in terms of the asset administration shell"}
                        ),
                    }

                def __init__(self, **kwargs: Unpack[EntityMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RelatesToParty(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToParty",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Component"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing a party"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-party"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Component",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"part used as a constituent in an assembled product, system or plant"}
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#Component"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                asset: Optional[Iterable[Asset]] = None,
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # A str would be split into its characters
                if isinstance(asset, str):
                    raise TypeError("asset takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # A str would be split into its characters
                if isinstance(relatesToParty, str):
                    raise TypeError("relatesToParty takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, asset, label, relatesToParty)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ProductFeature(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ProductFeature",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"product characteristics"}),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ProductFeature"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ProductLifeCyclePhase(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ProductLifeCyclePhase",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Defined period in the evolution of a product from the conceptual idea to its ultimate disposal"
                        }
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ProductLifeCyclePhase"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ProductVariant(aas.SubmodelElementCollection):

            class ResourceIRI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResourceIRI",
                        "value_type": xsd.AnyURI,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identifies instances of the iirds:classes and subclasses"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ResourceIRI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Label(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Label",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "used to provide a human-readable version of a resource's name"}
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2000/01/rdf-schema#label"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RelatesToParty(aas.RelationshipElement):

                @staticmethod
                def template_defaults() -> RelationshipElementMetadata:
                    return {
                        "id_short": r"RelatesToParty",
                        "first": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductMetadataCollection"
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"ProductVariant"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "second": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL, value=r"https://example.com/ids/sm/1154_0130_2032_3996"
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"AdministrativeMetadataCollection",
                                ),
                                aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Party"),
                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=aas.Property,
                            referred_semantic_id=None,
                        ),
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "iiRDS resource's property referencing a party"}
                        ),
                        "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#relates-to-party"),
                    }

                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ProductVariant",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"item or service offered on the market and designed to meet the needs or wishes of customers"
                        }
                    ),
                    "semantic_id": global_ref(r"http://iirds.tekom.de/iirds#ProductVariant"),
                }

            def __init__(
                self,
                resourceIRI: Union[xsd.AnyURI, ResourceIRI],
                label: Optional[Union[aas.MultiLanguageTextType, Label]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument

                if label is not None and not isinstance(label, aas.SubmodelElement):
                    label = self.Label(label)

                # A str would be split into its characters
                if isinstance(relatesToParty, str):
                    raise TypeError("relatesToParty takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(resourceIRI, label, relatesToParty)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ProductMetadataCollection",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"collection of instances of the subclasses of iirds:ProductMetadata"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/IntelligentInformationForUse/ProductMetadataCollection/1/0"
                ),
            }

        def __init__(
            self,
            component: Optional[Iterable[Component]] = None,
            productFeature: Optional[Iterable[ProductFeature]] = None,
            productLifeCyclePhase: Optional[Iterable[ProductLifeCyclePhase]] = None,
            productVariant: Optional[Iterable[ProductVariant]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(component, str):
                raise TypeError("component takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(productFeature, str):
                raise TypeError("productFeature takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(productLifeCyclePhase, str):
                raise TypeError("productLifeCyclePhase takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(productVariant, str):
                raise TypeError("productVariant takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                component, productFeature, productLifeCyclePhase, productVariant
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"IntelligentInformationforUse",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"This Submodel template aims at interoperable provision of information describing the provisioning of “Intelligent Information for Use”, i.e. information of the Technical Documentation enriched by metadata based on the iiRDS"
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02063-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/IntelligentInformationForUse/1/0"),
        }

    def __init__(
        self,
        id_: str,
        resourceIRI: Union[xsd.AnyURI, ResourceIRI],
        iirdsVersion: Union[str, IirdsVersion],
        formatRestriction: Optional[Union[str, FormatRestriction]] = None,
        informationUnitCollection: Optional[InformationUnitCollection] = None,
        informationObjectCollection: Optional[InformationObjectCollection] = None,
        directoryNodeCollection: Optional[DirectoryNodeCollection] = None,
        renditionCollection: Optional[RenditionCollection] = None,
        administrativeMetadataCollection: Optional[AdministrativeMetadataCollection] = None,
        functionalMetadataCollection: Optional[FunctionalMetadataCollection] = None,
        productMetadataCollection: Optional[ProductMetadataCollection] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if resourceIRI is not None and not isinstance(resourceIRI, aas.SubmodelElement):
            resourceIRI = self.ResourceIRI(resourceIRI)

        # Build a submodel element if a raw value was passed in the argument

        if formatRestriction is not None and not isinstance(formatRestriction, aas.SubmodelElement):
            formatRestriction = self.FormatRestriction(formatRestriction)

        # Build a submodel element if a raw value was passed in the argument

        if iirdsVersion is not None and not isinstance(iirdsVersion, aas.SubmodelElement):
            iirdsVersion = self.IirdsVersion(iirdsVersion)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            resourceIRI,
            formatRestriction,
            iirdsVersion,
            informationUnitCollection,
            informationObjectCollection,
            directoryNodeCollection,
            renditionCollection,
            administrativeMetadataCollection,
            functionalMetadataCollection,
            productMetadataCollection,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
