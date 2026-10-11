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


class AssetInterfacesDescription(aas.Submodel):

    class InterfaceTemplateForHTTP(aas.SubmodelElementCollection):

        class Title(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"title",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Created(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"created",
                    "value_type": xsd.DateTime,
                    "semantic_id": global_ref(r"http://purl.org/dc/terms/created"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Modified(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"modified",
                    "value_type": xsd.DateTime,
                    "semantic_id": global_ref(r"http://purl.org/dc/terms/modified"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Support(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"support",
                    "value_type": xsd.AnyURI,
                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#supportContact"),
                }

            def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EndpointMetadata(aas.SubmodelElementCollection):

            class Base(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"base",
                        "value_type": xsd.AnyURI,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#baseURI"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContentType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"contentType",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#forContentType"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Security(GeneratedSubmodelElementList):

                class Security_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {"id_short": None}

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"security",
                        "type_value_list_element": aas.ReferenceElement,
                        "semantic_id_list_element": global_ref(
                            r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"),
                    }

                def __init__(
                    self,
                    security_items: Iterable[Union[aas.Reference, Security_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(security_items, str):
                        raise TypeError("security_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if security_items:
                        security_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Security_item(i) for i in security_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(security_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SecurityDefinitions(aas.SubmodelElementCollection):

                class Nosec_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"nosec_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#NoSecurityScheme"),
                        }

                    def __init__(self, scheme: Union[str, Scheme], **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Auto_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"auto_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#AutoSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Basic_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"basic_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#BasicSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Combo_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class OneOf(GeneratedSubmodelElementList):

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"oneOf",
                                "type_value_list_element": aas.SubmodelElement,
                                "semantic_id_list_element": global_ref(r"https://www.w3.org/2019/wot/security#allOf"),
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#oneOf"),
                            }

                        def __init__(
                            self,
                            oneof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(oneof_items, str):
                                raise TypeError("oneof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(oneof_items, number_repeated=False)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class AllOf(GeneratedSubmodelElementList):

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"allOf",
                                "type_value_list_element": aas.SubmodelElement,
                                "semantic_id_list_element": global_ref(r"https://www.w3.org/2019/wot/security#allOf"),
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#allOf"),
                            }

                        def __init__(
                            self,
                            allof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(allof_items, str):
                                raise TypeError("allof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(allof_items, number_repeated=False)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"combo_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#ComboSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        oneOf: Union[Iterable[aas.SubmodelElement], OneOf],
                        allOf: Union[Iterable[aas.SubmodelElement], AllOf],
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # A str would be split into its characters
                        if isinstance(oneOf, str):
                            raise TypeError("oneOf takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if oneOf is not None and not isinstance(oneOf, aas.SubmodelElement):
                            oneOf = self.OneOf(oneOf)

                        # A str would be split into its characters
                        if isinstance(allOf, str):
                            raise TypeError("allOf takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if allOf is not None and not isinstance(allOf, aas.SubmodelElement):
                            allOf = self.AllOf(allOf)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, oneOf, allOf, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Apikey_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"apikey_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#APIKeySecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Psk_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Identity(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"identity",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#identity"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"psk_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#PSKSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        identity: Optional[Union[str, Identity]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if identity is not None and not isinstance(identity, aas.SubmodelElement):
                            identity = self.Identity(identity)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, identity, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Digest_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Qop(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"qop",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#qop"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"digest_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#DigestSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        qop: Optional[Union[str, Qop]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if qop is not None and not isinstance(qop, aas.SubmodelElement):
                            qop = self.Qop(qop)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, qop, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Bearer_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Authorization(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"authorization",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#authorization"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Alg(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"alg",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#alg"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Format(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"format",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#format"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"bearer_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#BearerSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        authorization: Optional[Union[str, Authorization]] = None,
                        alg: Optional[Union[str, Alg]] = None,
                        format: Optional[Union[str, Format]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if authorization is not None and not isinstance(authorization, aas.SubmodelElement):
                            authorization = self.Authorization(authorization)

                        # Build a submodel element if a raw value was passed in the argument

                        if alg is not None and not isinstance(alg, aas.SubmodelElement):
                            alg = self.Alg(alg)

                        # Build a submodel element if a raw value was passed in the argument

                        if format is not None and not isinstance(format, aas.SubmodelElement):
                            format = self.Format(format)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            scheme, name, in_, authorization, alg, format, proxy
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Oauth2_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Token(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"token",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#token"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Refresh(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"refresh",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#refresh"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Authorization(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"authorization",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#authorization"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Scopes(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scopes",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#scopes"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Flow(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"flow",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#flow"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"oauth2_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        token: Optional[Union[xsd.AnyURI, Token]] = None,
                        refresh: Optional[Union[xsd.AnyURI, Refresh]] = None,
                        authorization: Optional[Union[xsd.AnyURI, Authorization]] = None,
                        scopes: Optional[Union[str, Scopes]] = None,
                        flow: Optional[Union[str, Flow]] = None,
                        proxy: Optional[Union[xsd.AnyURI, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if token is not None and not isinstance(token, aas.SubmodelElement):
                            token = self.Token(token)

                        # Build a submodel element if a raw value was passed in the argument

                        if refresh is not None and not isinstance(refresh, aas.SubmodelElement):
                            refresh = self.Refresh(refresh)

                        # Build a submodel element if a raw value was passed in the argument

                        if authorization is not None and not isinstance(authorization, aas.SubmodelElement):
                            authorization = self.Authorization(authorization)

                        # Build a submodel element if a raw value was passed in the argument

                        if scopes is not None and not isinstance(scopes, aas.SubmodelElement):
                            scopes = self.Scopes(scopes)

                        # Build a submodel element if a raw value was passed in the argument

                        if flow is not None and not isinstance(flow, aas.SubmodelElement):
                            flow = self.Flow(flow)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            scheme, token, refresh, authorization, scopes, flow, proxy
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"securityDefinitions",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#definesSecurityScheme"),
                    }

                def __init__(
                    self,
                    nosec_sc: Optional[Nosec_sc] = None,
                    auto_sc: Optional[Auto_sc] = None,
                    basic_sc: Optional[Basic_sc] = None,
                    combo_sc: Optional[Combo_sc] = None,
                    apikey_sc: Optional[Apikey_sc] = None,
                    psk_sc: Optional[Psk_sc] = None,
                    digest_sc: Optional[Digest_sc] = None,
                    bearer_sc: Optional[Bearer_sc] = None,
                    oauth2_sc: Optional[Oauth2_sc] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        nosec_sc, auto_sc, basic_sc, combo_sc, apikey_sc, psk_sc, digest_sc, bearer_sc, oauth2_sc
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"EndpointMetadata",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
                    ),
                }

            def __init__(
                self,
                base: Union[xsd.AnyURI, Base],
                contentType: Union[str, ContentType],
                security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                securityDefinitions: SecurityDefinitions,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if base is not None and not isinstance(base, aas.SubmodelElement):
                    base = self.Base(base)

                # Build a submodel element if a raw value was passed in the argument

                if contentType is not None and not isinstance(contentType, aas.SubmodelElement):
                    contentType = self.ContentType(contentType)

                # A str would be split into its characters
                if isinstance(security, str):
                    raise TypeError("security takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if security is not None and not isinstance(security, aas.SubmodelElement):
                    security = self.Security(security)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(base, contentType, security, securityDefinitions)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class InteractionMetadata(aas.SubmodelElementCollection):

            class Properties(aas.SubmodelElementCollection):

                class Property_name(aas.SubmodelElementCollection):

                    class Key(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"key",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                ),
                                "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#name"),),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Type(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"type",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Title(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"title",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Observable(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"observable",
                                "value_type": bool,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Const(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"const",
                                "value_type": xsd.Int,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                            }

                        def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Default(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"default",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Unit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"unit",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://schema.org/unitCode"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Min_max(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"min_max",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for number-/interger-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class LengthRange(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"lengthRange",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for string-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class Items(aas.SubmodelElementCollection):

                        class Type(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"type",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Unit(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"unit",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Default(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"default",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Const(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"const",
                                    "value_type": xsd.Int,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                }

                            def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Observable(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"observable",
                                    "value_type": bool,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                }

                            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Title(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"title",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Min_max(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"min_max",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for number-/interger-based values",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Select",
                                            value_type=str,
                                            value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                    "supplemental_semantic_id": (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                    ),
                                }

                            def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class LengthRange(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"lengthRange",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for string-based values",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Select",
                                            value_type=str,
                                            value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                    "supplemental_semantic_id": (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                    ),
                                }

                            def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class ValueSemantics(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": r"valueSemantics",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                    ),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"items",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#items"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for array-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(
                            self,
                            type: Optional[Union[str, Type]] = None,
                            unit: Optional[Union[str, Unit]] = None,
                            default: Optional[Union[str, Default]] = None,
                            const: Optional[Union[xsd.Int, Const]] = None,
                            observable: Optional[Union[bool, Observable]] = None,
                            title: Optional[Union[str, Title]] = None,
                            min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                            lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                            valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if type is not None and not isinstance(type, aas.SubmodelElement):
                                type = self.Type(type)

                            # Build a submodel element if a raw value was passed in the argument

                            if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                unit = self.Unit(unit)

                            # Build a submodel element if a raw value was passed in the argument

                            if default is not None and not isinstance(default, aas.SubmodelElement):
                                default = self.Default(default)

                            # Build a submodel element if a raw value was passed in the argument

                            if const is not None and not isinstance(const, aas.SubmodelElement):
                                const = self.Const(const)

                            # Build a submodel element if a raw value was passed in the argument

                            if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                observable = self.Observable(observable)

                            # Build a submodel element if a raw value was passed in the argument

                            if title is not None and not isinstance(title, aas.SubmodelElement):
                                title = self.Title(title)

                            # Build a submodel element if a raw value was passed in the argument

                            if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                min_max = self.Min_max(min=min_max[0], max=min_max[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                                valueSemantics = self.ValueSemantics(valueSemantics)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                type, unit, default, const, observable, title, min_max, lengthRange, valueSemantics
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class ItemsRange(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"itemsRange",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for string-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minItems | maxItems | minItems AND maxItems as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class Properties(aas.SubmodelElementCollection):

                        class Property_name(aas.SubmodelElementCollection):

                            class Key(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"key",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Type(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"type",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Title(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"title",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Observable(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"observable",
                                        "value_type": bool,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                    }

                                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Const(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"const",
                                        "value_type": xsd.Int,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                    }

                                def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Default(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"default",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Unit(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"unit",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Min_max(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"min_max",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for number-/interger-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class LengthRange(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"lengthRange",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for string-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class Items(aas.SubmodelElementCollection):

                                class Type(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"type",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class ValueSemantics(aas.ReferenceElement):

                                    @staticmethod
                                    def template_defaults() -> ReferenceElementMetadata:
                                        return {
                                            "id_short": r"valueSemantics",
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                            ),
                                        }

                                    def __init__(
                                        self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]
                                    ):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Unit(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"unit",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Default(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"default",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://www.w3.org/2019/wot/json-schema#default"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Const(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"const",
                                            "value_type": xsd.Int,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                        }

                                    def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Observable(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"observable",
                                            "value_type": bool,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                        }

                                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Title(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"title",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Min_max(aas.Range):

                                    @staticmethod
                                    def template_defaults() -> RangeMetadata:
                                        return {
                                            "id_short": r"min_max",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                            ),
                                            "qualifier": (
                                                aas.Qualifier(
                                                    type_=r"Constraint",
                                                    value_type=str,
                                                    value=r"Only applicable for number-/interger-based values",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                                aas.Qualifier(
                                                    type_=r"Select",
                                                    value_type=str,
                                                    value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            ),
                                            "supplemental_semantic_id": (
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                            ),
                                        }

                                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                                class LengthRange(aas.Range):

                                    @staticmethod
                                    def template_defaults() -> RangeMetadata:
                                        return {
                                            "id_short": r"lengthRange",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                            ),
                                            "qualifier": (
                                                aas.Qualifier(
                                                    type_=r"Constraint",
                                                    value_type=str,
                                                    value=r"Only applicable for string-based values",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                                aas.Qualifier(
                                                    type_=r"Select",
                                                    value_type=str,
                                                    value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            ),
                                            "supplemental_semantic_id": (
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                            ),
                                        }

                                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"items",
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#items"),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for array-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                    }

                                def __init__(
                                    self,
                                    type: Optional[Union[str, Type]] = None,
                                    valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                                    unit: Optional[Union[str, Unit]] = None,
                                    default: Optional[Union[str, Default]] = None,
                                    const: Optional[Union[xsd.Int, Const]] = None,
                                    observable: Optional[Union[bool, Observable]] = None,
                                    title: Optional[Union[str, Title]] = None,
                                    min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                                    lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if type is not None and not isinstance(type, aas.SubmodelElement):
                                        type = self.Type(type)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if valueSemantics is not None and not isinstance(
                                        valueSemantics, aas.SubmodelElement
                                    ):
                                        valueSemantics = self.ValueSemantics(valueSemantics)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                        unit = self.Unit(unit)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if default is not None and not isinstance(default, aas.SubmodelElement):
                                        default = self.Default(default)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if const is not None and not isinstance(const, aas.SubmodelElement):
                                        const = self.Const(const)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                        observable = self.Observable(observable)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if title is not None and not isinstance(title, aas.SubmodelElement):
                                        title = self.Title(title)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                        min_max = self.Min_max(min=min_max[0], max=min_max[1])

                                    # Build a submodel element if a raw value was passed in the argument

                                    if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                        lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        type,
                                        valueSemantics,
                                        unit,
                                        default,
                                        const,
                                        observable,
                                        title,
                                        min_max,
                                        lengthRange,
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class ItemsRange(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"itemsRange",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for string-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minItems | maxItems | minItems AND maxItems as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class Properties(aas.SubmodelElementCollection):

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"properties",
                                        "semantic_id": global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for object-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Comment",
                                                value_type=str,
                                                value=r"Recusive definition of last propertyName SMC",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                    }

                                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements()

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class ValueSemantics(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {
                                        "id_short": r"valueSemantics",
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                        ),
                                    }

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"property_name",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Current counter value",
                                            r"de": r"Derzeitiger Zählerwert",
                                            r"it": r"Valore attuale del contatore",
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#propertyName"),
                                }

                            def __init__(
                                self,
                                key: Optional[Union[str, Key]] = None,
                                type: Optional[Union[str, Type]] = None,
                                title: Optional[Union[str, Title]] = None,
                                observable: Optional[Union[bool, Observable]] = None,
                                const: Optional[Union[xsd.Int, Const]] = None,
                                default: Optional[Union[str, Default]] = None,
                                unit: Optional[Union[str, Unit]] = None,
                                min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                                lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                                items: Optional[Items] = None,
                                itemsRange: Optional[Union[Tuple[str, str], ItemsRange]] = None,
                                properties: Optional[Properties] = None,
                                valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if key is not None and not isinstance(key, aas.SubmodelElement):
                                    key = self.Key(key)

                                # Build a submodel element if a raw value was passed in the argument

                                if type is not None and not isinstance(type, aas.SubmodelElement):
                                    type = self.Type(type)

                                # Build a submodel element if a raw value was passed in the argument

                                if title is not None and not isinstance(title, aas.SubmodelElement):
                                    title = self.Title(title)

                                # Build a submodel element if a raw value was passed in the argument

                                if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                    observable = self.Observable(observable)

                                # Build a submodel element if a raw value was passed in the argument

                                if const is not None and not isinstance(const, aas.SubmodelElement):
                                    const = self.Const(const)

                                # Build a submodel element if a raw value was passed in the argument

                                if default is not None and not isinstance(default, aas.SubmodelElement):
                                    default = self.Default(default)

                                # Build a submodel element if a raw value was passed in the argument

                                if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                    unit = self.Unit(unit)

                                # Build a submodel element if a raw value was passed in the argument

                                if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                    min_max = self.Min_max(min=min_max[0], max=min_max[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                    lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if itemsRange is not None and not isinstance(itemsRange, aas.SubmodelElement):
                                    itemsRange = self.ItemsRange(min=itemsRange[0], max=itemsRange[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                                    valueSemantics = self.ValueSemantics(valueSemantics)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    key,
                                    type,
                                    title,
                                    observable,
                                    const,
                                    default,
                                    unit,
                                    min_max,
                                    lengthRange,
                                    items,
                                    itemsRange,
                                    properties,
                                    valueSemantics,
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"properties",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#properties"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for object-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(
                            self,
                            property_name: Optional[Iterable[Property_name]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(property_name, str):
                                raise TypeError("property_name takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(property_name)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class ValueSemantics(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"valueSemantics",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Forms(aas.SubmodelElementCollection):

                        class Href(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"href",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#hasTarget"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ContentType(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"contentType",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#forContentType"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Security(GeneratedSubmodelElementList):

                            class Security_item(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {"id_short": None}

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"security",
                                    "type_value_list_element": aas.ReferenceElement,
                                    "semantic_id_list_element": global_ref(
                                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                    ),
                                }

                            def __init__(
                                self,
                                security_items: Iterable[Union[aas.Reference, Security_item]],
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(security_items, str):
                                    raise TypeError("security_items takes several elements, got a str")

                                # Build submodel elements from raw values passed in the argument
                                if security_items:
                                    security_items = [
                                        i if isinstance(i, aas.SubmodelElement) else self.Security_item(i)
                                        for i in security_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    security_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class Htv_methodName(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"htv_methodName",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2011/http#methodName"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for HTTP binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Htv_headers(GeneratedSubmodelElementList):

                            class Htv_headers_item(aas.SubmodelElementCollection):

                                class Htv_fieldName(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"htv_fieldName",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://www.w3.org/2011/http#fieldName"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Htv_fieldValue(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"htv_fieldValue",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://www.w3.org/2011/http#fieldValue"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": None,
                                        "semantic_id": global_ref(r"https://www.w3.org/2011/http#headers"),
                                    }

                                def __init__(
                                    self,
                                    htv_fieldName: Union[str, Htv_fieldName],
                                    htv_fieldValue: Union[str, Htv_fieldValue],
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if htv_fieldName is not None and not isinstance(htv_fieldName, aas.SubmodelElement):
                                        htv_fieldName = self.Htv_fieldName(htv_fieldName)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if htv_fieldValue is not None and not isinstance(
                                        htv_fieldValue, aas.SubmodelElement
                                    ):
                                        htv_fieldValue = self.Htv_fieldValue(htv_fieldValue)

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        htv_fieldName, htv_fieldValue
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"htv_headers",
                                    "type_value_list_element": aas.SubmodelElementCollection,
                                    "semantic_id_list_element": global_ref(r"https://www.w3.org/2011/http#headers"),
                                    "value_type_list_element": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2011/http#headers"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for HTTP binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(
                                self,
                                htv_headers_items: Iterable[Htv_headers_item],
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(htv_headers_items, str):
                                    raise TypeError("htv_headers_items takes several elements, got a str")

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    htv_headers_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"forms",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#hasForm"),
                            }

                        def __init__(
                            self,
                            href: Union[str, Href],
                            security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                            contentType: Optional[Union[str, ContentType]] = None,
                            htv_methodName: Optional[Union[str, Htv_methodName]] = None,
                            htv_headers: Optional[Union[Iterable[Htv_headers.Htv_headers_item], Htv_headers]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if href is not None and not isinstance(href, aas.SubmodelElement):
                                href = self.Href(href)

                            # Build a submodel element if a raw value was passed in the argument

                            if contentType is not None and not isinstance(contentType, aas.SubmodelElement):
                                contentType = self.ContentType(contentType)

                            # A str would be split into its characters
                            if isinstance(security, str):
                                raise TypeError("security takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if security is not None and not isinstance(security, aas.SubmodelElement):
                                security = self.Security(security)

                            # Build a submodel element if a raw value was passed in the argument

                            if htv_methodName is not None and not isinstance(htv_methodName, aas.SubmodelElement):
                                htv_methodName = self.Htv_methodName(htv_methodName)

                            # A str would be split into its characters
                            if isinstance(htv_headers, str):
                                raise TypeError("htv_headers takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if htv_headers is not None and not isinstance(htv_headers, aas.SubmodelElement):
                                htv_headers = self.Htv_headers(htv_headers)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                href, contentType, security, htv_methodName, htv_headers
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"property_name",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Current counter value",
                                    r"de": r"Derzeitiger Zählerwert",
                                    r"it": r"Valore attuale del contatore",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AssetInterfaceDescription/1/0/PropertyDefinition"
                            ),
                            "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#name"),),
                        }

                    def __init__(
                        self,
                        forms: Forms,
                        key: Optional[Union[str, Key]] = None,
                        type: Optional[Union[str, Type]] = None,
                        title: Optional[Union[str, Title]] = None,
                        observable: Optional[Union[bool, Observable]] = None,
                        const: Optional[Union[xsd.Int, Const]] = None,
                        default: Optional[Union[str, Default]] = None,
                        unit: Optional[Union[str, Unit]] = None,
                        min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                        lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                        items: Optional[Items] = None,
                        itemsRange: Optional[Union[Tuple[str, str], ItemsRange]] = None,
                        properties: Optional[Properties] = None,
                        valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if key is not None and not isinstance(key, aas.SubmodelElement):
                            key = self.Key(key)

                        # Build a submodel element if a raw value was passed in the argument

                        if type is not None and not isinstance(type, aas.SubmodelElement):
                            type = self.Type(type)

                        # Build a submodel element if a raw value was passed in the argument

                        if title is not None and not isinstance(title, aas.SubmodelElement):
                            title = self.Title(title)

                        # Build a submodel element if a raw value was passed in the argument

                        if observable is not None and not isinstance(observable, aas.SubmodelElement):
                            observable = self.Observable(observable)

                        # Build a submodel element if a raw value was passed in the argument

                        if const is not None and not isinstance(const, aas.SubmodelElement):
                            const = self.Const(const)

                        # Build a submodel element if a raw value was passed in the argument

                        if default is not None and not isinstance(default, aas.SubmodelElement):
                            default = self.Default(default)

                        # Build a submodel element if a raw value was passed in the argument

                        if unit is not None and not isinstance(unit, aas.SubmodelElement):
                            unit = self.Unit(unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                            min_max = self.Min_max(min=min_max[0], max=min_max[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                            lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if itemsRange is not None and not isinstance(itemsRange, aas.SubmodelElement):
                            itemsRange = self.ItemsRange(min=itemsRange[0], max=itemsRange[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                            valueSemantics = self.ValueSemantics(valueSemantics)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            key,
                            type,
                            title,
                            observable,
                            const,
                            default,
                            unit,
                            min_max,
                            lengthRange,
                            items,
                            itemsRange,
                            properties,
                            valueSemantics,
                            forms,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"properties",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#PropertyAffordance"),
                    }

                def __init__(
                    self,
                    property_name: Optional[Iterable[Property_name]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(property_name, str):
                        raise TypeError("property_name takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(property_name)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Actions(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"actions",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#ActionAffordance"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Events(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"events",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#EventAffordance"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InteractionMetadata",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
                    ),
                    "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#InteractionAffordance"),),
                }

            def __init__(
                self,
                properties: Optional[Properties] = None,
                actions: Optional[Actions] = None,
                events: Optional[Events] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(properties, actions, events)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ExternalDescriptor(aas.SubmodelElementCollection):

            class FileName(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"fileName",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ExternalDescriptor",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
                    ),
                }

            def __init__(self, fileName: FileName, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(fileName)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"InterfaceTemplateForHTTP",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"),
                "supplemental_semantic_id": (
                    global_ref(r"http://www.w3.org/2011/http"),
                    global_ref(r"https://www.w3.org/2019/wot/td"),
                ),
            }

        def __init__(
            self,
            title: Union[str, Title],
            endpointMetadata: EndpointMetadata,
            interactionMetadata: InteractionMetadata,
            created: Optional[Union[xsd.DateTime, Created]] = None,
            modified: Optional[Union[xsd.DateTime, Modified]] = None,
            support: Optional[Union[xsd.AnyURI, Support]] = None,
            externalDescriptor: Optional[ExternalDescriptor] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if title is not None and not isinstance(title, aas.SubmodelElement):
                title = self.Title(title)

            # Build a submodel element if a raw value was passed in the argument

            if created is not None and not isinstance(created, aas.SubmodelElement):
                created = self.Created(created)

            # Build a submodel element if a raw value was passed in the argument

            if modified is not None and not isinstance(modified, aas.SubmodelElement):
                modified = self.Modified(modified)

            # Build a submodel element if a raw value was passed in the argument

            if support is not None and not isinstance(support, aas.SubmodelElement):
                support = self.Support(support)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                title, created, modified, support, endpointMetadata, interactionMetadata, externalDescriptor
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class InterfaceTemplateForMODBUS(aas.SubmodelElementCollection):

        class Title(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"title",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Created(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"created",
                    "value_type": xsd.DateTime,
                    "semantic_id": global_ref(r"http://purl.org/dc/terms/created"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Modified(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"modified",
                    "value_type": xsd.DateTime,
                    "semantic_id": global_ref(r"http://purl.org/dc/terms/modified"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Support(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"support",
                    "value_type": xsd.AnyURI,
                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#support"),
                }

            def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EndpointMetadata(aas.SubmodelElementCollection):

            class Base(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"base",
                        "value_type": xsd.AnyURI,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#base"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContentType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"contentType",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#forContentType"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Security(GeneratedSubmodelElementList):

                class Security_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {"id_short": None}

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"security",
                        "type_value_list_element": aas.ReferenceElement,
                        "semantic_id_list_element": global_ref(
                            r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"),
                    }

                def __init__(
                    self,
                    security_items: Iterable[Union[aas.Reference, Security_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(security_items, str):
                        raise TypeError("security_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if security_items:
                        security_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Security_item(i) for i in security_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(security_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SecurityDefinitions(aas.SubmodelElementCollection):

                class Nosec_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"nosec_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#NoSecurityScheme"),
                        }

                    def __init__(self, scheme: Union[str, Scheme], **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Auto_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"auto_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#AutoSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Basic_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"basic_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#BasicSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Combo_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class OneOf(GeneratedSubmodelElementList):

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"oneOf",
                                "type_value_list_element": aas.SubmodelElement,
                                "semantic_id_list_element": global_ref(r"https://www.w3.org/2019/wot/security#oneOf"),
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#oneOf"),
                            }

                        def __init__(
                            self,
                            oneof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(oneof_items, str):
                                raise TypeError("oneof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(oneof_items, number_repeated=False)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class AllOf(GeneratedSubmodelElementList):

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"allOf",
                                "type_value_list_element": aas.SubmodelElement,
                                "semantic_id_list_element": global_ref(r"https://www.w3.org/2019/wot/security#allOf"),
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#allOf"),
                            }

                        def __init__(
                            self,
                            allof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(allof_items, str):
                                raise TypeError("allof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(allof_items, number_repeated=False)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"combo_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#ComboSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        oneOf: Union[Iterable[aas.SubmodelElement], OneOf],
                        allOf: Union[Iterable[aas.SubmodelElement], AllOf],
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # A str would be split into its characters
                        if isinstance(oneOf, str):
                            raise TypeError("oneOf takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if oneOf is not None and not isinstance(oneOf, aas.SubmodelElement):
                            oneOf = self.OneOf(oneOf)

                        # A str would be split into its characters
                        if isinstance(allOf, str):
                            raise TypeError("allOf takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if allOf is not None and not isinstance(allOf, aas.SubmodelElement):
                            allOf = self.AllOf(allOf)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, oneOf, allOf, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Apikey_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"apikey_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#APIKeySecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Psk_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Identity(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"identity",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#identity"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"psk_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#PSKSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        identity: Optional[Union[str, Identity]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if identity is not None and not isinstance(identity, aas.SubmodelElement):
                            identity = self.Identity(identity)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, identity, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Digest_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Qop(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"qop",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#qop"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"digest_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#DigestSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        qop: Optional[Union[str, Qop]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if qop is not None and not isinstance(qop, aas.SubmodelElement):
                            qop = self.Qop(qop)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, qop, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Bearer_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Authorization(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"authorization",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#authorization"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Alg(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"alg",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#alg"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Format(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"format",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#format"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"bearer_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#BearerSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        authorization: Optional[Union[str, Authorization]] = None,
                        alg: Optional[Union[str, Alg]] = None,
                        format: Optional[Union[str, Format]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if authorization is not None and not isinstance(authorization, aas.SubmodelElement):
                            authorization = self.Authorization(authorization)

                        # Build a submodel element if a raw value was passed in the argument

                        if alg is not None and not isinstance(alg, aas.SubmodelElement):
                            alg = self.Alg(alg)

                        # Build a submodel element if a raw value was passed in the argument

                        if format is not None and not isinstance(format, aas.SubmodelElement):
                            format = self.Format(format)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            scheme, name, in_, authorization, alg, format, proxy
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Oauth2_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Token(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"token",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#token"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Refresh(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"refresh",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#refresh"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Authorization(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"authorization",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#authorization"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Scopes(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scopes",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#scopes"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Flow(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"flow",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#flow"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"oauth2_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        token: Optional[Union[xsd.AnyURI, Token]] = None,
                        refresh: Optional[Union[xsd.AnyURI, Refresh]] = None,
                        authorization: Optional[Union[xsd.AnyURI, Authorization]] = None,
                        scopes: Optional[Union[str, Scopes]] = None,
                        flow: Optional[Union[str, Flow]] = None,
                        proxy: Optional[Union[xsd.AnyURI, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if token is not None and not isinstance(token, aas.SubmodelElement):
                            token = self.Token(token)

                        # Build a submodel element if a raw value was passed in the argument

                        if refresh is not None and not isinstance(refresh, aas.SubmodelElement):
                            refresh = self.Refresh(refresh)

                        # Build a submodel element if a raw value was passed in the argument

                        if authorization is not None and not isinstance(authorization, aas.SubmodelElement):
                            authorization = self.Authorization(authorization)

                        # Build a submodel element if a raw value was passed in the argument

                        if scopes is not None and not isinstance(scopes, aas.SubmodelElement):
                            scopes = self.Scopes(scopes)

                        # Build a submodel element if a raw value was passed in the argument

                        if flow is not None and not isinstance(flow, aas.SubmodelElement):
                            flow = self.Flow(flow)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            scheme, token, refresh, authorization, scopes, flow, proxy
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"securityDefinitions",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#definesSecurityScheme"),
                    }

                def __init__(
                    self,
                    nosec_sc: Optional[Nosec_sc] = None,
                    auto_sc: Optional[Auto_sc] = None,
                    basic_sc: Optional[Basic_sc] = None,
                    combo_sc: Optional[Combo_sc] = None,
                    apikey_sc: Optional[Apikey_sc] = None,
                    psk_sc: Optional[Psk_sc] = None,
                    digest_sc: Optional[Digest_sc] = None,
                    bearer_sc: Optional[Bearer_sc] = None,
                    oauth2_sc: Optional[Oauth2_sc] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        nosec_sc, auto_sc, basic_sc, combo_sc, apikey_sc, psk_sc, digest_sc, bearer_sc, oauth2_sc
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Modv_mostSignificantByte(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"modv_mostSignificantByte",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/modbus#hasMostSignificantByte"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"Constraint",
                                value_type=str,
                                value=r"Only applicable for Modbus binding",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Modv_mostSignificantWord(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"modv_mostSignificantWord",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/modbus#hasMostSignificantWord"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"Constraint",
                                value_type=str,
                                value=r"Only applicable for Modbus binding",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"EndpointMetadata",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
                    ),
                }

            def __init__(
                self,
                base: Union[xsd.AnyURI, Base],
                contentType: Union[str, ContentType],
                security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                securityDefinitions: SecurityDefinitions,
                modv_mostSignificantByte: Optional[Union[str, Modv_mostSignificantByte]] = None,
                modv_mostSignificantWord: Optional[Union[str, Modv_mostSignificantWord]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if base is not None and not isinstance(base, aas.SubmodelElement):
                    base = self.Base(base)

                # Build a submodel element if a raw value was passed in the argument

                if contentType is not None and not isinstance(contentType, aas.SubmodelElement):
                    contentType = self.ContentType(contentType)

                # A str would be split into its characters
                if isinstance(security, str):
                    raise TypeError("security takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if security is not None and not isinstance(security, aas.SubmodelElement):
                    security = self.Security(security)

                # Build a submodel element if a raw value was passed in the argument

                if modv_mostSignificantByte is not None and not isinstance(
                    modv_mostSignificantByte, aas.SubmodelElement
                ):
                    modv_mostSignificantByte = self.Modv_mostSignificantByte(modv_mostSignificantByte)

                # Build a submodel element if a raw value was passed in the argument

                if modv_mostSignificantWord is not None and not isinstance(
                    modv_mostSignificantWord, aas.SubmodelElement
                ):
                    modv_mostSignificantWord = self.Modv_mostSignificantWord(modv_mostSignificantWord)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    base, contentType, security, securityDefinitions, modv_mostSignificantByte, modv_mostSignificantWord
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class InteractionMetadata(aas.SubmodelElementCollection):

            class Properties(aas.SubmodelElementCollection):

                class Property_name(aas.SubmodelElementCollection):

                    class Key(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"key",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                ),
                                "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#name"),),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Type(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"type",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Title(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"title",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Observable(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"observable",
                                "value_type": bool,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Const(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"const",
                                "value_type": xsd.Int,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                            }

                        def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Default(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"default",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Unit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"unit",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://schema.org/unitCode"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Min_max(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"min_max",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for number-/interger-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class LengthRange(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"lengthRange",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for string-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class Items(aas.SubmodelElementCollection):

                        class Type(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"type",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Unit(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"unit",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Default(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"default",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Const(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"const",
                                    "value_type": xsd.Int,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                }

                            def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Observable(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"observable",
                                    "value_type": bool,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                }

                            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Title(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"title",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Min_max(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"min_max",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for number-/interger-based values",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Select",
                                            value_type=str,
                                            value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                    "supplemental_semantic_id": (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                    ),
                                }

                            def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class LengthRange(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"lengthRange",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for string-based values",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Select",
                                            value_type=str,
                                            value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                    "supplemental_semantic_id": (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                    ),
                                }

                            def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class ValueSemantics(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": r"valueSemantics",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                    ),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"items",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#items"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for array-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(
                            self,
                            type: Optional[Union[str, Type]] = None,
                            unit: Optional[Union[str, Unit]] = None,
                            default: Optional[Union[str, Default]] = None,
                            const: Optional[Union[xsd.Int, Const]] = None,
                            observable: Optional[Union[bool, Observable]] = None,
                            title: Optional[Union[str, Title]] = None,
                            min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                            lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                            valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if type is not None and not isinstance(type, aas.SubmodelElement):
                                type = self.Type(type)

                            # Build a submodel element if a raw value was passed in the argument

                            if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                unit = self.Unit(unit)

                            # Build a submodel element if a raw value was passed in the argument

                            if default is not None and not isinstance(default, aas.SubmodelElement):
                                default = self.Default(default)

                            # Build a submodel element if a raw value was passed in the argument

                            if const is not None and not isinstance(const, aas.SubmodelElement):
                                const = self.Const(const)

                            # Build a submodel element if a raw value was passed in the argument

                            if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                observable = self.Observable(observable)

                            # Build a submodel element if a raw value was passed in the argument

                            if title is not None and not isinstance(title, aas.SubmodelElement):
                                title = self.Title(title)

                            # Build a submodel element if a raw value was passed in the argument

                            if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                min_max = self.Min_max(min=min_max[0], max=min_max[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                                valueSemantics = self.ValueSemantics(valueSemantics)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                type, unit, default, const, observable, title, min_max, lengthRange, valueSemantics
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class ItemsRange(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"itemsRange",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for string-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minItems | maxItems | minItems AND maxItems as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class Properties(aas.SubmodelElementCollection):

                        class Property_name(aas.SubmodelElementCollection):

                            class Key(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"key",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Type(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"type",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Title(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"title",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Observable(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"observable",
                                        "value_type": bool,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                    }

                                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Const(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"const",
                                        "value_type": xsd.Int,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                    }

                                def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Default(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"default",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Unit(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"unit",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Min_max(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"min_max",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for number-/interger-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class LengthRange(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"lengthRange",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for string-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class Items(aas.SubmodelElementCollection):

                                class Type(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"type",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class ValueSemantics(aas.ReferenceElement):

                                    @staticmethod
                                    def template_defaults() -> ReferenceElementMetadata:
                                        return {
                                            "id_short": r"valueSemantics",
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                            ),
                                        }

                                    def __init__(
                                        self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]
                                    ):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Unit(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"unit",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Default(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"default",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://www.w3.org/2019/wot/json-schema#default"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Const(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"const",
                                            "value_type": xsd.Int,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                        }

                                    def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Observable(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"observable",
                                            "value_type": bool,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                        }

                                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Title(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"title",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Min_max(aas.Range):

                                    @staticmethod
                                    def template_defaults() -> RangeMetadata:
                                        return {
                                            "id_short": r"min_max",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                            ),
                                            "qualifier": (
                                                aas.Qualifier(
                                                    type_=r"Constraint",
                                                    value_type=str,
                                                    value=r"Only applicable for number-/interger-based values",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                                aas.Qualifier(
                                                    type_=r"Select",
                                                    value_type=str,
                                                    value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            ),
                                            "supplemental_semantic_id": (
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                            ),
                                        }

                                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                                class LengthRange(aas.Range):

                                    @staticmethod
                                    def template_defaults() -> RangeMetadata:
                                        return {
                                            "id_short": r"lengthRange",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                            ),
                                            "qualifier": (
                                                aas.Qualifier(
                                                    type_=r"Constraint",
                                                    value_type=str,
                                                    value=r"Only applicable for string-based values",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                                aas.Qualifier(
                                                    type_=r"Select",
                                                    value_type=str,
                                                    value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            ),
                                            "supplemental_semantic_id": (
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                            ),
                                        }

                                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"items",
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#items"),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for array-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                    }

                                def __init__(
                                    self,
                                    type: Optional[Union[str, Type]] = None,
                                    valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                                    unit: Optional[Union[str, Unit]] = None,
                                    default: Optional[Union[str, Default]] = None,
                                    const: Optional[Union[xsd.Int, Const]] = None,
                                    observable: Optional[Union[bool, Observable]] = None,
                                    title: Optional[Union[str, Title]] = None,
                                    min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                                    lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if type is not None and not isinstance(type, aas.SubmodelElement):
                                        type = self.Type(type)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if valueSemantics is not None and not isinstance(
                                        valueSemantics, aas.SubmodelElement
                                    ):
                                        valueSemantics = self.ValueSemantics(valueSemantics)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                        unit = self.Unit(unit)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if default is not None and not isinstance(default, aas.SubmodelElement):
                                        default = self.Default(default)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if const is not None and not isinstance(const, aas.SubmodelElement):
                                        const = self.Const(const)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                        observable = self.Observable(observable)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if title is not None and not isinstance(title, aas.SubmodelElement):
                                        title = self.Title(title)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                        min_max = self.Min_max(min=min_max[0], max=min_max[1])

                                    # Build a submodel element if a raw value was passed in the argument

                                    if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                        lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        type,
                                        valueSemantics,
                                        unit,
                                        default,
                                        const,
                                        observable,
                                        title,
                                        min_max,
                                        lengthRange,
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class ItemsRange(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"itemsRange",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for string-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minItems | maxItems | minItems AND maxItems as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class Properties(aas.SubmodelElementCollection):

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"properties",
                                        "semantic_id": global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for object-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Comment",
                                                value_type=str,
                                                value=r"Recusive definition of last propertyName SMC",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                    }

                                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements()

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class ValueSemantics(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {
                                        "id_short": r"valueSemantics",
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                        ),
                                    }

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"property_name",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Current counter value",
                                            r"de": r"Derzeitiger Zählerwert",
                                            r"it": r"Valore attuale del contatore",
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#propertyName"),
                                }

                            def __init__(
                                self,
                                key: Optional[Union[str, Key]] = None,
                                type: Optional[Union[str, Type]] = None,
                                title: Optional[Union[str, Title]] = None,
                                observable: Optional[Union[bool, Observable]] = None,
                                const: Optional[Union[xsd.Int, Const]] = None,
                                default: Optional[Union[str, Default]] = None,
                                unit: Optional[Union[str, Unit]] = None,
                                min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                                lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                                items: Optional[Items] = None,
                                itemsRange: Optional[Union[Tuple[str, str], ItemsRange]] = None,
                                properties: Optional[Properties] = None,
                                valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if key is not None and not isinstance(key, aas.SubmodelElement):
                                    key = self.Key(key)

                                # Build a submodel element if a raw value was passed in the argument

                                if type is not None and not isinstance(type, aas.SubmodelElement):
                                    type = self.Type(type)

                                # Build a submodel element if a raw value was passed in the argument

                                if title is not None and not isinstance(title, aas.SubmodelElement):
                                    title = self.Title(title)

                                # Build a submodel element if a raw value was passed in the argument

                                if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                    observable = self.Observable(observable)

                                # Build a submodel element if a raw value was passed in the argument

                                if const is not None and not isinstance(const, aas.SubmodelElement):
                                    const = self.Const(const)

                                # Build a submodel element if a raw value was passed in the argument

                                if default is not None and not isinstance(default, aas.SubmodelElement):
                                    default = self.Default(default)

                                # Build a submodel element if a raw value was passed in the argument

                                if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                    unit = self.Unit(unit)

                                # Build a submodel element if a raw value was passed in the argument

                                if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                    min_max = self.Min_max(min=min_max[0], max=min_max[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                    lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if itemsRange is not None and not isinstance(itemsRange, aas.SubmodelElement):
                                    itemsRange = self.ItemsRange(min=itemsRange[0], max=itemsRange[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                                    valueSemantics = self.ValueSemantics(valueSemantics)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    key,
                                    type,
                                    title,
                                    observable,
                                    const,
                                    default,
                                    unit,
                                    min_max,
                                    lengthRange,
                                    items,
                                    itemsRange,
                                    properties,
                                    valueSemantics,
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"properties",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#properties"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for object-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(
                            self,
                            property_name: Optional[Iterable[Property_name]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(property_name, str):
                                raise TypeError("property_name takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(property_name)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class ValueSemantics(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"valueSemantics",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Forms(aas.SubmodelElementCollection):

                        class Href(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"href",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#hasTarget"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ContentType(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"contentType",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#forContentType"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Security(GeneratedSubmodelElementList):

                            class Security_item(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {"id_short": None}

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"security",
                                    "type_value_list_element": aas.ReferenceElement,
                                    "semantic_id_list_element": global_ref(
                                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                    ),
                                }

                            def __init__(
                                self,
                                security_items: Iterable[Union[aas.Reference, Security_item]],
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(security_items, str):
                                    raise TypeError("security_items takes several elements, got a str")

                                # Build submodel elements from raw values passed in the argument
                                if security_items:
                                    security_items = [
                                        i if isinstance(i, aas.SubmodelElement) else self.Security_item(i)
                                        for i in security_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    security_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class Modv_function(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_function",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/modbus#hasFunction"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Modv_entity(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_entity",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/modbus#hasEntity"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Modv_zeroBasedAddressing(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_zeroBasedAddressing",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://www.w3.org/2019/wot/modbus#hasZeroBasedAddressingFlag"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Modv_pollingTime(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_pollingTime",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/modbus#hasPollingTime"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Modv_timeout(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_timeout",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/modbus#hasTimeout"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Modv_type(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_type",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/modbus#hasPayloadDataType"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Modv_mostSignificantByte(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_mostSignificantByte",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://www.w3.org/2019/wot/modbus#hasMostSignificantByte"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Modv_mostSignificantWord(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"modv_mostSignificantWord",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://www.w3.org/2019/wot/modbus#hasMostSignificantWord"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"forms",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#hasForm"),
                            }

                        def __init__(
                            self,
                            href: Union[str, Href],
                            security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                            contentType: Optional[Union[str, ContentType]] = None,
                            modv_function: Optional[Union[str, Modv_function]] = None,
                            modv_entity: Optional[Union[str, Modv_entity]] = None,
                            modv_zeroBasedAddressing: Optional[Union[str, Modv_zeroBasedAddressing]] = None,
                            modv_pollingTime: Optional[Union[str, Modv_pollingTime]] = None,
                            modv_timeout: Optional[Union[str, Modv_timeout]] = None,
                            modv_type: Optional[Union[str, Modv_type]] = None,
                            modv_mostSignificantByte: Optional[Union[str, Modv_mostSignificantByte]] = None,
                            modv_mostSignificantWord: Optional[Union[str, Modv_mostSignificantWord]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if href is not None and not isinstance(href, aas.SubmodelElement):
                                href = self.Href(href)

                            # Build a submodel element if a raw value was passed in the argument

                            if contentType is not None and not isinstance(contentType, aas.SubmodelElement):
                                contentType = self.ContentType(contentType)

                            # A str would be split into its characters
                            if isinstance(security, str):
                                raise TypeError("security takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if security is not None and not isinstance(security, aas.SubmodelElement):
                                security = self.Security(security)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_function is not None and not isinstance(modv_function, aas.SubmodelElement):
                                modv_function = self.Modv_function(modv_function)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_entity is not None and not isinstance(modv_entity, aas.SubmodelElement):
                                modv_entity = self.Modv_entity(modv_entity)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_zeroBasedAddressing is not None and not isinstance(
                                modv_zeroBasedAddressing, aas.SubmodelElement
                            ):
                                modv_zeroBasedAddressing = self.Modv_zeroBasedAddressing(modv_zeroBasedAddressing)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_pollingTime is not None and not isinstance(modv_pollingTime, aas.SubmodelElement):
                                modv_pollingTime = self.Modv_pollingTime(modv_pollingTime)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_timeout is not None and not isinstance(modv_timeout, aas.SubmodelElement):
                                modv_timeout = self.Modv_timeout(modv_timeout)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_type is not None and not isinstance(modv_type, aas.SubmodelElement):
                                modv_type = self.Modv_type(modv_type)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_mostSignificantByte is not None and not isinstance(
                                modv_mostSignificantByte, aas.SubmodelElement
                            ):
                                modv_mostSignificantByte = self.Modv_mostSignificantByte(modv_mostSignificantByte)

                            # Build a submodel element if a raw value was passed in the argument

                            if modv_mostSignificantWord is not None and not isinstance(
                                modv_mostSignificantWord, aas.SubmodelElement
                            ):
                                modv_mostSignificantWord = self.Modv_mostSignificantWord(modv_mostSignificantWord)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                href,
                                contentType,
                                security,
                                modv_function,
                                modv_entity,
                                modv_zeroBasedAddressing,
                                modv_pollingTime,
                                modv_timeout,
                                modv_type,
                                modv_mostSignificantByte,
                                modv_mostSignificantWord,
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"property_name",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Current counter value",
                                    r"de": r"Derzeitiger Zählerwert",
                                    r"it": r"Valore attuale del contatore",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AssetInterfaceDescription/1/0/PropertyDefinition"
                            ),
                            "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#name"),),
                        }

                    def __init__(
                        self,
                        forms: Forms,
                        key: Optional[Union[str, Key]] = None,
                        type: Optional[Union[str, Type]] = None,
                        title: Optional[Union[str, Title]] = None,
                        observable: Optional[Union[bool, Observable]] = None,
                        const: Optional[Union[xsd.Int, Const]] = None,
                        default: Optional[Union[str, Default]] = None,
                        unit: Optional[Union[str, Unit]] = None,
                        min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                        lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                        items: Optional[Items] = None,
                        itemsRange: Optional[Union[Tuple[str, str], ItemsRange]] = None,
                        properties: Optional[Properties] = None,
                        valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if key is not None and not isinstance(key, aas.SubmodelElement):
                            key = self.Key(key)

                        # Build a submodel element if a raw value was passed in the argument

                        if type is not None and not isinstance(type, aas.SubmodelElement):
                            type = self.Type(type)

                        # Build a submodel element if a raw value was passed in the argument

                        if title is not None and not isinstance(title, aas.SubmodelElement):
                            title = self.Title(title)

                        # Build a submodel element if a raw value was passed in the argument

                        if observable is not None and not isinstance(observable, aas.SubmodelElement):
                            observable = self.Observable(observable)

                        # Build a submodel element if a raw value was passed in the argument

                        if const is not None and not isinstance(const, aas.SubmodelElement):
                            const = self.Const(const)

                        # Build a submodel element if a raw value was passed in the argument

                        if default is not None and not isinstance(default, aas.SubmodelElement):
                            default = self.Default(default)

                        # Build a submodel element if a raw value was passed in the argument

                        if unit is not None and not isinstance(unit, aas.SubmodelElement):
                            unit = self.Unit(unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                            min_max = self.Min_max(min=min_max[0], max=min_max[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                            lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if itemsRange is not None and not isinstance(itemsRange, aas.SubmodelElement):
                            itemsRange = self.ItemsRange(min=itemsRange[0], max=itemsRange[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                            valueSemantics = self.ValueSemantics(valueSemantics)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            key,
                            type,
                            title,
                            observable,
                            const,
                            default,
                            unit,
                            min_max,
                            lengthRange,
                            items,
                            itemsRange,
                            properties,
                            valueSemantics,
                            forms,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"properties",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#PropertyAffordance"),
                    }

                def __init__(
                    self,
                    property_name: Optional[Iterable[Property_name]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(property_name, str):
                        raise TypeError("property_name takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(property_name)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Actions(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"actions",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#ActionAffordance"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Events(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"events",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#EventAffordance"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InteractionMetadata",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
                    ),
                    "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#InteractionAffordance"),),
                }

            def __init__(
                self,
                properties: Optional[Properties] = None,
                actions: Optional[Actions] = None,
                events: Optional[Events] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(properties, actions, events)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ExternalDescriptor(aas.SubmodelElementCollection):

            class FileName(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"fileName",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ExternalDescriptor",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
                    ),
                }

            def __init__(self, fileName: FileName, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(fileName)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"InterfaceTemplateForMODBUS",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"),
                "supplemental_semantic_id": (
                    global_ref(r"http://www.w3.org/2011/modbus"),
                    global_ref(r"https://www.w3.org/2019/wot/td"),
                ),
            }

        def __init__(
            self,
            title: Union[str, Title],
            endpointMetadata: EndpointMetadata,
            interactionMetadata: InteractionMetadata,
            created: Optional[Union[xsd.DateTime, Created]] = None,
            modified: Optional[Union[xsd.DateTime, Modified]] = None,
            support: Optional[Union[xsd.AnyURI, Support]] = None,
            externalDescriptor: Optional[ExternalDescriptor] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if title is not None and not isinstance(title, aas.SubmodelElement):
                title = self.Title(title)

            # Build a submodel element if a raw value was passed in the argument

            if created is not None and not isinstance(created, aas.SubmodelElement):
                created = self.Created(created)

            # Build a submodel element if a raw value was passed in the argument

            if modified is not None and not isinstance(modified, aas.SubmodelElement):
                modified = self.Modified(modified)

            # Build a submodel element if a raw value was passed in the argument

            if support is not None and not isinstance(support, aas.SubmodelElement):
                support = self.Support(support)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                title, created, modified, support, endpointMetadata, interactionMetadata, externalDescriptor
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class InterfaceTemplateForMQTT(aas.SubmodelElementCollection):

        class Title(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"title",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Created(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"created",
                    "value_type": xsd.DateTime,
                    "semantic_id": global_ref(r"http://purl.org/dc/terms/created"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Modified(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"modified",
                    "value_type": xsd.DateTime,
                    "semantic_id": global_ref(r"http://purl.org/dc/terms/modified"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Support(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"support",
                    "value_type": xsd.AnyURI,
                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#support"),
                }

            def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EndpointMetadata(aas.SubmodelElementCollection):

            class Base(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"base",
                        "value_type": xsd.AnyURI,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#base"),
                    }

                def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContentType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"contentType",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#forContentType"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Security(GeneratedSubmodelElementList):

                class Security_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {"id_short": None}

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"security",
                        "type_value_list_element": aas.ReferenceElement,
                        "semantic_id_list_element": global_ref(
                            r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                        ),
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"),
                    }

                def __init__(
                    self,
                    security_items: Iterable[Union[aas.Reference, Security_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(security_items, str):
                        raise TypeError("security_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if security_items:
                        security_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Security_item(i) for i in security_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(security_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SecurityDefinitions(aas.SubmodelElementCollection):

                class Nosec_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"nosec_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#NoSecurityScheme"),
                        }

                    def __init__(self, scheme: Union[str, Scheme], **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Auto_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"auto_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#AutoSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Basic_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"basic_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#BasicSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Combo_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class OneOf(GeneratedSubmodelElementList):

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"oneOf",
                                "type_value_list_element": aas.SubmodelElement,
                                "semantic_id_list_element": global_ref(r"https://www.w3.org/2019/wot/security#oneOf"),
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#oneOf"),
                            }

                        def __init__(
                            self,
                            oneof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(oneof_items, str):
                                raise TypeError("oneof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(oneof_items, number_repeated=False)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class AllOf(GeneratedSubmodelElementList):

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"allOf",
                                "type_value_list_element": aas.SubmodelElement,
                                "semantic_id_list_element": global_ref(r"https://www.w3.org/2019/wot/security#allOf"),
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#allOf"),
                            }

                        def __init__(
                            self,
                            allof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(allof_items, str):
                                raise TypeError("allof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(allof_items, number_repeated=False)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"combo_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#ComboSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        oneOf: Union[Iterable[aas.SubmodelElement], OneOf],
                        allOf: Union[Iterable[aas.SubmodelElement], AllOf],
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # A str would be split into its characters
                        if isinstance(oneOf, str):
                            raise TypeError("oneOf takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if oneOf is not None and not isinstance(oneOf, aas.SubmodelElement):
                            oneOf = self.OneOf(oneOf)

                        # A str would be split into its characters
                        if isinstance(allOf, str):
                            raise TypeError("allOf takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if allOf is not None and not isinstance(allOf, aas.SubmodelElement):
                            allOf = self.AllOf(allOf)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, oneOf, allOf, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Apikey_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"apikey_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#APIKeySecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Psk_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Identity(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"identity",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#identity"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"psk_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#PSKSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        identity: Optional[Union[str, Identity]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if identity is not None and not isinstance(identity, aas.SubmodelElement):
                            identity = self.Identity(identity)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, identity, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Digest_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Qop(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"qop",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#qop"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"digest_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#DigestSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        qop: Optional[Union[str, Qop]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if qop is not None and not isinstance(qop, aas.SubmodelElement):
                            qop = self.Qop(qop)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, name, in_, qop, proxy)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Bearer_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Name(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"name",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#name"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class In(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"in",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#in"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Authorization(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"authorization",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#authorization"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Alg(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"alg",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#alg"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Format(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"format",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#format"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"bearer_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#BearerSecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        authorization: Optional[Union[str, Authorization]] = None,
                        alg: Optional[Union[str, Alg]] = None,
                        format: Optional[Union[str, Format]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if in_ is not None and not isinstance(in_, aas.SubmodelElement):
                            in_ = self.In(in_)

                        # Build a submodel element if a raw value was passed in the argument

                        if authorization is not None and not isinstance(authorization, aas.SubmodelElement):
                            authorization = self.Authorization(authorization)

                        # Build a submodel element if a raw value was passed in the argument

                        if alg is not None and not isinstance(alg, aas.SubmodelElement):
                            alg = self.Alg(alg)

                        # Build a submodel element if a raw value was passed in the argument

                        if format is not None and not isinstance(format, aas.SubmodelElement):
                            format = self.Format(format)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            scheme, name, in_, authorization, alg, format, proxy
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Oauth2_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scheme",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#SecurityScheme"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Token(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"token",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#token"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Refresh(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"refresh",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#refresh"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Authorization(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"authorization",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#authorization"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Scopes(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"scopes",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#scopes"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Flow(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"flow",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#flow"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Proxy(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"proxy",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#proxy"),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"oauth2_sc",
                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"),
                        }

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        token: Optional[Union[xsd.AnyURI, Token]] = None,
                        refresh: Optional[Union[xsd.AnyURI, Refresh]] = None,
                        authorization: Optional[Union[xsd.AnyURI, Authorization]] = None,
                        scopes: Optional[Union[str, Scopes]] = None,
                        flow: Optional[Union[str, Flow]] = None,
                        proxy: Optional[Union[xsd.AnyURI, Proxy]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if token is not None and not isinstance(token, aas.SubmodelElement):
                            token = self.Token(token)

                        # Build a submodel element if a raw value was passed in the argument

                        if refresh is not None and not isinstance(refresh, aas.SubmodelElement):
                            refresh = self.Refresh(refresh)

                        # Build a submodel element if a raw value was passed in the argument

                        if authorization is not None and not isinstance(authorization, aas.SubmodelElement):
                            authorization = self.Authorization(authorization)

                        # Build a submodel element if a raw value was passed in the argument

                        if scopes is not None and not isinstance(scopes, aas.SubmodelElement):
                            scopes = self.Scopes(scopes)

                        # Build a submodel element if a raw value was passed in the argument

                        if flow is not None and not isinstance(flow, aas.SubmodelElement):
                            flow = self.Flow(flow)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            scheme, token, refresh, authorization, scopes, flow, proxy
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"securityDefinitions",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#definesSecurityScheme"),
                    }

                def __init__(
                    self,
                    nosec_sc: Optional[Nosec_sc] = None,
                    auto_sc: Optional[Auto_sc] = None,
                    basic_sc: Optional[Basic_sc] = None,
                    combo_sc: Optional[Combo_sc] = None,
                    apikey_sc: Optional[Apikey_sc] = None,
                    psk_sc: Optional[Psk_sc] = None,
                    digest_sc: Optional[Digest_sc] = None,
                    bearer_sc: Optional[Bearer_sc] = None,
                    oauth2_sc: Optional[Oauth2_sc] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        nosec_sc, auto_sc, basic_sc, combo_sc, apikey_sc, psk_sc, digest_sc, bearer_sc, oauth2_sc
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"EndpointMetadata",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
                    ),
                }

            def __init__(
                self,
                base: Union[xsd.AnyURI, Base],
                contentType: Union[str, ContentType],
                security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                securityDefinitions: SecurityDefinitions,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if base is not None and not isinstance(base, aas.SubmodelElement):
                    base = self.Base(base)

                # Build a submodel element if a raw value was passed in the argument

                if contentType is not None and not isinstance(contentType, aas.SubmodelElement):
                    contentType = self.ContentType(contentType)

                # A str would be split into its characters
                if isinstance(security, str):
                    raise TypeError("security takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if security is not None and not isinstance(security, aas.SubmodelElement):
                    security = self.Security(security)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(base, contentType, security, securityDefinitions)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class InteractionMetadata(aas.SubmodelElementCollection):

            class Properties(aas.SubmodelElementCollection):

                class Property_name(aas.SubmodelElementCollection):

                    class Key(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"key",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                ),
                                "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#name"),),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Type(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"type",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Title(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"title",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Observable(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"observable",
                                "value_type": bool,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                            }

                        def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Const(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"const",
                                "value_type": xsd.Int,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                            }

                        def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Default(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"default",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Unit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"unit",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://schema.org/unitCode"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Min_max(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"min_max",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for number-/interger-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class LengthRange(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"lengthRange",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for string-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class Items(aas.SubmodelElementCollection):

                        class Type(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"type",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Unit(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"unit",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Default(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"default",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Const(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"const",
                                    "value_type": xsd.Int,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                }

                            def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Observable(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"observable",
                                    "value_type": bool,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                }

                            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Title(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"title",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Min_max(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"min_max",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for number-/interger-based values",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Select",
                                            value_type=str,
                                            value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                    "supplemental_semantic_id": (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                    ),
                                }

                            def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class LengthRange(aas.Range):

                            @staticmethod
                            def template_defaults() -> RangeMetadata:
                                return {
                                    "id_short": r"lengthRange",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                    ),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for string-based values",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Select",
                                            value_type=str,
                                            value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                    "supplemental_semantic_id": (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                    ),
                                }

                            def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                        class ValueSemantics(aas.ReferenceElement):

                            @staticmethod
                            def template_defaults() -> ReferenceElementMetadata:
                                return {
                                    "id_short": r"valueSemantics",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                    ),
                                }

                            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"items",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#items"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for array-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(
                            self,
                            type: Optional[Union[str, Type]] = None,
                            unit: Optional[Union[str, Unit]] = None,
                            default: Optional[Union[str, Default]] = None,
                            const: Optional[Union[xsd.Int, Const]] = None,
                            observable: Optional[Union[bool, Observable]] = None,
                            title: Optional[Union[str, Title]] = None,
                            min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                            lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                            valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if type is not None and not isinstance(type, aas.SubmodelElement):
                                type = self.Type(type)

                            # Build a submodel element if a raw value was passed in the argument

                            if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                unit = self.Unit(unit)

                            # Build a submodel element if a raw value was passed in the argument

                            if default is not None and not isinstance(default, aas.SubmodelElement):
                                default = self.Default(default)

                            # Build a submodel element if a raw value was passed in the argument

                            if const is not None and not isinstance(const, aas.SubmodelElement):
                                const = self.Const(const)

                            # Build a submodel element if a raw value was passed in the argument

                            if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                observable = self.Observable(observable)

                            # Build a submodel element if a raw value was passed in the argument

                            if title is not None and not isinstance(title, aas.SubmodelElement):
                                title = self.Title(title)

                            # Build a submodel element if a raw value was passed in the argument

                            if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                min_max = self.Min_max(min=min_max[0], max=min_max[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                            # Build a submodel element if a raw value was passed in the argument

                            if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                                valueSemantics = self.ValueSemantics(valueSemantics)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                type, unit, default, const, observable, title, min_max, lengthRange, valueSemantics
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class ItemsRange(aas.Range):

                        @staticmethod
                        def template_defaults() -> RangeMetadata:
                            return {
                                "id_short": r"itemsRange",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                ),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for string-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Select",
                                        value_type=str,
                                        value=r"minItems | maxItems | minItems AND maxItems as supplementalSem.Id",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                ),
                            }

                        def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                            super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                    class Properties(aas.SubmodelElementCollection):

                        class Property_name(aas.SubmodelElementCollection):

                            class Key(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"key",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Type(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"type",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Title(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"title",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Observable(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"observable",
                                        "value_type": bool,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                    }

                                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Const(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"const",
                                        "value_type": xsd.Int,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                    }

                                def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Default(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"default",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#default"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Unit(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"unit",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Min_max(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"min_max",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for number-/interger-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class LengthRange(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"lengthRange",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for string-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class Items(aas.SubmodelElementCollection):

                                class Type(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"type",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class ValueSemantics(aas.ReferenceElement):

                                    @staticmethod
                                    def template_defaults() -> ReferenceElementMetadata:
                                        return {
                                            "id_short": r"valueSemantics",
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                            ),
                                        }

                                    def __init__(
                                        self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]
                                    ):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Unit(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"unit",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://schema.org/unitCode"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Default(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"default",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://www.w3.org/2019/wot/json-schema#default"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Const(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"const",
                                            "value_type": xsd.Int,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#const"),
                                        }

                                    def __init__(self, value: xsd.Int, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Observable(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"observable",
                                            "value_type": bool,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#isObservable"),
                                        }

                                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Title(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"title",
                                            "value_type": str,
                                            "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#title"),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Min_max(aas.Range):

                                    @staticmethod
                                    def template_defaults() -> RangeMetadata:
                                        return {
                                            "id_short": r"min_max",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                            ),
                                            "qualifier": (
                                                aas.Qualifier(
                                                    type_=r"Constraint",
                                                    value_type=str,
                                                    value=r"Only applicable for number-/interger-based values",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                                aas.Qualifier(
                                                    type_=r"Select",
                                                    value_type=str,
                                                    value=r"minimum | maximum | minimum AND maximum as supplementalSem.Id",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            ),
                                            "supplemental_semantic_id": (
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                            ),
                                        }

                                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                                class LengthRange(aas.Range):

                                    @staticmethod
                                    def template_defaults() -> RangeMetadata:
                                        return {
                                            "id_short": r"lengthRange",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                            ),
                                            "qualifier": (
                                                aas.Qualifier(
                                                    type_=r"Constraint",
                                                    value_type=str,
                                                    value=r"Only applicable for string-based values",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                                aas.Qualifier(
                                                    type_=r"Select",
                                                    value_type=str,
                                                    value=r"minLength | maxLength | minLength AND maxLength as supplementalSem.Id",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            ),
                                            "supplemental_semantic_id": (
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                            ),
                                        }

                                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"items",
                                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#items"),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for array-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                    }

                                def __init__(
                                    self,
                                    type: Optional[Union[str, Type]] = None,
                                    valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                                    unit: Optional[Union[str, Unit]] = None,
                                    default: Optional[Union[str, Default]] = None,
                                    const: Optional[Union[xsd.Int, Const]] = None,
                                    observable: Optional[Union[bool, Observable]] = None,
                                    title: Optional[Union[str, Title]] = None,
                                    min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                                    lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if type is not None and not isinstance(type, aas.SubmodelElement):
                                        type = self.Type(type)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if valueSemantics is not None and not isinstance(
                                        valueSemantics, aas.SubmodelElement
                                    ):
                                        valueSemantics = self.ValueSemantics(valueSemantics)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                        unit = self.Unit(unit)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if default is not None and not isinstance(default, aas.SubmodelElement):
                                        default = self.Default(default)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if const is not None and not isinstance(const, aas.SubmodelElement):
                                        const = self.Const(const)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                        observable = self.Observable(observable)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if title is not None and not isinstance(title, aas.SubmodelElement):
                                        title = self.Title(title)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                        min_max = self.Min_max(min=min_max[0], max=min_max[1])

                                    # Build a submodel element if a raw value was passed in the argument

                                    if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                        lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        type,
                                        valueSemantics,
                                        unit,
                                        default,
                                        const,
                                        observable,
                                        title,
                                        min_max,
                                        lengthRange,
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class ItemsRange(aas.Range):

                                @staticmethod
                                def template_defaults() -> RangeMetadata:
                                    return {
                                        "id_short": r"itemsRange",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for string-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Select",
                                                value_type=str,
                                                value=r"minItems | maxItems | minItems AND maxItems as supplementalSem.Id",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                        "supplemental_semantic_id": (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                        ),
                                    }

                                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                            class Properties(aas.SubmodelElementCollection):

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"properties",
                                        "semantic_id": global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                        ),
                                        "qualifier": (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for object-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                            aas.Qualifier(
                                                type_=r"Comment",
                                                value_type=str,
                                                value=r"Recusive definition of last propertyName SMC",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        ),
                                    }

                                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements()

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class ValueSemantics(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {
                                        "id_short": r"valueSemantics",
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                        ),
                                    }

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"property_name",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Current counter value",
                                            r"de": r"Derzeitiger Zählerwert",
                                            r"it": r"Valore attuale del contatore",
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#propertyName"),
                                }

                            def __init__(
                                self,
                                key: Optional[Union[str, Key]] = None,
                                type: Optional[Union[str, Type]] = None,
                                title: Optional[Union[str, Title]] = None,
                                observable: Optional[Union[bool, Observable]] = None,
                                const: Optional[Union[xsd.Int, Const]] = None,
                                default: Optional[Union[str, Default]] = None,
                                unit: Optional[Union[str, Unit]] = None,
                                min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                                lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                                items: Optional[Items] = None,
                                itemsRange: Optional[Union[Tuple[str, str], ItemsRange]] = None,
                                properties: Optional[Properties] = None,
                                valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if key is not None and not isinstance(key, aas.SubmodelElement):
                                    key = self.Key(key)

                                # Build a submodel element if a raw value was passed in the argument

                                if type is not None and not isinstance(type, aas.SubmodelElement):
                                    type = self.Type(type)

                                # Build a submodel element if a raw value was passed in the argument

                                if title is not None and not isinstance(title, aas.SubmodelElement):
                                    title = self.Title(title)

                                # Build a submodel element if a raw value was passed in the argument

                                if observable is not None and not isinstance(observable, aas.SubmodelElement):
                                    observable = self.Observable(observable)

                                # Build a submodel element if a raw value was passed in the argument

                                if const is not None and not isinstance(const, aas.SubmodelElement):
                                    const = self.Const(const)

                                # Build a submodel element if a raw value was passed in the argument

                                if default is not None and not isinstance(default, aas.SubmodelElement):
                                    default = self.Default(default)

                                # Build a submodel element if a raw value was passed in the argument

                                if unit is not None and not isinstance(unit, aas.SubmodelElement):
                                    unit = self.Unit(unit)

                                # Build a submodel element if a raw value was passed in the argument

                                if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                                    min_max = self.Min_max(min=min_max[0], max=min_max[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                                    lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if itemsRange is not None and not isinstance(itemsRange, aas.SubmodelElement):
                                    itemsRange = self.ItemsRange(min=itemsRange[0], max=itemsRange[1])

                                # Build a submodel element if a raw value was passed in the argument

                                if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                                    valueSemantics = self.ValueSemantics(valueSemantics)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    key,
                                    type,
                                    title,
                                    observable,
                                    const,
                                    default,
                                    unit,
                                    min_max,
                                    lengthRange,
                                    items,
                                    itemsRange,
                                    properties,
                                    valueSemantics,
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"properties",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/json-schema#properties"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for object-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(
                            self,
                            property_name: Optional[Iterable[Property_name]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(property_name, str):
                                raise TypeError("property_name takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(property_name)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class ValueSemantics(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"valueSemantics",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Forms(aas.SubmodelElementCollection):

                        class Href(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"href",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#hasTarget"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ContentType(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"contentType",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/hypermedia#forContentType"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Security(GeneratedSubmodelElementList):

                            class Security_item(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {"id_short": None}

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"security",
                                    "type_value_list_element": aas.ReferenceElement,
                                    "semantic_id_list_element": global_ref(
                                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                    ),
                                }

                            def __init__(
                                self,
                                security_items: Iterable[Union[aas.Reference, Security_item]],
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(security_items, str):
                                    raise TypeError("security_items takes several elements, got a str")

                                # Build submodel elements from raw values passed in the argument
                                if security_items:
                                    security_items = [
                                        i if isinstance(i, aas.SubmodelElement) else self.Security_item(i)
                                        for i in security_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    security_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class Mqv_retain(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"mqv_retain",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/mqtt#hasRetainFlag"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for MQTT binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Mqv_controlPacket(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"mqv_controlPacket",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/mqtt#ControlPacket"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for MQTT binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Mqv_qos(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"mqv_qos",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"https://www.w3.org/2019/wot/mqtt#hasQoSFlag"),
                                    "qualifier": (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for MQTT binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"forms",
                                "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#hasForm"),
                            }

                        def __init__(
                            self,
                            href: Union[str, Href],
                            security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                            contentType: Optional[Union[str, ContentType]] = None,
                            mqv_retain: Optional[Union[str, Mqv_retain]] = None,
                            mqv_controlPacket: Optional[Union[str, Mqv_controlPacket]] = None,
                            mqv_qos: Optional[Union[str, Mqv_qos]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if href is not None and not isinstance(href, aas.SubmodelElement):
                                href = self.Href(href)

                            # Build a submodel element if a raw value was passed in the argument

                            if contentType is not None and not isinstance(contentType, aas.SubmodelElement):
                                contentType = self.ContentType(contentType)

                            # A str would be split into its characters
                            if isinstance(security, str):
                                raise TypeError("security takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if security is not None and not isinstance(security, aas.SubmodelElement):
                                security = self.Security(security)

                            # Build a submodel element if a raw value was passed in the argument

                            if mqv_retain is not None and not isinstance(mqv_retain, aas.SubmodelElement):
                                mqv_retain = self.Mqv_retain(mqv_retain)

                            # Build a submodel element if a raw value was passed in the argument

                            if mqv_controlPacket is not None and not isinstance(mqv_controlPacket, aas.SubmodelElement):
                                mqv_controlPacket = self.Mqv_controlPacket(mqv_controlPacket)

                            # Build a submodel element if a raw value was passed in the argument

                            if mqv_qos is not None and not isinstance(mqv_qos, aas.SubmodelElement):
                                mqv_qos = self.Mqv_qos(mqv_qos)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                href, contentType, security, mqv_retain, mqv_controlPacket, mqv_qos
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"property_name",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Current counter value",
                                    r"de": r"Derzeitiger Zählerwert",
                                    r"it": r"Valore attuale del contatore",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AssetInterfaceDescription/1/0/PropertyDefinition"
                            ),
                            "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#name"),),
                        }

                    def __init__(
                        self,
                        forms: Forms,
                        key: Optional[Union[str, Key]] = None,
                        type: Optional[Union[str, Type]] = None,
                        title: Optional[Union[str, Title]] = None,
                        observable: Optional[Union[bool, Observable]] = None,
                        const: Optional[Union[xsd.Int, Const]] = None,
                        default: Optional[Union[str, Default]] = None,
                        unit: Optional[Union[str, Unit]] = None,
                        min_max: Optional[Union[Tuple[str, str], Min_max]] = None,
                        lengthRange: Optional[Union[Tuple[str, str], LengthRange]] = None,
                        items: Optional[Items] = None,
                        itemsRange: Optional[Union[Tuple[str, str], ItemsRange]] = None,
                        properties: Optional[Properties] = None,
                        valueSemantics: Optional[Union[aas.Reference, ValueSemantics]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if key is not None and not isinstance(key, aas.SubmodelElement):
                            key = self.Key(key)

                        # Build a submodel element if a raw value was passed in the argument

                        if type is not None and not isinstance(type, aas.SubmodelElement):
                            type = self.Type(type)

                        # Build a submodel element if a raw value was passed in the argument

                        if title is not None and not isinstance(title, aas.SubmodelElement):
                            title = self.Title(title)

                        # Build a submodel element if a raw value was passed in the argument

                        if observable is not None and not isinstance(observable, aas.SubmodelElement):
                            observable = self.Observable(observable)

                        # Build a submodel element if a raw value was passed in the argument

                        if const is not None and not isinstance(const, aas.SubmodelElement):
                            const = self.Const(const)

                        # Build a submodel element if a raw value was passed in the argument

                        if default is not None and not isinstance(default, aas.SubmodelElement):
                            default = self.Default(default)

                        # Build a submodel element if a raw value was passed in the argument

                        if unit is not None and not isinstance(unit, aas.SubmodelElement):
                            unit = self.Unit(unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if min_max is not None and not isinstance(min_max, aas.SubmodelElement):
                            min_max = self.Min_max(min=min_max[0], max=min_max[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if lengthRange is not None and not isinstance(lengthRange, aas.SubmodelElement):
                            lengthRange = self.LengthRange(min=lengthRange[0], max=lengthRange[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if itemsRange is not None and not isinstance(itemsRange, aas.SubmodelElement):
                            itemsRange = self.ItemsRange(min=itemsRange[0], max=itemsRange[1])

                        # Build a submodel element if a raw value was passed in the argument

                        if valueSemantics is not None and not isinstance(valueSemantics, aas.SubmodelElement):
                            valueSemantics = self.ValueSemantics(valueSemantics)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            key,
                            type,
                            title,
                            observable,
                            const,
                            default,
                            unit,
                            min_max,
                            lengthRange,
                            items,
                            itemsRange,
                            properties,
                            valueSemantics,
                            forms,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"properties",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#PropertyAffordance"),
                    }

                def __init__(
                    self,
                    property_name: Optional[Iterable[Property_name]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(property_name, str):
                        raise TypeError("property_name takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(property_name)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Actions(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"actions",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#ActionAffordance"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Events(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"events",
                        "semantic_id": global_ref(r"https://www.w3.org/2019/wot/td#EventAffordance"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InteractionMetadata",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
                    ),
                    "supplemental_semantic_id": (global_ref(r"https://www.w3.org/2019/wot/td#InteractionAffordance"),),
                }

            def __init__(
                self,
                properties: Optional[Properties] = None,
                actions: Optional[Actions] = None,
                events: Optional[Events] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(properties, actions, events)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ExternalDescriptor(aas.SubmodelElementCollection):

            class FileName(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"fileName",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ExternalDescriptor",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
                    ),
                }

            def __init__(self, fileName: FileName, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(fileName)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"InterfaceTemplateForMQTT",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"),
                "supplemental_semantic_id": (
                    global_ref(r"http://www.w3.org/2011/mqtt"),
                    global_ref(r"https://www.w3.org/2019/wot/td"),
                ),
            }

        def __init__(
            self,
            title: Union[str, Title],
            endpointMetadata: EndpointMetadata,
            interactionMetadata: InteractionMetadata,
            created: Optional[Union[xsd.DateTime, Created]] = None,
            modified: Optional[Union[xsd.DateTime, Modified]] = None,
            support: Optional[Union[xsd.AnyURI, Support]] = None,
            externalDescriptor: Optional[ExternalDescriptor] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if title is not None and not isinstance(title, aas.SubmodelElement):
                title = self.Title(title)

            # Build a submodel element if a raw value was passed in the argument

            if created is not None and not isinstance(created, aas.SubmodelElement):
                created = self.Created(created)

            # Build a submodel element if a raw value was passed in the argument

            if modified is not None and not isinstance(modified, aas.SubmodelElement):
                modified = self.Modified(modified)

            # Build a submodel element if a raw value was passed in the argument

            if support is not None and not isinstance(support, aas.SubmodelElement):
                support = self.Support(support)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                title, created, modified, support, endpointMetadata, interactionMetadata, externalDescriptor
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"AssetInterfacesDescription",
            "description": aas.MultiLanguageTextType(dict_={r"en": r"AID Template Sample"}),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Submodel"),
        }

    def __init__(
        self,
        id_: str,
        interfaceTemplateForHTTP: Optional[Iterable[InterfaceTemplateForHTTP]] = None,
        interfaceTemplateForMODBUS: Optional[Iterable[InterfaceTemplateForMODBUS]] = None,
        interfaceTemplateForMQTT: Optional[Iterable[InterfaceTemplateForMQTT]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(interfaceTemplateForHTTP, str):
            raise TypeError("interfaceTemplateForHTTP takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(interfaceTemplateForMODBUS, str):
            raise TypeError("interfaceTemplateForMODBUS takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(interfaceTemplateForMQTT, str):
            raise TypeError("interfaceTemplateForMQTT takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            interfaceTemplateForHTTP, interfaceTemplateForMODBUS, interfaceTemplateForMQTT
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
