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


class MeasurementValue(aas.Submodel):

    class MeasuredValue(aas.SubmodelElementCollection):

        class Value(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Value",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                    "category": r"VARIABLE",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"The value of the of measured sensor output"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Unit(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Unit",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"}),
                    "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Kind(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Kind",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                    "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                    "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MeasuredValue",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"This is the measured value of the sensor output"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"),
            }

        def __init__(
            self,
            value_: Union[xsd.Float, Value],
            unit: Union[str, Unit],
            kind: Union[str, Kind],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

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

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MeasuredValuePreDefined(aas.SubmodelElementCollection):

        class Distance(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Distance",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Distance"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"The measured length between two points."}),
                    "semantic_id": global_ref(r"0112/2///61987#ABN718#001"),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MeasuredValuePreDefined",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value Pre Defined"}),
                "description": aas.MultiLanguageTextType(dict_={r"en": r"The predefined measured value of the sensor"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvaluepredefined/1/0"),
            }

        def __init__(self, distance: Union[xsd.Float, Distance], **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # Build a submodel element if a raw value was passed in the argument

            if distance is not None and not isinstance(distance, aas.SubmodelElement):
                distance = self.Distance(distance)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(distance)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MeasurementTimestamp(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"MeasurementTimestamp",
                "value_type": xsd.DateTime,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measurement Timestamp"}),
                "category": r"VARIABLE",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Date and time when the measurement was taken."}
                ),
                "semantic_id": global_ref(r"0112/2///61360_7#CBA007"),
                "supplemental_semantic_id": (global_ref(r"0112/2///61360_7#CBA008"),),
            }

        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Concept(aas.SubmodelElementCollection):

        class Origin(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Origin",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Origin"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"The origin of the semantic description"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/origin/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Version(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Version",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Version"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"The version of the semantic defintion used"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/version/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Identifier(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Identifier",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Identifier"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"The identifier of the semantic definition used"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/identifier/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Concept",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Concept"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"This collection defines which semantic definition is used for measuredvalue"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/concept/1/0"),
            }

        def __init__(
            self,
            origin: Optional[Union[str, Origin]] = None,
            version: Optional[Union[str, Version]] = None,
            identifier: Optional[Union[str, Identifier]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

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

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MeasurementQualifier(aas.SubmodelElementCollection):

        class Quality(aas.Property):

            ALLOWED_VALUES = (r"good", r"bad", r"uncertain", r"others")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Quality",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Quality"}),
                    "category": r"VARIABLE",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Quality of the measured value (e.g., Good, Bad, Uncertain and others like out of range)."
                        }
                    ),
                    "semantic_id": global_ref(r"0112/2///61360_7#CBA006"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Range(aas.Range):

            @staticmethod
            def template_defaults() -> RangeMetadata:
                return {
                    "id_short": r"Range",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Range"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Allowed minimum and maximum measurement limits."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/meaurementvalue/range/1/0"),
                }

            def __init__(self, min: xsd.Float, max: xsd.Float, **kwargs: Unpack[RangeMetadata]):

                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

        class Scale(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Scale",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Scale"}),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Factor used to convert or adjust the measured value."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/scale/1/0"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Tag(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Tag",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Tag"}),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Identifier linking the measurement to its source or device."}
                    ),
                    "semantic_id": global_ref(r"0112/2///61987#ABB271"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MeasurementQualifier",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measurement Qualifier"}),
                "description": aas.MultiLanguageTextType(dict_={r"en": r"The Qualifier of the measurement"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measurementqualifier/1/0"),
            }

        def __init__(
            self,
            quality: Union[str, Quality],
            range: Optional[Union[Tuple[xsd.Float, xsd.Float], Range]] = None,
            scale: Optional[Union[int, Scale]] = None,
            tag: Optional[Union[str, Tag]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

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

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"MeasurementValue",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measurement Value"}),
            "description": aas.MultiLanguageTextType(dict_={r"en": r"The Submodel Template for Measurement Value"}),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/SubmodelTemplate/measurementValue/1/0"),
        }

    def __init__(
        self,
        id_: str,
        measuredValue: MeasuredValue,
        measurementTimestamp: Union[xsd.DateTime, MeasurementTimestamp],
        measurementQualifier: MeasurementQualifier,
        measuredValuePreDefined: Optional[MeasuredValuePreDefined] = None,
        concept: Optional[Concept] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if measurementTimestamp is not None and not isinstance(measurementTimestamp, aas.SubmodelElement):
            measurementTimestamp = self.MeasurementTimestamp(measurementTimestamp)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            measuredValue, measuredValuePreDefined, measurementTimestamp, concept, measurementQualifier
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
