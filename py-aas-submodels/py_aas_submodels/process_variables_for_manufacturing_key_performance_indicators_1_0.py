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


class ProcessVariablesForManufacturingKPICalculation(aas.Submodel):

    class ActualPersonnelWorkTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual personnel work time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualPersonnelWorkTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualPersonnelWorkTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Personnel Work Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual personnel work time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualUnitProcessingTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual unit processing time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualUnitProcessingTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitProcessingTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Unit Processing Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual unit processing time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualUnitBusyTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual unit busy time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualUnitBusyTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitBusyTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Unit Busy Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual unit busy time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualOrderExecutionTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual order execution time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualOrderExecutionTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualOrderExecutionTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Order Execution Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual order execution time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualPersonnelAttendanceTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual personnel attendance time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualPersonnelAttendanceTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualPersonnelAttendanceTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Personnel Attendance Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual personnel attendance time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualProductionTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual production time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualProductionTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualProductionTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Production Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual production time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualQueuingTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual queuing time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualQueuingTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualQueuingTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Queuing Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual queuing time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualUnitDownTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual unit down time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualUnitDownTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitDownTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Unit Down Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual unit down time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualUnitDelayTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual unit delay time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualUnitDelayTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitDelayTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Unit Delay Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual unit delay time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualUnitSetupTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual unit setup time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualUnitSetupTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualSetupTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Unit Setup Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual unit setup time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ActualTransportTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for actual transport time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ActualTransportTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ActualTransportTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Actual Transport Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for actual transport time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class GoodPart(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Decimal,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Decimal,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"Provides optional comments for good part."})

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Decimal, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"GoodPart",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"http://www.w3id.org/hsu-aut/ISO22400-2#GoodPart"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Good Part"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Groups the data points for good part, including key, current value, and comment."}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if key is not None and not isinstance(key, aas.SubmodelElement):
                key = self.Key(key)

            # Build a submodel element if a raw value was passed in the argument

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class InspectedPart(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Decimal,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Decimal,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for inspected part."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Decimal, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"InspectedPart",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"http://www.w3id.org/hsu-aut/ISO22400-2#InspectedPart"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Inspected Part"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for inspected part, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ScrapQuantity(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Decimal,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Decimal,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for scrap quantity."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Decimal, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ScrapQuantity",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"http://www.w3id.org/hsu-aut/ISO22400-2#ScrapQuantity"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Scrap Quantity"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for scrap quantity, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class GoodQuantity(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Decimal,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Decimal,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for good quantity."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Decimal, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"GoodQuantity",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"http://www.w3id.org/hsu-aut/ISO22400-2#GoodQuantity"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Good Quantity"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for good quantity, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ReworkQuantity(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Decimal,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Decimal,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for rework quantity."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Decimal, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ReworkQuantity",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"http://www.w3id.org/hsu-aut/ISO22400-2#ReworkQuantity"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Rework Quantity"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for rework quantity, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class ProducedQuantity(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Decimal,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Decimal,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for produced quantity."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Decimal, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"ProducedQuantity",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#ProducedQuantity"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Produced Quantity"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for produced quantity, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class PlannedBusyTime(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for planned busy time."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"PlannedBusyTime",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#PlannedBusyTime"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Planned Busy Time"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for planned busy time, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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

    class PlannedRuntimePerItem(aas.SubmodelElementCollection):

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
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/key/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Key"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"de": r"Bezeichner aus ISO 22400-2:2014.", r"en": r"Identifier from ISO 22400-2:2014."}
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

        class CurrentValue(aas.Property):

            def __init__(
                self,
                value: xsd.Duration,
                id_short: Optional[str] = r"currentValue",
                value_type: aas.DataTypeDefXsd = xsd.Duration,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/currentValue/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Current Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"de": r"Aktueller Wert der Prozessvariable.",
                            r"en": r"Current value of process variable.",
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

        class Comment(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"comment",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalculation/comment/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Comment"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides optional comments for planned runtime per item."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
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
            key: Union[str, Key],
            currentValue: Union[xsd.Duration, CurrentValue],
            comment: Union[aas.LangStringSet, Comment],
            id_short: Optional[str] = r"PlannedRuntimePerItem",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"http://www.w3id.org/hsu-aut/ISO22400-2#PlannedRuntimePerUnit"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Planned Runtime Per Item"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Groups the data points for planned runtime per item, including key, current value, and comment."
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

            if currentValue is not None and not isinstance(currentValue, aas.SubmodelElement):
                currentValue = self.CurrentValue(currentValue)

            # Build a submodel element if a raw value was passed in the argument

            if comment is not None and not isinstance(comment, aas.SubmodelElement):
                comment = self.Comment(comment)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(key, currentValue, comment)

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
        actualPersonnelWorkTime: Optional[ActualPersonnelWorkTime] = None,
        actualUnitProcessingTime: Optional[ActualUnitProcessingTime] = None,
        actualUnitBusyTime: Optional[ActualUnitBusyTime] = None,
        actualOrderExecutionTime: Optional[ActualOrderExecutionTime] = None,
        actualPersonnelAttendanceTime: Optional[ActualPersonnelAttendanceTime] = None,
        actualProductionTime: Optional[ActualProductionTime] = None,
        actualQueuingTime: Optional[ActualQueuingTime] = None,
        actualUnitDownTime: Optional[ActualUnitDownTime] = None,
        actualUnitDelayTime: Optional[ActualUnitDelayTime] = None,
        actualUnitSetupTime: Optional[ActualUnitSetupTime] = None,
        actualTransportTime: Optional[ActualTransportTime] = None,
        goodPart: Optional[GoodPart] = None,
        inspectedPart: Optional[InspectedPart] = None,
        scrapQuantity: Optional[ScrapQuantity] = None,
        goodQuantity: Optional[GoodQuantity] = None,
        reworkQuantity: Optional[ReworkQuantity] = None,
        producedQuantity: Optional[ProducedQuantity] = None,
        plannedBusyTime: Optional[PlannedBusyTime] = None,
        plannedRuntimePerItem: Optional[PlannedRuntimePerItem] = None,
        id_short: Optional[str] = r"ProcessVariablesForManufacturingKPICalculation",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/ProcessVariablesForManufacturingKPICalculation/1/0",
                ),
            ),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if display_name is None:
            display_name = aas.MultiLanguageNameType(
                dict_={r"en": r"Process Variables For Manufacturing KPI Calculation"}
            )

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Defines the template submodel for process variables used in manufacturing KPI calculation."
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            actualPersonnelWorkTime,
            actualUnitProcessingTime,
            actualUnitBusyTime,
            actualOrderExecutionTime,
            actualPersonnelAttendanceTime,
            actualProductionTime,
            actualQueuingTime,
            actualUnitDownTime,
            actualUnitDelayTime,
            actualUnitSetupTime,
            actualTransportTime,
            goodPart,
            inspectedPart,
            scrapQuantity,
            goodQuantity,
            reworkQuantity,
            producedQuantity,
            plannedBusyTime,
            plannedRuntimePerItem,
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
