from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class ProductionCalendar(Submodel):

    class Calendar(File):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"calendar",
            content_type: str = r"text/calendar",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Contains the iCalendar file with mimeType text/calendar. The format should comply to the standard RFC 5545."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ProductionCalendar/calendar/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

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

    class InheritedFrom(ReferenceElement):

        def __init__(
            self,
            value: Reference,
            id_short: Optional[str] = r"inheritedFrom",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Reference to a superordinate calendar from which this Submodel inherits."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ProductionCalendar/inheritedFrom/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

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

    class SpecificationExtensionVariables(SubmodelElementList):

        class Specificationextensionvariables_item(SubmodelElementCollection):

            class VariableName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"variableName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Variable which is used to define time slots in a calendar that are breaks."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ProductionCalendar/variableName/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class VariableSpecification(File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"variableSpecification",
                    content_type: str = r"text/plain",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Human readable description to specify the extension variable and its correct interpretation within an application."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ProductionCalendar/variableSpecification/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

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
                variableName: Union[str, VariableName],
                variableSpecification: VariableSpecification,
                id_short: Optional[str] = r"specificationextensionvariables_item",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the specification details for every variable extension."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ProductionCalendar/specificationExtensionVariables/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if variableName and not isinstance(variableName, SubmodelElement):
                    variableName = self.VariableName(variableName)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [variableName, variableSpecification]:
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
            specificationextensionvariables_items: Iterable[
                Specificationextensionvariables_item
            ],
            id_short: Optional[str] = r"specificationExtensionVariables",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"List of additional variables which extends the iCalendar file format."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ProductionCalendar/specificationExtensionVariables/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [specificationextensionvariables_items]:
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

        def _check_constraints(self, new, existing) -> None:
            # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
            # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
            saved_id_short = new.id_short
            new.id_short = None

            # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
            if not isinstance(new, self.type_value_list_element):
                raise base.AASConstraintViolation(
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
                raise base.AASConstraintViolation(
                    107,
                    f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                    "is specified all first level children must have the same "
                    f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                )

            # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
            # is either Property or Range. Thus, `new` must have the value_type property.
            # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
            if (
                isinstance(self.type_value_list_element, Property)
                or isinstance(self.type_value_list_element, Range)
                and not isinstance(new.value_type, self.value_type_list_element)
            ):  # type: ignore
                raise base.AASConstraintViolation(
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise base.AASConstraintViolation(
                            114,
                            f"Element to be added {new!r} has semantic_id "
                            f"{new.semantic_id!r}, while already contained element "
                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                            "aren't equal.",
                        )

            # Re-assign id_short
            new.id_short = saved_id_short

    def __init__(
        self,
        id_: str,
        specificationExtensionVariables: SpecificationExtensionVariables,
        calendar: Optional[Calendar] = None,
        inheritedFrom: Optional[Union[Reference, InheritedFrom]] = None,
        id_short: Optional[str] = r"ProductionCalendar",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"The Submodel allows the storage of one production calendar for e.g. a machine, work station, department, production location etc."
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=None,
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(
                Key(
                    type_=KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/ProductionCalendar/1/0",
                ),
            ),
            type_=Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[Qualifier] = None,
        kind: ModellingKind = ModellingKind.TEMPLATE,
        extension: Iterable[Extension] = (),
        supplemental_semantic_id: Iterable[Reference] = (),
        embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
    ):

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument
        if inheritedFrom and not isinstance(inheritedFrom, SubmodelElement):
            inheritedFrom = self.InheritedFrom(inheritedFrom)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [calendar, inheritedFrom, specificationExtensionVariables]:
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
