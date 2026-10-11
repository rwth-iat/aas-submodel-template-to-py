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


class ControlComponentType(aas.Submodel):

    class Interfaces(aas.SubmodelElementCollection):

        class Interface(aas.SubmodelElementCollection):

            class InterfaceProfile(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InterfaceProfile",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Type/Interface/Profile/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"The profile according to which the referred control interface operates."}
                        )

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

            class InterfaceProfileSupplement(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InterfaceProfileSupplement",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Type/Interface/ProfileSupplement/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Supplemental information to further specify the interface."}
                        )

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

            class InterfaceReference(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"InterfaceReference",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Type/Interface/Reference/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A reference to a control interface supported by the component type and described by the interfaceProfile and the optional supplement"
                            }
                        )

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
                interfaceProfile: Union[str, InterfaceProfile],
                interfaceProfileSupplement: Optional[Union[str, InterfaceProfileSupplement]] = None,
                interfaceReference: Optional[Union[aas.Reference, InterfaceReference]] = None,
                id_short: Optional[str] = r"Interface",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ControlComponent/Type/Interface/2/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"An interface description"})

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if interfaceProfile is not None and not isinstance(interfaceProfile, aas.SubmodelElement):
                    interfaceProfile = self.InterfaceProfile(interfaceProfile)

                # Build a submodel element if a raw value was passed in the argument

                if interfaceProfileSupplement is not None and not isinstance(
                    interfaceProfileSupplement, aas.SubmodelElement
                ):
                    interfaceProfileSupplement = self.InterfaceProfileSupplement(interfaceProfileSupplement)

                # Build a submodel element if a raw value was passed in the argument

                if interfaceReference is not None and not isinstance(interfaceReference, aas.SubmodelElement):
                    interfaceReference = self.InterfaceReference(interfaceReference)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    interfaceProfile, interfaceProfileSupplement, interfaceReference
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
            interface: Optional[Iterable[Interface]] = None,
            id_short: Optional[str] = r"Interfaces",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/ControlComponent/Type/Interfaces/2/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Collection of references to control interfaces supported by the component type, e.g. to elements of the Interface Metadata SMC of the Asset Interface Description submodel, the MTP submodel or OPC UA Server Datasheet submodel."
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(interface, str):
                raise TypeError("interface takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(interface)

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

    class Errors(aas.SubmodelElementCollection):

        class Error(aas.SubmodelElementCollection):

            class ErrorCode(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ErrorCode",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Type/Error/Code/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"The error code."})

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
                errorCode: Union[str, ErrorCode],
                id_short: Optional[str] = r"Error",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ControlComponent/Type/Error/2/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"A container representing an error."})

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if errorCode is not None and not isinstance(errorCode, aas.SubmodelElement):
                    errorCode = self.ErrorCode(errorCode)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(errorCode)

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
            error: Optional[Iterable[Error]] = None,
            id_short: Optional[str] = r"Errors",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/ControlComponent/Type/Errors/2/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of all possible error codes that may appear in components of this type."}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(error, str):
                raise TypeError("error takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(error)

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

    class Skills(aas.SubmodelElementCollection):

        class Skill(aas.SubmodelElementCollection):

            class Disabled(aas.Property):

                ALLOWED_VALUES = (True, False)

                def __init__(
                    self,
                    value: bool,
                    id_short: Optional[str] = r"Disabled",
                    value_type: aas.DataTypeDefXsd = bool,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Skill/Disabled/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Boolean property that defines if the skill is (currently) disabled, e.g. not licensed, tested, suitable."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

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

            class Modes(aas.SubmodelElementCollection):

                class Mode(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Mode",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/ControlComponent/Skill/Mode/2/0"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name of the operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
                                }
                            )

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
                    mode: Iterable[Union[str, Mode]],
                    id_short: Optional[str] = r"Modes",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Skill/Modes/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Collection of operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(mode, str):
                        raise TypeError("mode takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if mode:
                        mode = [i if isinstance(i, aas.SubmodelElement) else self.Mode(i) for i in mode]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(mode)

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

            class Parameters(aas.SubmodelElementCollection):

                class Parameter(aas.SubmodelElementCollection):

                    class Direction(aas.Property):

                        ALLOWED_VALUES = (r"In", r"Out", r"InOut")

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Direction",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Direction/2/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Indicates whether the parameter is an input (In) or an output (Out) of the skill. An InOut parameter can be set from outside and can also be changed from skill itself. "
                                    }
                                )

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

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
                            id_short: Optional[str] = r"Type",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Type/2/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Data type as string used to interpret the parameter. "}
                                )

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

                    class Values(aas.SubmodelElementCollection):

                        def __init__(
                            self,
                            id_short: Optional[str] = r"Values",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Values/2/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Collection of properties of the accepted values that the parameter may take."
                                    }
                                )

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
                        direction: Union[str, Direction],
                        type: Union[str, Type],
                        values: Values,
                        id_short: Optional[str] = r"Parameter",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/2/0"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Parameter used for the configuration of the skill."}
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if direction is not None and not isinstance(direction, aas.SubmodelElement):
                            direction = self.Direction(direction)

                        # Build a submodel element if a raw value was passed in the argument

                        if type is not None and not isinstance(type, aas.SubmodelElement):
                            type = self.Type(type)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(direction, type, values)

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
                    parameter: Optional[Iterable[Parameter]] = None,
                    id_short: Optional[str] = r"Parameters",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Skill/Parameters/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection of parameters used for the configuration of the skill."}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(parameter, str):
                        raise TypeError("parameter takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(parameter)

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

            class Errors(aas.SubmodelElementCollection):

                class ErrorReference(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = r"ErrorReference",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/ControlComponent/Skill/ErrorReference/2/0"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"A reference to an SMC “Error” (Table 5) that that can be "}
                            )

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
                    errorReference: Optional[Iterable[Union[aas.Reference, ErrorReference]]] = None,
                    id_short: Optional[str] = r"Errors",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Skill/Errors/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Collection of references to the error codes of the component that may be raised by this skill."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(errorReference, str):
                        raise TypeError("errorReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if errorReference:
                        errorReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.ErrorReference(i) for i in errorReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(errorReference)

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

            class Uses(aas.SubmodelElementCollection):

                class SkillReference(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = r"SkillReference",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/ControlComponent/Skill/SkillReference/2/0"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"A reference to an SMC “Skill” (Table 7) of this or another "}
                            )

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
                    skillReference: Optional[Iterable[Union[aas.Reference, SkillReference]]] = None,
                    id_short: Optional[str] = r"Uses",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/ControlComponent/Skill/Uses/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection of references to other skills, that this skill uses."}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(skillReference, str):
                        raise TypeError("skillReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if skillReference:
                        skillReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.SkillReference(i) for i in skillReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(skillReference)

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
                disabled: Union[bool, Disabled],
                modes: Modes,
                parameters: Parameters,
                errors: Errors,
                uses: Uses,
                id_short: Optional[str] = r"Skill",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ControlComponent/Skill/2/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Contains the basic information to call (request the execution of) a skill, e.g. its signature"
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if disabled is not None and not isinstance(disabled, aas.SubmodelElement):
                    disabled = self.Disabled(disabled)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(disabled, modes, parameters, errors, uses)

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
            skill: Optional[Iterable[Skill]] = None,
            id_short: Optional[str] = r"Skills",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/ControlComponent/Skills/2/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of skills offered by the component type"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(skill, str):
                raise TypeError("skill takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(skill)

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
        interfaces: Interfaces,
        errors: Errors,
        skills: Skills,
        id_short: Optional[str] = r"ControlComponentType",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/ControlComponent/Type/2/0"),),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"2",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/IDTA02015-2-0",
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(interfaces, errors, skills)

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
