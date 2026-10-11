from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
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


class AssetInterfacesDescription(aas.Submodel):

    class InterfaceTemplateForHTTP(aas.SubmodelElementCollection):

        class Title(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"title",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#title"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Created(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"created",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"http://purl.org/dc/terms/created"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Modified(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"modified",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"http://purl.org/dc/terms/modified"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Support(aas.Property):

            def __init__(
                self,
                value: xsd.AnyURI,
                id_short: Optional[str] = r"support",
                value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#supportContact"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class EndpointMetadata(aas.SubmodelElementCollection):

            class Base(aas.Property):

                def __init__(
                    self,
                    value: xsd.AnyURI,
                    id_short: Optional[str] = r"base",
                    value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#baseURI"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ContentType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"contentType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/hypermedia#forContentType"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Security(GeneratedSubmodelElementList):

                class Security_item(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = None,
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    security_items: Iterable[Union[aas.Reference, Security_item]],
                    id_short: Optional[str] = r"security",
                    type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                    semantic_id_list_element: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                    ),
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SecurityDefinitions(aas.SubmodelElementCollection):

                class Nosec_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        id_short: Optional[str] = r"nosec_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#NoSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme)

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Auto_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"auto_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#AutoSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, proxy)

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Basic_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"basic_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#BasicSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Combo_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class OneOf(GeneratedSubmodelElementList):

                        def __init__(
                            self,
                            oneof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            id_short: Optional[str] = r"oneOf",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#allOf"
                            ),
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#oneOf"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(oneof_items, str):
                                raise TypeError("oneof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(oneof_items, number_repeated=False)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                type_value_list_element=type_value_list_element,
                                semantic_id_list_element=semantic_id_list_element,
                                value_type_list_element=value_type_list_element,
                                order_relevant=order_relevant,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class AllOf(GeneratedSubmodelElementList):

                        def __init__(
                            self,
                            allof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            id_short: Optional[str] = r"allOf",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#allOf"
                            ),
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#allOf"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(allof_items, str):
                                raise TypeError("allof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(allof_items, number_repeated=False)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                type_value_list_element=type_value_list_element,
                                semantic_id_list_element=semantic_id_list_element,
                                value_type_list_element=value_type_list_element,
                                order_relevant=order_relevant,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        oneOf: Union[Iterable[aas.SubmodelElement], OneOf],
                        allOf: Union[Iterable[aas.SubmodelElement], AllOf],
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"combo_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#ComboSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Apikey_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"apikey_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#APIKeySecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Psk_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Identity(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"identity",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#identity"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        identity: Optional[Union[str, Identity]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"psk_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#PSKSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Digest_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Qop(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"qop",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#qop"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        qop: Optional[Union[str, Qop]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"digest_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#DigestSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Bearer_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Authorization(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"authorization",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#authorization"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Alg(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"alg",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#alg"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Format(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"format",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#format"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        authorization: Optional[Union[str, Authorization]] = None,
                        alg: Optional[Union[str, Alg]] = None,
                        format: Optional[Union[str, Format]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"bearer_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#BearerSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Oauth2_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Token(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"token",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#token"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Refresh(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"refresh",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#refresh"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Authorization(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"authorization",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#authorization"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Scopes(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scopes",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#scopes"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Flow(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"flow",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#flow"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        token: Optional[Union[xsd.AnyURI, Token]] = None,
                        refresh: Optional[Union[xsd.AnyURI, Refresh]] = None,
                        authorization: Optional[Union[xsd.AnyURI, Authorization]] = None,
                        scopes: Optional[Union[str, Scopes]] = None,
                        flow: Optional[Union[str, Flow]] = None,
                        proxy: Optional[Union[xsd.AnyURI, Proxy]] = None,
                        id_short: Optional[str] = r"oauth2_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

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
                    id_short: Optional[str] = r"securityDefinitions",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#definesSecurityScheme"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        nosec_sc, auto_sc, basic_sc, combo_sc, apikey_sc, psk_sc, digest_sc, bearer_sc, oauth2_sc
                    )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                base: Union[xsd.AnyURI, Base],
                contentType: Union[str, ContentType],
                security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                securityDefinitions: SecurityDefinitions,
                id_short: Optional[str] = r"EndpointMetadata",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class InteractionMetadata(aas.SubmodelElementCollection):

            class Properties(aas.SubmodelElementCollection):

                class Property_name(aas.SubmodelElementCollection):

                    class Key(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"key",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/td#name"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Type(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"type",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Title(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"title",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#title"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Observable(aas.Property):

                        def __init__(
                            self,
                            value: bool,
                            id_short: Optional[str] = r"observable",
                            value_type: aas.DataTypeDefXsd = bool,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/td#isObservable"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Const(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Int,
                            id_short: Optional[str] = r"const",
                            value_type: aas.DataTypeDefXsd = xsd.Int,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#const"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Default(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"default",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#default"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Unit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"unit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Min_max(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"min_max",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class LengthRange(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"lengthRange",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Items(aas.SubmodelElementCollection):

                        class Type(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"type",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Unit(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"unit",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Default(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"default",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#default"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Const(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Int,
                                id_short: Optional[str] = r"const",
                                value_type: aas.DataTypeDefXsd = xsd.Int,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#const"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Observable(aas.Property):

                            def __init__(
                                self,
                                value: bool,
                                id_short: Optional[str] = r"observable",
                                value_type: aas.DataTypeDefXsd = bool,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#isObservable"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Title(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"title",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#title"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Min_max(aas.Range):

                            def __init__(
                                self,
                                min: str,
                                max: str,
                                id_short: Optional[str] = r"min_max",
                                value_type: aas.DataTypeDefXsd = str,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                ),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
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
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    min=min,
                                    max=max,
                                    id_short=id_short,
                                    value_type=value_type,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class LengthRange(aas.Range):

                            def __init__(
                                self,
                                min: str,
                                max: str,
                                id_short: Optional[str] = r"lengthRange",
                                value_type: aas.DataTypeDefXsd = str,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                ),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
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
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    min=min,
                                    max=max,
                                    id_short=id_short,
                                    value_type=value_type,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class ValueSemantics(aas.ReferenceElement):

                            def __init__(
                                self,
                                value: aas.Reference,
                                id_short: Optional[str] = r"valueSemantics",
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

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
                            id_short: Optional[str] = r"items",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#items"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for array-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

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

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ItemsRange(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"itemsRange",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Properties(aas.SubmodelElementCollection):

                        class Property_name(aas.SubmodelElementCollection):

                            class Key(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"key",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Type(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"type",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Title(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"title",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/td#title"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Observable(aas.Property):

                                def __init__(
                                    self,
                                    value: bool,
                                    id_short: Optional[str] = r"observable",
                                    value_type: aas.DataTypeDefXsd = bool,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/td#isObservable"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Const(aas.Property):

                                def __init__(
                                    self,
                                    value: xsd.Int,
                                    id_short: Optional[str] = r"const",
                                    value_type: aas.DataTypeDefXsd = xsd.Int,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#const"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Default(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"default",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#default"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Unit(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"unit",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Min_max(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"min_max",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class LengthRange(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"lengthRange",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Items(aas.SubmodelElementCollection):

                                class Type(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"type",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class ValueSemantics(aas.ReferenceElement):

                                    def __init__(
                                        self,
                                        value: aas.Reference,
                                        id_short: Optional[str] = r"valueSemantics",
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Unit(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"unit",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://schema.org/unitCode"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Default(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"default",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#default"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Const(aas.Property):

                                    def __init__(
                                        self,
                                        value: xsd.Int,
                                        id_short: Optional[str] = r"const",
                                        value_type: aas.DataTypeDefXsd = xsd.Int,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#const"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Observable(aas.Property):

                                    def __init__(
                                        self,
                                        value: bool,
                                        id_short: Optional[str] = r"observable",
                                        value_type: aas.DataTypeDefXsd = bool,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/td#isObservable"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Title(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"title",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/td#title"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Min_max(aas.Range):

                                    def __init__(
                                        self,
                                        min: str,
                                        max: str,
                                        id_short: Optional[str] = r"min_max",
                                        value_type: aas.DataTypeDefXsd = str,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                        ),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = (
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
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            min=min,
                                            max=max,
                                            id_short=id_short,
                                            value_type=value_type,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class LengthRange(aas.Range):

                                    def __init__(
                                        self,
                                        min: str,
                                        max: str,
                                        id_short: Optional[str] = r"lengthRange",
                                        value_type: aas.DataTypeDefXsd = str,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                        ),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = (
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
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            min=min,
                                            max=max,
                                            id_short=id_short,
                                            value_type=value_type,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

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
                                    id_short: Optional[str] = r"items",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#items"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for array-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

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
                                        value=embedded_submodel_elements,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class ItemsRange(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"itemsRange",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Properties(aas.SubmodelElementCollection):

                                def __init__(
                                    self,
                                    id_short: Optional[str] = r"properties",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements()

                                    super().__init__(
                                        value=embedded_submodel_elements,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class ValueSemantics(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = r"valueSemantics",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

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
                                id_short: Optional[str] = r"property_name",
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Current counter value",
                                            r"de": r"Derzeitiger Zählerwert",
                                            r"it": r"Valore attuale del contatore",
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

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
                                    value=embedded_submodel_elements,
                                    id_short=id_short,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        def __init__(
                            self,
                            property_name: Optional[Iterable[Property_name]] = None,
                            id_short: Optional[str] = r"properties",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#properties"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for object-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(property_name, str):
                                raise TypeError("property_name takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(property_name)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ValueSemantics(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = r"valueSemantics",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Forms(aas.SubmodelElementCollection):

                        class Href(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"href",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/hypermedia#hasTarget"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class ContentType(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"contentType",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/hypermedia#forContentType"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Security(GeneratedSubmodelElementList):

                            class Security_item(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = None,
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            def __init__(
                                self,
                                security_items: Iterable[Union[aas.Reference, Security_item]],
                                id_short: Optional[str] = r"security",
                                type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                                semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                ),
                                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                                order_relevant: bool = True,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

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
                                    value=embedded_submodel_elements,
                                    id_short=id_short,
                                    type_value_list_element=type_value_list_element,
                                    semantic_id_list_element=semantic_id_list_element,
                                    value_type_list_element=value_type_list_element,
                                    order_relevant=order_relevant,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Htv_methodName(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"htv_methodName",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2011/http#methodName"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for HTTP binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Htv_headers(GeneratedSubmodelElementList):

                            class Htv_headers_item(aas.SubmodelElementCollection):

                                class Htv_fieldName(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"htv_fieldName",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2011/http#fieldName"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Htv_fieldValue(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"htv_fieldValue",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2011/http#fieldValue"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                def __init__(
                                    self,
                                    htv_fieldName: Union[str, Htv_fieldName],
                                    htv_fieldValue: Union[str, Htv_fieldValue],
                                    id_short: Optional[str] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2011/http#headers"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

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
                                        value=embedded_submodel_elements,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            def __init__(
                                self,
                                htv_headers_items: Iterable[Htv_headers_item],
                                id_short: Optional[str] = r"htv_headers",
                                type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                                semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2011/http#headers"
                                ),
                                value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                                order_relevant: bool = True,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2011/http#headers"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for HTTP binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(htv_headers_items, str):
                                    raise TypeError("htv_headers_items takes several elements, got a str")

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    htv_headers_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements,
                                    id_short=id_short,
                                    type_value_list_element=type_value_list_element,
                                    semantic_id_list_element=semantic_id_list_element,
                                    value_type_list_element=value_type_list_element,
                                    order_relevant=order_relevant,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        def __init__(
                            self,
                            href: Union[str, Href],
                            security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                            contentType: Optional[Union[str, ContentType]] = None,
                            htv_methodName: Optional[Union[str, Htv_methodName]] = None,
                            htv_headers: Optional[Union[Iterable[Htv_headers.Htv_headers_item], Htv_headers]] = None,
                            id_short: Optional[str] = r"forms",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/td#hasForm"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

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

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

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
                        id_short: Optional[str] = r"property_name",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/AssetInterfaceDescription/1/0/PropertyDefinition"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (
                            global_ref(r"https://www.w3.org/2019/wot/td#name"),
                        ),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Current counter value",
                                    r"de": r"Derzeitiger Zählerwert",
                                    r"it": r"Valore attuale del contatore",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    property_name: Optional[Iterable[Property_name]] = None,
                    id_short: Optional[str] = r"properties",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#PropertyAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(property_name, str):
                        raise TypeError("property_name takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(property_name)

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Actions(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"actions",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#ActionAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Events(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"events",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#EventAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                properties: Optional[Properties] = None,
                actions: Optional[Actions] = None,
                events: Optional[Events] = None,
                id_short: Optional[str] = r"InteractionMetadata",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://www.w3.org/2019/wot/td#InteractionAffordance"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(properties, actions, events)

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ExternalDescriptor(aas.SubmodelElementCollection):

            class FileName(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"fileName",
                    content_type: Optional[str] = r"application/json",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        content_type=content_type,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                fileName: FileName,
                id_short: Optional[str] = r"ExternalDescriptor",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(fileName)

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            title: Union[str, Title],
            endpointMetadata: EndpointMetadata,
            interactionMetadata: InteractionMetadata,
            created: Optional[Union[xsd.DateTime, Created]] = None,
            modified: Optional[Union[xsd.DateTime, Modified]] = None,
            support: Optional[Union[xsd.AnyURI, Support]] = None,
            externalDescriptor: Optional[ExternalDescriptor] = None,
            id_short: Optional[str] = r"InterfaceTemplateForHTTP",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"http://www.w3.org/2011/http"),
                global_ref(r"https://www.w3.org/2019/wot/td"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

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

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class InterfaceTemplateForMODBUS(aas.SubmodelElementCollection):

        class Title(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"title",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#title"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Created(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"created",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"http://purl.org/dc/terms/created"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Modified(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"modified",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"http://purl.org/dc/terms/modified"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Support(aas.Property):

            def __init__(
                self,
                value: xsd.AnyURI,
                id_short: Optional[str] = r"support",
                value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#support"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class EndpointMetadata(aas.SubmodelElementCollection):

            class Base(aas.Property):

                def __init__(
                    self,
                    value: xsd.AnyURI,
                    id_short: Optional[str] = r"base",
                    value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#base"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ContentType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"contentType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/hypermedia#forContentType"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Security(GeneratedSubmodelElementList):

                class Security_item(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = None,
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    security_items: Iterable[Union[aas.Reference, Security_item]],
                    id_short: Optional[str] = r"security",
                    type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                    semantic_id_list_element: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                    ),
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SecurityDefinitions(aas.SubmodelElementCollection):

                class Nosec_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        id_short: Optional[str] = r"nosec_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#NoSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme)

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Auto_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"auto_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#AutoSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, proxy)

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Basic_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"basic_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#BasicSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Combo_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class OneOf(GeneratedSubmodelElementList):

                        def __init__(
                            self,
                            oneof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            id_short: Optional[str] = r"oneOf",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#oneOf"
                            ),
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#oneOf"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(oneof_items, str):
                                raise TypeError("oneof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(oneof_items, number_repeated=False)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                type_value_list_element=type_value_list_element,
                                semantic_id_list_element=semantic_id_list_element,
                                value_type_list_element=value_type_list_element,
                                order_relevant=order_relevant,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class AllOf(GeneratedSubmodelElementList):

                        def __init__(
                            self,
                            allof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            id_short: Optional[str] = r"allOf",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#allOf"
                            ),
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#allOf"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(allof_items, str):
                                raise TypeError("allof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(allof_items, number_repeated=False)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                type_value_list_element=type_value_list_element,
                                semantic_id_list_element=semantic_id_list_element,
                                value_type_list_element=value_type_list_element,
                                order_relevant=order_relevant,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        oneOf: Union[Iterable[aas.SubmodelElement], OneOf],
                        allOf: Union[Iterable[aas.SubmodelElement], AllOf],
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"combo_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#ComboSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Apikey_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"apikey_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#APIKeySecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Psk_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Identity(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"identity",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#identity"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        identity: Optional[Union[str, Identity]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"psk_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#PSKSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Digest_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Qop(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"qop",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#qop"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        qop: Optional[Union[str, Qop]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"digest_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#DigestSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Bearer_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Authorization(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"authorization",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#authorization"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Alg(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"alg",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#alg"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Format(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"format",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#format"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        authorization: Optional[Union[str, Authorization]] = None,
                        alg: Optional[Union[str, Alg]] = None,
                        format: Optional[Union[str, Format]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"bearer_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#BearerSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Oauth2_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Token(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"token",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#token"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Refresh(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"refresh",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#refresh"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Authorization(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"authorization",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#authorization"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Scopes(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scopes",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#scopes"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Flow(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"flow",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#flow"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        token: Optional[Union[xsd.AnyURI, Token]] = None,
                        refresh: Optional[Union[xsd.AnyURI, Refresh]] = None,
                        authorization: Optional[Union[xsd.AnyURI, Authorization]] = None,
                        scopes: Optional[Union[str, Scopes]] = None,
                        flow: Optional[Union[str, Flow]] = None,
                        proxy: Optional[Union[xsd.AnyURI, Proxy]] = None,
                        id_short: Optional[str] = r"oauth2_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

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
                    id_short: Optional[str] = r"securityDefinitions",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#definesSecurityScheme"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        nosec_sc, auto_sc, basic_sc, combo_sc, apikey_sc, psk_sc, digest_sc, bearer_sc, oauth2_sc
                    )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Modv_mostSignificantByte(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"modv_mostSignificantByte",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/modbus#hasMostSignificantByte"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Constraint",
                                value_type=str,
                                value=r"Only applicable for Modbus binding",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Modv_mostSignificantWord(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"modv_mostSignificantWord",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/modbus#hasMostSignificantWord"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Constraint",
                                value_type=str,
                                value=r"Only applicable for Modbus binding",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                base: Union[xsd.AnyURI, Base],
                contentType: Union[str, ContentType],
                security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                securityDefinitions: SecurityDefinitions,
                modv_mostSignificantByte: Optional[Union[str, Modv_mostSignificantByte]] = None,
                modv_mostSignificantWord: Optional[Union[str, Modv_mostSignificantWord]] = None,
                id_short: Optional[str] = r"EndpointMetadata",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class InteractionMetadata(aas.SubmodelElementCollection):

            class Properties(aas.SubmodelElementCollection):

                class Property_name(aas.SubmodelElementCollection):

                    class Key(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"key",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/td#name"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Type(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"type",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Title(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"title",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#title"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Observable(aas.Property):

                        def __init__(
                            self,
                            value: bool,
                            id_short: Optional[str] = r"observable",
                            value_type: aas.DataTypeDefXsd = bool,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/td#isObservable"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Const(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Int,
                            id_short: Optional[str] = r"const",
                            value_type: aas.DataTypeDefXsd = xsd.Int,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#const"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Default(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"default",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#default"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Unit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"unit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Min_max(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"min_max",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class LengthRange(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"lengthRange",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Items(aas.SubmodelElementCollection):

                        class Type(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"type",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Unit(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"unit",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Default(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"default",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#default"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Const(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Int,
                                id_short: Optional[str] = r"const",
                                value_type: aas.DataTypeDefXsd = xsd.Int,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#const"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Observable(aas.Property):

                            def __init__(
                                self,
                                value: bool,
                                id_short: Optional[str] = r"observable",
                                value_type: aas.DataTypeDefXsd = bool,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#isObservable"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Title(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"title",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#title"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Min_max(aas.Range):

                            def __init__(
                                self,
                                min: str,
                                max: str,
                                id_short: Optional[str] = r"min_max",
                                value_type: aas.DataTypeDefXsd = str,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                ),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
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
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    min=min,
                                    max=max,
                                    id_short=id_short,
                                    value_type=value_type,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class LengthRange(aas.Range):

                            def __init__(
                                self,
                                min: str,
                                max: str,
                                id_short: Optional[str] = r"lengthRange",
                                value_type: aas.DataTypeDefXsd = str,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                ),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
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
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    min=min,
                                    max=max,
                                    id_short=id_short,
                                    value_type=value_type,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class ValueSemantics(aas.ReferenceElement):

                            def __init__(
                                self,
                                value: aas.Reference,
                                id_short: Optional[str] = r"valueSemantics",
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

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
                            id_short: Optional[str] = r"items",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#items"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for array-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

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

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ItemsRange(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"itemsRange",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Properties(aas.SubmodelElementCollection):

                        class Property_name(aas.SubmodelElementCollection):

                            class Key(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"key",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Type(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"type",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Title(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"title",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/td#title"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Observable(aas.Property):

                                def __init__(
                                    self,
                                    value: bool,
                                    id_short: Optional[str] = r"observable",
                                    value_type: aas.DataTypeDefXsd = bool,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/td#isObservable"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Const(aas.Property):

                                def __init__(
                                    self,
                                    value: xsd.Int,
                                    id_short: Optional[str] = r"const",
                                    value_type: aas.DataTypeDefXsd = xsd.Int,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#const"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Default(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"default",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#default"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Unit(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"unit",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Min_max(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"min_max",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class LengthRange(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"lengthRange",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Items(aas.SubmodelElementCollection):

                                class Type(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"type",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class ValueSemantics(aas.ReferenceElement):

                                    def __init__(
                                        self,
                                        value: aas.Reference,
                                        id_short: Optional[str] = r"valueSemantics",
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Unit(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"unit",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://schema.org/unitCode"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Default(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"default",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#default"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Const(aas.Property):

                                    def __init__(
                                        self,
                                        value: xsd.Int,
                                        id_short: Optional[str] = r"const",
                                        value_type: aas.DataTypeDefXsd = xsd.Int,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#const"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Observable(aas.Property):

                                    def __init__(
                                        self,
                                        value: bool,
                                        id_short: Optional[str] = r"observable",
                                        value_type: aas.DataTypeDefXsd = bool,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/td#isObservable"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Title(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"title",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/td#title"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Min_max(aas.Range):

                                    def __init__(
                                        self,
                                        min: str,
                                        max: str,
                                        id_short: Optional[str] = r"min_max",
                                        value_type: aas.DataTypeDefXsd = str,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                        ),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = (
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
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            min=min,
                                            max=max,
                                            id_short=id_short,
                                            value_type=value_type,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class LengthRange(aas.Range):

                                    def __init__(
                                        self,
                                        min: str,
                                        max: str,
                                        id_short: Optional[str] = r"lengthRange",
                                        value_type: aas.DataTypeDefXsd = str,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                        ),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = (
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
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            min=min,
                                            max=max,
                                            id_short=id_short,
                                            value_type=value_type,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

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
                                    id_short: Optional[str] = r"items",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#items"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for array-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

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
                                        value=embedded_submodel_elements,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class ItemsRange(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"itemsRange",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Properties(aas.SubmodelElementCollection):

                                def __init__(
                                    self,
                                    id_short: Optional[str] = r"properties",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements()

                                    super().__init__(
                                        value=embedded_submodel_elements,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class ValueSemantics(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = r"valueSemantics",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

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
                                id_short: Optional[str] = r"property_name",
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Current counter value",
                                            r"de": r"Derzeitiger Zählerwert",
                                            r"it": r"Valore attuale del contatore",
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

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
                                    value=embedded_submodel_elements,
                                    id_short=id_short,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        def __init__(
                            self,
                            property_name: Optional[Iterable[Property_name]] = None,
                            id_short: Optional[str] = r"properties",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#properties"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for object-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(property_name, str):
                                raise TypeError("property_name takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(property_name)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ValueSemantics(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = r"valueSemantics",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Forms(aas.SubmodelElementCollection):

                        class Href(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"href",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/hypermedia#hasTarget"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class ContentType(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"contentType",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/hypermedia#forContentType"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Security(GeneratedSubmodelElementList):

                            class Security_item(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = None,
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            def __init__(
                                self,
                                security_items: Iterable[Union[aas.Reference, Security_item]],
                                id_short: Optional[str] = r"security",
                                type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                                semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                ),
                                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                                order_relevant: bool = True,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

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
                                    value=embedded_submodel_elements,
                                    id_short=id_short,
                                    type_value_list_element=type_value_list_element,
                                    semantic_id_list_element=semantic_id_list_element,
                                    value_type_list_element=value_type_list_element,
                                    order_relevant=order_relevant,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_function(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_function",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasFunction"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_entity(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_entity",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasEntity"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_zeroBasedAddressing(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_zeroBasedAddressing",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasZeroBasedAddressingFlag"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_pollingTime(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_pollingTime",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasPollingTime"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_timeout(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_timeout",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasTimeout"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_type(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_type",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasPayloadDataType"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_mostSignificantByte(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_mostSignificantByte",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasMostSignificantByte"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Modv_mostSignificantWord(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"modv_mostSignificantWord",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/modbus#hasMostSignificantWord"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for Modbus binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

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
                            id_short: Optional[str] = r"forms",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/td#hasForm"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

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

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

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
                        id_short: Optional[str] = r"property_name",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/AssetInterfaceDescription/1/0/PropertyDefinition"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (
                            global_ref(r"https://www.w3.org/2019/wot/td#name"),
                        ),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Current counter value",
                                    r"de": r"Derzeitiger Zählerwert",
                                    r"it": r"Valore attuale del contatore",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    property_name: Optional[Iterable[Property_name]] = None,
                    id_short: Optional[str] = r"properties",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#PropertyAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(property_name, str):
                        raise TypeError("property_name takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(property_name)

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Actions(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"actions",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#ActionAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Events(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"events",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#EventAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                properties: Optional[Properties] = None,
                actions: Optional[Actions] = None,
                events: Optional[Events] = None,
                id_short: Optional[str] = r"InteractionMetadata",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://www.w3.org/2019/wot/td#InteractionAffordance"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(properties, actions, events)

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ExternalDescriptor(aas.SubmodelElementCollection):

            class FileName(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"fileName",
                    content_type: Optional[str] = r"application/json",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        content_type=content_type,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                fileName: FileName,
                id_short: Optional[str] = r"ExternalDescriptor",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(fileName)

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            title: Union[str, Title],
            endpointMetadata: EndpointMetadata,
            interactionMetadata: InteractionMetadata,
            created: Optional[Union[xsd.DateTime, Created]] = None,
            modified: Optional[Union[xsd.DateTime, Modified]] = None,
            support: Optional[Union[xsd.AnyURI, Support]] = None,
            externalDescriptor: Optional[ExternalDescriptor] = None,
            id_short: Optional[str] = r"InterfaceTemplateForMODBUS",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"http://www.w3.org/2011/modbus"),
                global_ref(r"https://www.w3.org/2019/wot/td"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

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

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class InterfaceTemplateForMQTT(aas.SubmodelElementCollection):

        class Title(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"title",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#title"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Created(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"created",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"http://purl.org/dc/terms/created"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Modified(aas.Property):

            def __init__(
                self,
                value: xsd.DateTime,
                id_short: Optional[str] = r"modified",
                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"http://purl.org/dc/terms/modified"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class Support(aas.Property):

            def __init__(
                self,
                value: xsd.AnyURI,
                id_short: Optional[str] = r"support",
                value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#support"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class EndpointMetadata(aas.SubmodelElementCollection):

            class Base(aas.Property):

                def __init__(
                    self,
                    value: xsd.AnyURI,
                    id_short: Optional[str] = r"base",
                    value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#base"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ContentType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"contentType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/hypermedia#forContentType"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Security(GeneratedSubmodelElementList):

                class Security_item(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = None,
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    security_items: Iterable[Union[aas.Reference, Security_item]],
                    id_short: Optional[str] = r"security",
                    type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                    semantic_id_list_element: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                    ),
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SecurityDefinitions(aas.SubmodelElementCollection):

                class Nosec_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        id_short: Optional[str] = r"nosec_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#NoSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme)

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Auto_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"auto_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#AutoSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if scheme is not None and not isinstance(scheme, aas.SubmodelElement):
                            scheme = self.Scheme(scheme)

                        # Build a submodel element if a raw value was passed in the argument

                        if proxy is not None and not isinstance(proxy, aas.SubmodelElement):
                            proxy = self.Proxy(proxy)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(scheme, proxy)

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Basic_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"basic_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#BasicSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Combo_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class OneOf(GeneratedSubmodelElementList):

                        def __init__(
                            self,
                            oneof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            id_short: Optional[str] = r"oneOf",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#oneOf"
                            ),
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#oneOf"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(oneof_items, str):
                                raise TypeError("oneof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(oneof_items, number_repeated=False)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                type_value_list_element=type_value_list_element,
                                semantic_id_list_element=semantic_id_list_element,
                                value_type_list_element=value_type_list_element,
                                order_relevant=order_relevant,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class AllOf(GeneratedSubmodelElementList):

                        def __init__(
                            self,
                            allof_items: Optional[Iterable[aas.SubmodelElement]] = None,
                            id_short: Optional[str] = r"allOf",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#allOf"
                            ),
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#allOf"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(allof_items, str):
                                raise TypeError("allof_items takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(allof_items, number_repeated=False)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                type_value_list_element=type_value_list_element,
                                semantic_id_list_element=semantic_id_list_element,
                                value_type_list_element=value_type_list_element,
                                order_relevant=order_relevant,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        oneOf: Union[Iterable[aas.SubmodelElement], OneOf],
                        allOf: Union[Iterable[aas.SubmodelElement], AllOf],
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"combo_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#ComboSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Apikey_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"apikey_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#APIKeySecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Psk_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Identity(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"identity",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#identity"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        identity: Optional[Union[str, Identity]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"psk_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#PSKSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Digest_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Qop(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"qop",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#qop"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        qop: Optional[Union[str, Qop]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"digest_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#DigestSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Bearer_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#name"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class In(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"in",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#in"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Authorization(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"authorization",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#authorization"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Alg(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"alg",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#alg"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Format(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"format",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#format"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        name: Optional[Union[str, Name]] = None,
                        in_: Optional[Union[str, In]] = None,
                        authorization: Optional[Union[str, Authorization]] = None,
                        alg: Optional[Union[str, Alg]] = None,
                        format: Optional[Union[str, Format]] = None,
                        proxy: Optional[Union[str, Proxy]] = None,
                        id_short: Optional[str] = r"bearer_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#BearerSecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class Oauth2_sc(aas.SubmodelElementCollection):

                    class Scheme(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scheme",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#SecurityScheme"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Token(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"token",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#token"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Refresh(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"refresh",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#refresh"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Authorization(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"authorization",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#authorization"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Scopes(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"scopes",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#scopes"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Flow(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"flow",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#flow"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Proxy(aas.Property):

                        def __init__(
                            self,
                            value: xsd.AnyURI,
                            id_short: Optional[str] = r"proxy",
                            value_type: aas.DataTypeDefXsd = xsd.AnyURI,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/security#proxy"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        scheme: Union[str, Scheme],
                        token: Optional[Union[xsd.AnyURI, Token]] = None,
                        refresh: Optional[Union[xsd.AnyURI, Refresh]] = None,
                        authorization: Optional[Union[xsd.AnyURI, Authorization]] = None,
                        scopes: Optional[Union[str, Scopes]] = None,
                        flow: Optional[Union[str, Flow]] = None,
                        proxy: Optional[Union[xsd.AnyURI, Proxy]] = None,
                        id_short: Optional[str] = r"oauth2_sc",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

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
                    id_short: Optional[str] = r"securityDefinitions",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#definesSecurityScheme"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        nosec_sc, auto_sc, basic_sc, combo_sc, apikey_sc, psk_sc, digest_sc, bearer_sc, oauth2_sc
                    )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                base: Union[xsd.AnyURI, Base],
                contentType: Union[str, ContentType],
                security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                securityDefinitions: SecurityDefinitions,
                id_short: Optional[str] = r"EndpointMetadata",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class InteractionMetadata(aas.SubmodelElementCollection):

            class Properties(aas.SubmodelElementCollection):

                class Property_name(aas.SubmodelElementCollection):

                    class Key(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"key",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/td#name"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Type(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"type",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Title(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"title",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"https://www.w3.org/2019/wot/td#title"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Observable(aas.Property):

                        def __init__(
                            self,
                            value: bool,
                            id_short: Optional[str] = r"observable",
                            value_type: aas.DataTypeDefXsd = bool,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/td#isObservable"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Const(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Int,
                            id_short: Optional[str] = r"const",
                            value_type: aas.DataTypeDefXsd = xsd.Int,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#const"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Default(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"default",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#default"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Unit(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"unit",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Min_max(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"min_max",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class LengthRange(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"lengthRange",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Items(aas.SubmodelElementCollection):

                        class Type(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"type",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Unit(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"unit",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Default(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"default",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#default"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Const(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Int,
                                id_short: Optional[str] = r"const",
                                value_type: aas.DataTypeDefXsd = xsd.Int,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#const"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Observable(aas.Property):

                            def __init__(
                                self,
                                value: bool,
                                id_short: Optional[str] = r"observable",
                                value_type: aas.DataTypeDefXsd = bool,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#isObservable"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Title(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"title",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#title"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Min_max(aas.Range):

                            def __init__(
                                self,
                                min: str,
                                max: str,
                                id_short: Optional[str] = r"min_max",
                                value_type: aas.DataTypeDefXsd = str,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                ),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
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
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    min=min,
                                    max=max,
                                    id_short=id_short,
                                    value_type=value_type,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class LengthRange(aas.Range):

                            def __init__(
                                self,
                                min: str,
                                max: str,
                                id_short: Optional[str] = r"lengthRange",
                                value_type: aas.DataTypeDefXsd = str,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                    global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                ),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
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
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    min=min,
                                    max=max,
                                    id_short=id_short,
                                    value_type=value_type,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class ValueSemantics(aas.ReferenceElement):

                            def __init__(
                                self,
                                value: aas.Reference,
                                id_short: Optional[str] = r"valueSemantics",
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

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
                            id_short: Optional[str] = r"items",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#items"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for array-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

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

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ItemsRange(aas.Range):

                        def __init__(
                            self,
                            min: str,
                            max: str,
                            id_short: Optional[str] = r"itemsRange",
                            value_type: aas.DataTypeDefXsd = str,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                            ),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
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
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                min=min,
                                max=max,
                                id_short=id_short,
                                value_type=value_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Properties(aas.SubmodelElementCollection):

                        class Property_name(aas.SubmodelElementCollection):

                            class Key(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"key",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Type(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"type",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Title(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"title",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/td#title"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Observable(aas.Property):

                                def __init__(
                                    self,
                                    value: bool,
                                    id_short: Optional[str] = r"observable",
                                    value_type: aas.DataTypeDefXsd = bool,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/td#isObservable"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Const(aas.Property):

                                def __init__(
                                    self,
                                    value: xsd.Int,
                                    id_short: Optional[str] = r"const",
                                    value_type: aas.DataTypeDefXsd = xsd.Int,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#const"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Default(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"default",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#default"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Unit(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"unit",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(r"https://schema.org/unitCode"),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        value_type=value_type,
                                        value_id=value_id,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Min_max(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"min_max",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class LengthRange(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"lengthRange",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Items(aas.SubmodelElementCollection):

                                class Type(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"type",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class ValueSemantics(aas.ReferenceElement):

                                    def __init__(
                                        self,
                                        value: aas.Reference,
                                        id_short: Optional[str] = r"valueSemantics",
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Unit(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"unit",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://schema.org/unitCode"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Default(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"default",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#default"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Const(aas.Property):

                                    def __init__(
                                        self,
                                        value: xsd.Int,
                                        id_short: Optional[str] = r"const",
                                        value_type: aas.DataTypeDefXsd = xsd.Int,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/json-schema#const"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Observable(aas.Property):

                                    def __init__(
                                        self,
                                        value: bool,
                                        id_short: Optional[str] = r"observable",
                                        value_type: aas.DataTypeDefXsd = bool,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/td#isObservable"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Title(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"title",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://www.w3.org/2019/wot/td#title"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            value=value,
                                            id_short=id_short,
                                            value_type=value_type,
                                            value_id=value_id,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class Min_max(aas.Range):

                                    def __init__(
                                        self,
                                        min: str,
                                        max: str,
                                        id_short: Optional[str] = r"min_max",
                                        value_type: aas.DataTypeDefXsd = str,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minimum"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maximum"),
                                        ),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = (
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
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            min=min,
                                            max=max,
                                            id_short=id_short,
                                            value_type=value_type,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

                                class LengthRange(aas.Range):

                                    def __init__(
                                        self,
                                        min: str,
                                        max: str,
                                        id_short: Optional[str] = r"lengthRange",
                                        value_type: aas.DataTypeDefXsd = str,
                                        display_name: Optional[aas.MultiLanguageNameType] = None,
                                        category: Optional[str] = None,
                                        description: Optional[aas.MultiLanguageTextType] = None,
                                        semantic_id: Optional[aas.Reference] = global_ref(
                                            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange"
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[aas.Reference] = (
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#minLength"),
                                            global_ref(r"https://www.w3.org/2019/wot/json-schema#maxLength"),
                                        ),
                                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = (
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
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        super().__init__(
                                            min=min,
                                            max=max,
                                            id_short=id_short,
                                            value_type=value_type,
                                            display_name=display_name,
                                            category=category,
                                            description=description,
                                            semantic_id=semantic_id,
                                            qualifier=qualifier,
                                            extension=extension,
                                            supplemental_semantic_id=supplemental_semantic_id,
                                            embedded_data_specifications=embedded_data_specifications,
                                        )

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
                                    id_short: Optional[str] = r"items",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#items"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"Constraint",
                                                value_type=str,
                                                value=r"Only applicable for array-based values",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

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
                                        value=embedded_submodel_elements,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class ItemsRange(aas.Range):

                                def __init__(
                                    self,
                                    min: str,
                                    max: str,
                                    id_short: Optional[str] = r"itemsRange",
                                    value_type: aas.DataTypeDefXsd = str,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#minItems"),
                                        global_ref(r"https://www.w3.org/2019/wot/json-schema#maxItems"),
                                    ),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        min=min,
                                        max=max,
                                        id_short=id_short,
                                        value_type=value_type,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class Properties(aas.SubmodelElementCollection):

                                def __init__(
                                    self,
                                    id_short: Optional[str] = r"properties",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
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
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements()

                                    super().__init__(
                                        value=embedded_submodel_elements,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class ValueSemantics(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = r"valueSemantics",
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = global_ref(
                                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

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
                                id_short: Optional[str] = r"property_name",
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/json-schema#propertyName"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Current counter value",
                                            r"de": r"Derzeitiger Zählerwert",
                                            r"it": r"Valore attuale del contatore",
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

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
                                    value=embedded_submodel_elements,
                                    id_short=id_short,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        def __init__(
                            self,
                            property_name: Optional[Iterable[Property_name]] = None,
                            id_short: Optional[str] = r"properties",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/json-schema#properties"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"Constraint",
                                        value_type=str,
                                        value=r"Only applicable for object-based values",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(property_name, str):
                                raise TypeError("property_name takes several elements, got a str")

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(property_name)

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class ValueSemantics(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = r"valueSemantics",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class Forms(aas.SubmodelElementCollection):

                        class Href(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"href",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/hypermedia#hasTarget"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class ContentType(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"contentType",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/hypermedia#forContentType"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Security(GeneratedSubmodelElementList):

                            class Security_item(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = None,
                                    display_name: Optional[aas.MultiLanguageNameType] = None,
                                    category: Optional[str] = None,
                                    description: Optional[aas.MultiLanguageTextType] = None,
                                    semantic_id: Optional[aas.Reference] = None,
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    super().__init__(
                                        value=value,
                                        id_short=id_short,
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            def __init__(
                                self,
                                security_items: Iterable[Union[aas.Reference, Security_item]],
                                id_short: Optional[str] = r"security",
                                type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                                semantic_id_list_element: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                ),
                                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                                order_relevant: bool = True,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

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
                                    value=embedded_submodel_elements,
                                    id_short=id_short,
                                    type_value_list_element=type_value_list_element,
                                    semantic_id_list_element=semantic_id_list_element,
                                    value_type_list_element=value_type_list_element,
                                    order_relevant=order_relevant,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Mqv_retain(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"mqv_retain",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/mqtt#hasRetainFlag"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for MQTT binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Mqv_controlPacket(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"mqv_controlPacket",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/mqtt#ControlPacket"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for MQTT binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        class Mqv_qos(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"mqv_qos",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://www.w3.org/2019/wot/mqtt#hasQoSFlag"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"Constraint",
                                            value_type=str,
                                            value=r"Only applicable for MQTT binding",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                super().__init__(
                                    value=value,
                                    id_short=id_short,
                                    value_type=value_type,
                                    value_id=value_id,
                                    display_name=display_name,
                                    category=category,
                                    description=description,
                                    semantic_id=semantic_id,
                                    qualifier=qualifier,
                                    extension=extension,
                                    supplemental_semantic_id=supplemental_semantic_id,
                                    embedded_data_specifications=embedded_data_specifications,
                                )

                        def __init__(
                            self,
                            href: Union[str, Href],
                            security: Union[Iterable[Union[aas.Reference, Security.Security_item]], Security],
                            contentType: Optional[Union[str, ContentType]] = None,
                            mqv_retain: Optional[Union[str, Mqv_retain]] = None,
                            mqv_controlPacket: Optional[Union[str, Mqv_controlPacket]] = None,
                            mqv_qos: Optional[Union[str, Mqv_qos]] = None,
                            id_short: Optional[str] = r"forms",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://www.w3.org/2019/wot/td#hasForm"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

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

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

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
                        id_short: Optional[str] = r"property_name",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/AssetInterfaceDescription/1/0/PropertyDefinition"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (
                            global_ref(r"https://www.w3.org/2019/wot/td#name"),
                        ),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Current counter value",
                                    r"de": r"Derzeitiger Zählerwert",
                                    r"it": r"Valore attuale del contatore",
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

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

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    property_name: Optional[Iterable[Property_name]] = None,
                    id_short: Optional[str] = r"properties",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#PropertyAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(property_name, str):
                        raise TypeError("property_name takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(property_name)

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Actions(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"actions",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#ActionAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Events(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"events",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://www.w3.org/2019/wot/td#EventAffordance"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                properties: Optional[Properties] = None,
                actions: Optional[Actions] = None,
                events: Optional[Events] = None,
                id_short: Optional[str] = r"InteractionMetadata",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://www.w3.org/2019/wot/td#InteractionAffordance"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(properties, actions, events)

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ExternalDescriptor(aas.SubmodelElementCollection):

            class FileName(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"fileName",
                    content_type: Optional[str] = r"application/json",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        content_type=content_type,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                fileName: FileName,
                id_short: Optional[str] = r"ExternalDescriptor",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(fileName)

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            title: Union[str, Title],
            endpointMetadata: EndpointMetadata,
            interactionMetadata: InteractionMetadata,
            created: Optional[Union[xsd.DateTime, Created]] = None,
            modified: Optional[Union[xsd.DateTime, Modified]] = None,
            support: Optional[Union[xsd.AnyURI, Support]] = None,
            externalDescriptor: Optional[ExternalDescriptor] = None,
            id_short: Optional[str] = r"InterfaceTemplateForMQTT",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"http://www.w3.org/2011/mqtt"),
                global_ref(r"https://www.w3.org/2019/wot/td"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

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

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    def __init__(
        self,
        id_: str,
        interfaceTemplateForHTTP: Optional[Iterable[InterfaceTemplateForHTTP]] = None,
        interfaceTemplateForMODBUS: Optional[Iterable[InterfaceTemplateForMODBUS]] = None,
        interfaceTemplateForMQTT: Optional[Iterable[InterfaceTemplateForMQTT]] = None,
        id_short: Optional[str] = r"AssetInterfacesDescription",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = global_ref(
            r"https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Submodel"
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(dict_={r"en": r"AID Template Sample"})

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

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

        super().__init__(
            submodel_element=embedded_submodel_elements,
            id_=id_,
            id_short=id_short,
            display_name=display_name,
            category=category,
            description=description,
            administration=administration,
            semantic_id=semantic_id,
            qualifier=qualifier,
            kind=kind,
            extension=extension,
            supplemental_semantic_id=supplemental_semantic_id,
            embedded_data_specifications=embedded_data_specifications,
        )
