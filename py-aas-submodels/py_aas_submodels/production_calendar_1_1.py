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


class ProductionCalendar(aas.Submodel):

    class Calendar(aas.File):

        @staticmethod
        def template_defaults() -> FileMetadata:
            return {
                "id_short": r"calendar",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Contains the iCalendar file with mimeType text/calendar. The format should comply to the standard RFC 5545."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ProductionCalendar/calendar/1/0"),
            }

        def __init__(self, value: str, content_type: Optional[str] = r"text/calendar", **kwargs: Unpack[FileMetadata]):

            super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

    class InheritedFrom(aas.ReferenceElement):

        @staticmethod
        def template_defaults() -> ReferenceElementMetadata:
            return {
                "id_short": r"inheritedFrom",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Reference to a superordinate calendar from which this Submodel inherits."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ProductionCalendar/inheritedFrom/1/0"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class SpecificationExtensionVariables(GeneratedSubmodelElementList):

        class Specificationextensionvariables_item(aas.SubmodelElementCollection):

            class VariableName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"variableName",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Variable which is used to define time slots in a calendar that are breaks."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ProductionCalendar/variableName/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class VariableSpecification(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"variableSpecification",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Human readable description to specify the extension variable and its correct interpretation within an application."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ProductionCalendar/variableSpecification/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/plain", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Groups the specification details for every variable extension."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/ProductionCalendar/specificationExtensionVariables/1/0"
                    ),
                }

            def __init__(
                self,
                variableName: Union[str, VariableName],
                variableSpecification: VariableSpecification,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if variableName is not None and not isinstance(variableName, aas.SubmodelElement):
                    variableName = self.VariableName(variableName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(variableName, variableSpecification)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"specificationExtensionVariables",
                "type_value_list_element": aas.SubmodelElementCollection,
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"List of additional variables which extends the iCalendar file format."}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/ProductionCalendar/specificationExtensionVariables/1/0"
                ),
            }

        def __init__(
            self,
            specificationextensionvariables_items: Iterable[Specificationextensionvariables_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(specificationextensionvariables_items, str):
                raise TypeError("specificationextensionvariables_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                specificationextensionvariables_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ProductionCalendar",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel allows the storage of one production calendar for e.g. a machine, work station, department, production location etc."
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/ProductionCalendar/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        specificationExtensionVariables: Union[
            Iterable[SpecificationExtensionVariables.Specificationextensionvariables_item],
            SpecificationExtensionVariables,
        ],
        calendar: Optional[Calendar] = None,
        inheritedFrom: Optional[Union[aas.Reference, InheritedFrom]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if inheritedFrom is not None and not isinstance(inheritedFrom, aas.SubmodelElement):
            inheritedFrom = self.InheritedFrom(inheritedFrom)

        # A str would be split into its characters
        if isinstance(specificationExtensionVariables, str):
            raise TypeError("specificationExtensionVariables takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if specificationExtensionVariables is not None and not isinstance(
            specificationExtensionVariables, aas.SubmodelElement
        ):
            specificationExtensionVariables = self.SpecificationExtensionVariables(specificationExtensionVariables)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(calendar, inheritedFrom, specificationExtensionVariables)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
