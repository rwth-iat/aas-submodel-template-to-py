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


class ControlComponentInstance(aas.Submodel):

    class Endpoints(aas.SubmodelElementCollection):

        class Endpoint(aas.SubmodelElementCollection):

            class InterfaceReference(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"InterfaceReference",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A reference to an interface description (SMC Interface) in a Control Component Type submodel that specifies the semantics of the interface."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/InterfaceReference/2/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EndpointReference(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"EndpointReference",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A reference to a technical control endpoint that adheres to the semantics of the referenced interface."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/Reference/2/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Endpoint",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"A control endpoint supported by the instance of the component."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/2/0"),
                }

            def __init__(
                self,
                interfaceReference: Union[aas.Reference, InterfaceReference],
                endpointReference: Union[aas.Reference, EndpointReference],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if interfaceReference is not None and not isinstance(interfaceReference, aas.SubmodelElement):
                    interfaceReference = self.InterfaceReference(interfaceReference)

                # Build a submodel element if a raw value was passed in the argument

                if endpointReference is not None and not isinstance(endpointReference, aas.SubmodelElement):
                    endpointReference = self.EndpointReference(endpointReference)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(interfaceReference, endpointReference)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Endpoints",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Collection of references to control endpoints supported by the instance of the component"
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Instance/Endpoints/2/0"),
            }

        def __init__(
            self, endpoint: Optional[Iterable[Endpoint]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(endpoint, str):
                raise TypeError("endpoint takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(endpoint)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Skills(aas.SubmodelElementCollection):

        class Skill(aas.SubmodelElementCollection):

            class Disabled(aas.Property):

                ALLOWED_VALUES = (True, False)

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Disabled",
                        "value_type": bool,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Boolean property that defines if the skill is (currently) disabled, e.g. not licensed, tested, suitable."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skill/Disabled/2/0"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Modes(aas.SubmodelElementCollection):

                class Mode(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Mode",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name of the operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skill/Mode/2/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Modes",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Collection of operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skill/Modes/2/0"),
                    }

                def __init__(
                    self, mode: Iterable[Union[str, Mode]], **kwargs: Unpack[SubmodelElementCollectionMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(mode, str):
                        raise TypeError("mode takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if mode:
                        mode = [i if isinstance(i, aas.SubmodelElement) else self.Mode(i) for i in mode]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(mode)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Parameters(aas.SubmodelElementCollection):

                class Parameter(aas.SubmodelElementCollection):

                    class Direction(aas.Property):

                        ALLOWED_VALUES = (r"In", r"Out", r"InOut")

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Direction",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Indicates whether the parameter is an input (In) or an output (Out) of the skill. An InOut parameter can be set from outside and can also be changed from skill itself. "
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Direction/2/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            if value is not None and value not in self.ALLOWED_VALUES:
                                raise ValueError(
                                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                                )

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Type(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Type",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Data type as string used to interpret the parameter. "}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Type/2/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Values(aas.SubmodelElementCollection):

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"Values",
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Collection of properties of the accepted values that the parameter may take."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Values/2/0"
                                ),
                            }

                        def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements()

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Parameter",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Parameter used for the configuration of the skill."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlComponent/Skill/Parameter/2/0"
                            ),
                        }

                    def __init__(
                        self,
                        direction: Union[str, Direction],
                        type: Union[str, Type],
                        values: Values,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if direction is not None and not isinstance(direction, aas.SubmodelElement):
                            direction = self.Direction(direction)

                        # Build a submodel element if a raw value was passed in the argument

                        if type is not None and not isinstance(type, aas.SubmodelElement):
                            type = self.Type(type)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(direction, type, values)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Parameters",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection of parameters used for the configuration of the skill."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skill/Parameters/2/0"),
                    }

                def __init__(
                    self,
                    parameter: Optional[Iterable[Parameter]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(parameter, str):
                        raise TypeError("parameter takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(parameter)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Errors(aas.SubmodelElementCollection):

                class ErrorReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ErrorReference",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlComponent/Skill/ErrorReference/2/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Errors",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Collection of references to the error codes of the component that may be raised by this skill."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skill/Errors/2/0"),
                    }

                def __init__(
                    self,
                    errorReference: Optional[Iterable[Union[aas.Reference, ErrorReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

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

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Uses(aas.SubmodelElementCollection):

                class SkillReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"SkillReference",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlComponent/Skill/SkillReference/2/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Uses",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection of references to other skills, that this skill uses."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skill/Uses/2/0"),
                    }

                def __init__(
                    self,
                    skillReference: Optional[Iterable[Union[aas.Reference, SkillReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

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

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Skill",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Contains the basic information to call (request the execution of) a skill, e.g. its signature"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skill/2/0"),
                }

            def __init__(
                self,
                disabled: Union[bool, Disabled],
                modes: Modes,
                parameters: Parameters,
                errors: Errors,
                uses: Uses,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if disabled is not None and not isinstance(disabled, aas.SubmodelElement):
                    disabled = self.Disabled(disabled)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(disabled, modes, parameters, errors, uses)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Skills",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of skills offered by the component instance"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Skills/2/0"),
            }

        def __init__(
            self, skill: Optional[Iterable[Skill]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
        ):

            # A str would be split into its characters
            if isinstance(skill, str):
                raise TypeError("skill takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(skill)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Type(aas.ReferenceElement):

        @staticmethod
        def template_defaults() -> ReferenceElementMetadata:
            return {
                "id_short": r"Type",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference between the component instance and its respective ControlComponentType Submodel."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlComponent/Instance/Type/2/0"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ControlComponentInstance",
            "description": aas.MultiLanguageTextType(dict_={r"en": r"A ControlComponentInstance Submodel."}),
            "administration": aas.AdministrativeInformation(
                version=r"2",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/02016-2-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/ControlComponent/Instance/2/0"
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        endpoints: Endpoints,
        skills: Skills,
        type: Union[aas.Reference, Type],
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if type is not None and not isinstance(type, aas.SubmodelElement):
            type = self.Type(type)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(endpoints, skills, type)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
