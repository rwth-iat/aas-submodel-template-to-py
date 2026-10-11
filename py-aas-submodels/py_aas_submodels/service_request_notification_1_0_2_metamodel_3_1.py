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


class ServiceRequestNotification(aas.Submodel):

    class NumberOfServiceRequestNotifications(aas.Property):

        def __init__(
            self,
            value: int,
            id_short: Optional[str] = r"NumberOfServiceRequestNotifications",
            value_type: aas.DataTypeDefXsd = int,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI761#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"de": r"Anzahl Servicebedarfsmeldungen", r"en": r"Number Service Request Notification  "}
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

    class ServiceRequestNotification(aas.SubmodelElementCollection):

        class ReportedBy(aas.SubmodelElementCollection):

            class CustomerNumber(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"CustomerNumber",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI769#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Kundennummer", r"en": r"Customer number"}
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

            class SenderSystem(aas.Entity):

                def __init__(
                    self,
                    id_short: Optional[str] = r"SenderSystem",
                    entity_type: Optional[aas.EntityType] = aas.EntityType.CO_MANAGED_ENTITY,
                    global_asset_id: Optional[str] = None,
                    specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI770#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Sendendes System", r"en": r"Sender system"}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

                    super().__init__(
                        statement=embedded_submodel_elements,
                        id_short=id_short,
                        entity_type=entity_type,
                        global_asset_id=global_asset_id,
                        specific_asset_id=specific_asset_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class NumberOfContacs(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NumberOfContacs",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAO203#004"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Anzahl der Kontakte", r"en": r"Number of contacts"}
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

            class ContactInformation(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"ContactInformation",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAQ837#007/0173-1#01-ADR448#007"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Kontaktinformationen", r"en": r"Contact information"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required"
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

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
                contactInformation: Iterable[ContactInformation],
                customerNumber: Optional[Union[str, CustomerNumber]] = None,
                senderSystem: Optional[SenderSystem] = None,
                numberOfContacs: Optional[Union[str, NumberOfContacs]] = None,
                id_short: Optional[str] = r"ReportedBy",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI792#00/0173-1#01-AHX448#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"de": r"Gemeldet von", r"en": r"Reported by"})

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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

        class ServiceRequestNotificationId(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ServiceRequestNotificationId",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI772#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"ID der Bedarfsmeldung", r"en": r"ID of Service Request Notification"}
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

        class Status(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Status",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABH938#002"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

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

        class Priority(aas.Property):

            def __init__(
                self,
                value: str = r"Medium",
                id_short: Optional[str] = r"Priority",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI773#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Priorität der Meldung", r"en": r"Priority of notification"}
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

        class RelatedAsset(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = r"RelatedAsset",
                entity_type: Optional[aas.EntityType] = aas.EntityType.CO_MANAGED_ENTITY,
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI774#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Betroffenes Asset", r"en": r"Related Asset"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(
                    statement=embedded_submodel_elements,
                    id_short=id_short,
                    entity_type=entity_type,
                    global_asset_id=global_asset_id,
                    specific_asset_id=specific_asset_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ShortText(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ShortText",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI762#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Kurztext zur Servicebedarfsmeldung", r"en": r"Short text of Service Request"}
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

        class ServiceType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ServiceType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI763#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Typ des notwendigen Service", r"en": r"Type of requested service"}
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

        class DetailedInformation(aas.SubmodelElementCollection):

            class LongText(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"LongText",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI764#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Langtext zur Servicebedarfsmeldung",
                                r"en": r"Long text of Service Request ",
                            }
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

            class StartOfFault(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"StartOfFault",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI765#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Beginn der Störung", r"en": r"Start of fault"}
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

            class ErrorCode(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ErrorCode",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI766#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(dict_={r"de": r"Fehlercode", r"en": r"Error code"})

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

            class AttachedMedia(aas.SubmodelElementCollection):

                class NumberOfMedias(aas.Property):

                    def __init__(
                        self,
                        value: int,
                        id_short: Optional[str] = r"NumberOfMedias",
                        value_type: aas.DataTypeDefXsd = int,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI767#001"),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"de": r"Anzahl der Anhänge", r"en": r"Number of Media"}
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

                class Media(aas.SubmodelElementCollection):

                    class DigitalFile(aas.File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"DigitalFile",
                            content_type: Optional[str] = r"image/jpeg",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK126#001"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"de": r"Digitale Datei", r"en": r"Digital File"}
                                )

                            if qualifier is None:
                                qualifier = ()

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

                    class Comment(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"Comment",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI768#001"),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"de": r"Anmerkdung zur Datei", r"en": r"Comment to File"}
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
                        digitalFile: DigitalFile,
                        comment: Optional[Union[aas.LangStringSet, Comment]] = None,
                        id_short: Optional[str] = r"Media",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI791#001/0173-1#01-AHX447#001"),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(dict_={r"de": r"Anhang", r"en": r"Media"})

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if comment is not None and not isinstance(comment, aas.SubmodelElement):
                            comment = self.Comment(comment)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(digitalFile, comment)

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
                    media: Iterable[Media],
                    numberOfMedias: Optional[Union[int, NumberOfMedias]] = None,
                    id_short: Optional[str] = r"AttachedMedia",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI790#001/0173-1#01-AHX446#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Angehängte Dateien", r"en": r"Attached media"}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if numberOfMedias is not None and not isinstance(numberOfMedias, aas.SubmodelElement):
                        numberOfMedias = self.NumberOfMedias(numberOfMedias)

                    # A str would be split into its characters
                    if isinstance(media, str):
                        raise TypeError("media takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(numberOfMedias, media)

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
                longText: Optional[Union[aas.LangStringSet, LongText]] = None,
                startOfFault: Optional[Union[xsd.DateTime, StartOfFault]] = None,
                errorCode: Optional[Union[str, ErrorCode]] = None,
                attachedMedia: Optional[AttachedMedia] = None,
                id_short: Optional[str] = r"DetailedInformation",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI789#001/0173-1#01-AHX445#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={
                            r"de": r"Detailinformationen zum Servicebedarf",
                            r"en": r"Detailed information of service need",
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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

        class OnsiteContact(aas.SubmodelElementCollection):

            class PartnerNumber(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PartnerNumber",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI771#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Partnernummer", r"en": r"Partner number"}
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

            class NumberOfContacts(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"NumberOfContacts",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAO203#004"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Anzahl der Kontakte", r"en": r"Number of contacts "}
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

            class ContactInformation(aas.SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"ContactInformation",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAQ837#007/0173-1#01-ADR448#007"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"de": r"Kontaktinformationen", r"en": r"Contact information"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required"
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements()

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
                contactInformation: Iterable[ContactInformation],
                partnerNumber: Optional[Union[str, PartnerNumber]] = None,
                numberOfContacts: Optional[Union[int, NumberOfContacts]] = None,
                id_short: Optional[str] = r"OnsiteContact",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI793#001/0173-1#01-AHX449#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"de": r"Ansprechpartner vor Ort", r"en": r"Onsite contact"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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
            reportedBy: ReportedBy,
            status: Union[str, Status],
            priority: Union[str, Priority],
            relatedAsset: RelatedAsset,
            shortText: Union[aas.LangStringSet, ShortText],
            serviceType: Union[str, ServiceType],
            serviceRequestNotificationId: Optional[Union[str, ServiceRequestNotificationId]] = None,
            detailedInformation: Optional[DetailedInformation] = None,
            onsiteContact: Optional[OnsiteContact] = None,
            id_short: Optional[str] = r"ServiceRequestNotification",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI788#001/0173-1#01-AHX444#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"de": r"Servicebedarfsmeldung", r"en": r"Service request notification"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

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
        numberOfServiceRequestNotifications: Optional[Union[int, NumberOfServiceRequestNotifications]] = None,
        serviceRequestNotification: Optional[Iterable[ServiceRequestNotification]] = None,
        id_short: Optional[str] = r"ServiceRequestNotification",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AHX443#001"),),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"This submodel aims to standardize the description of a service request notification that can be used to create a service request notification for industrial assets or the asset creates it by itself."
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
