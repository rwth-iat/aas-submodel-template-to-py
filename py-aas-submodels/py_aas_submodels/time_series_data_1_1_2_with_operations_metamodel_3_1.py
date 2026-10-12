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


class BlobMetadata(TypedDict, total=False):
    """Metadata of aas.Blob, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


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


class MultiLanguagePropertyMetadata(TypedDict, total=False):
    """Metadata of aas.MultiLanguageProperty, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_id: Optional[aas.Reference]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class OperationMetadata(TypedDict, total=False):
    """Metadata of aas.Operation, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    input_variable: Iterable[aas.SubmodelElement]
    output_variable: Iterable[aas.SubmodelElement]
    in_output_variable: Iterable[aas.SubmodelElement]
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


class TimeSeries(aas.Submodel):

    class Metadata(aas.SubmodelElementCollection):

        class Name(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"Name",
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Metadata/Name/1/1"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Description(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"Description",
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Metadata/Description/1/1"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Record(aas.SubmodelElementCollection):

            class Time(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Time",
                        "value_type": xsd.Long,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SampleAccelerationX(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"sampleAccelerationX",
                        "value_type": xsd.Long,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://sample.com/AccelerationX/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SampleAccelerationY(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"sampleAccelerationY",
                        "value_type": xsd.Long,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://sample.com/AccelerationY/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SampleAccelerationZ(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"sampleAccelerationZ",
                        "value_type": xsd.Long,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://sample.com/AccelerationZ/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Record",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Record/1/1"),
                }

            def __init__(
                self,
                time: Iterable[Union[xsd.Long, Time]],
                sampleAccelerationX: Optional[Union[xsd.Long, SampleAccelerationX]] = None,
                sampleAccelerationY: Optional[Union[xsd.Long, SampleAccelerationY]] = None,
                sampleAccelerationZ: Optional[Union[xsd.Long, SampleAccelerationZ]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(time, str):
                    raise TypeError("time takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if time:
                    time = [i if isinstance(i, aas.SubmodelElement) else self.Time(i) for i in time]

                # Build a submodel element if a raw value was passed in the argument

                if sampleAccelerationX is not None and not isinstance(sampleAccelerationX, aas.SubmodelElement):
                    sampleAccelerationX = self.SampleAccelerationX(sampleAccelerationX)

                # Build a submodel element if a raw value was passed in the argument

                if sampleAccelerationY is not None and not isinstance(sampleAccelerationY, aas.SubmodelElement):
                    sampleAccelerationY = self.SampleAccelerationY(sampleAccelerationY)

                # Build a submodel element if a raw value was passed in the argument

                if sampleAccelerationZ is not None and not isinstance(sampleAccelerationZ, aas.SubmodelElement):
                    sampleAccelerationZ = self.SampleAccelerationZ(sampleAccelerationZ)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    time, sampleAccelerationX, sampleAccelerationY, sampleAccelerationZ
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Metadata",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Metadata/1/1"),
            }

        def __init__(
            self,
            name: Union[aas.MultiLanguageTextType, Name],
            record: Record,
            description_: Optional[Union[aas.MultiLanguageTextType, Description]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if name is not None and not isinstance(name, aas.SubmodelElement):
                name = self.Name(name)

            # Build a submodel element if a raw value was passed in the argument

            if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                description_ = self.Description(description_)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(name, description_, record)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Segments(aas.SubmodelElementCollection):

        class ExternalSegment(aas.SubmodelElementCollection):

            class Name(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Name",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RecordCount(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RecordCount",
                        "value_type": xsd.Long,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StartTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StartTime",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EndTime",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Duration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Duration",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SamplingInterval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SamplingInterval",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SamplingRate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SamplingRate",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class State(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"State",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/State/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LastUpdate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LastUpdate",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class File(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"File",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/File/1/1"),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class Blob(aas.Blob):

                @staticmethod
                def template_defaults() -> BlobMetadata:
                    return {
                        "id_short": r"Blob",
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Blob/1/1"),
                    }

                def __init__(
                    self,
                    value: Optional[bytes] = None,
                    content_type: Optional[str] = r"application/json",
                    **kwargs: Unpack[BlobMetadata],
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ExternalSegment",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segments/ExternalSegment/1/1"),
                }

            def __init__(
                self,
                name: Optional[Union[aas.MultiLanguageTextType, Name]] = None,
                description_: Optional[Union[aas.MultiLanguageTextType, Description]] = None,
                recordCount: Optional[Union[xsd.Long, RecordCount]] = None,
                startTime: Optional[Union[str, StartTime]] = None,
                endTime: Optional[Union[str, EndTime]] = None,
                duration: Optional[Union[str, Duration]] = None,
                samplingInterval: Optional[Union[xsd.Long, SamplingInterval]] = None,
                samplingRate: Optional[Union[xsd.Long, SamplingRate]] = None,
                state: Optional[Union[str, State]] = None,
                lastUpdate: Optional[Union[str, LastUpdate]] = None,
                file: Optional[File] = None,
                blob: Optional[Blob] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if name is not None and not isinstance(name, aas.SubmodelElement):
                    name = self.Name(name)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if recordCount is not None and not isinstance(recordCount, aas.SubmodelElement):
                    recordCount = self.RecordCount(recordCount)

                # Build a submodel element if a raw value was passed in the argument

                if startTime is not None and not isinstance(startTime, aas.SubmodelElement):
                    startTime = self.StartTime(startTime)

                # Build a submodel element if a raw value was passed in the argument

                if endTime is not None and not isinstance(endTime, aas.SubmodelElement):
                    endTime = self.EndTime(endTime)

                # Build a submodel element if a raw value was passed in the argument

                if duration is not None and not isinstance(duration, aas.SubmodelElement):
                    duration = self.Duration(duration)

                # Build a submodel element if a raw value was passed in the argument

                if samplingInterval is not None and not isinstance(samplingInterval, aas.SubmodelElement):
                    samplingInterval = self.SamplingInterval(samplingInterval)

                # Build a submodel element if a raw value was passed in the argument

                if samplingRate is not None and not isinstance(samplingRate, aas.SubmodelElement):
                    samplingRate = self.SamplingRate(samplingRate)

                # Build a submodel element if a raw value was passed in the argument

                if state is not None and not isinstance(state, aas.SubmodelElement):
                    state = self.State(state)

                # Build a submodel element if a raw value was passed in the argument

                if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                    lastUpdate = self.LastUpdate(lastUpdate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    name,
                    description_,
                    recordCount,
                    startTime,
                    endTime,
                    duration,
                    samplingInterval,
                    samplingRate,
                    state,
                    lastUpdate,
                    file,
                    blob,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LinkedSegment(aas.SubmodelElementCollection):

            class Name(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Name",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RecordCount(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RecordCount",
                        "value_type": xsd.Long,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StartTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StartTime",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EndTime",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Duration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Duration",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SamplingInterval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SamplingInterval",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SamplingRate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SamplingRate",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class State(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"State",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/State/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LastUpdate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LastUpdate",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Endpoint(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Endpoint",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Endpoint/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Query(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Query",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Query/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"LinkedSegment",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segments/LinkedSegment/1/1"),
                }

            def __init__(
                self,
                endpoint: Union[str, Endpoint],
                query: Union[str, Query],
                name: Optional[Union[aas.MultiLanguageTextType, Name]] = None,
                description_: Optional[Union[aas.MultiLanguageTextType, Description]] = None,
                recordCount: Optional[Union[xsd.Long, RecordCount]] = None,
                startTime: Optional[Union[str, StartTime]] = None,
                endTime: Optional[Union[str, EndTime]] = None,
                duration: Optional[Union[str, Duration]] = None,
                samplingInterval: Optional[Union[xsd.Long, SamplingInterval]] = None,
                samplingRate: Optional[Union[xsd.Long, SamplingRate]] = None,
                state: Optional[Union[str, State]] = None,
                lastUpdate: Optional[Union[str, LastUpdate]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if name is not None and not isinstance(name, aas.SubmodelElement):
                    name = self.Name(name)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if recordCount is not None and not isinstance(recordCount, aas.SubmodelElement):
                    recordCount = self.RecordCount(recordCount)

                # Build a submodel element if a raw value was passed in the argument

                if startTime is not None and not isinstance(startTime, aas.SubmodelElement):
                    startTime = self.StartTime(startTime)

                # Build a submodel element if a raw value was passed in the argument

                if endTime is not None and not isinstance(endTime, aas.SubmodelElement):
                    endTime = self.EndTime(endTime)

                # Build a submodel element if a raw value was passed in the argument

                if duration is not None and not isinstance(duration, aas.SubmodelElement):
                    duration = self.Duration(duration)

                # Build a submodel element if a raw value was passed in the argument

                if samplingInterval is not None and not isinstance(samplingInterval, aas.SubmodelElement):
                    samplingInterval = self.SamplingInterval(samplingInterval)

                # Build a submodel element if a raw value was passed in the argument

                if samplingRate is not None and not isinstance(samplingRate, aas.SubmodelElement):
                    samplingRate = self.SamplingRate(samplingRate)

                # Build a submodel element if a raw value was passed in the argument

                if state is not None and not isinstance(state, aas.SubmodelElement):
                    state = self.State(state)

                # Build a submodel element if a raw value was passed in the argument

                if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                    lastUpdate = self.LastUpdate(lastUpdate)

                # Build a submodel element if a raw value was passed in the argument

                if endpoint is not None and not isinstance(endpoint, aas.SubmodelElement):
                    endpoint = self.Endpoint(endpoint)

                # Build a submodel element if a raw value was passed in the argument

                if query is not None and not isinstance(query, aas.SubmodelElement):
                    query = self.Query(query)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    name,
                    description_,
                    recordCount,
                    startTime,
                    endTime,
                    duration,
                    samplingInterval,
                    samplingRate,
                    state,
                    lastUpdate,
                    endpoint,
                    query,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class InternalSegment(aas.SubmodelElementCollection):

            class Name(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Name",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RecordCount(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RecordCount",
                        "value_type": xsd.Long,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StartTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StartTime",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EndTime",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Duration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Duration",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SamplingInterval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SamplingInterval",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SamplingRate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SamplingRate",
                        "value_type": xsd.Long,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class State(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"State",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/State/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LastUpdate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LastUpdate",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Records(aas.SubmodelElementCollection):

                class Record(aas.SubmodelElementCollection):

                    class Time(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Time",
                                "value_type": xsd.Long,
                                "category": r"VARIABLE",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1"
                                ),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SampleAccelerationX(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"sampleAccelerationX",
                                "value_type": xsd.Long,
                                "category": r"VARIABLE",
                                "semantic_id": global_ref(r"https://sample.com/AccelerationX/1/1"),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SampleAccelerationY(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"sampleAccelerationY",
                                "value_type": xsd.Long,
                                "category": r"VARIABLE",
                                "semantic_id": global_ref(r"https://sample.com/AccelerationY/1/1"),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SampleAccelerationZ(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"sampleAccelerationZ",
                                "value_type": xsd.Long,
                                "category": r"VARIABLE",
                                "semantic_id": global_ref(r"https://sample.com/AccelerationZ/1/1"),
                            }

                        def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Record",
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Record/1/1"),
                        }

                    def __init__(
                        self,
                        time: Iterable[Union[xsd.Long, Time]],
                        sampleAccelerationX: Optional[Union[xsd.Long, SampleAccelerationX]] = None,
                        sampleAccelerationY: Optional[Union[xsd.Long, SampleAccelerationY]] = None,
                        sampleAccelerationZ: Optional[Union[xsd.Long, SampleAccelerationZ]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(time, str):
                            raise TypeError("time takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if time:
                            time = [i if isinstance(i, aas.SubmodelElement) else self.Time(i) for i in time]

                        # Build a submodel element if a raw value was passed in the argument

                        if sampleAccelerationX is not None and not isinstance(sampleAccelerationX, aas.SubmodelElement):
                            sampleAccelerationX = self.SampleAccelerationX(sampleAccelerationX)

                        # Build a submodel element if a raw value was passed in the argument

                        if sampleAccelerationY is not None and not isinstance(sampleAccelerationY, aas.SubmodelElement):
                            sampleAccelerationY = self.SampleAccelerationY(sampleAccelerationY)

                        # Build a submodel element if a raw value was passed in the argument

                        if sampleAccelerationZ is not None and not isinstance(sampleAccelerationZ, aas.SubmodelElement):
                            sampleAccelerationZ = self.SampleAccelerationZ(sampleAccelerationZ)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            time, sampleAccelerationX, sampleAccelerationY, sampleAccelerationZ
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Records",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Records/1/1"),
                    }

                def __init__(
                    self, record: Optional[Iterable[Record]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(record, str):
                        raise TypeError("record takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(record)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InternalSegment",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segments/InternalSegment/1/1"),
                }

            def __init__(
                self,
                records: Records,
                name: Optional[Union[aas.MultiLanguageTextType, Name]] = None,
                description_: Optional[Union[aas.MultiLanguageTextType, Description]] = None,
                recordCount: Optional[Union[xsd.Long, RecordCount]] = None,
                startTime: Optional[Union[str, StartTime]] = None,
                endTime: Optional[Union[str, EndTime]] = None,
                duration: Optional[Union[str, Duration]] = None,
                samplingInterval: Optional[Union[xsd.Long, SamplingInterval]] = None,
                samplingRate: Optional[Union[xsd.Long, SamplingRate]] = None,
                state: Optional[Union[str, State]] = None,
                lastUpdate: Optional[Union[str, LastUpdate]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if name is not None and not isinstance(name, aas.SubmodelElement):
                    name = self.Name(name)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if recordCount is not None and not isinstance(recordCount, aas.SubmodelElement):
                    recordCount = self.RecordCount(recordCount)

                # Build a submodel element if a raw value was passed in the argument

                if startTime is not None and not isinstance(startTime, aas.SubmodelElement):
                    startTime = self.StartTime(startTime)

                # Build a submodel element if a raw value was passed in the argument

                if endTime is not None and not isinstance(endTime, aas.SubmodelElement):
                    endTime = self.EndTime(endTime)

                # Build a submodel element if a raw value was passed in the argument

                if duration is not None and not isinstance(duration, aas.SubmodelElement):
                    duration = self.Duration(duration)

                # Build a submodel element if a raw value was passed in the argument

                if samplingInterval is not None and not isinstance(samplingInterval, aas.SubmodelElement):
                    samplingInterval = self.SamplingInterval(samplingInterval)

                # Build a submodel element if a raw value was passed in the argument

                if samplingRate is not None and not isinstance(samplingRate, aas.SubmodelElement):
                    samplingRate = self.SamplingRate(samplingRate)

                # Build a submodel element if a raw value was passed in the argument

                if state is not None and not isinstance(state, aas.SubmodelElement):
                    state = self.State(state)

                # Build a submodel element if a raw value was passed in the argument

                if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
                    lastUpdate = self.LastUpdate(lastUpdate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    name,
                    description_,
                    recordCount,
                    startTime,
                    endTime,
                    duration,
                    samplingInterval,
                    samplingRate,
                    state,
                    lastUpdate,
                    records,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Segments",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/Segments/1/1"),
            }

        def __init__(
            self,
            externalSegment: Optional[Iterable[ExternalSegment]] = None,
            linkedSegment: Optional[Iterable[LinkedSegment]] = None,
            internalSegment: Optional[Iterable[InternalSegment]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(externalSegment, str):
                raise TypeError("externalSegment takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(linkedSegment, str):
                raise TypeError("linkedSegment takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(internalSegment, str):
                raise TypeError("internalSegment takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(externalSegment, linkedSegment, internalSegment)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DeriveSegment(aas.Operation):

        @staticmethod
        def template_defaults() -> OperationMetadata:
            return {
                "id_short": r"DeriveSegment",
                "input_variable": (
                    aas.Range(
                        id_short=r"Timespan",
                        value_type=xsd.DateTime,
                        min=xsd.from_xsd(r"0001-01-01T00:00:00+00:00", xsd.DateTime),
                        max=xsd.from_xsd(r"9999-12-31T23:59:59+00:00", xsd.DateTime),
                        display_name=None,
                        category=None,
                        description=aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The valueType of the given timespan must match the valueType of the time properties of the segments."
                            }
                        ),
                        semantic_id=global_ref(r"https://admin-shell.io/idta/TimeSeries/Timespan/1/1"),
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    aas.Property(
                        id_short=r"SamplingInterval",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=None,
                        description=None,
                        semantic_id=global_ref(r"https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1"),
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                    aas.Property(
                        id_short=r"AggregationMethod",
                        value_type=str,
                        value=None,
                        value_id=None,
                        display_name=None,
                        category=None,
                        description=None,
                        semantic_id=global_ref(r"https://admin-shell.io/idta/TimeSeries/AggregationMethod/1/1"),
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                "output_variable": (
                    aas.SubmodelElementCollection(
                        id_short=r"Segments",
                        value=(),
                        display_name=None,
                        category=None,
                        description=None,
                        semantic_id=global_ref(r"https://admin-shell.io/idta/TimeSeries/AggregationMethod/1/1"),
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/DeriveSegment/1/1"),
            }

        def __init__(self, **kwargs: Unpack[OperationMetadata]):

            super().__init__(**(self.template_defaults() | kwargs))

    class ReadSegments(aas.Operation):

        @staticmethod
        def template_defaults() -> OperationMetadata:
            return {
                "id_short": r"ReadSegments",
                "input_variable": (
                    aas.Range(
                        id_short=r"Timespan",
                        value_type=xsd.DateTime,
                        min=xsd.from_xsd(r"0001-01-01T00:00:00+00:00", xsd.DateTime),
                        max=xsd.from_xsd(r"9999-12-31T23:59:59+00:00", xsd.DateTime),
                        display_name=None,
                        category=None,
                        description=aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The valueType of the given timespan must match the valueType of the time properties of the segments."
                            }
                        ),
                        semantic_id=global_ref(r"https://admin-shell.io/idta/TimeSeries/Timespan/1/1"),
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                "output_variable": (
                    aas.SubmodelElementCollection(
                        id_short=r"Segment",
                        value=(),
                        display_name=None,
                        category=None,
                        description=None,
                        semantic_id=None,
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/ReadSegments/1/1"),
            }

        def __init__(self, **kwargs: Unpack[OperationMetadata]):

            super().__init__(**(self.template_defaults() | kwargs))

    class ReadRecords(aas.Operation):

        @staticmethod
        def template_defaults() -> OperationMetadata:
            return {
                "id_short": r"ReadRecords",
                "input_variable": (
                    aas.Range(
                        id_short=r"Timespan",
                        value_type=xsd.DateTime,
                        min=xsd.from_xsd(r"0001-01-01T00:00:00+00:00", xsd.DateTime),
                        max=xsd.from_xsd(r"9999-12-31T23:59:59+00:00", xsd.DateTime),
                        display_name=None,
                        category=None,
                        description=aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The valueType of the given timespan must match the valueType of the time properties of the segments."
                            }
                        ),
                        semantic_id=global_ref(r"https://admin-shell.io/idta/TimeSeries/Timespan/1/1"),
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                "output_variable": (
                    aas.SubmodelElementCollection(
                        id_short=r"Records",
                        value=(),
                        display_name=None,
                        category=None,
                        description=None,
                        semantic_id=None,
                        qualifier=(),
                        extension=(),
                        supplemental_semantic_id=(),
                        embedded_data_specifications=[],
                    ),
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/TimeSeries/ReadRecords/1/1"),
            }

        def __init__(self, **kwargs: Unpack[OperationMetadata]):

            super().__init__(**(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"TimeSeries",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"de": r"Enthält Zeitreihendaten und Referenzen auf Zeitreihendaten, um diese entlang des Asset Lebenszyklus aufzufinden und semantisch zu beschreiben.",
                    r"en": r"Contains time series data and references to time series data to discover and semantically describe them along the asset lifecycle.",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"1", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/TimeSeries/1/1"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        metadata: Metadata,
        segments: Segments,
        deriveSegment: Optional[DeriveSegment] = None,
        readSegments: Optional[ReadSegments] = None,
        readRecords: Optional[ReadRecords] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            metadata, segments, deriveSegment, readSegments, readRecords
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
