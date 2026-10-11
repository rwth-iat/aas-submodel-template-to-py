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


class MeasurementValue(aas.Submodel):

    class MeasuredValue(aas.SubmodelElementCollection):

        class Value(aas.Property):

            def __init__(
                self,
                value: xsd.Float,
                id_short: Optional[str] = r"Value",
                value_type: aas.DataTypeDefXsd = xsd.Float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"VARIABLE",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/measurementvalue/value/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Value"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"The value of the of measured sensor output"}
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

        class Unit(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Unit",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62720#UBA000"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Unit"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"})

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

        class Kind(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Kind",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACI144"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (global_ref(r"0112/2///62683#ACI144"),),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Kind"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"})

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
            value_: Union[xsd.Float, Value],
            unit: Union[str, Unit],
            kind: Union[str, Kind],
            id_short: Optional[str] = r"MeasuredValue",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"This is the measured value of the sensor output"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                value_ = self.Value(value_)

            # Build a submodel element if a raw value was passed in the argument

            if unit is not None and not isinstance(unit, aas.SubmodelElement):
                unit = self.Unit(unit)

            # Build a submodel element if a raw value was passed in the argument

            if kind is not None and not isinstance(kind, aas.SubmodelElement):
                kind = self.Kind(kind)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

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

    class MeasuredValuePreDefined(aas.SubmodelElementCollection):

        class Distance(aas.Property):

            def __init__(
                self,
                value: xsd.Float,
                id_short: Optional[str] = r"Distance",
                value_type: aas.DataTypeDefXsd = xsd.Float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61987#ABN718#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Distance"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"The measured length between two points."})

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
            distance: Union[xsd.Float, Distance],
            id_short: Optional[str] = r"MeasuredValuePreDefined",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/measurementvalue/measuredvaluepredefined/1/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Measured Value Pre Defined"})

            if description is None:
                description = aas.MultiLanguageTextType(dict_={r"en": r"The predefined measured value of the sensor"})

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if distance is not None and not isinstance(distance, aas.SubmodelElement):
                distance = self.Distance(distance)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(distance)

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

    class MeasurementTimestamp(aas.Property):

        def __init__(
            self,
            value: xsd.DateTime,
            id_short: Optional[str] = r"MeasurementTimestamp",
            value_type: aas.DataTypeDefXsd = xsd.DateTime,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"VARIABLE",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61360_7#CBA007"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (global_ref(r"0112/2///61360_7#CBA008"),),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Measurement Timestamp"})

            if description is None:
                description = aas.MultiLanguageTextType(dict_={r"en": r"Date and time when the measurement was taken."})

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

    class Concept(aas.SubmodelElementCollection):

        class Origin(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Origin",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/measurementvalue/origin/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Origin"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"The origin of the semantic description"})

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

        class Version(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Version",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/measurementvalue/version/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Version"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"The version of the semantic defintion used"}
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

        class Identifier(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Identifier",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/measurementvalue/identifier/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Identifier"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"The identifier of the semantic definition used"}
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
            origin: Optional[Union[str, Origin]] = None,
            version: Optional[Union[str, Version]] = None,
            identifier: Optional[Union[str, Identifier]] = None,
            id_short: Optional[str] = r"Concept",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/measurementvalue/concept/1/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Concept"})

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"This collection defines which semantic definition is used for measuredvalue"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if origin is not None and not isinstance(origin, aas.SubmodelElement):
                origin = self.Origin(origin)

            # Build a submodel element if a raw value was passed in the argument

            if version is not None and not isinstance(version, aas.SubmodelElement):
                version = self.Version(version)

            # Build a submodel element if a raw value was passed in the argument

            if identifier is not None and not isinstance(identifier, aas.SubmodelElement):
                identifier = self.Identifier(identifier)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(origin, version, identifier)

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

    class MeasurementQualifier(aas.SubmodelElementCollection):

        class Quality(aas.Property):

            ALLOWED_VALUES = (r"good", r"bad", r"uncertain", r"others")

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Quality",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"VARIABLE",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61360_7#CBA006"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Quality"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Quality of the measured value (e.g., Good, Bad, Uncertain and others like out of range)."
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

        class Range(aas.Range):

            def __init__(
                self,
                min: xsd.Float,
                max: xsd.Float,
                id_short: Optional[str] = r"Range",
                value_type: aas.DataTypeDefXsd = xsd.Float,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/meaurementvalue/range/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Range"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Allowed minimum and maximum measurement limits."}
                    )

                if qualifier is None:
                    qualifier = ()

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

        class Scale(aas.Property):

            def __init__(
                self,
                value: int,
                id_short: Optional[str] = r"Scale",
                value_type: aas.DataTypeDefXsd = int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/measurementvalue/scale/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Scale"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Factor used to convert or adjust the measured value."}
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

        class Tag(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Tag",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61987#ABB271"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Tag"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Identifier linking the measurement to its source or device."}
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
            quality: Union[str, Quality],
            range: Optional[Union[Tuple[xsd.Float, xsd.Float], Range]] = None,
            scale: Optional[Union[int, Scale]] = None,
            tag: Optional[Union[str, Tag]] = None,
            id_short: Optional[str] = r"MeasurementQualifier",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/measurementvalue/measurementqualifier/1/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"Measurement Qualifier"})

            if description is None:
                description = aas.MultiLanguageTextType(dict_={r"en": r"The Qualifier of the measurement"})

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if quality is not None and not isinstance(quality, aas.SubmodelElement):
                quality = self.Quality(quality)

            # Build a submodel element if a raw value was passed in the argument

            if range is not None and not isinstance(range, aas.SubmodelElement):
                range = self.Range(min=range[0], max=range[1])

            # Build a submodel element if a raw value was passed in the argument

            if scale is not None and not isinstance(scale, aas.SubmodelElement):
                scale = self.Scale(scale)

            # Build a submodel element if a raw value was passed in the argument

            if tag is not None and not isinstance(tag, aas.SubmodelElement):
                tag = self.Tag(tag)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(quality, range, scale, tag)

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
        measuredValue: MeasuredValue,
        measurementTimestamp: Union[xsd.DateTime, MeasurementTimestamp],
        measurementQualifier: MeasurementQualifier,
        measuredValuePreDefined: Optional[MeasuredValuePreDefined] = None,
        concept: Optional[Concept] = None,
        id_short: Optional[str] = r"MeasurementValue",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = global_ref(
            r"https://admin-shell.io/idta/SubmodelTemplate/measurementValue/1/0"
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if display_name is None:
            display_name = aas.MultiLanguageNameType(dict_={r"en": r"Measurement Value"})

        if description is None:
            description = aas.MultiLanguageTextType(dict_={r"en": r"The Submodel Template for Measurement Value"})

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if measurementTimestamp is not None and not isinstance(measurementTimestamp, aas.SubmodelElement):
            measurementTimestamp = self.MeasurementTimestamp(measurementTimestamp)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            measuredValue, measuredValuePreDefined, measurementTimestamp, concept, measurementQualifier
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
