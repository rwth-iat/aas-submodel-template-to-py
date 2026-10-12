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


class InspectionDocumentsOfSteelProducts(aas.Submodel):

    class Manufacturer(aas.SubmodelElementCollection):

        class CompanyName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CompanyName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Firmenname", r"en": r"Company Name"}),
                    "semantic_id": global_ref(r"0173-1#02-AAO677#003"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Street(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Street",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Straße", r"en": r"Street"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL858#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ZIPCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ZIPCode",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Postleitzahl", r"en": r"ZIP Code"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL861#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class City(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"City",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Stadt", r"en": r"City"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL860#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NationalCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NationalCode",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Ländercode", r"en": r"National Code"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL863#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MailAddress(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MailAddress",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Mailadresse", r"en": r"Mail Address"}),
                    "semantic_id": global_ref(r"0173-1#07-ABA042#003"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Manufacturer",
                "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Hersteller", r"en": r"Manufacturer"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/Manufacturer/1/0"
                ),
            }

        def __init__(
            self,
            companyName: Union[str, CompanyName],
            street: Union[str, Street],
            zIPCode: Union[str, ZIPCode],
            city: Union[str, City],
            nationalCode: Union[str, NationalCode],
            mailAddress: Optional[Iterable[Union[str, MailAddress]]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if companyName is not None and not isinstance(companyName, aas.SubmodelElement):
                companyName = self.CompanyName(companyName)

            # Build a submodel element if a raw value was passed in the argument

            if street is not None and not isinstance(street, aas.SubmodelElement):
                street = self.Street(street)

            # Build a submodel element if a raw value was passed in the argument

            if zIPCode is not None and not isinstance(zIPCode, aas.SubmodelElement):
                zIPCode = self.ZIPCode(zIPCode)

            # Build a submodel element if a raw value was passed in the argument

            if city is not None and not isinstance(city, aas.SubmodelElement):
                city = self.City(city)

            # Build a submodel element if a raw value was passed in the argument

            if nationalCode is not None and not isinstance(nationalCode, aas.SubmodelElement):
                nationalCode = self.NationalCode(nationalCode)

            # A str would be split into its characters
            if isinstance(mailAddress, str):
                raise TypeError("mailAddress takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if mailAddress:
                mailAddress = [i if isinstance(i, aas.SubmodelElement) else self.MailAddress(i) for i in mailAddress]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                companyName, street, zIPCode, city, nationalCode, mailAddress
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Customer(aas.SubmodelElementCollection):

        class CompanyName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CompanyName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Firmenname", r"en": r"Company Name"}),
                    "semantic_id": global_ref(r"0173-1#02-AAO677#003"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CustomerRole(aas.Property):

            ALLOWED_VALUES = (r"Purchaser", r"Consignee", r"ConsigneeOfCertificate")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CustomerRole",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Kundenrolle", r"en": r"Customer Role"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/CustomerRole/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Street(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Street",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Straße", r"en": r"Street"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL858#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ZIPCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ZIPCode",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Postleitzahl", r"en": r"ZIP Code"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL861#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class City(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"City",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Stadt", r"en": r"City"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL860#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NationalCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NationalCode",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Ländercode", r"en": r"National Code"}),
                    "semantic_id": global_ref(r"0173-1#07-ABL863#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MailAddress(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MailAddress",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Mailadresse", r"en": r"Mail Address"}),
                    "semantic_id": global_ref(r"0173-1#07-ABA042#003"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Customer",
                "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Kunde", r"en": r"Customer"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/Customer/1/0"
                ),
            }

        def __init__(
            self,
            companyName: Union[str, CompanyName],
            street: Iterable[Union[str, Street]],
            zIPCode: Union[str, ZIPCode],
            city: Union[str, City],
            nationalCode: Union[str, NationalCode],
            customerRole: Optional[Iterable[Union[str, CustomerRole]]] = None,
            mailAddress: Optional[Iterable[Union[str, MailAddress]]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if companyName is not None and not isinstance(companyName, aas.SubmodelElement):
                companyName = self.CompanyName(companyName)

            # A str would be split into its characters
            if isinstance(customerRole, str):
                raise TypeError("customerRole takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if customerRole:
                customerRole = [i if isinstance(i, aas.SubmodelElement) else self.CustomerRole(i) for i in customerRole]

            # A str would be split into its characters
            if isinstance(street, str):
                raise TypeError("street takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if street:
                street = [i if isinstance(i, aas.SubmodelElement) else self.Street(i) for i in street]

            # Build a submodel element if a raw value was passed in the argument

            if zIPCode is not None and not isinstance(zIPCode, aas.SubmodelElement):
                zIPCode = self.ZIPCode(zIPCode)

            # Build a submodel element if a raw value was passed in the argument

            if city is not None and not isinstance(city, aas.SubmodelElement):
                city = self.City(city)

            # Build a submodel element if a raw value was passed in the argument

            if nationalCode is not None and not isinstance(nationalCode, aas.SubmodelElement):
                nationalCode = self.NationalCode(nationalCode)

            # A str would be split into its characters
            if isinstance(mailAddress, str):
                raise TypeError("mailAddress takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if mailAddress:
                mailAddress = [i if isinstance(i, aas.SubmodelElement) else self.MailAddress(i) for i in mailAddress]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                companyName, customerRole, street, zIPCode, city, nationalCode, mailAddress
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class OrderData(aas.SubmodelElementCollection):

        class TypeOfInspectionDocument(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TypeOfInspectionDocument",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"de": r"Art der Prüfbescheinigung (DIN EN 10204)",
                            r"en": r"Type Of Inspection Document (EN 10204)",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/KindOfInspectionDocument/1/0"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-AAZ530#003"),),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class OrderDate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"OrderDate",
                    "value_type": xsd.Date,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Auftragsdatum", r"en": r"Order Date"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/OrderDate/1/0"
                    ),
                }

            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ManufacturerOrderNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerOrderNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Werkauftragsnummer", r"en": r"Manufacturer Order Number"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/ManufacturerOrderNumber/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PurchaserOrderNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PurchaserOrderNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Kundenbestellnummer", r"en": r"Purchaser Order Number"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABF517#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DeliveryNoteNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DeliveryNoteNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Lieferscheinnummer", r"en": r"Delivery Note Number"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/DeliveryNoteNumber/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"OrderData",
                "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Auftragsdaten", r"en": r"Order Data"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/OrderData/1/0"
                ),
            }

        def __init__(
            self,
            typeOfInspectionDocument: Union[str, TypeOfInspectionDocument],
            orderDate: Union[xsd.Date, OrderDate],
            manufacturerOrderNumber: Optional[Union[str, ManufacturerOrderNumber]] = None,
            purchaserOrderNumber: Optional[Union[str, PurchaserOrderNumber]] = None,
            deliveryNoteNumber: Optional[Union[str, DeliveryNoteNumber]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if typeOfInspectionDocument is not None and not isinstance(typeOfInspectionDocument, aas.SubmodelElement):
                typeOfInspectionDocument = self.TypeOfInspectionDocument(typeOfInspectionDocument)

            # Build a submodel element if a raw value was passed in the argument

            if orderDate is not None and not isinstance(orderDate, aas.SubmodelElement):
                orderDate = self.OrderDate(orderDate)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerOrderNumber is not None and not isinstance(manufacturerOrderNumber, aas.SubmodelElement):
                manufacturerOrderNumber = self.ManufacturerOrderNumber(manufacturerOrderNumber)

            # Build a submodel element if a raw value was passed in the argument

            if purchaserOrderNumber is not None and not isinstance(purchaserOrderNumber, aas.SubmodelElement):
                purchaserOrderNumber = self.PurchaserOrderNumber(purchaserOrderNumber)

            # Build a submodel element if a raw value was passed in the argument

            if deliveryNoteNumber is not None and not isinstance(deliveryNoteNumber, aas.SubmodelElement):
                deliveryNoteNumber = self.DeliveryNoteNumber(deliveryNoteNumber)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                typeOfInspectionDocument, orderDate, manufacturerOrderNumber, purchaserOrderNumber, deliveryNoteNumber
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ProductData(aas.SubmodelElementCollection):

        class ManufacturerProductNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerProductNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Produktnummer des Herstellers", r"en": r"Manufacturer Product Number"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAO689#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PurchaserArticleNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PurchaserArticleNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Artikelnummer des Kunden", r"en": r"Purchaser Article Number"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/PurchaserArticleNumber/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductDescription(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"ProductDescription",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Erzeugnisbeschreibung", r"en": r"Product Description"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAU734#002"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AdditionalProductRequirements(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"AdditionalProductRequirements",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Zusätzliche Produktanforderungen", r"en": r"Additional Product Requirements"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/AdditionalProductRequirements/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BatchNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"BatchNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Chargennummer", r"en": r"Batch Number"}),
                    "semantic_id": global_ref(r"0173-1#02-AAQ196#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaterialNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaterialNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Werkstoffnummer", r"en": r"Material Number"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAZ538#003"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaterialShortName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaterialShortName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Materialkurzname", r"en": r"Material Short Name"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAZ536#003"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaterialAdditionalInformation(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"MaterialAdditionalInformation",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"de": r"Zusätzliche Informationen zum Material",
                            r"en": r"Material Additional Information",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MaterialAdditionalInformation/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NumberOfPieces(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfPieces",
                    "value_type": xsd.PositiveInteger,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Stückzahl", r"en": r"Number of Pieces"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NumberOfPieces/1/0"
                    ),
                }

            def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TheoreticalMass(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TheoreticalMass",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Theoretische Masse", r"en": r"Theoretical Mass"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TheoreticalMass/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ActualMass(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ActualMass",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Ist-Masse", r"en": r"Actual Mass"}),
                    "semantic_id": global_ref(r"0173-1#02-AAZ533#002"),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SemiFinishedProductSpecification(aas.SubmodelElementCollection):

            class Tube(aas.SubmodelElementCollection):

                class WallThickness(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"WallThickness",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Wandstärke", r"en": r"Wall Thickness"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-BAG269#006"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class OuterDiameter(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"OuterDiameter",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Außendurchmesser", r"en": r"Outer Diameter"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABG720#002"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Length(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Length",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Länge", r"en": r"Length"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA018#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StandardReference(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"StandardReference",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Normreferenz", r"en": r"Standard Reference"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ523#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Tube",
                        "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Rohr", r"en": r"Tube"}),
                        "semantic_id": global_ref(r"0173-1#01-AGU746#002"),
                    }

                def __init__(
                    self,
                    wallThickness: Union[xsd.Float, WallThickness],
                    outerDiameter: Union[xsd.Float, OuterDiameter],
                    length: Union[xsd.Float, Length],
                    standardReference: Optional[Iterable[Union[str, StandardReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if wallThickness is not None and not isinstance(wallThickness, aas.SubmodelElement):
                        wallThickness = self.WallThickness(wallThickness)

                    # Build a submodel element if a raw value was passed in the argument

                    if outerDiameter is not None and not isinstance(outerDiameter, aas.SubmodelElement):
                        outerDiameter = self.OuterDiameter(outerDiameter)

                    # Build a submodel element if a raw value was passed in the argument

                    if length is not None and not isinstance(length, aas.SubmodelElement):
                        length = self.Length(length)

                    # A str would be split into its characters
                    if isinstance(standardReference, str):
                        raise TypeError("standardReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if standardReference:
                        standardReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.StandardReference(i)
                            for i in standardReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        wallThickness, outerDiameter, length, standardReference
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class RectangularTube(aas.SubmodelElementCollection):

                class WallThickness(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"WallThickness",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Wandstärke", r"en": r"Wall Thickness"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-BAG269#006"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Height(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Height",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Höhe", r"en": r"Height"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA020#011"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Width(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Width",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Breite", r"en": r"Width"}),
                            "semantic_id": global_ref(r"0173-1#02-BAF016#007"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Length(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Length",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Länge", r"en": r"Length"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA018#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StandardReference(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"StandardReference",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Normreferenz", r"en": r"Standard Reference"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ523#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"RectangularTube",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Rechteckrohr", r"en": r"Rectangular Tube"}
                        ),
                        "semantic_id": global_ref(r"0173-1#01-AGV504#005"),
                    }

                def __init__(
                    self,
                    wallThickness: Union[xsd.Float, WallThickness],
                    height: Union[xsd.Float, Height],
                    width: Union[xsd.Float, Width],
                    length: Union[xsd.Float, Length],
                    standardReference: Optional[Iterable[Union[str, StandardReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if wallThickness is not None and not isinstance(wallThickness, aas.SubmodelElement):
                        wallThickness = self.WallThickness(wallThickness)

                    # Build a submodel element if a raw value was passed in the argument

                    if height is not None and not isinstance(height, aas.SubmodelElement):
                        height = self.Height(height)

                    # Build a submodel element if a raw value was passed in the argument

                    if width is not None and not isinstance(width, aas.SubmodelElement):
                        width = self.Width(width)

                    # Build a submodel element if a raw value was passed in the argument

                    if length is not None and not isinstance(length, aas.SubmodelElement):
                        length = self.Length(length)

                    # A str would be split into its characters
                    if isinstance(standardReference, str):
                        raise TypeError("standardReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if standardReference:
                        standardReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.StandardReference(i)
                            for i in standardReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        wallThickness, height, width, length, standardReference
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class RoundBar(aas.SubmodelElementCollection):

                class OuterDiameter(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"OuterDiameter",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Außendurchmesser", r"en": r"Outer Diameter"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABG720#002"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Length(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Length",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Länge", r"en": r"Length"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA018#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StandardReference(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"StandardReference",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Normreferenz", r"en": r"Standard Reference"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ523#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"RoundBar",
                        "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Rundstahl", r"en": r"Round Bar"}),
                        "semantic_id": global_ref(r"0173-1#01-AGV490#005"),
                    }

                def __init__(
                    self,
                    outerDiameter: Union[xsd.Float, OuterDiameter],
                    length: Union[xsd.Float, Length],
                    standardReference: Optional[Iterable[Union[str, StandardReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if outerDiameter is not None and not isinstance(outerDiameter, aas.SubmodelElement):
                        outerDiameter = self.OuterDiameter(outerDiameter)

                    # Build a submodel element if a raw value was passed in the argument

                    if length is not None and not isinstance(length, aas.SubmodelElement):
                        length = self.Length(length)

                    # A str would be split into its characters
                    if isinstance(standardReference, str):
                        raise TypeError("standardReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if standardReference:
                        standardReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.StandardReference(i)
                            for i in standardReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(outerDiameter, length, standardReference)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class HexagonalBar(aas.SubmodelElementCollection):

                class WidthAcrossFlats(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"WidthAcrossFlats",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Schlüsselweite", r"en": r"Width Across Flats"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAA103#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Length(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Length",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Länge", r"en": r"Length"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA018#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StandardReference(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"StandardReference",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Normreferenz", r"en": r"Standard Reference"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ523#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"HexagonalBar",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Sechskantstahl", r"en": r"Hexagonal Bar"}
                        ),
                        "semantic_id": global_ref(r"0173-1#01-AGV493#005"),
                    }

                def __init__(
                    self,
                    widthAcrossFlats: Union[xsd.Float, WidthAcrossFlats],
                    length: Union[xsd.Float, Length],
                    standardReference: Optional[Iterable[Union[str, StandardReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if widthAcrossFlats is not None and not isinstance(widthAcrossFlats, aas.SubmodelElement):
                        widthAcrossFlats = self.WidthAcrossFlats(widthAcrossFlats)

                    # Build a submodel element if a raw value was passed in the argument

                    if length is not None and not isinstance(length, aas.SubmodelElement):
                        length = self.Length(length)

                    # A str would be split into its characters
                    if isinstance(standardReference, str):
                        raise TypeError("standardReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if standardReference:
                        standardReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.StandardReference(i)
                            for i in standardReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(widthAcrossFlats, length, standardReference)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class RectangularBar(aas.SubmodelElementCollection):

                class Height(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Height",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Höhe", r"en": r"Height"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA020#011"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Width(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Width",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Breite", r"en": r"Width"}),
                            "semantic_id": global_ref(r"0173-1#02-BAF016#007"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Length(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Length",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Länge", r"en": r"Length"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA018#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StandardReference(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"StandardReference",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Normreferenz", r"en": r"Standard Reference"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ523#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"RectangularBar",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Rechteckstab", r"en": r"RectangularBar"}
                        ),
                        "semantic_id": global_ref(r"0173-1#01-AGV492#005"),
                    }

                def __init__(
                    self,
                    height: Union[xsd.Float, Height],
                    width: Union[xsd.Float, Width],
                    length: Union[xsd.Float, Length],
                    standardReference: Optional[Iterable[Union[str, StandardReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if height is not None and not isinstance(height, aas.SubmodelElement):
                        height = self.Height(height)

                    # Build a submodel element if a raw value was passed in the argument

                    if width is not None and not isinstance(width, aas.SubmodelElement):
                        width = self.Width(width)

                    # Build a submodel element if a raw value was passed in the argument

                    if length is not None and not isinstance(length, aas.SubmodelElement):
                        length = self.Length(length)

                    # A str would be split into its characters
                    if isinstance(standardReference, str):
                        raise TypeError("standardReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if standardReference:
                        standardReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.StandardReference(i)
                            for i in standardReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(height, width, length, standardReference)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SheetMetal(aas.SubmodelElementCollection):

                class Thickness(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Thickness",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Dicke", r"en": r"Thickness"}),
                            "semantic_id": global_ref(r"0173-1#02-AAV127#003"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Width(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Width",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Breite", r"en": r"Width"}),
                            "semantic_id": global_ref(r"0173-1#02-BAF016#007"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Length(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Length",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Länge", r"en": r"Length"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA018#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StandardReference(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"StandardReference",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Normreferenz", r"en": r"Standard Reference"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ523#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"SheetMetal",
                        "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Metallblech", r"en": r"Sheet Metal"}),
                        "semantic_id": global_ref(r"0173-1#01-AGU743#002"),
                    }

                def __init__(
                    self,
                    thickness: Union[xsd.Float, Thickness],
                    width: Union[xsd.Float, Width],
                    length: Union[xsd.Float, Length],
                    standardReference: Optional[Iterable[Union[str, StandardReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if thickness is not None and not isinstance(thickness, aas.SubmodelElement):
                        thickness = self.Thickness(thickness)

                    # Build a submodel element if a raw value was passed in the argument

                    if width is not None and not isinstance(width, aas.SubmodelElement):
                        width = self.Width(width)

                    # Build a submodel element if a raw value was passed in the argument

                    if length is not None and not isinstance(length, aas.SubmodelElement):
                        length = self.Length(length)

                    # A str would be split into its characters
                    if isinstance(standardReference, str):
                        raise TypeError("standardReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if standardReference:
                        standardReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.StandardReference(i)
                            for i in standardReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(thickness, width, length, standardReference)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Profile(aas.SubmodelElementCollection):

                class ProfileSpecification(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ProfileSpecification",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Profilbezeichnung", r"en": r"Profile Specification"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ528#005"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Height(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Height",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Höhe", r"en": r"Height"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA020#011"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Width(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Width",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Breite", r"en": r"Width"}),
                            "semantic_id": global_ref(r"0173-1#02-BAF016#007"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Length(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Length",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Länge", r"en": r"Length"}),
                            "semantic_id": global_ref(r"0173-1#02-BAA018#008"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class StandardReference(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"StandardReference",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"de": r"Normreferenz", r"en": r"Standard Reference"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAZ523#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Profile",
                        "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Profil", r"en": r"Profile"}),
                        "semantic_id": global_ref(r"0173-1#01-AGU744#002"),
                    }

                def __init__(
                    self,
                    profileSpecification: Union[str, ProfileSpecification],
                    height: Optional[Union[xsd.Float, Height]] = None,
                    width: Optional[Union[xsd.Float, Width]] = None,
                    length: Optional[Union[xsd.Float, Length]] = None,
                    standardReference: Optional[Iterable[Union[str, StandardReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if profileSpecification is not None and not isinstance(profileSpecification, aas.SubmodelElement):
                        profileSpecification = self.ProfileSpecification(profileSpecification)

                    # Build a submodel element if a raw value was passed in the argument

                    if height is not None and not isinstance(height, aas.SubmodelElement):
                        height = self.Height(height)

                    # Build a submodel element if a raw value was passed in the argument

                    if width is not None and not isinstance(width, aas.SubmodelElement):
                        width = self.Width(width)

                    # Build a submodel element if a raw value was passed in the argument

                    if length is not None and not isinstance(length, aas.SubmodelElement):
                        length = self.Length(length)

                    # A str would be split into its characters
                    if isinstance(standardReference, str):
                        raise TypeError("standardReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if standardReference:
                        standardReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.StandardReference(i)
                            for i in standardReference
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        profileSpecification, height, width, length, standardReference
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"SemiFinishedProductSpecification",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Halbzeugspezifikation", r"en": r"Specification of semi-finished Product"}
                    ),
                    "semantic_id": global_ref(r"0173-1#01-AGO030#002"),
                }

            def __init__(
                self,
                tube: Optional[Tube] = None,
                rectangularTube: Optional[RectangularTube] = None,
                roundBar: Optional[RoundBar] = None,
                hexagonalBar: Optional[HexagonalBar] = None,
                rectangularBar: Optional[RectangularBar] = None,
                sheetMetal: Optional[SheetMetal] = None,
                profile: Optional[Profile] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                if (
                    sum(
                        arg is not None
                        for arg in (tube, rectangularTube, roundBar, hexagonalBar, rectangularBar, sheetMetal, profile)
                    )
                    > 1
                ):
                    raise ValueError(
                        "Only one of tube, rectangularTube, roundBar, hexagonalBar, rectangularBar, sheetMetal, profile may be given (SMT/EitherOr 'SemiFinishedProductSpecification')"
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    tube, rectangularTube, roundBar, hexagonalBar, rectangularBar, sheetMetal, profile
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Drawing(aas.Blob):

            @staticmethod
            def template_defaults() -> BlobMetadata:
                return {
                    "id_short": r"Drawing",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Zeichnung", r"en": r"Drawing"}),
                    "semantic_id": global_ref(r"0173-1#02-AAQ318#002"),
                }

            def __init__(
                self,
                value: Optional[bytes] = None,
                content_type: Optional[str] = r"application/pdf",
                **kwargs: Unpack[BlobMetadata],
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ProductData",
                "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Produktdaten", r"en": r"Product Data"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/ProductData/1/0"
                ),
            }

        def __init__(
            self,
            manufacturerProductNumber: Optional[Union[str, ManufacturerProductNumber]] = None,
            purchaserArticleNumber: Optional[Union[str, PurchaserArticleNumber]] = None,
            productDescription: Optional[Union[aas.MultiLanguageTextType, ProductDescription]] = None,
            additionalProductRequirements: Optional[
                Union[aas.MultiLanguageTextType, AdditionalProductRequirements]
            ] = None,
            batchNumber: Optional[Union[str, BatchNumber]] = None,
            materialNumber: Optional[Union[str, MaterialNumber]] = None,
            materialShortName: Optional[Union[str, MaterialShortName]] = None,
            materialAdditionalInformation: Optional[
                Union[aas.MultiLanguageTextType, MaterialAdditionalInformation]
            ] = None,
            numberOfPieces: Optional[Union[xsd.PositiveInteger, NumberOfPieces]] = None,
            theoreticalMass: Optional[Union[xsd.Float, TheoreticalMass]] = None,
            actualMass: Optional[Union[xsd.Float, ActualMass]] = None,
            semiFinishedProductSpecification: Optional[SemiFinishedProductSpecification] = None,
            drawing: Optional[Iterable[Drawing]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerProductNumber is not None and not isinstance(manufacturerProductNumber, aas.SubmodelElement):
                manufacturerProductNumber = self.ManufacturerProductNumber(manufacturerProductNumber)

            # Build a submodel element if a raw value was passed in the argument

            if purchaserArticleNumber is not None and not isinstance(purchaserArticleNumber, aas.SubmodelElement):
                purchaserArticleNumber = self.PurchaserArticleNumber(purchaserArticleNumber)

            # Build a submodel element if a raw value was passed in the argument

            if productDescription is not None and not isinstance(productDescription, aas.SubmodelElement):
                productDescription = self.ProductDescription(productDescription)

            # Build a submodel element if a raw value was passed in the argument

            if additionalProductRequirements is not None and not isinstance(
                additionalProductRequirements, aas.SubmodelElement
            ):
                additionalProductRequirements = self.AdditionalProductRequirements(additionalProductRequirements)

            # Build a submodel element if a raw value was passed in the argument

            if batchNumber is not None and not isinstance(batchNumber, aas.SubmodelElement):
                batchNumber = self.BatchNumber(batchNumber)

            # Build a submodel element if a raw value was passed in the argument

            if materialNumber is not None and not isinstance(materialNumber, aas.SubmodelElement):
                materialNumber = self.MaterialNumber(materialNumber)

            # Build a submodel element if a raw value was passed in the argument

            if materialShortName is not None and not isinstance(materialShortName, aas.SubmodelElement):
                materialShortName = self.MaterialShortName(materialShortName)

            # Build a submodel element if a raw value was passed in the argument

            if materialAdditionalInformation is not None and not isinstance(
                materialAdditionalInformation, aas.SubmodelElement
            ):
                materialAdditionalInformation = self.MaterialAdditionalInformation(materialAdditionalInformation)

            # Build a submodel element if a raw value was passed in the argument

            if numberOfPieces is not None and not isinstance(numberOfPieces, aas.SubmodelElement):
                numberOfPieces = self.NumberOfPieces(numberOfPieces)

            # Build a submodel element if a raw value was passed in the argument

            if theoreticalMass is not None and not isinstance(theoreticalMass, aas.SubmodelElement):
                theoreticalMass = self.TheoreticalMass(theoreticalMass)

            # Build a submodel element if a raw value was passed in the argument

            if actualMass is not None and not isinstance(actualMass, aas.SubmodelElement):
                actualMass = self.ActualMass(actualMass)

            # A str would be split into its characters
            if isinstance(drawing, str):
                raise TypeError("drawing takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                manufacturerProductNumber,
                purchaserArticleNumber,
                productDescription,
                additionalProductRequirements,
                batchNumber,
                materialNumber,
                materialShortName,
                materialAdditionalInformation,
                numberOfPieces,
                theoreticalMass,
                actualMass,
                semiFinishedProductSpecification,
                drawing,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MechanicalTests(aas.SubmodelElementCollection):

        class TensileTest(aas.SubmodelElementCollection):

            class YieldOrProofStrengthMean(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"YieldOrProofStrengthMean",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Streck- oder Dehngrenze Mittelwert", r"en": r"Yield or Proof Strength Mean"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/YieldOrProofStrengthMean/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TensileStrengthMean(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TensileStrengthMean",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Zugfestigkeit Mittelwert", r"en": r"Tensile Strength Mean"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TensileStrengthMean/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ElongationAfterFractureMean(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ElongationAfterFractureMean",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Bruchdehnung Mittelwert", r"en": r"Elongation after Fracture Mean"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/ElongationAfterFractureMean/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class YieldOrProofStrengthIndividualValues(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"YieldOrProofStrengthIndividualValues",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/YieldOrProofStrengthInidivualValues/1/0"
                        ),
                        "value_type_list_element": xsd.Float,
                        "order_relevant": False,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Streck- oder Dehngrenze Einzelwerte",
                                r"en": r"Yield or Proof Strength Individual Values",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/YieldOrProofStrengthInidivualValues/1/0"
                        ),
                    }

                def __init__(
                    self,
                    yieldorproofstrengthindividualvalues_items: Optional[
                        Iterable[Union[xsd.Float, aas.Property]]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(yieldorproofstrengthindividualvalues_items, str):
                        raise TypeError("yieldorproofstrengthindividualvalues_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if yieldorproofstrengthindividualvalues_items:
                        yieldorproofstrengthindividualvalues_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else aas.Property(None, kwargs.get("value_type_list_element", xsd.Float), i)
                            )
                            for i in yieldorproofstrengthindividualvalues_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        yieldorproofstrengthindividualvalues_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TensileStrengthIndividualValues(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"TensileStrengthIndividualValues",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TensileStrengthIndividualValues/1/0"
                        ),
                        "value_type_list_element": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Zugfestigkeit Einzelwerte", r"en": r"Tensile Strength Individual Values"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TensileStrengthIndividualValues/1/0"
                        ),
                    }

                def __init__(
                    self,
                    tensilestrengthindividualvalues_items: Optional[Iterable[Union[xsd.Float, aas.Property]]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(tensilestrengthindividualvalues_items, str):
                        raise TypeError("tensilestrengthindividualvalues_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if tensilestrengthindividualvalues_items:
                        tensilestrengthindividualvalues_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else aas.Property(None, kwargs.get("value_type_list_element", xsd.Float), i)
                            )
                            for i in tensilestrengthindividualvalues_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tensilestrengthindividualvalues_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ElongationAfterFractureIndividualValues(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"ElongationAfterFractureIndividualValues",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/ElongationAfterFractureIndividualValues/1/0"
                        ),
                        "value_type_list_element": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Bruchdehnung Einzelwerte",
                                r"en": r"Elongation after Fracture Individual Values",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/ElongationAfterFractureIndividualValues/1/0"
                        ),
                    }

                def __init__(
                    self,
                    elongationafterfractureindividualvalues_items: Optional[
                        Iterable[Union[xsd.Float, aas.Property]]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(elongationafterfractureindividualvalues_items, str):
                        raise TypeError(
                            "elongationafterfractureindividualvalues_items takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if elongationafterfractureindividualvalues_items:
                        elongationafterfractureindividualvalues_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else aas.Property(None, kwargs.get("value_type_list_element", xsd.Float), i)
                            )
                            for i in elongationafterfractureindividualvalues_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        elongationafterfractureindividualvalues_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TestTemperature(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestTemperature",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Prüftemperatur", r"en": r"Test Temperature"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TestTemperature/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SampleShape(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"SampleShape",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Probenform", r"en": r"Shape of the Test Piece"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/SampleShape/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LocationOfSample(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"LocationOfSample",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Lage des Probenabschnittes", r"en": r"Location of the Sample"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/LocationOfSample/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DirectionOfSample(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"DirectionOfSample",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Probenrichtung", r"en": r"Direction of the Sample"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/DirectionOfSample/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"TensileTest",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Zugversuch", r"en": r"Tensile Test"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TensileTest/1/0"
                    ),
                }

            def __init__(
                self,
                yieldOrProofStrengthMean: Optional[Union[xsd.Float, YieldOrProofStrengthMean]] = None,
                tensileStrengthMean: Optional[Union[xsd.Float, TensileStrengthMean]] = None,
                elongationAfterFractureMean: Optional[Union[xsd.Float, ElongationAfterFractureMean]] = None,
                yieldOrProofStrengthIndividualValues: Optional[
                    Union[Iterable[Union[xsd.Float, aas.Property]], YieldOrProofStrengthIndividualValues]
                ] = None,
                tensileStrengthIndividualValues: Optional[
                    Union[Iterable[Union[xsd.Float, aas.Property]], TensileStrengthIndividualValues]
                ] = None,
                elongationAfterFractureIndividualValues: Optional[
                    Union[Iterable[Union[xsd.Float, aas.Property]], ElongationAfterFractureIndividualValues]
                ] = None,
                testTemperature: Optional[Union[xsd.Float, TestTemperature]] = None,
                sampleShape: Optional[Union[aas.MultiLanguageTextType, SampleShape]] = None,
                locationOfSample: Optional[Iterable[Union[aas.MultiLanguageTextType, LocationOfSample]]] = None,
                directionOfSample: Optional[Iterable[Union[aas.MultiLanguageTextType, DirectionOfSample]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if yieldOrProofStrengthMean is not None and not isinstance(
                    yieldOrProofStrengthMean, aas.SubmodelElement
                ):
                    yieldOrProofStrengthMean = self.YieldOrProofStrengthMean(yieldOrProofStrengthMean)

                # Build a submodel element if a raw value was passed in the argument

                if tensileStrengthMean is not None and not isinstance(tensileStrengthMean, aas.SubmodelElement):
                    tensileStrengthMean = self.TensileStrengthMean(tensileStrengthMean)

                # Build a submodel element if a raw value was passed in the argument

                if elongationAfterFractureMean is not None and not isinstance(
                    elongationAfterFractureMean, aas.SubmodelElement
                ):
                    elongationAfterFractureMean = self.ElongationAfterFractureMean(elongationAfterFractureMean)

                # A str would be split into its characters
                if isinstance(yieldOrProofStrengthIndividualValues, str):
                    raise TypeError("yieldOrProofStrengthIndividualValues takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if yieldOrProofStrengthIndividualValues is not None and not isinstance(
                    yieldOrProofStrengthIndividualValues, aas.SubmodelElement
                ):
                    yieldOrProofStrengthIndividualValues = self.YieldOrProofStrengthIndividualValues(
                        yieldOrProofStrengthIndividualValues
                    )

                # A str would be split into its characters
                if isinstance(tensileStrengthIndividualValues, str):
                    raise TypeError("tensileStrengthIndividualValues takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if tensileStrengthIndividualValues is not None and not isinstance(
                    tensileStrengthIndividualValues, aas.SubmodelElement
                ):
                    tensileStrengthIndividualValues = self.TensileStrengthIndividualValues(
                        tensileStrengthIndividualValues
                    )

                # A str would be split into its characters
                if isinstance(elongationAfterFractureIndividualValues, str):
                    raise TypeError("elongationAfterFractureIndividualValues takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if elongationAfterFractureIndividualValues is not None and not isinstance(
                    elongationAfterFractureIndividualValues, aas.SubmodelElement
                ):
                    elongationAfterFractureIndividualValues = self.ElongationAfterFractureIndividualValues(
                        elongationAfterFractureIndividualValues
                    )

                # Build a submodel element if a raw value was passed in the argument

                if testTemperature is not None and not isinstance(testTemperature, aas.SubmodelElement):
                    testTemperature = self.TestTemperature(testTemperature)

                # Build a submodel element if a raw value was passed in the argument

                if sampleShape is not None and not isinstance(sampleShape, aas.SubmodelElement):
                    sampleShape = self.SampleShape(sampleShape)

                # A str would be split into its characters
                if isinstance(locationOfSample, str):
                    raise TypeError("locationOfSample takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if locationOfSample:
                    locationOfSample = [
                        i if isinstance(i, aas.SubmodelElement) else self.LocationOfSample(i) for i in locationOfSample
                    ]

                # A str would be split into its characters
                if isinstance(directionOfSample, str):
                    raise TypeError("directionOfSample takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if directionOfSample:
                    directionOfSample = [
                        i if isinstance(i, aas.SubmodelElement) else self.DirectionOfSample(i)
                        for i in directionOfSample
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    yieldOrProofStrengthMean,
                    tensileStrengthMean,
                    elongationAfterFractureMean,
                    yieldOrProofStrengthIndividualValues,
                    tensileStrengthIndividualValues,
                    elongationAfterFractureIndividualValues,
                    testTemperature,
                    sampleShape,
                    locationOfSample,
                    directionOfSample,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class HardnessTest(aas.SubmodelElementCollection):

            class HardnessTestingMethod(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"HardnessTestingMethod",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Härteprüfverfahren", r"en": r"Hardness Testing Method"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/HardnessTestingMethod/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HardnessMean(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"HardnessMean",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Härte Mittelwert", r"en": r"Hardness Mean"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/HardnessMean/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class HardnessIndividualValues(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"HardnessIndividualValues",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/HardnessIndividualValues/1/0"
                        ),
                        "value_type_list_element": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Härte Einzelwerte", r"en": r"Hardness Individual Values"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/HardnessIndividualValues/1/0"
                        ),
                    }

                def __init__(
                    self,
                    hardnessindividualvalues_items: Optional[Iterable[Union[str, aas.Property]]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(hardnessindividualvalues_items, str):
                        raise TypeError("hardnessindividualvalues_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if hardnessindividualvalues_items:
                        hardnessindividualvalues_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else aas.Property(None, kwargs.get("value_type_list_element", str), i)
                            )
                            for i in hardnessindividualvalues_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        hardnessindividualvalues_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TestTemperature(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestTemperature",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Prüftemperatur", r"en": r"Test Temperature"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TestTemperature/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LocationOfSample(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"LocationOfSample",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Lage des Probenabschnittes", r"en": r"Location of the Sample"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/LocationOfSample/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DirectionOfSample(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"DirectionOfSample",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Probenrichtung", r"en": r"Direction of the Sample"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/DirectionOfSample/1/0"
                        ),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"HardnessTest",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Härteprüfung", r"en": r"Hardness Test"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/HardnessTest/1/0"
                    ),
                }

            def __init__(
                self,
                hardnessTestingMethod: Optional[Union[str, HardnessTestingMethod]] = None,
                hardnessMean: Optional[Union[str, HardnessMean]] = None,
                hardnessIndividualValues: Optional[
                    Union[Iterable[Union[str, aas.Property]], HardnessIndividualValues]
                ] = None,
                testTemperature: Optional[Union[xsd.Float, TestTemperature]] = None,
                locationOfSample: Optional[Iterable[Union[aas.MultiLanguageTextType, LocationOfSample]]] = None,
                directionOfSample: Optional[Iterable[Union[aas.MultiLanguageTextType, DirectionOfSample]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if hardnessTestingMethod is not None and not isinstance(hardnessTestingMethod, aas.SubmodelElement):
                    hardnessTestingMethod = self.HardnessTestingMethod(hardnessTestingMethod)

                # Build a submodel element if a raw value was passed in the argument

                if hardnessMean is not None and not isinstance(hardnessMean, aas.SubmodelElement):
                    hardnessMean = self.HardnessMean(hardnessMean)

                # A str would be split into its characters
                if isinstance(hardnessIndividualValues, str):
                    raise TypeError("hardnessIndividualValues takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if hardnessIndividualValues is not None and not isinstance(
                    hardnessIndividualValues, aas.SubmodelElement
                ):
                    hardnessIndividualValues = self.HardnessIndividualValues(hardnessIndividualValues)

                # Build a submodel element if a raw value was passed in the argument

                if testTemperature is not None and not isinstance(testTemperature, aas.SubmodelElement):
                    testTemperature = self.TestTemperature(testTemperature)

                # A str would be split into its characters
                if isinstance(locationOfSample, str):
                    raise TypeError("locationOfSample takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if locationOfSample:
                    locationOfSample = [
                        i if isinstance(i, aas.SubmodelElement) else self.LocationOfSample(i) for i in locationOfSample
                    ]

                # A str would be split into its characters
                if isinstance(directionOfSample, str):
                    raise TypeError("directionOfSample takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if directionOfSample:
                    directionOfSample = [
                        i if isinstance(i, aas.SubmodelElement) else self.DirectionOfSample(i)
                        for i in directionOfSample
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    hardnessTestingMethod,
                    hardnessMean,
                    hardnessIndividualValues,
                    testTemperature,
                    locationOfSample,
                    directionOfSample,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class NotchImpactTest(aas.SubmodelElementCollection):

            class NotchImpactStrengthMean(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NotchImpactStrengthMean",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Kerbschlagzähigkeit Mittelwert", r"en": r"Notch Impact Strength Mean"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NotchImpactStrengthMean/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NotchImpactStrengthIndividualValues(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"NotchImpactStrengthIndividualValues",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NotchImpactStrengthIndividualValues/1/0"
                        ),
                        "value_type_list_element": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Kerbschlagzähigkeit Einzelwerte",
                                r"en": r"Notch Impact Strength Individual Values",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NotchImpactStrengthIndividualValues/1/0"
                        ),
                    }

                def __init__(
                    self,
                    notchimpactstrengthindividualvalues_items: Optional[
                        Iterable[Union[xsd.Float, aas.Property]]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(notchimpactstrengthindividualvalues_items, str):
                        raise TypeError("notchimpactstrengthindividualvalues_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if notchimpactstrengthindividualvalues_items:
                        notchimpactstrengthindividualvalues_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else aas.Property(None, kwargs.get("value_type_list_element", xsd.Float), i)
                            )
                            for i in notchimpactstrengthindividualvalues_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        notchimpactstrengthindividualvalues_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class NotchImpactWorkMean(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NotchImpactWorkMean",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Notch Impact Work Mean", r"de": r"Kerbschlagbiegearbeit Mittelwert"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NotchImpactWorkMean/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NotchImpactWorkIndividualValues(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"NotchImpactWorkIndividualValues",
                        "type_value_list_element": aas.Property,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NotchImpactWorkIndividualValues/1/0"
                        ),
                        "value_type_list_element": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"de": r"Kerbschlagbiegearbeit Einzelwerte",
                                r"en": r"Notch Impact Work Individual Values",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NotchImpactWorkIndividualValues/1/0"
                        ),
                    }

                def __init__(
                    self,
                    notchimpactworkindividualvalues_items: Optional[Iterable[Union[xsd.Float, aas.Property]]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(notchimpactworkindividualvalues_items, str):
                        raise TypeError("notchimpactworkindividualvalues_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if notchimpactworkindividualvalues_items:
                        notchimpactworkindividualvalues_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else aas.Property(None, kwargs.get("value_type_list_element", xsd.Float), i)
                            )
                            for i in notchimpactworkindividualvalues_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        notchimpactworkindividualvalues_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SampleType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SampleType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Probenform", r"en": r"Type of Test Piece"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/SampleType/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SampleWidth(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SampleWidth",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Probenbreite", r"en": r"Width of Test Piece"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/SampleWidth/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TestTemperature(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestTemperature",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Prüftemperatur", r"en": r"Test Temperature"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/TestTemperature/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LocationOfSample(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LocationOfSample",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Lage des Probenabschnittes", r"en": r"Location of the Sample"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/LocationOfSample/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DirectionOfSample(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DirectionOfSample",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"de": r"Probenrichtung", r"en": r"Direction of the Test Piece"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/DirectionOfSample/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"NotchImpactTest",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Kerbschlagbiegeversuch", r"en": r"Notch Impact Test"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/NotchImpactTest/1/0"
                    ),
                }

            def __init__(
                self,
                notchImpactStrengthMean: Optional[Union[xsd.Float, NotchImpactStrengthMean]] = None,
                notchImpactStrengthIndividualValues: Optional[
                    Union[Iterable[Union[xsd.Float, aas.Property]], NotchImpactStrengthIndividualValues]
                ] = None,
                notchImpactWorkMean: Optional[Union[str, NotchImpactWorkMean]] = None,
                notchImpactWorkIndividualValues: Optional[
                    Union[Iterable[Union[xsd.Float, aas.Property]], NotchImpactWorkIndividualValues]
                ] = None,
                sampleType: Optional[Union[str, SampleType]] = None,
                sampleWidth: Optional[Union[xsd.Float, SampleWidth]] = None,
                testTemperature: Optional[Union[xsd.Float, TestTemperature]] = None,
                locationOfSample: Optional[Iterable[Union[str, LocationOfSample]]] = None,
                directionOfSample: Optional[Iterable[Union[str, DirectionOfSample]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if notchImpactStrengthMean is not None and not isinstance(notchImpactStrengthMean, aas.SubmodelElement):
                    notchImpactStrengthMean = self.NotchImpactStrengthMean(notchImpactStrengthMean)

                # A str would be split into its characters
                if isinstance(notchImpactStrengthIndividualValues, str):
                    raise TypeError("notchImpactStrengthIndividualValues takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if notchImpactStrengthIndividualValues is not None and not isinstance(
                    notchImpactStrengthIndividualValues, aas.SubmodelElement
                ):
                    notchImpactStrengthIndividualValues = self.NotchImpactStrengthIndividualValues(
                        notchImpactStrengthIndividualValues
                    )

                # Build a submodel element if a raw value was passed in the argument

                if notchImpactWorkMean is not None and not isinstance(notchImpactWorkMean, aas.SubmodelElement):
                    notchImpactWorkMean = self.NotchImpactWorkMean(notchImpactWorkMean)

                # A str would be split into its characters
                if isinstance(notchImpactWorkIndividualValues, str):
                    raise TypeError("notchImpactWorkIndividualValues takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if notchImpactWorkIndividualValues is not None and not isinstance(
                    notchImpactWorkIndividualValues, aas.SubmodelElement
                ):
                    notchImpactWorkIndividualValues = self.NotchImpactWorkIndividualValues(
                        notchImpactWorkIndividualValues
                    )

                # Build a submodel element if a raw value was passed in the argument

                if sampleType is not None and not isinstance(sampleType, aas.SubmodelElement):
                    sampleType = self.SampleType(sampleType)

                # Build a submodel element if a raw value was passed in the argument

                if sampleWidth is not None and not isinstance(sampleWidth, aas.SubmodelElement):
                    sampleWidth = self.SampleWidth(sampleWidth)

                # Build a submodel element if a raw value was passed in the argument

                if testTemperature is not None and not isinstance(testTemperature, aas.SubmodelElement):
                    testTemperature = self.TestTemperature(testTemperature)

                # A str would be split into its characters
                if isinstance(locationOfSample, str):
                    raise TypeError("locationOfSample takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if locationOfSample:
                    locationOfSample = [
                        i if isinstance(i, aas.SubmodelElement) else self.LocationOfSample(i) for i in locationOfSample
                    ]

                # A str would be split into its characters
                if isinstance(directionOfSample, str):
                    raise TypeError("directionOfSample takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if directionOfSample:
                    directionOfSample = [
                        i if isinstance(i, aas.SubmodelElement) else self.DirectionOfSample(i)
                        for i in directionOfSample
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    notchImpactStrengthMean,
                    notchImpactStrengthIndividualValues,
                    notchImpactWorkMean,
                    notchImpactWorkIndividualValues,
                    sampleType,
                    sampleWidth,
                    testTemperature,
                    locationOfSample,
                    directionOfSample,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MechanicalTests",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Mechanische Prüfungen", r"en": r"Mechanical Tests"}
                ),
                "semantic_id": global_ref(r"0173-1#01-AKG420#020"),
            }

        def __init__(
            self,
            tensileTest: Optional[Iterable[TensileTest]] = None,
            hardnessTest: Optional[Iterable[HardnessTest]] = None,
            notchImpactTest: Optional[Iterable[NotchImpactTest]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(tensileTest, str):
                raise TypeError("tensileTest takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(hardnessTest, str):
                raise TypeError("hardnessTest takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(notchImpactTest, str):
                raise TypeError("notchImpactTest takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(tensileTest, hardnessTest, notchImpactTest)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ChemicalAnalysis(aas.SubmodelElementCollection):

        class MassFraction_Al(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Al",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Al", r"en": r"Mass Fraction Al"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Al/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Be(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Be",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Be", r"en": r"Mass Fraction Be"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Be/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_C(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_C",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil C", r"en": r"Mass Fraction C"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_C/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Cr(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Cr",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Cr", r"en": r"Mass Fraction Cr"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Cr/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Cu(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Cu",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Cu", r"en": r"Mass Fraction Cu"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Cu/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Mn(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Mn",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Mn", r"en": r"Mass Fraction Mn"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Mn/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Mo(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Mo",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Mo", r"en": r"Mass Fraction Mo"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Mo/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_N(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_N",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil N", r"en": r"Mass Fraction N"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_N/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Nb(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Nb",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Nb", r"en": r"Mass Fraction Nb"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Nb/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Ni(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Ni",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Ni", r"en": r"Mass Fraction Ni"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Ni/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_P(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_P",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil P", r"en": r"Mass Fraction P"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_P/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Pb(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Pb",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Pb", r"en": r"Mass Fraction Pb"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Pb/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_S(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_S",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil S", r"en": r"Mass Fraction S"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_S/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Si(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Si",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Si", r"en": r"Mass Fraction Si"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Si/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Ta(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Ta",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Ta", r"en": r"Mass Fraction Ta"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Ta/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_Ti(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_Ti",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil Ti", r"en": r"Mass Fraction Ti"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_Ti/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_V(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_V",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil V", r"en": r"Mass Fraction V"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_V/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MassFraction_W(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MassFraction_W",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Masseanteil W", r"en": r"Mass Fraction W"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/MassFraction_W/1/0"
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SteelmakingProcess(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"SteelmakingProcess",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Stahlherstellungsverfahren", r"en": r"Steelmaking Process"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/SteelmakingProcess/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ChemicalAnalysis",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"de": r"Chemische Analyse", r"en": r"Chemical Analysis"}
                ),
                "semantic_id": global_ref(r"0173-1#01-AKG373#020"),
            }

        def __init__(
            self,
            massFraction_Al: Optional[Union[xsd.Float, MassFraction_Al]] = None,
            massFraction_Be: Optional[Union[xsd.Float, MassFraction_Be]] = None,
            massFraction_C: Optional[Union[xsd.Float, MassFraction_C]] = None,
            massFraction_Cr: Optional[Union[xsd.Float, MassFraction_Cr]] = None,
            massFraction_Cu: Optional[Union[xsd.Float, MassFraction_Cu]] = None,
            massFraction_Mn: Optional[Union[xsd.Float, MassFraction_Mn]] = None,
            massFraction_Mo: Optional[Union[xsd.Float, MassFraction_Mo]] = None,
            massFraction_N: Optional[Union[xsd.Float, MassFraction_N]] = None,
            massFraction_Nb: Optional[Union[xsd.Float, MassFraction_Nb]] = None,
            massFraction_Ni: Optional[Union[xsd.Float, MassFraction_Ni]] = None,
            massFraction_P: Optional[Union[xsd.Float, MassFraction_P]] = None,
            massFraction_Pb: Optional[Union[xsd.Float, MassFraction_Pb]] = None,
            massFraction_S: Optional[Union[xsd.Float, MassFraction_S]] = None,
            massFraction_Si: Optional[Union[xsd.Float, MassFraction_Si]] = None,
            massFraction_Ta: Optional[Union[xsd.Float, MassFraction_Ta]] = None,
            massFraction_Ti: Optional[Union[xsd.Float, MassFraction_Ti]] = None,
            massFraction_V: Optional[Union[xsd.Float, MassFraction_V]] = None,
            massFraction_W: Optional[Union[xsd.Float, MassFraction_W]] = None,
            steelmakingProcess: Optional[Union[aas.MultiLanguageTextType, SteelmakingProcess]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Al is not None and not isinstance(massFraction_Al, aas.SubmodelElement):
                massFraction_Al = self.MassFraction_Al(massFraction_Al)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Be is not None and not isinstance(massFraction_Be, aas.SubmodelElement):
                massFraction_Be = self.MassFraction_Be(massFraction_Be)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_C is not None and not isinstance(massFraction_C, aas.SubmodelElement):
                massFraction_C = self.MassFraction_C(massFraction_C)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Cr is not None and not isinstance(massFraction_Cr, aas.SubmodelElement):
                massFraction_Cr = self.MassFraction_Cr(massFraction_Cr)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Cu is not None and not isinstance(massFraction_Cu, aas.SubmodelElement):
                massFraction_Cu = self.MassFraction_Cu(massFraction_Cu)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Mn is not None and not isinstance(massFraction_Mn, aas.SubmodelElement):
                massFraction_Mn = self.MassFraction_Mn(massFraction_Mn)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Mo is not None and not isinstance(massFraction_Mo, aas.SubmodelElement):
                massFraction_Mo = self.MassFraction_Mo(massFraction_Mo)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_N is not None and not isinstance(massFraction_N, aas.SubmodelElement):
                massFraction_N = self.MassFraction_N(massFraction_N)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Nb is not None and not isinstance(massFraction_Nb, aas.SubmodelElement):
                massFraction_Nb = self.MassFraction_Nb(massFraction_Nb)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Ni is not None and not isinstance(massFraction_Ni, aas.SubmodelElement):
                massFraction_Ni = self.MassFraction_Ni(massFraction_Ni)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_P is not None and not isinstance(massFraction_P, aas.SubmodelElement):
                massFraction_P = self.MassFraction_P(massFraction_P)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Pb is not None and not isinstance(massFraction_Pb, aas.SubmodelElement):
                massFraction_Pb = self.MassFraction_Pb(massFraction_Pb)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_S is not None and not isinstance(massFraction_S, aas.SubmodelElement):
                massFraction_S = self.MassFraction_S(massFraction_S)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Si is not None and not isinstance(massFraction_Si, aas.SubmodelElement):
                massFraction_Si = self.MassFraction_Si(massFraction_Si)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Ta is not None and not isinstance(massFraction_Ta, aas.SubmodelElement):
                massFraction_Ta = self.MassFraction_Ta(massFraction_Ta)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_Ti is not None and not isinstance(massFraction_Ti, aas.SubmodelElement):
                massFraction_Ti = self.MassFraction_Ti(massFraction_Ti)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_V is not None and not isinstance(massFraction_V, aas.SubmodelElement):
                massFraction_V = self.MassFraction_V(massFraction_V)

            # Build a submodel element if a raw value was passed in the argument

            if massFraction_W is not None and not isinstance(massFraction_W, aas.SubmodelElement):
                massFraction_W = self.MassFraction_W(massFraction_W)

            # Build a submodel element if a raw value was passed in the argument

            if steelmakingProcess is not None and not isinstance(steelmakingProcess, aas.SubmodelElement):
                steelmakingProcess = self.SteelmakingProcess(steelmakingProcess)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                massFraction_Al,
                massFraction_Be,
                massFraction_C,
                massFraction_Cr,
                massFraction_Cu,
                massFraction_Mn,
                massFraction_Mo,
                massFraction_N,
                massFraction_Nb,
                massFraction_Ni,
                massFraction_P,
                massFraction_Pb,
                massFraction_S,
                massFraction_Si,
                massFraction_Ta,
                massFraction_Ti,
                massFraction_V,
                massFraction_W,
                steelmakingProcess,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Validation(aas.SubmodelElementCollection):

        class StatementOfCompliance(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"StatementOfCompliance",
                    "value_type": bool,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Konformitätserklärung", r"en": r"Statement of Compliance"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/StatementOfCompliance/1/0"
                    ),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DateOfIssue(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DateOfIssue",
                    "value_type": xsd.Date,
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Ausstelldatum", r"en": r"Date of Issue"}),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/DateOfIssue/1/0"
                    ),
                }

            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class OriginatorOfDocument(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"OriginatorOfDocument",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"de": r"Aussteller der Bescheinigung", r"en": r"Originator of the document"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/OriginatorOfDocument/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CEMarking(aas.SubmodelElementCollection):

            class MarkingName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MarkingName",
                        "value_type": str,
                        "value_id": global_ref(r"0173-1#07-DAA603#005"),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: see also [IRDI] 0173-1#02-BAB392#015 certificate/approval valueId with ECLASS enumeration IRDI is preferable, e.g. [IRDI] 0173-1#07-DAA603#004 for CE. If no IRDI available, string value can also be accepted. Note: CE marking is declared as mandatory according to Blue Guide of the EU-Commission "
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/MarkingName"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DesignationOfCertificateOrApproval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DesignationOfCertificateOrApproval",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Approval identifier, reference to the certificate number, to be entered without spaces "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABH783#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IssueDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IssueDate",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/IssueDate"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MarkingFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"MarkingFile",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/MarkingFile"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class MarkingAdditionalText(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MarkingAdditionalText",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: see also [IRDI] 0173-1#02-AAM954#002 details of other certificate "}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/MarkingAdditionalText"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"CEMarking",
                    "display_name": aas.MultiLanguageNameType(dict_={r"de": r"CE-Zeichen", r"en": r"CE Marking"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Note: see also [IRDI] 0112/2///61987#ABH515#003 Certificate or approval Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission "
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#01-AHD206#001"),
                }

            def __init__(
                self,
                markingName: Union[str, MarkingName],
                markingFile: MarkingFile,
                designationOfCertificateOrApproval: Optional[Union[str, DesignationOfCertificateOrApproval]] = None,
                issueDate: Optional[Union[str, IssueDate]] = None,
                markingAdditionalText: Optional[Iterable[Union[str, MarkingAdditionalText]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if markingName is not None and not isinstance(markingName, aas.SubmodelElement):
                    markingName = self.MarkingName(markingName)

                # Build a submodel element if a raw value was passed in the argument

                if designationOfCertificateOrApproval is not None and not isinstance(
                    designationOfCertificateOrApproval, aas.SubmodelElement
                ):
                    designationOfCertificateOrApproval = self.DesignationOfCertificateOrApproval(
                        designationOfCertificateOrApproval
                    )

                # Build a submodel element if a raw value was passed in the argument

                if issueDate is not None and not isinstance(issueDate, aas.SubmodelElement):
                    issueDate = self.IssueDate(issueDate)

                # A str would be split into its characters
                if isinstance(markingAdditionalText, str):
                    raise TypeError("markingAdditionalText takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if markingAdditionalText:
                    markingAdditionalText = [
                        i if isinstance(i, aas.SubmodelElement) else self.MarkingAdditionalText(i)
                        for i in markingAdditionalText
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    markingName, designationOfCertificateOrApproval, issueDate, markingFile, markingAdditionalText
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Validation",
                "display_name": aas.MultiLanguageNameType(dict_={r"de": r"Bestätigung", r"en": r"Validation"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/InspectionDocumentsOfSteelProducts/Validation/1/0"
                ),
            }

        def __init__(
            self,
            statementOfCompliance: Union[bool, StatementOfCompliance],
            dateOfIssue: Union[xsd.Date, DateOfIssue],
            originatorOfDocument: Union[str, OriginatorOfDocument],
            cEMarking: Optional[CEMarking] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if statementOfCompliance is not None and not isinstance(statementOfCompliance, aas.SubmodelElement):
                statementOfCompliance = self.StatementOfCompliance(statementOfCompliance)

            # Build a submodel element if a raw value was passed in the argument

            if dateOfIssue is not None and not isinstance(dateOfIssue, aas.SubmodelElement):
                dateOfIssue = self.DateOfIssue(dateOfIssue)

            # Build a submodel element if a raw value was passed in the argument

            if originatorOfDocument is not None and not isinstance(originatorOfDocument, aas.SubmodelElement):
                originatorOfDocument = self.OriginatorOfDocument(originatorOfDocument)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                statementOfCompliance, dateOfIssue, originatorOfDocument, cEMarking
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"InspectionDocumentsOfSteelProducts",
            "display_name": aas.MultiLanguageNameType(
                dict_={r"de": r"Prüfbescheinigung für Stahlprodukte", r"en": r"Inspection Documents for Steel Products"}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta/02032-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(
                r"https://admin-shell.io/idta/SubmodelTemplate/InspectionDocumentsOfSteelProducts/1/0"
            ),
        }

    def __init__(
        self,
        id_: str,
        manufacturer: Manufacturer,
        customer: Iterable[Customer],
        orderData: OrderData,
        productData: ProductData,
        validation: Validation,
        mechanicalTests: Optional[MechanicalTests] = None,
        chemicalAnalysis: Optional[ChemicalAnalysis] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(customer, str):
            raise TypeError("customer takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            manufacturer, customer, orderData, productData, mechanicalTests, chemicalAnalysis, validation
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
