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


class EntityMetadata(TypedDict, total=False):
    """Metadata of aas.Entity, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    entity_type: Optional[aas.EntityType]
    global_asset_id: Optional[str]
    specific_asset_id: Iterable[aas.SpecificAssetId]
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


class ServiceRequestNotification(aas.Submodel):

    class NumberOfServiceRequestNotifications(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"NumberOfServiceRequestNotifications",
                "value_type": int,
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Anzahl Servicebedarfsmeldungen", r"en": r"Number Service Request Notification  "}
                ),
                "category": r"PARAMETER",
                "semantic_id": global_ref(r"0173-1#02-ABI761#001"),
            }

        def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ServiceRequestNotification(aas.SubmodelElementCollection):

        class ReportedBy(aas.SubmodelElementCollection):

            class CustomerNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CustomerNumber",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Kundennummer", r"en": r"Customer number"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABI769#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SenderSystem(aas.Entity):

                @staticmethod
                def template_defaults() -> EntityMetadata:
                    return {
                        "id_short": r"SenderSystem",
                        "entity_type": aas.EntityType.CO_MANAGED_ENTITY,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Sendendes System", r"en": r"Sender system"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI770#001"),
                    }

                def __init__(self, **kwargs: Unpack[EntityMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class NumberOfContacs(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NumberOfContacs",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Anzahl der Kontakte", r"en": r"Number of contacts"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO203#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContactInformation(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ContactInformation",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Kontaktinformationen", r"en": r"Contact information"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAQ837#007/0173-1#01-ADR448#007"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ReportedBy",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Gemeldet von", r"en": r"Reported by"}),
                    "semantic_id": global_ref(r"0173-1#02-ABI792#00/0173-1#01-AHX448#001"),
                }

            def __init__(
                self,
                contactInformation: Iterable[ContactInformation],
                customerNumber: Optional[Union[str, CustomerNumber]] = None,
                senderSystem: Optional[SenderSystem] = None,
                numberOfContacs: Optional[Union[str, NumberOfContacs]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if customerNumber is not None and not isinstance(customerNumber, aas.SubmodelElement):
                    customerNumber = self.CustomerNumber(customerNumber)

                # Build a submodel element if a raw value was passed in the argument

                if numberOfContacs is not None and not isinstance(numberOfContacs, aas.SubmodelElement):
                    numberOfContacs = self.NumberOfContacs(numberOfContacs)

                # A str would be split into its characters
                if isinstance(contactInformation, str):
                    raise TypeError("contactInformation takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    customerNumber, senderSystem, numberOfContacs, contactInformation
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ServiceRequestNotificationId(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ServiceRequestNotificationId",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"ID der Bedarfsmeldung", r"en": r"ID of Service Request Notification"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABI772#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Status(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Status",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABH938#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Priority(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Priority",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Priorität der Meldung", r"en": r"Priority of notification"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABI773#001"),
                }

            def __init__(self, value: str = r"Medium", **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RelatedAsset(aas.Entity):

            @staticmethod
            def template_defaults() -> EntityMetadata:
                return {
                    "id_short": r"RelatedAsset",
                    "entity_type": aas.EntityType.CO_MANAGED_ENTITY,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Betroffenes Asset", r"en": r"Related Asset"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABI774#001"),
                }

            def __init__(self, **kwargs: Unpack[EntityMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(statement=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ShortText(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"ShortText",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Kurztext zur Servicebedarfsmeldung", r"en": r"Short text of Service Request"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABI762#001"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ServiceType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ServiceType",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Typ des notwendigen Service", r"en": r"Type of requested service"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABI763#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DetailedInformation(aas.SubmodelElementCollection):

            class LongText(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"LongText",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Langtext zur Servicebedarfsmeldung",
                                r"en": r"Long text of Service Request ",
                            }
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABI764#001"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StartOfFault(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StartOfFault",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Beginn der Störung", r"en": r"Start of fault"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABI765#001"),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ErrorCode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ErrorCode",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Fehlercode", r"en": r"Error code"}),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABI766#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AttachedMedia(aas.SubmodelElementCollection):

                class NumberOfMedias(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NumberOfMedias",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Anzahl der Anhänge", r"en": r"Number of Media"}
                            ),
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"0173-1#02-ABI767#001"),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Media(aas.SubmodelElementCollection):

                    class DigitalFile(aas.File):

                        @staticmethod
                        def template_defaults() -> FileMetadata:
                            return {
                                "id_short": r"DigitalFile",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"de": r"Digitale Datei", r"en": r"Digital File"}
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABK126#001"),
                            }

                        def __init__(
                            self,
                            value: str,
                            content_type: Optional[str] = r"image/jpeg",
                            **kwargs: Unpack[FileMetadata],
                        ):

                            super().__init__(
                                value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                            )

                    class Comment(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"Comment",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"de": r"Anmerkdung zur Datei", r"en": r"Comment to File"}
                                ),
                                "category": r"PARAMETER",
                                "semantic_id": global_ref(r"0173-1#02-ABI768#001"),
                            }

                        def __init__(
                            self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                        ):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Media",
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Anhang", r"en": r"Media"}),
                            "semantic_id": global_ref(r"0173-1#02-ABI791#001/0173-1#01-AHX447#001"),
                        }

                    def __init__(
                        self,
                        digitalFile: DigitalFile,
                        comment: Optional[Union[aas.MultiLanguageTextType, Comment]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if comment is not None and not isinstance(comment, aas.SubmodelElement):
                            comment = self.Comment(comment)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(digitalFile, comment)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"AttachedMedia",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Angehängte Dateien", r"en": r"Attached media"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABI790#001/0173-1#01-AHX446#001"),
                    }

                def __init__(
                    self,
                    media: Iterable[Media],
                    numberOfMedias: Optional[Union[int, NumberOfMedias]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if numberOfMedias is not None and not isinstance(numberOfMedias, aas.SubmodelElement):
                        numberOfMedias = self.NumberOfMedias(numberOfMedias)

                    # A str would be split into its characters
                    if isinstance(media, str):
                        raise TypeError("media takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(numberOfMedias, media)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DetailedInformation",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"de": r"Detailinformationen zum Servicebedarf",
                            r"en": r"Detailed information of service need",
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI789#001/0173-1#01-AHX445#001"),
                }

            def __init__(
                self,
                longText: Optional[Union[aas.MultiLanguageTextType, LongText]] = None,
                startOfFault: Optional[Union[xsd.DateTime, StartOfFault]] = None,
                errorCode: Optional[Union[str, ErrorCode]] = None,
                attachedMedia: Optional[AttachedMedia] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if longText is not None and not isinstance(longText, aas.SubmodelElement):
                    longText = self.LongText(longText)

                # Build a submodel element if a raw value was passed in the argument

                if startOfFault is not None and not isinstance(startOfFault, aas.SubmodelElement):
                    startOfFault = self.StartOfFault(startOfFault)

                # Build a submodel element if a raw value was passed in the argument

                if errorCode is not None and not isinstance(errorCode, aas.SubmodelElement):
                    errorCode = self.ErrorCode(errorCode)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(longText, startOfFault, errorCode, attachedMedia)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class OnsiteContact(aas.SubmodelElementCollection):

            class PartnerNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PartnerNumber",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Partnernummer", r"en": r"Partner number"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABI771#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NumberOfContacts(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NumberOfContacts",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Anzahl der Kontakte", r"en": r"Number of contacts "}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAO203#004"),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContactInformation(aas.SubmodelElementCollection):

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ContactInformation",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Kontaktinformationen", r"en": r"Contact information"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAQ837#007/0173-1#01-ADR448#007"),
                    }

                def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"OnsiteContact",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Ansprechpartner vor Ort", r"en": r"Onsite contact"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI793#001/0173-1#01-AHX449#001"),
                }

            def __init__(
                self,
                contactInformation: Iterable[ContactInformation],
                partnerNumber: Optional[Union[str, PartnerNumber]] = None,
                numberOfContacts: Optional[Union[int, NumberOfContacts]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if partnerNumber is not None and not isinstance(partnerNumber, aas.SubmodelElement):
                    partnerNumber = self.PartnerNumber(partnerNumber)

                # Build a submodel element if a raw value was passed in the argument

                if numberOfContacts is not None and not isinstance(numberOfContacts, aas.SubmodelElement):
                    numberOfContacts = self.NumberOfContacts(numberOfContacts)

                # A str would be split into its characters
                if isinstance(contactInformation, str):
                    raise TypeError("contactInformation takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    partnerNumber, numberOfContacts, contactInformation
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ServiceRequestNotification",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Servicebedarfsmeldung", r"en": r"Service request notification"}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABI788#001/0173-1#01-AHX444#001"),
            }

        def __init__(
            self,
            reportedBy: ReportedBy,
            status: Union[str, Status],
            priority: Union[str, Priority],
            relatedAsset: RelatedAsset,
            shortText: Union[aas.MultiLanguageTextType, ShortText],
            serviceType: Union[str, ServiceType],
            serviceRequestNotificationId: Optional[Union[str, ServiceRequestNotificationId]] = None,
            detailedInformation: Optional[DetailedInformation] = None,
            onsiteContact: Optional[OnsiteContact] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if serviceRequestNotificationId is not None and not isinstance(
                serviceRequestNotificationId, aas.SubmodelElement
            ):
                serviceRequestNotificationId = self.ServiceRequestNotificationId(serviceRequestNotificationId)

            # Build a submodel element if a raw value was passed in the argument

            if status is not None and not isinstance(status, aas.SubmodelElement):
                status = self.Status(status)

            # Build a submodel element if a raw value was passed in the argument

            if priority is not None and not isinstance(priority, aas.SubmodelElement):
                priority = self.Priority(priority)

            # Build a submodel element if a raw value was passed in the argument

            if shortText is not None and not isinstance(shortText, aas.SubmodelElement):
                shortText = self.ShortText(shortText)

            # Build a submodel element if a raw value was passed in the argument

            if serviceType is not None and not isinstance(serviceType, aas.SubmodelElement):
                serviceType = self.ServiceType(serviceType)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                reportedBy,
                serviceRequestNotificationId,
                status,
                priority,
                relatedAsset,
                shortText,
                serviceType,
                detailedInformation,
                onsiteContact,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"ServiceRequestNotification",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"This submodel aims to standardize the description of a service request notification that can be used to create a service request notification for industrial assets or the asset creates it by itself."
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AHX443#001"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        numberOfServiceRequestNotifications: Optional[Union[int, NumberOfServiceRequestNotifications]] = None,
        serviceRequestNotification: Optional[Iterable[ServiceRequestNotification]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if numberOfServiceRequestNotifications is not None and not isinstance(
            numberOfServiceRequestNotifications, aas.SubmodelElement
        ):
            numberOfServiceRequestNotifications = self.NumberOfServiceRequestNotifications(
                numberOfServiceRequestNotifications
            )

        # A str would be split into its characters
        if isinstance(serviceRequestNotification, str):
            raise TypeError("serviceRequestNotification takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            numberOfServiceRequestNotifications, serviceRequestNotification
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
