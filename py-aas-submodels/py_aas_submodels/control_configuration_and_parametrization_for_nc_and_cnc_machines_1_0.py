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


class ControlConfig(aas.Submodel):

    class DigitalNameplate(aas.ReferenceElement):

        @staticmethod
        def template_defaults() -> ReferenceElementMetadata:
            return {
                "id_short": r"DigitalNameplate",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Reference to the digital nameplate of the controller."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/nameplate/3/0/Nameplate"),
            }

        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ControllerType(aas.Property):

        ALLOWED_VALUES = (r"Path controlled", r"Point controlled", r"Track controlled")

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"ControllerType",
                "value_type": str,
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"The Controller Type describes the type of controller"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/ControllerType/1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            if value is not None and value not in self.ALLOWED_VALUES:
                raise ValueError(
                    f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                )

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class TimeUnit(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"TimeUnit",
                "value_type": xsd.Float,
                "category": r"VARIABLE",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Time unit of the control"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/TimeUnit/1/0"),
            }

        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class LengthUnit(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"LengthUnit",
                "value_type": float,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Length Unit of the control"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/LengthUnit/1/0"),
            }

        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class FieldbusType(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"FieldbusType",
                "value_type": str,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Fieldbus Type of the control"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/FieldbusType/1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class CNCCycleTime(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"CNCCycleTime",
                "value_type": float,
                "category": r"VARIABLE",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Defines the cycle time of the CNC control"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/CNCCycleTime/1/0"),
            }

        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class PLCCycleTime(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"PLCCycleTime",
                "value_type": float,
                "category": r"VARIABLE",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Defines the cycle time of the PLC control"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/PLCCycleTime/1/0"),
            }

        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class FieldbusCycleTime(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"FieldbusCycleTime",
                "value_type": float,
                "category": r"VARIABLE",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the cycle time of the fieldbus control"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/FieldbusCycleTime/1/0"),
            }

        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class VelocityUnit(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"VelocityUnit",
                "value_type": str,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the velocity unit of the CNC control "}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/VelocityType/1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class AccelerationUnit(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"AccelerationUnit",
                "value_type": str,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the acceleration unit unit of the CNC control"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/ AccelerationUnit /1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class JerkUnit(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"JerkUnit",
                "value_type": str,
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Defines the jerk unit of the CNC control "}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/JerkUnit/1/0"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ControlConfigData(aas.SubmodelElementCollection):

        class ControlConfigFileName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ControlConfigFileName",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the control configuration file"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/ControlConfigFileName /1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ControlConfigFile(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"ControlConfigFile",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"File to configure the control"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/ControlConfigFile/1/0"),
                }

            def __init__(
                self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ControlConfigData",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Control configuration data", r"de": r"Steuerungskonfigurationsdaten"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/ControlConfigData/1/0"),
            }

        def __init__(
            self,
            controlConfigFileName: Union[str, ControlConfigFileName],
            controlConfigFile: ControlConfigFile,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if controlConfigFileName is not None and not isinstance(controlConfigFileName, aas.SubmodelElement):
                controlConfigFileName = self.ControlConfigFileName(controlConfigFileName)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(controlConfigFileName, controlConfigFile)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Channels(aas.SubmodelElementCollection):

        class Channel(aas.SubmodelElementCollection):

            class ChannelIdentification(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ChannelIdentification",
                        "value_type": str,
                        "category": r"VARIABLE",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"This describes the unique channel identification of the specific channel"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlConfig/Channels/ChannelIdentification/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AxesReference(aas.SubmodelElementCollection):

                class AxisName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AxisName",
                            "value_type": str,
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Unique axis name"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlConfig/Channels/AxesReference/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReferenceToAxis(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ReferenceToAxis",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Reference to the axis"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlConfig/Channels/ReferenceToAxis/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"AxesReference",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “AxesReference” is a collection of referenced axes for the specific channel."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlConfig/Channels/AxesReference/1/0"
                        ),
                    }

                def __init__(
                    self,
                    axisName: Union[str, AxisName],
                    referenceToAxis: Union[aas.Reference, ReferenceToAxis],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if axisName is not None and not isinstance(axisName, aas.SubmodelElement):
                        axisName = self.AxisName(axisName)

                    # Build a submodel element if a raw value was passed in the argument

                    if referenceToAxis is not None and not isinstance(referenceToAxis, aas.SubmodelElement):
                        referenceToAxis = self.ReferenceToAxis(referenceToAxis)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(axisName, referenceToAxis)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Channel",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Configuration information of a specific channel"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Channel/1/0"),
                }

            def __init__(
                self,
                channelIdentification: Union[str, ChannelIdentification],
                axesReference: Optional[Iterable[AxesReference]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if channelIdentification is not None and not isinstance(channelIdentification, aas.SubmodelElement):
                    channelIdentification = self.ChannelIdentification(channelIdentification)

                # A str would be split into its characters
                if isinstance(axesReference, str):
                    raise TypeError("axesReference takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(channelIdentification, axesReference)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Channels",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Collection of channels of the control"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Channels/1/0"),
            }

        def __init__(self, channel: Channel, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(channel)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Axes(aas.SubmodelElementCollection):

        class Axis(aas.SubmodelElementCollection):

            class AxisName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AxisName",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the axis"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Axes/AxisName/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AxisType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AxisType",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Type of the axis"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Axes/AxisType/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SimulationAxis(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SimulationAxis",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Axis is a simulated or real one"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlConfig/Axes/SwLimitSwitchPos/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SwLimitSwitchNeg(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SwLimitSwitchNeg",
                        "value_type": float,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Positive software limit switch"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlConfig/Axes/SwLimitSwitchNeg/1/0"
                        ),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SwLimitSwitchPos(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SwLimitSwitchPos",
                        "value_type": str,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Negative software limit switch"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlConfig/Axes/SwLimitSwitchPos/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class VelocityLimit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"VelocityLimit",
                        "value_type": xsd.Long,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Velocity limit of the axis"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Axes/VelocityLimit/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AccelerationLimit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AccelerationLimit",
                        "value_type": xsd.Long,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Accelerationlimit of the axis"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlConfig/Axes/AccelerationLimit /1/0"
                        ),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class JerkLimit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"JerkLimit",
                        "value_type": xsd.Long,
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Jerk limit of the axis"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Axes/JerkLimit/1/0"),
                    }

                def __init__(self, value: xsd.Long, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AxisConfigData(aas.SubmodelElementCollection):

                class AxisConfigFileName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AxisConfigFileName",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Axis configuration file name"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlConfig/Channels/Axes/AxisConfigFileName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AxisConfigFile(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"AxisConfigFile",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Configuration file of the axis"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlConfig/Channels/Axes/AxisConfigFile/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"AxisConfigData",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"The SMC “AxisConfigData” is a collection of axis configuration data."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/ControlConfig/Channels/Axes/AxisConfigData/1/0"
                        ),
                    }

                def __init__(
                    self,
                    axisConfigFileName: Optional[Union[str, AxisConfigFileName]] = None,
                    axisConfigFile: Optional[AxisConfigFile] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if axisConfigFileName is not None and not isinstance(axisConfigFileName, aas.SubmodelElement):
                        axisConfigFileName = self.AxisConfigFileName(axisConfigFileName)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(axisConfigFileName, axisConfigFile)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Drive(aas.SubmodelElementCollection):

                class Manual(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"Manual",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"The manual file of the drive "}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Manual/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class TechnicalData(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"TechnicalData",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to the Submodel Technical Specification of the axis to gather more information"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/IDTA/TechnicalData/Submodel/2/0"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DriveConfigData(aas.SubmodelElementCollection):

                    class DriveConfigFileName(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DriveConfigFileName",
                                "value_type": str,
                                "category": r"CONSTANT",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Name of the configuration file of the drive "}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Drive/DriveConfigFileName/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DriveConfigFile(aas.File):

                        @staticmethod
                        def template_defaults() -> FileMetadata:
                            return {
                                "id_short": r"DriveConfigFile",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Configuration File of the drive"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Drive/DriveConfigFile/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            value: str,
                            content_type: Optional[str] = r"application/json",
                            **kwargs: Unpack[FileMetadata],
                        ):

                            super().__init__(
                                value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                            )

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"DriveConfigData",
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The SMC “DriveConfigData” is a collection of drive configuration data."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/DriveConfigData/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        driveConfigFileName: Optional[Union[str, DriveConfigFileName]] = None,
                        driveConfigFile: Optional[DriveConfigFile] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if driveConfigFileName is not None and not isinstance(driveConfigFileName, aas.SubmodelElement):
                            driveConfigFileName = self.DriveConfigFileName(driveConfigFileName)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(driveConfigFileName, driveConfigFile)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Drive",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"The SMC “Drive” is a collection of drive configuration information."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Drive/1/0"),
                    }

                def __init__(
                    self,
                    manual: Optional[Manual] = None,
                    technicalData: Optional[Union[aas.Reference, TechnicalData]] = None,
                    driveConfigData: Optional[DriveConfigData] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if technicalData is not None and not isinstance(technicalData, aas.SubmodelElement):
                        technicalData = self.TechnicalData(technicalData)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(manual, technicalData, driveConfigData)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Axis",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"The SMC “Axis” is a collection of axis configuration information."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Channel/Axis/1/0"),
                }

            def __init__(
                self,
                axisName: Optional[Union[str, AxisName]] = None,
                axisType: Optional[Union[str, AxisType]] = None,
                simulationAxis: Optional[Union[str, SimulationAxis]] = None,
                swLimitSwitchNeg: Optional[Union[float, SwLimitSwitchNeg]] = None,
                swLimitSwitchPos: Optional[Union[str, SwLimitSwitchPos]] = None,
                velocityLimit: Optional[Union[xsd.Long, VelocityLimit]] = None,
                accelerationLimit: Optional[Union[xsd.Long, AccelerationLimit]] = None,
                jerkLimit: Optional[Union[xsd.Long, JerkLimit]] = None,
                axisConfigData: Optional[AxisConfigData] = None,
                drive: Optional[Drive] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if axisName is not None and not isinstance(axisName, aas.SubmodelElement):
                    axisName = self.AxisName(axisName)

                # Build a submodel element if a raw value was passed in the argument

                if axisType is not None and not isinstance(axisType, aas.SubmodelElement):
                    axisType = self.AxisType(axisType)

                # Build a submodel element if a raw value was passed in the argument

                if simulationAxis is not None and not isinstance(simulationAxis, aas.SubmodelElement):
                    simulationAxis = self.SimulationAxis(simulationAxis)

                # Build a submodel element if a raw value was passed in the argument

                if swLimitSwitchNeg is not None and not isinstance(swLimitSwitchNeg, aas.SubmodelElement):
                    swLimitSwitchNeg = self.SwLimitSwitchNeg(swLimitSwitchNeg)

                # Build a submodel element if a raw value was passed in the argument

                if swLimitSwitchPos is not None and not isinstance(swLimitSwitchPos, aas.SubmodelElement):
                    swLimitSwitchPos = self.SwLimitSwitchPos(swLimitSwitchPos)

                # Build a submodel element if a raw value was passed in the argument

                if velocityLimit is not None and not isinstance(velocityLimit, aas.SubmodelElement):
                    velocityLimit = self.VelocityLimit(velocityLimit)

                # Build a submodel element if a raw value was passed in the argument

                if accelerationLimit is not None and not isinstance(accelerationLimit, aas.SubmodelElement):
                    accelerationLimit = self.AccelerationLimit(accelerationLimit)

                # Build a submodel element if a raw value was passed in the argument

                if jerkLimit is not None and not isinstance(jerkLimit, aas.SubmodelElement):
                    jerkLimit = self.JerkLimit(jerkLimit)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    axisName,
                    axisType,
                    simulationAxis,
                    swLimitSwitchNeg,
                    swLimitSwitchPos,
                    velocityLimit,
                    accelerationLimit,
                    jerkLimit,
                    axisConfigData,
                    drive,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Axes",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"The SMC “Axes” is a collection of axes of the CNC controller."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Axes/1/0"),
            }

        def __init__(self, axis: Optional[Axis] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(axis)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class NCProgramConfig(aas.SubmodelElementCollection):

        class NCProgramFileType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NCProgramFileType",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"NC program file type, which the CNC control can work with"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/NCProgramFileType/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NCProgramSyntaxType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NCProgramSyntaxType",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"NC program syntax type"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/NCProgramSyntaxType/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NCProgramSyntaxManual(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"NCProgramSyntaxManual",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Manual file of the syntax of the NC program"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/NCProgramSyntaxManual/1/0"),
                }

            def __init__(
                self, value: str, content_type: Optional[str] = r"application/json", **kwargs: Unpack[FileMetadata]
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"NCProgramConfig",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"The SMC “NCProgramConfig” is a collection of NC program configuration information."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/NCProgramConfig/1/0"),
            }

        def __init__(
            self,
            nCProgramFileType: Optional[Union[str, NCProgramFileType]] = None,
            nCProgramSyntaxType: Optional[Union[str, NCProgramSyntaxType]] = None,
            nCProgramSyntaxManual: Optional[Iterable[NCProgramSyntaxManual]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if nCProgramFileType is not None and not isinstance(nCProgramFileType, aas.SubmodelElement):
                nCProgramFileType = self.NCProgramFileType(nCProgramFileType)

            # Build a submodel element if a raw value was passed in the argument

            if nCProgramSyntaxType is not None and not isinstance(nCProgramSyntaxType, aas.SubmodelElement):
                nCProgramSyntaxType = self.NCProgramSyntaxType(nCProgramSyntaxType)

            # A str would be split into its characters
            if isinstance(nCProgramSyntaxManual, str):
                raise TypeError("nCProgramSyntaxManual takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                nCProgramFileType, nCProgramSyntaxType, nCProgramSyntaxManual
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class CommunicationConfig(aas.SubmodelElementCollection):

        class CommunicationType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CommunicationType",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Type of communication to the control"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/CommunicationType/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CommunicationAdress(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CommunicationAdress",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Communication address into the control"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/CommunicationAdress/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CommunicationInformationModel(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CommunicationInformationModel",
                    "value_type": str,
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Communication information model if ones exist like OPCUA"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/ControlConfig/CommunicationInformationModel/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class OPCUAServerDataSheet(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"OPCUAServerDataSheet",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Reference to the OPCUA server datasheet Submodel"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/opcua-server-datasheet/1/0"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"CommunicationConfig",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The SMC “CommunicationConfig” is a collection of communication configuration information."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/CommunicationConfig/1/0"),
            }

        def __init__(
            self,
            communicationType: Optional[Union[str, CommunicationType]] = None,
            communicationAdress: Optional[Union[str, CommunicationAdress]] = None,
            communicationInformationModel: Optional[Union[str, CommunicationInformationModel]] = None,
            oPCUAServerDataSheet: Optional[Union[aas.Reference, OPCUAServerDataSheet]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if communicationType is not None and not isinstance(communicationType, aas.SubmodelElement):
                communicationType = self.CommunicationType(communicationType)

            # Build a submodel element if a raw value was passed in the argument

            if communicationAdress is not None and not isinstance(communicationAdress, aas.SubmodelElement):
                communicationAdress = self.CommunicationAdress(communicationAdress)

            # Build a submodel element if a raw value was passed in the argument

            if communicationInformationModel is not None and not isinstance(
                communicationInformationModel, aas.SubmodelElement
            ):
                communicationInformationModel = self.CommunicationInformationModel(communicationInformationModel)

            # Build a submodel element if a raw value was passed in the argument

            if oPCUAServerDataSheet is not None and not isinstance(oPCUAServerDataSheet, aas.SubmodelElement):
                oPCUAServerDataSheet = self.OPCUAServerDataSheet(oPCUAServerDataSheet)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                communicationType, communicationAdress, communicationInformationModel, oPCUAServerDataSheet
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Tools(aas.SubmodelElementCollection):

        class Tool(aas.SubmodelElementCollection):

            class ToolDescription(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"ToolDescription",
                        "category": r"CONSTANT",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Reference to the tool description Submodel of the specific tool."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ToolDescription/1/0"),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Tool",
                    "category": r"CONSTANT",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"The SMC “Tool” is a collection of tool configuration information."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Tool/1/0"),
                }

            def __init__(
                self,
                toolDescription: Optional[Union[aas.Reference, ToolDescription]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if toolDescription is not None and not isinstance(toolDescription, aas.SubmodelElement):
                    toolDescription = self.ToolDescription(toolDescription)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(toolDescription)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Tools",
                "category": r"CONSTANT",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Explanation: The SMC “Tools” is a collection of tools of the CNC controller."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/ControlConfig/Tools/1/0"),
            }

        def __init__(self, tool: Optional[Iterable[Tool]] = None, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # A str would be split into its characters
            if isinstance(tool, str):
                raise TypeError("tool takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(tool)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ControlConfig",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel “ControlConfig” is the collection for various parametrizations for the control of CNC machines "
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02053-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/ControlConfig/1/0"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        digitalNameplate: Union[aas.Reference, DigitalNameplate],
        controllerType: Union[str, ControllerType],
        timeUnit: Union[xsd.Float, TimeUnit],
        axes: Iterable[Axes],
        tools: Iterable[Tools],
        lengthUnit: Optional[Union[float, LengthUnit]] = None,
        fieldbusType: Optional[Union[str, FieldbusType]] = None,
        cNCCycleTime: Optional[Union[float, CNCCycleTime]] = None,
        pLCCycleTime: Optional[Union[float, PLCCycleTime]] = None,
        fieldbusCycleTime: Optional[Union[float, FieldbusCycleTime]] = None,
        velocityUnit: Optional[Union[str, VelocityUnit]] = None,
        accelerationUnit: Optional[Union[str, AccelerationUnit]] = None,
        jerkUnit: Optional[Union[str, JerkUnit]] = None,
        controlConfigData: Optional[Iterable[ControlConfigData]] = None,
        channels: Optional[Iterable[Channels]] = None,
        nCProgramConfig: Optional[NCProgramConfig] = None,
        communicationConfig: Optional[CommunicationConfig] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if digitalNameplate is not None and not isinstance(digitalNameplate, aas.SubmodelElement):
            digitalNameplate = self.DigitalNameplate(digitalNameplate)

        # Build a submodel element if a raw value was passed in the argument

        if controllerType is not None and not isinstance(controllerType, aas.SubmodelElement):
            controllerType = self.ControllerType(controllerType)

        # Build a submodel element if a raw value was passed in the argument

        if timeUnit is not None and not isinstance(timeUnit, aas.SubmodelElement):
            timeUnit = self.TimeUnit(timeUnit)

        # Build a submodel element if a raw value was passed in the argument

        if lengthUnit is not None and not isinstance(lengthUnit, aas.SubmodelElement):
            lengthUnit = self.LengthUnit(lengthUnit)

        # Build a submodel element if a raw value was passed in the argument

        if fieldbusType is not None and not isinstance(fieldbusType, aas.SubmodelElement):
            fieldbusType = self.FieldbusType(fieldbusType)

        # Build a submodel element if a raw value was passed in the argument

        if cNCCycleTime is not None and not isinstance(cNCCycleTime, aas.SubmodelElement):
            cNCCycleTime = self.CNCCycleTime(cNCCycleTime)

        # Build a submodel element if a raw value was passed in the argument

        if pLCCycleTime is not None and not isinstance(pLCCycleTime, aas.SubmodelElement):
            pLCCycleTime = self.PLCCycleTime(pLCCycleTime)

        # Build a submodel element if a raw value was passed in the argument

        if fieldbusCycleTime is not None and not isinstance(fieldbusCycleTime, aas.SubmodelElement):
            fieldbusCycleTime = self.FieldbusCycleTime(fieldbusCycleTime)

        # Build a submodel element if a raw value was passed in the argument

        if velocityUnit is not None and not isinstance(velocityUnit, aas.SubmodelElement):
            velocityUnit = self.VelocityUnit(velocityUnit)

        # Build a submodel element if a raw value was passed in the argument

        if accelerationUnit is not None and not isinstance(accelerationUnit, aas.SubmodelElement):
            accelerationUnit = self.AccelerationUnit(accelerationUnit)

        # Build a submodel element if a raw value was passed in the argument

        if jerkUnit is not None and not isinstance(jerkUnit, aas.SubmodelElement):
            jerkUnit = self.JerkUnit(jerkUnit)

        # A str would be split into its characters
        if isinstance(controlConfigData, str):
            raise TypeError("controlConfigData takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(channels, str):
            raise TypeError("channels takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(axes, str):
            raise TypeError("axes takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(tools, str):
            raise TypeError("tools takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            digitalNameplate,
            controllerType,
            timeUnit,
            lengthUnit,
            fieldbusType,
            cNCCycleTime,
            pLCCycleTime,
            fieldbusCycleTime,
            velocityUnit,
            accelerationUnit,
            jerkUnit,
            controlConfigData,
            channels,
            axes,
            nCProgramConfig,
            communicationConfig,
            tools,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
