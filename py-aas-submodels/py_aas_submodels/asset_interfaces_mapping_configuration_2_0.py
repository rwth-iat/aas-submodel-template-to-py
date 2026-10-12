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


class AssetInterfacesMappingConfiguration(aas.Submodel):

    class MappingConfigurations(GeneratedSubmodelElementList):

        class Mappingconfigurations_item(aas.SubmodelElementCollection):

            class DefaultPollingInterval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DefaultPollingInterval",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Default polling interval"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The DefaultPollingInterval defines the default time interval in seconds for fetching new data from the synchronous data sources defined in this MappingConfiguration. It must be greater than zero for synchronous protocols (e.g. HTTP) that need polling and is ignored for asynchronous protocols (e.g. MQTT)."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/DefaultPollingInterval"
                        ),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Transformation(aas.Blob):

                @staticmethod
                def template_defaults() -> BlobMetadata:
                    return {
                        "id_short": r"Transformation",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Transformation"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'The transformation allows for transforming incoming data before writing it to the sinks. The transformation must contain an "aimc_main(sources)" entrypoint function in Lua.'
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Transformation"
                        ),
                    }

                def __init__(
                    self,
                    value: Optional[bytes] = None,
                    content_type: Optional[str] = r"text/plain",
                    **kwargs: Unpack[BlobMetadata],
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class Sources(GeneratedSubmodelElementList):

                class Sources_item(aas.SubmodelElementCollection):

                    class Source(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"Source",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Source"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"This holds a reference to the respective SubmodelElement used as data source. A data source can be any SubmodelElement including those defined in the InteractionMetadata of AID Submodels for fetching live-data from assets."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/Source"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class PollingInterval(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"PollingInterval",
                                "value_type": float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Polling interval"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The PollingInterval defines the time interval in seconds for fetching new data from the given synchronous data source. It must be greater than zero for synchronous protocols (e.g. HTTP) that need polling and is ignored for asynchronous protocols (e.g. MQTT). It overwrites the DefaultPollingInterval of the respective MappingConfiguration of this source."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/PollingInterval"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SourceId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SourceId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Source ID"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"This is a unique and non-empty identifier that facilitates data access in the Lua transformation or establishes a relationship to a corresponding sink when no transformation is given. It must only be unique with respect to the Sources-list of the parent MappingConfiguration and not globally."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/SourceId"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Source"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"A data source is defined by a Source reference, PollingInterval and SourceId."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source"
                            ),
                        }

                    def __init__(
                        self,
                        source: Union[aas.Reference, Source],
                        sourceId: Union[str, SourceId],
                        pollingInterval: Optional[Union[float, PollingInterval]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if source is not None and not isinstance(source, aas.SubmodelElement):
                            source = self.Source(source)

                        # Build a submodel element if a raw value was passed in the argument

                        if pollingInterval is not None and not isinstance(pollingInterval, aas.SubmodelElement):
                            pollingInterval = self.PollingInterval(pollingInterval)

                        # Build a submodel element if a raw value was passed in the argument

                        if sourceId is not None and not isinstance(sourceId, aas.SubmodelElement):
                            sourceId = self.SourceId(sourceId)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(source, pollingInterval, sourceId)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"Sources",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source"
                        ),
                        "order_relevant": False,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sources"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"This list includes all data sources that are used in this MappingConfiguration."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sources"
                        ),
                    }

                def __init__(
                    self, sources_items: Iterable[Sources_item], **kwargs: Unpack[SubmodelElementListMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(sources_items, str):
                        raise TypeError("sources_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(sources_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Sinks(GeneratedSubmodelElementList):

                class Sinks_item(aas.SubmodelElementCollection):

                    class Sink(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"Sink",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sink"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"This holds a reference to the respective SubmodelElement used as data sink for live-data."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink/Sink"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SinkId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SinkId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sink ID"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"This is a unique and non-empty identifier that facilitates data writing in the Lua transformation or establishes a relationship to a corresponding source when no transformation is given. It must only be unique with respect to the Sinks-list of the containing MappingConfiguration and not globally."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink/SinkId"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sink"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"A data sink is defined by a Sink reference and SinkId."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink"
                            ),
                        }

                    def __init__(
                        self,
                        sink: Union[aas.Reference, Sink],
                        sinkId: Union[str, SinkId],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if sink is not None and not isinstance(sink, aas.SubmodelElement):
                            sink = self.Sink(sink)

                        # Build a submodel element if a raw value was passed in the argument

                        if sinkId is not None and not isinstance(sinkId, aas.SubmodelElement):
                            sinkId = self.SinkId(sinkId)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(sink, sinkId)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"Sinks",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink"
                        ),
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Sinks"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"This list includes all data sinks that are used in this MappingConfiguration."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sinks"
                        ),
                    }

                def __init__(self, sinks_items: Iterable[Sinks_item], **kwargs: Unpack[SubmodelElementListMetadata]):

                    # A str would be split into its characters
                    if isinstance(sinks_items, str):
                        raise TypeError("sinks_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(sinks_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Mapping configuration"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"A MappingConfiguration defines one logical unit of sources (inputs) and sinks (outputs) that are in relation to one another. The relation can be expressed via a transformation."
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration"
                    ),
                }

            def __init__(
                self,
                sources: Union[Iterable[Sources.Sources_item], Sources],
                sinks: Union[Iterable[Sinks.Sinks_item], Sinks],
                defaultPollingInterval: Optional[Union[float, DefaultPollingInterval]] = None,
                transformation: Optional[Transformation] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if defaultPollingInterval is not None and not isinstance(defaultPollingInterval, aas.SubmodelElement):
                    defaultPollingInterval = self.DefaultPollingInterval(defaultPollingInterval)

                # A str would be split into its characters
                if isinstance(sources, str):
                    raise TypeError("sources takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if sources is not None and not isinstance(sources, aas.SubmodelElement):
                    sources = self.Sources(sources)

                # A str would be split into its characters
                if isinstance(sinks, str):
                    raise TypeError("sinks takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if sinks is not None and not isinstance(sinks, aas.SubmodelElement):
                    sinks = self.Sinks(sinks)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    defaultPollingInterval, transformation, sources, sinks
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"MappingConfigurations",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration"
                ),
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Mapping configurations"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"List of MappingConfigurations that each map and transform data from their sources to their sinks."
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/1/0/MappingConfigurations"
                ),
            }

        def __init__(
            self,
            mappingconfigurations_items: Optional[Iterable[Mappingconfigurations_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(mappingconfigurations_items, str):
                raise TypeError("mappingconfigurations_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(mappingconfigurations_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"AssetInterfacesMappingConfiguration",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Asset interfaces mapping configuration"}),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The AIMC 2.0 is used to describe how data is mapped from asset to AAS or from AAS to AAS."
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"2",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/IDTA 02027-2-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/Submodel"),
        }

    def __init__(
        self,
        id_: str,
        mappingConfigurations: Union[Iterable[MappingConfigurations.Mappingconfigurations_item], MappingConfigurations],
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(mappingConfigurations, str):
            raise TypeError("mappingConfigurations takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if mappingConfigurations is not None and not isinstance(mappingConfigurations, aas.SubmodelElement):
            mappingConfigurations = self.MappingConfigurations(mappingConfigurations)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(mappingConfigurations)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
