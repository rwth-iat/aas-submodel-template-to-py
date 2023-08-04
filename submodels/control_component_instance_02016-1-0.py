from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class ControlComponentInstance(Submodel):
    class Type(ReferenceElement):
        def __init__(
            self,
            value: Reference,
            id_short: str = "Type",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="https://admin-shell.io/idta/ControlComponent/Instance/Type/1/0",
                        id_type=KeyType.IRI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Reference between the component instance and its respective ControlComponentType Submodel."
                }

            if qualifier is None:
                qualifier = {
                    Qualifier(
                        type_="Multiplicity",
                        value_type=str,
                        value="One",
                        value_id=None,
                        semantic_id=None,
                    )
                }

            super().__init__(
                value=value,
                id_short=id_short,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class Endpoints(SubmodelElementCollectionUnordered):
        class Endpoint(ReferenceElement):
            def __init__(
                self,
                value: Reference,
                id_short: str = "Endpoint",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/1/0",
                            id_type=KeyType.IRI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {"en": "A reference to a control endpoint."}

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
                        ),
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="To be filled; normally same as idShort, might be with {00}",
                            value_id=None,
                            semantic_id=None,
                        ),
                    }

                super().__init__(
                    value=value,
                    id_short=id_short,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        def __init__(
            self,
            endpoint: Optional[Iterable[Union[Reference, Endpoint]]] = None,
            id_short: str = "Endpoints",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="https://admin-shell.io/idta/ControlComponent/Instance/Endpoints/1/0",
                        id_type=KeyType.IRI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Collection of references to control endpoints supported by the instance of the component."
                }

            if qualifier is None:
                qualifier = {
                    Qualifier(
                        type_="Multiplicity",
                        value_type=str,
                        value="One",
                        value_id=None,
                        semantic_id=None,
                    )
                }

            # Build a list of submodel elements if a raw values were passed in the argument
            if endpoint and all([isinstance(i, Reference) for i in endpoint]):
                endpoint = [self.Endpoint(i) for i in endpoint]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [endpoint]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class Skills(SubmodelElementCollectionUnordered):
        class Skill(SubmodelElementCollectionUnordered):
            class Name(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "Name",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/ControlComponent/Skill/Name/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Name used to select the skill via its interface."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class DisplayName(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "DisplayName",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/ControlComponent/Skill/DisplayName/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Name to display the skill, e.g. in an HMI or GUI."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class Disabled(Property):
                def __init__(
                    self,
                    value: bool,
                    id_short: str = "Disabled",
                    value_type: DataTypeDef = bool,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/ControlComponent/Skill/Disabled/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Boolean property that defines if the skill is (currently) disabled, e.g. not licensed, tested, suitable."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class Modes(SubmodelElementCollectionUnordered):
                class Mode(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "Mode",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/ControlComponent/Skill/Mode/1/0",
                                    id_type=KeyType.IRI,
                                ),
                            )
                        ),
                        qualifier: Optional[Set[Constraint]] = None,
                        kind: ModelingKind = ModelingKind.INSTANCE,
                    ):
                        if description is None:
                            description = {
                                "en": "Name of the operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
                            }

                        if qualifier is None:
                            qualifier = {
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="To be filled; normally same as idShort, might be with {00}",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="OneToMany",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                def __init__(
                    self,
                    mode: Iterable[Union[str, Mode]],
                    id_short: str = "Modes",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/ControlComponent/Skill/Modes/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Collection of operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    # Build a list of submodel elements if a raw values were passed in the argument
                    if mode and all([isinstance(i, str) for i in mode]):
                        mode = [self.Mode(i) for i in mode]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [mode]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class Parameters(SubmodelElementCollectionUnordered):
                class Parameter(SubmodelElementCollectionUnordered):
                    class Name(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "Name",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Name/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {"en": "Name of the parameter."}

                            if qualifier is None:
                                qualifier = {
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    )
                                }

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                kind=kind,
                            )

                    class Direction(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "Direction",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Direction/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Indicates whether the parameter is an input (In) or an output (Out) of the skill. An InOut parameter can be set from outside and can also be changed from skill itself. "
                                }

                            if qualifier is None:
                                qualifier = {
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    )
                                }

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                kind=kind,
                            )

                    class Type(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "Type",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Type/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Data type as string used to interpret the parameter. "
                                }

                            if qualifier is None:
                                qualifier = {
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    )
                                }

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                kind=kind,
                            )

                    class Values(SubmodelElementCollectionUnordered):
                        def __init__(
                            self,
                            id_short: str = "Values",
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Values/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Collection of properties of the accepted values that the parameter may take."
                                }

                            if qualifier is None:
                                qualifier = {
                                    Qualifier(
                                        type_="Multiplicity",
                                        value_type=str,
                                        value="One",
                                        value_id=None,
                                        semantic_id=None,
                                    )
                                }

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in []:
                                if se_arg is None:
                                    continue
                                elif isinstance(se_arg, SubmodelElement):
                                    embedded_submodel_elements.append(se_arg)
                                elif isinstance(se_arg, Iterable):
                                    for n, element in enumerate(se_arg):
                                        element.id_short = f"{element.id_short}{n}"
                                        embedded_submodel_elements.append(element)
                                else:
                                    raise TypeError(
                                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                                    )

                            super().__init__(
                                value=embedded_submodel_elements,
                                id_short=id_short,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                kind=kind,
                            )

                    def __init__(
                        self,
                        name: Union[str, Name],
                        direction: Union[str, Direction],
                        type: Union[str, Type],
                        values: Values,
                        id_short: str = "Parameter",
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/idta/ControlComponent/Skill/Parameter/1/0",
                                    id_type=KeyType.IRI,
                                ),
                            )
                        ),
                        qualifier: Optional[Set[Constraint]] = None,
                        kind: ModelingKind = ModelingKind.INSTANCE,
                    ):
                        if description is None:
                            description = {
                                "en": "Parameter used for the configuration of the skill."
                            }

                        if qualifier is None:
                            qualifier = {
                                Qualifier(
                                    type_="PresetIdShort",
                                    value_type=str,
                                    value="To be filled; normally same as idShort, might be with {00}",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                                Qualifier(
                                    type_="Multiplicity",
                                    value_type=str,
                                    value="ZeroToMany",
                                    value_id=None,
                                    semantic_id=None,
                                ),
                            }

                        # Build a submodel element if a raw value was passed in the argument
                        if name and not isinstance(name, SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument
                        if direction and not isinstance(direction, SubmodelElement):
                            direction = self.Direction(direction)

                        # Build a submodel element if a raw value was passed in the argument
                        if type and not isinstance(type, SubmodelElement):
                            type = self.Type(type)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [name, direction, type, values]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                                )

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                def __init__(
                    self,
                    parameter: Optional[Iterable[Parameter]] = None,
                    id_short: str = "Parameters",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/ControlComponent/Skill/Parameters/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Collection of parameters used for the configuration of the skill."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [parameter]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class Errors(SubmodelElementCollectionUnordered):
                def __init__(
                    self,
                    id_short: str = "Errors",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/ControlComponent/Skill/Errors/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Collection of references to the error codes of the component that may be triggered by this skill."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in []:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class Uses(SubmodelElementCollectionUnordered):
                def __init__(
                    self,
                    id_short: str = "Uses",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/idta/ControlComponent/Skill/Uses/1/0",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Collection of references to other skills, that this skill uses."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in []:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            def __init__(
                self,
                name: Union[str, Name],
                disabled: Union[bool, Disabled],
                modes: Modes,
                parameters: Parameters,
                errors: Errors,
                uses: Uses,
                displayName: Optional[Union[LangStringSet, DisplayName]] = None,
                id_short: str = "Skill",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/idta/ControlComponent/Skill/1/0",
                            id_type=KeyType.IRI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Contains the basic information to call (request the execution of) a skill, e.g. its signature"
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="PresetIdShort",
                            value_type=str,
                            value="To be filled; normally same as idShort, might be with {00}",
                            value_id=None,
                            semantic_id=None,
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if name and not isinstance(name, SubmodelElement):
                    name = self.Name(name)

                # Build a submodel element if a raw value was passed in the argument
                if displayName and not isinstance(displayName, SubmodelElement):
                    displayName = self.DisplayName(displayName)

                # Build a submodel element if a raw value was passed in the argument
                if disabled and not isinstance(disabled, SubmodelElement):
                    disabled = self.Disabled(disabled)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    name,
                    displayName,
                    disabled,
                    modes,
                    parameters,
                    errors,
                    uses,
                ]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                        )

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        def __init__(
            self,
            skill: Skill,
            id_short: str = "Skills",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="https://admin-shell.io/idta/ControlComponent/Skills/1/0",
                        id_type=KeyType.IRI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Collection of skills offered by the component type"
                }

            if qualifier is None:
                qualifier = {
                    Qualifier(
                        type_="Multiplicity",
                        value_type=str,
                        value="One",
                        value_id=None,
                        semantic_id=None,
                    )
                }

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [skill]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    def __init__(
        self,
        identification: Identifier,
        type: Union[Reference, Type],
        endpoints: Endpoints,
        skills: Skills,
        id_short: str = "ControlComponentInstance",
        category: Optional[str] = None,
        description: Optional[LangStringSet] = None,
        administration: Optional[AdministrativeInformation] = None,
        semantic_id: Optional[Reference] = Reference(
            key=(
                Key(
                    type_=KeyElements.CONCEPT_DESCRIPTION,
                    local=True,
                    value="https://admin-shell.io/idta/ControlComponent/Instance/1/0",
                    id_type=KeyType.IRI,
                ),
            )
        ),
        qualifier: Optional[Set[Constraint]] = None,
        kind: ModelingKind = ModelingKind.INSTANCE,
    ):
        if description is None:
            description = {"en": "A ControlComponentInstance Submodel."}

        if qualifier is None:
            qualifier = set()

        # Build a submodel element if a raw value was passed in the argument
        if type and not isinstance(type, SubmodelElement):
            type = self.Type(type)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [type, endpoints, skills]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
                )

        super().__init__(
            submodel_element=embedded_submodel_elements,
            identification=identification,
            id_short=id_short,
            category=category,
            description=description,
            administration=administration,
            semantic_id=semantic_id,
            qualifier=qualifier,
            kind=kind,
        )
