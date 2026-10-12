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


class CapabilityMetadata(TypedDict, total=False):
    """Metadata of aas.Capability, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
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


class CapabilityDescription(aas.Submodel):

    class CapabilitySet(aas.SubmodelElementCollection):

        class CapabilityContainer(aas.SubmodelElementCollection):

            class Capability(aas.Capability):

                @staticmethod
                def template_defaults() -> CapabilityMetadata:
                    return {
                        "id_short": r"Capability",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"[A capability is a] implementation-independent specification of a function in industrial production to achieve an effect in the physical or virtual world. "
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CapabilityDescription/Capability/1/0"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"Required",
                                value_type=str,
                                value=r"[1, 0]",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/Required/1/0"
                                ),
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Offered",
                                value_type=str,
                                value=r"[1, 0]",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/Offered/1/0"
                                ),
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"NotAssigned",
                                value_type=str,
                                value=r"[1, 0]",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/NotAssigned/1/0"
                                ),
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, **kwargs: Unpack[CapabilityMetadata]):

                    super().__init__(**(self.template_defaults() | kwargs))

            class CapabilityComment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"CapabilityComment",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability Comment"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Individual comment of the capability."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CapabilityDescription/CapabilityComment/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PropertySet(aas.SubmodelElementCollection):

                class PropertyContainer(aas.SubmodelElementCollection):

                    class SameProperty(aas.RelationshipElement):

                        @staticmethod
                        def template_defaults() -> RelationshipElementMetadata:
                            return {
                                "id_short": r"SameProperty",
                                "first": global_ref(r"urn:example:capability-description:same-property:first"),
                                "second": global_ref(r"urn:example:capability-description:same-property:second"),
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Same Property"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Relationship of the Property described in the Property container as first element and the identical property as second element in another Submodel or an external information source."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/SameProperty/1/0"
                                ),
                            }

                        def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                            super().__init__(**(self.template_defaults() | kwargs))

                    class PropertyRange(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"PropertyRange",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Property Range"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Range made of min and max values forming an interval. A valueId shall be set to define the semantic for the values."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityPropertyEnumType/Range/1/0"
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class PropertyProperty(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"PropertyProperty",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Property Property"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Property with a value describing an information data point. A valueId shall be set to define the semantic for the value."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityPropertyType/Property/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class PropertyMultiLanguageProperty(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"PropertyMultiLanguageProperty",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Property Multi Language Property"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Property with a value for one or more language entries with corresponding text describing an information data point. A valueId shall be set to define the semantic for the value."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityPropertyType/MultiLanguageProperty/1/0"
                                ),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class PropertyComment(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"PropertyComment",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Property Comment"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"General description of the property."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/PropertyComment/1/0"
                                ),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"PropertyContainer",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Property Container"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information for a certain property as defined by CapabilityPropertyType and its descriptive elements."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CapabilityDescription/PropertyContainer/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        sameProperty: Optional[Iterable[SameProperty]] = None,
                        propertyRange: Optional[Iterable[Union[Tuple[str, str], PropertyRange]]] = None,
                        propertyProperty: Optional[Iterable[Union[str, PropertyProperty]]] = None,
                        propertyMultiLanguageProperty: Optional[
                            Iterable[Union[aas.MultiLanguageTextType, PropertyMultiLanguageProperty]]
                        ] = None,
                        propertyComment: Optional[Union[aas.MultiLanguageTextType, PropertyComment]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(sameProperty, str):
                            raise TypeError("sameProperty takes several elements, got a str")

                        # A str would be split into its characters
                        if isinstance(propertyRange, str):
                            raise TypeError("propertyRange takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if propertyRange:
                            propertyRange = [
                                i if isinstance(i, aas.SubmodelElement) else self.PropertyRange(min=i[0], max=i[1])
                                for i in propertyRange
                            ]

                        # A str would be split into its characters
                        if isinstance(propertyProperty, str):
                            raise TypeError("propertyProperty takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if propertyProperty:
                            propertyProperty = [
                                i if isinstance(i, aas.SubmodelElement) else self.PropertyProperty(i)
                                for i in propertyProperty
                            ]

                        # A str would be split into its characters
                        if isinstance(propertyMultiLanguageProperty, str):
                            raise TypeError("propertyMultiLanguageProperty takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if propertyMultiLanguageProperty:
                            propertyMultiLanguageProperty = [
                                i if isinstance(i, aas.SubmodelElement) else self.PropertyMultiLanguageProperty(i)
                                for i in propertyMultiLanguageProperty
                            ]

                        # Build a submodel element if a raw value was passed in the argument

                        if propertyComment is not None and not isinstance(propertyComment, aas.SubmodelElement):
                            propertyComment = self.PropertyComment(propertyComment)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            sameProperty,
                            propertyRange,
                            propertyProperty,
                            propertyMultiLanguageProperty,
                            propertyComment,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"PropertySet",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Property Set"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Set of properties describing the capability in more detail, if existing."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CapabilityDescription/PropertySet/1/0"),
                    }

                def __init__(
                    self,
                    propertyContainer: Iterable[PropertyContainer],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(propertyContainer, str):
                        raise TypeError("propertyContainer takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(propertyContainer)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class CapabilityRelations(aas.SubmodelElementCollection):

                class CapabilityRealizedBy(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"CapabilityRealizedBy",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilitySet"),
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilityContainer"
                                    ),
                                    aas.Key(type_=aas.KeyTypes.CAPABILITY, value=r"Capability"),
                                ),
                                type_=aas.Capability,
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"urn:example:capability-description:capability-realized-by:skill"),
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability Realized By"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Relationship between the Capability element in the CapabilityContainer as first element and a Skill implementation, not defined in this Submodel template, as second element."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CapabilityDescription/CapabilityRealizedBy/1/0"
                            ),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                class ComposedOfSet(aas.SubmodelElementCollection):

                    class ComposedOfContainer(aas.SubmodelElementCollection):

                        class CapabilityComposedOf(aas.RelationshipElement):

                            @staticmethod
                            def template_defaults() -> RelationshipElementMetadata:
                                return {
                                    "id_short": r"CapabilityComposedOf",
                                    "first": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL,
                                                value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilitySet"
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                value=r"CapabilityContainer",
                                            ),
                                            aas.Key(type_=aas.KeyTypes.CAPABILITY, value=r"Capability"),
                                        ),
                                        type_=aas.Capability,
                                        referred_semantic_id=None,
                                    ),
                                    "second": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL,
                                                value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilitySet"
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                value=r"CapabilityContainer",
                                            ),
                                            aas.Key(type_=aas.KeyTypes.CAPABILITY, value=r"Capability"),
                                        ),
                                        type_=aas.Capability,
                                        referred_semantic_id=None,
                                    ),
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability Composed Of"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Relationship between a composed capability as first element and one of its minimum two subordinate capabilities as second element."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/CapabilityComposedOf/1/0"
                                    ),
                                }

                            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                                super().__init__(**(self.template_defaults() | kwargs))

                        class ComposedOfComment(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {
                                    "id_short": r"ComposedOfComment",
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Composed Of Comment"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Comment to describe the composition in human readable form."}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/ComposedOfComment/1/0"
                                    ),
                                }

                            def __init__(
                                self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"ComposedOfContainer",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Composed Of Container"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Container corresponding to one composition for the Capability in the CapabilityContainer."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/ComposedOfContainer/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            capabilityComposedOf: Iterable[CapabilityComposedOf],
                            composedOfComment: Optional[Union[aas.MultiLanguageTextType, ComposedOfComment]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(capabilityComposedOf, str):
                                raise TypeError("capabilityComposedOf takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if composedOfComment is not None and not isinstance(composedOfComment, aas.SubmodelElement):
                                composedOfComment = self.ComposedOfComment(composedOfComment)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                capabilityComposedOf, composedOfComment
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ComposedOfSet",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Composed Of Set"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"If composition(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CapabilityDescription/ComposedOfSet/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        composedOfContainer: Iterable[ComposedOfContainer],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(composedOfContainer, str):
                            raise TypeError("composedOfContainer takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(composedOfContainer)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class GeneralizedBySet(aas.SubmodelElementCollection):

                    class CapabilityGeneralizedBy(aas.RelationshipElement):

                        @staticmethod
                        def template_defaults() -> RelationshipElementMetadata:
                            return {
                                "id_short": r"CapabilityGeneralizedBy",
                                "first": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.SUBMODEL,
                                            value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                        ),
                                        aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilitySet"),
                                        aas.Key(
                                            type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilityContainer"
                                        ),
                                        aas.Key(type_=aas.KeyTypes.CAPABILITY, value=r"Capability"),
                                    ),
                                    type_=aas.Capability,
                                    referred_semantic_id=None,
                                ),
                                "second": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.SUBMODEL,
                                            value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                        ),
                                        aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilitySet"),
                                        aas.Key(
                                            type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilityContainer"
                                        ),
                                        aas.Key(type_=aas.KeyTypes.CAPABILITY, value=r"Capability"),
                                    ),
                                    type_=aas.Capability,
                                    referred_semantic_id=None,
                                ),
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability Generalized By"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Relationship between the Capability as first element, described in the CapabilityContainer, and a more general Capability as second element."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/CapabilityGeneralizedBy/1/0"
                                ),
                            }

                        def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                            super().__init__(**(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"GeneralizedBySet",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Generalized By Set"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"If generalization(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CapabilityDescription/GeneralizedBySet/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        capabilityGeneralizedBy: Iterable[CapabilityGeneralizedBy],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(capabilityGeneralizedBy, str):
                            raise TypeError("capabilityGeneralizedBy takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(capabilityGeneralizedBy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ConstraintSet(aas.SubmodelElementCollection):

                    class PropertyConstraintContainer(aas.SubmodelElementCollection):

                        class BasicConstraint(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"BasicConstraint",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Basic Constraint"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Property element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/BasicConstraint/1/0"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"PredicateRelationTemplate",
                                            value_type=str,
                                            value=r"ALL",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class CustomConstraint(aas.SubmodelElementCollection):

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"CustomConstraint",
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Custom Constraint"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"SubmodelElement which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties. This can be freely defined for the purpose of constraining a property and is not specified in this Submodel Template."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/CustomConstraint/1/0"
                                    ),
                                }

                            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements()

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class OCLConstraint(aas.File):

                            @staticmethod
                            def template_defaults() -> FileMetadata:
                                return {
                                    "id_short": r"OCLConstraint",
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"OCL Constraint"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Object Contraint Language (OCL) as File element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OCLConstraint/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                value: str,
                                content_type: Optional[str] = r"application/octet-stream",
                                **kwargs: Unpack[FileMetadata],
                            ):

                                super().__init__(
                                    value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                                )

                        class OperationConstraint(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": r"OperationConstraint",
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Operation Constraint"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Reference to an (external) Operation element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OperationConstraint/1/0"
                                    ),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ConstraintType(aas.Property):

                            ALLOWED_VALUES = (
                                r"OperationConstraint",
                                r"OCLConstraint",
                                r"BasicConstraint",
                                r"CustomConstraint",
                            )

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ConstraintType",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Constraint Type"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Abstract Enum type of allowed SubmodelElements for these Properties constraints. Exactly one of the SubmodelElements below must be instanciated, e.g., similar to SubmodelElementList with exactly one element."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/ConstraintType/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                if value is not None and value not in self.ALLOWED_VALUES:
                                    raise ValueError(
                                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                    )

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class PropertyConditionalType(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"PropertyConditionalType",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Property Conditional Type"}
                                    ),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Defines the type of the property conditions as defined in the ConceptDescription with the same name (PropertyConditionalType)."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/PropertyConditionalType/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ConstraintPropertyRelations(aas.SubmodelElementCollection):

                            class ConstraintHasProperty(aas.RelationshipElement):

                                @staticmethod
                                def template_defaults() -> RelationshipElementMetadata:
                                    return {
                                        "id_short": r"ConstraintHasProperty",
                                        "first": aas.ModelReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL,
                                                    value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"CapabilitySet",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"CapabilityContainer",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"CapabilityRelations",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"ConstraintSet",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"PropertyConstraintContainer",
                                                ),
                                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"BasicConstraint"),
                                            ),
                                            type_=aas.Property,
                                            referred_semantic_id=None,
                                        ),
                                        "second": aas.ModelReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL,
                                                    value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"CapabilitySet",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"CapabilityContainer",
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"PropertySet"
                                                ),
                                                aas.Key(
                                                    type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                    value=r"PropertyContainer",
                                                ),
                                                aas.Key(type_=aas.KeyTypes.PROPERTY, value=r"PropertyProperty"),
                                            ),
                                            type_=aas.Property,
                                            referred_semantic_id=None,
                                        ),
                                        "display_name": aas.MultiLanguageNameType(
                                            dict_={r"en": r"Constraint Has Property"}
                                        ),
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Relates the PropertyConstraint as first element to a Property from a PropertyContainer as second element."
                                            }
                                        ),
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/CapabilityDescription/ConstraintHasProperty/1/0"
                                        ),
                                    }

                                def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                                    super().__init__(**(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"ConstraintPropertyRelations",
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Constraint Property Relations"}
                                    ),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Contains all relationships for the constraint in the PropertyConstraintContainer."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/ConstraintPropertyRelations/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                constraintHasProperty: Iterable[ConstraintHasProperty],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(constraintHasProperty, str):
                                    raise TypeError("constraintHasProperty takes several elements, got a str")

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(constraintHasProperty)

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"PropertyConstraintContainer",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Property Constraint Container"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"If one or more constraints exist for a Capability Property, then for every constraint a PropertyConstraintContainer has to be created."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintContainer/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            basicConstraint: Union[str, BasicConstraint],
                            customConstraint: CustomConstraint,
                            oCLConstraint: OCLConstraint,
                            operationConstraint: Union[aas.Reference, OperationConstraint],
                            constraintType: Union[str, ConstraintType],
                            propertyConditionalType: Union[str, PropertyConditionalType],
                            constraintPropertyRelations: ConstraintPropertyRelations,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if basicConstraint is not None and not isinstance(basicConstraint, aas.SubmodelElement):
                                basicConstraint = self.BasicConstraint(basicConstraint)

                            # Build a submodel element if a raw value was passed in the argument

                            if operationConstraint is not None and not isinstance(
                                operationConstraint, aas.SubmodelElement
                            ):
                                operationConstraint = self.OperationConstraint(operationConstraint)

                            # Build a submodel element if a raw value was passed in the argument

                            if constraintType is not None and not isinstance(constraintType, aas.SubmodelElement):
                                constraintType = self.ConstraintType(constraintType)

                            # Build a submodel element if a raw value was passed in the argument

                            if propertyConditionalType is not None and not isinstance(
                                propertyConditionalType, aas.SubmodelElement
                            ):
                                propertyConditionalType = self.PropertyConditionalType(propertyConditionalType)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                basicConstraint,
                                customConstraint,
                                oCLConstraint,
                                operationConstraint,
                                constraintType,
                                propertyConditionalType,
                                constraintPropertyRelations,
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class TransitionConstraintContainer(aas.SubmodelElementCollection):

                        class TransitionConstrainedBy(aas.RelationshipElement):

                            @staticmethod
                            def template_defaults() -> RelationshipElementMetadata:
                                return {
                                    "id_short": r"TransitionConstrainedBy",
                                    "first": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL,
                                                value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilitySet"
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                value=r"CapabilityContainer",
                                            ),
                                            aas.Key(type_=aas.KeyTypes.CAPABILITY, value=r"Capability"),
                                        ),
                                        type_=aas.Capability,
                                        referred_semantic_id=None,
                                    ),
                                    "second": aas.ModelReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL,
                                                value=r"https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel",
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"CapabilitySet"
                                            ),
                                            aas.Key(
                                                type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                                value=r"CapabilityContainer",
                                            ),
                                            aas.Key(type_=aas.KeyTypes.CAPABILITY, value=r"Capability"),
                                        ),
                                        type_=aas.Capability,
                                        referred_semantic_id=None,
                                    ),
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Transition Constrained By"}
                                    ),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Relates the constrained Capability as first element to a constraining Capability from another CapabilityContainer as second element."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/TransitionConstrainedBy/1/0"
                                    ),
                                }

                            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                                super().__init__(**(self.template_defaults() | kwargs))

                        class TransitionConditionalType(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TransitionConditionalType",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Transition Conditional Type"}
                                    ),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Defines the element TransitionConstrainedBy of TransitionConstraintType."
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/CapabilityDescription/TransitionConditionalType/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"TransitionConstraintContainer",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Transition Constraint Container"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"If one or more constraints exist for a Capability, then for every transitional constraint a TransitionConstraintContainer has to be created."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CapabilityDescription/TransitionConstraintContainer/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            transitionConstrainedBy: TransitionConstrainedBy,
                            transitionConditionalType: Union[str, TransitionConditionalType],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if transitionConditionalType is not None and not isinstance(
                                transitionConditionalType, aas.SubmodelElement
                            ):
                                transitionConditionalType = self.TransitionConditionalType(transitionConditionalType)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                transitionConstrainedBy, transitionConditionalType
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ConstraintSet",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Constraint Set"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"If constraint(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CapabilityDescription/ConstraintSet/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        propertyConstraintContainer: Optional[Iterable[PropertyConstraintContainer]] = None,
                        transitionConstraintContainer: Optional[Iterable[TransitionConstraintContainer]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(propertyConstraintContainer, str):
                            raise TypeError("propertyConstraintContainer takes several elements, got a str")

                        # A str would be split into its characters
                        if isinstance(transitionConstraintContainer, str):
                            raise TypeError("transitionConstraintContainer takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            propertyConstraintContainer, transitionConstraintContainer
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"CapabilityRelations",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability Relations"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection of relationships for the capability, if existing."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CapabilityDescription/CapabilityRelations/1/0"
                        ),
                    }

                def __init__(
                    self,
                    capabilityRealizedBy: Optional[Iterable[CapabilityRealizedBy]] = None,
                    composedOfSet: Optional[ComposedOfSet] = None,
                    generalizedBySet: Optional[Iterable[GeneralizedBySet]] = None,
                    constraintSet: Optional[Iterable[ConstraintSet]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(capabilityRealizedBy, str):
                        raise TypeError("capabilityRealizedBy takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(generalizedBySet, str):
                        raise TypeError("generalizedBySet takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(constraintSet, str):
                        raise TypeError("constraintSet takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        capabilityRealizedBy, composedOfSet, generalizedBySet, constraintSet
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"CapabilityContainer",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability Container"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"A Container for one capability and all its additional descriptive elements."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/CapabilityDescription/CapabilityContainer/1/0"
                    ),
                }

            def __init__(
                self,
                capability: Capability,
                capabilityComment: Optional[Union[aas.MultiLanguageTextType, CapabilityComment]] = None,
                propertySet: Optional[Iterable[PropertySet]] = None,
                capabilityRelations: Optional[CapabilityRelations] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if capabilityComment is not None and not isinstance(capabilityComment, aas.SubmodelElement):
                    capabilityComment = self.CapabilityComment(capabilityComment)

                # A str would be split into its characters
                if isinstance(propertySet, str):
                    raise TypeError("propertySet takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    capability, capabilityComment, propertySet, capabilityRelations
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"CapabilitySet",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Capability Set"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"A Set of CapabilityContainer for a Use Case for the asset."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/CapabilityDescription/CapabilitySet/1/0"),
            }

        def __init__(
            self,
            capabilityContainer: Iterable[CapabilityContainer],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(capabilityContainer, str):
                raise TypeError("capabilityContainer takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(capabilityContainer)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"CapabilityDescription",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Submodel Template Capability Description"}),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Definition of the Submodel CapabilityDescription identified by its semanticId. The Submodel idShort can be picked freely."
                }
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/CapabilityDescription/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(self, id_: str, capabilitySet: Iterable[CapabilitySet], **kwargs: Unpack[SubmodelMetadata]):

        # A str would be split into its characters
        if isinstance(capabilitySet, str):
            raise TypeError("capabilitySet takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(capabilitySet)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
