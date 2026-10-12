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


class AssetLocation(aas.Submodel):

    class Addresses(GeneratedSubmodelElementList):

        class Addresses_item(aas.SubmodelElementCollection):

            class AddressLine1(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressLine1",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"address line 1", r"de": r"Adresszeile 1"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"address line 1", r"de": r"Adresszeile 1"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAO124#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressLine2(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressLine2",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"address line 2", r"de": r"Adresszeile 2"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"address line 2", r"de": r"Adresszeile 2"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAO125#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressLine3(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressLine3",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"address line 3", r"de": r"Adresszeile 3"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"address line 3", r"de": r"Adresszeile 3"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAO126#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressOfAdditionalLink(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressOfAdditionalLink",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"address of additional link", r"de": r"zusätzlicher Online-Verweis"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"address of additional link", r"de": r"zusätzlicher Online-Verweis"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAQ326#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressRemarks(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AddressRemarks",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"address remarks", r"de": r"Anmerkungen zur Adresse"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"address remarks", r"de": r"Anmerkungen zur Adresse"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAO202#004"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NationalCode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NationalCode",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"national code", r"de": r"Ländercode"}
                        ),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"national code", r"de": r"Ländercode"}),
                        "semantic_id": global_ref(r"0173-1#02-AAO134#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Statecounty(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Statecounty",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"state/county", r"de": r"Bundesland"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"state/county", r"de": r"Bundesland"}),
                        "semantic_id": global_ref(r"0173-1#02-AAO133#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Citytown(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Citytown",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"city/town", r"de": r"Ort"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"city/town", r"de": r"Ort"}),
                        "semantic_id": global_ref(r"0173-1#02-AAO132#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Street(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Street",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"street", r"de": r"Straße"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"street", r"de": r"Straße"}),
                        "semantic_id": global_ref(r"0173-1#02-AAO128#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ZipCode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ZipCode",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"zip code", r"de": r"Postleitzahl"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"zip code", r"de": r"Postleitzahl"}),
                        "semantic_id": global_ref(r"0173-1#02-AAO129#003"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Postal addresses where an object has been located",
                            r"de": r"Postadresse an der ein Objekt lokalisiert wurde",
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#01-ADR442#007"),
                }

            def __init__(
                self,
                addressLine1: Optional[Union[str, AddressLine1]] = None,
                addressLine2: Optional[Union[str, AddressLine2]] = None,
                addressLine3: Optional[Union[str, AddressLine3]] = None,
                addressOfAdditionalLink: Optional[Union[str, AddressOfAdditionalLink]] = None,
                addressRemarks: Optional[Union[str, AddressRemarks]] = None,
                nationalCode: Optional[Union[str, NationalCode]] = None,
                statecounty: Optional[Union[str, Statecounty]] = None,
                citytown: Optional[Union[str, Citytown]] = None,
                street: Optional[Union[str, Street]] = None,
                zipCode: Optional[Union[str, ZipCode]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if addressLine1 is not None and not isinstance(addressLine1, aas.SubmodelElement):
                    addressLine1 = self.AddressLine1(addressLine1)

                # Build a submodel element if a raw value was passed in the argument

                if addressLine2 is not None and not isinstance(addressLine2, aas.SubmodelElement):
                    addressLine2 = self.AddressLine2(addressLine2)

                # Build a submodel element if a raw value was passed in the argument

                if addressLine3 is not None and not isinstance(addressLine3, aas.SubmodelElement):
                    addressLine3 = self.AddressLine3(addressLine3)

                # Build a submodel element if a raw value was passed in the argument

                if addressOfAdditionalLink is not None and not isinstance(addressOfAdditionalLink, aas.SubmodelElement):
                    addressOfAdditionalLink = self.AddressOfAdditionalLink(addressOfAdditionalLink)

                # Build a submodel element if a raw value was passed in the argument

                if addressRemarks is not None and not isinstance(addressRemarks, aas.SubmodelElement):
                    addressRemarks = self.AddressRemarks(addressRemarks)

                # Build a submodel element if a raw value was passed in the argument

                if nationalCode is not None and not isinstance(nationalCode, aas.SubmodelElement):
                    nationalCode = self.NationalCode(nationalCode)

                # Build a submodel element if a raw value was passed in the argument

                if statecounty is not None and not isinstance(statecounty, aas.SubmodelElement):
                    statecounty = self.Statecounty(statecounty)

                # Build a submodel element if a raw value was passed in the argument

                if citytown is not None and not isinstance(citytown, aas.SubmodelElement):
                    citytown = self.Citytown(citytown)

                # Build a submodel element if a raw value was passed in the argument

                if street is not None and not isinstance(street, aas.SubmodelElement):
                    street = self.Street(street)

                # Build a submodel element if a raw value was passed in the argument

                if zipCode is not None and not isinstance(zipCode, aas.SubmodelElement):
                    zipCode = self.ZipCode(zipCode)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    addressLine1,
                    addressLine2,
                    addressLine3,
                    addressOfAdditionalLink,
                    addressRemarks,
                    nationalCode,
                    statecounty,
                    citytown,
                    street,
                    zipCode,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"Addresses",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#01-ADR442#007"),
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Addresses", r"de": r"Adressen"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"List with postal addresses where an object has been located",
                        r"de": r"Liste mit Postadressen, an denen sich ein Asset aufgehalten hat",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/addresses/1/0"),
            }

        def __init__(self, addresses_items: Iterable[Addresses_item], **kwargs: Unpack[SubmodelElementListMetadata]):

            # A str would be split into its characters
            if isinstance(addresses_items, str):
                raise TypeError("addresses_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(addresses_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class CoordinateSystems(GeneratedSubmodelElementList):

        class Coordinatesystems_item(aas.SubmodelElementCollection):

            class CoordinateSystemName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CoordinateSystemName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"coordinate system name", r"de": r"Koordinatensystenbezeichnung"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/coordinatesystemname/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CoordinateSystemId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CoordinateSystemId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"coordinate system (ID)", r"de": r"Koordinatensystem (ID)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/coordinatesystemid/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CoordinateSystemType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CoordinateSystemType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"coordinate system type", r"de": r"Koordinatensystemtyp"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/coordinatesystemtype/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ElevationReference(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ElevationReference",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"elevation reference", r"de": r"Referenz der Höhenangabe"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/elevationreference/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SeaLevelOfBaseHeight(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SeaLevelOfBaseHeight",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"sea level of base height", r"de": r"Seehöhe der Basishöhe"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/sealevelofbaseheight/1/0"),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class GroundControlPoints(GeneratedSubmodelElementList):

                class Groundcontrolpoints_item(aas.SubmodelElementCollection):

                    class GeographicCoordinates(aas.SubmodelElementCollection):

                        class Longitude(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Longitude",
                                    "value_type": float,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"longitude", r"de": r"Längengrad"}
                                    ),
                                    "semantic_id": global_ref(r" 0173-1#02-ABH961#002"),
                                }

                            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Latitude(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Latitude",
                                    "value_type": float,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"latitude", r"de": r"Breitengrad"}
                                    ),
                                    "semantic_id": global_ref(r" 0173-1#02-ABH960#002"),
                                }

                            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"GeographicCoordinates",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"geographic coordinates", r"de": r"Geographische Koordinaten"}
                                ),
                                "semantic_id": global_ref(r" 0173-1#02-ABH934#002"),
                            }

                        def __init__(
                            self,
                            longitude: Union[float, Longitude],
                            latitude: Union[float, Latitude],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if longitude is not None and not isinstance(longitude, aas.SubmodelElement):
                                longitude = self.Longitude(longitude)

                            # Build a submodel element if a raw value was passed in the argument

                            if latitude is not None and not isinstance(latitude, aas.SubmodelElement):
                                latitude = self.Latitude(latitude)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(longitude, latitude)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class RelativeCoordinates(aas.SubmodelElementCollection):

                        class X(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"X",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"X-coordinate", r"de": r"X-Koordinate"}
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/x/1/0"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Y(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Y",
                                    "value_type": xsd.Float,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Y-coordinate", r"de": r"Y-Koordinate"}
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/y/1/0"),
                                }

                            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"RelativeCoordinates",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"relative coordinates", r"de": r"relative Koordinaten"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Coordinates within a cartisian coordinate system",
                                        r"de": r"Koordinaten in einem kartesischen Koordinatensystem",
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-ABG741#001"),
                            }

                        def __init__(
                            self,
                            x: Union[xsd.Float, X],
                            y: Union[xsd.Float, Y],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if x is not None and not isinstance(x, aas.SubmodelElement):
                                x = self.X(x)

                            # Build a submodel element if a raw value was passed in the argument

                            if y is not None and not isinstance(y, aas.SubmodelElement):
                                y = self.Y(y)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(x, y)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"An array containing a mapping between geographic coordinates (longitude, latitude) in WGS84 (EPSG:4326) and relative coordinates (x,y)"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/groundcontrolpointsentry/1/0"),
                        }

                    def __init__(
                        self,
                        geographicCoordinates: GeographicCoordinates,
                        relativeCoordinates: RelativeCoordinates,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            geographicCoordinates, relativeCoordinates
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"GroundControlPoints",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/smc/groundcontrolpointsentry/1/0"
                        ),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"ground control points", r"de": r"Bodenkontrollpunkte"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Arrays containing a mapping between geographic coordinates (longitude, latitude) in WGS84 (EPSG:4326) and relative coordinates (x,y)",
                                r"de": r"Arrays, die ein Mapping von geographischen Koordinaten (Längengrad, Breitengrad) nach WGS84 (EPSG:4326) in relative Koordinaten (x,y) enthalten",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/groundcontrolpoints/1/0"),
                    }

                def __init__(
                    self,
                    groundcontrolpoints_items: Iterable[Groundcontrolpoints_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(groundcontrolpoints_items, str):
                        raise TypeError("groundcontrolpoints_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        groundcontrolpoints_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Coordinate reference system (CRS) record",
                            r"de": r"Listeneintrag für ein Koordinatenreferenzsystem (CRS)",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/coordinatesystemsrecord/1/0"),
                }

            def __init__(
                self,
                coordinateSystemId: Union[str, CoordinateSystemId],
                coordinateSystemType: Union[str, CoordinateSystemType],
                elevationReference: Union[str, ElevationReference],
                groundControlPoints: Union[Iterable[GroundControlPoints.Groundcontrolpoints_item], GroundControlPoints],
                coordinateSystemName: Optional[Union[str, CoordinateSystemName]] = None,
                seaLevelOfBaseHeight: Optional[Union[xsd.Float, SeaLevelOfBaseHeight]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if coordinateSystemName is not None and not isinstance(coordinateSystemName, aas.SubmodelElement):
                    coordinateSystemName = self.CoordinateSystemName(coordinateSystemName)

                # Build a submodel element if a raw value was passed in the argument

                if coordinateSystemId is not None and not isinstance(coordinateSystemId, aas.SubmodelElement):
                    coordinateSystemId = self.CoordinateSystemId(coordinateSystemId)

                # Build a submodel element if a raw value was passed in the argument

                if coordinateSystemType is not None and not isinstance(coordinateSystemType, aas.SubmodelElement):
                    coordinateSystemType = self.CoordinateSystemType(coordinateSystemType)

                # Build a submodel element if a raw value was passed in the argument

                if elevationReference is not None and not isinstance(elevationReference, aas.SubmodelElement):
                    elevationReference = self.ElevationReference(elevationReference)

                # Build a submodel element if a raw value was passed in the argument

                if seaLevelOfBaseHeight is not None and not isinstance(seaLevelOfBaseHeight, aas.SubmodelElement):
                    seaLevelOfBaseHeight = self.SeaLevelOfBaseHeight(seaLevelOfBaseHeight)

                # A str would be split into its characters
                if isinstance(groundControlPoints, str):
                    raise TypeError("groundControlPoints takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if groundControlPoints is not None and not isinstance(groundControlPoints, aas.SubmodelElement):
                    groundControlPoints = self.GroundControlPoints(groundControlPoints)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    coordinateSystemName,
                    coordinateSystemId,
                    coordinateSystemType,
                    elevationReference,
                    seaLevelOfBaseHeight,
                    groundControlPoints,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"CoordinateSystems",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"https://admin-shell.io/idta/smc/coordinatesystemsrecord/1/0"),
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"coordinate systems", r"de": r"Koordinatensysteme"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"List with information about different coordinate systems that have been used to determine the location of an asset",
                        r"de": r"Liste mit Informationen zu Koordinatensystemen die verwendet wurden, um die Assetposition zu bestimmen",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/coordinatesystems/1/0"),
            }

        def __init__(
            self,
            coordinatesystems_items: Iterable[Coordinatesystems_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(coordinatesystems_items, str):
                raise TypeError("coordinatesystems_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(coordinatesystems_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class VisitedAreas(GeneratedSubmodelElementList):

        class Visitedareas_item(aas.SubmodelElementCollection):

            class CoordinateSystemOfArea(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"CoordinateSystemOfArea",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Reference to a local coordinate reference system for an area",
                                r"de": r"Referenz auf ein lokales Koordinatenreferenzsystem für ein Areal",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/ref/coordinatesystemreference/1/0"),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AddressReferences(GeneratedSubmodelElementList):

                class Addressreferences_item(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Reference to an address", r"de": r"Referenz zu einer Adresse"}
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"AddressReferences",
                        "type_value_list_element": aas.ReferenceElement,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/sml/addressreferences/1/0"
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List with references to addresses for the area (area addresses)",
                                r"de": r"Liste mit Referenzen zu Adressen für das Areal",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/addressreferences/1/0"),
                    }

                def __init__(
                    self,
                    addressreferences_items: Iterable[Union[aas.Reference, Addressreferences_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(addressreferences_items, str):
                        raise TypeError("addressreferences_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if addressreferences_items:
                        addressreferences_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Addressreferences_item(i)
                            for i in addressreferences_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        addressreferences_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class AreaRegionCoordinates(GeneratedSubmodelElementList):

                class Arearegioncoordinates_item(aas.SubmodelElementCollection):

                    class X(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"X",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"X-coordinate", r"de": r"X-Koordinate"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/x/1/0"),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Y(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Y",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Y-coordinate", r"de": r"Y-Koordinate"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/y/1/0"),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"One coordinate of coordinates forming a polygon that describes the region of the area within the coordinate reference system of the area"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/regioncoordinateentry/1/0"),
                        }

                    def __init__(
                        self,
                        x: Union[xsd.Float, X],
                        y: Union[xsd.Float, Y],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if x is not None and not isinstance(x, aas.SubmodelElement):
                            x = self.X(x)

                        # Build a submodel element if a raw value was passed in the argument

                        if y is not None and not isinstance(y, aas.SubmodelElement):
                            y = self.Y(y)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(x, y)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"AreaRegionCoordinates",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/smc/regioncoordinateentry/1/0"
                        ),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"area region coordinates", r"de": r"Arealgrenzkoordinaten"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Coordinates forming a polygon that describes the area within the coordinate reference system of the area",
                                r"de": r"Koordinaten die ein Polygon formen, das die Grenzen eines Areals im Koordinatenrefernzsystem des Areals beschreibt",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/regioncoordinates/1/0"),
                    }

                def __init__(
                    self,
                    arearegioncoordinates_items: Iterable[Arearegioncoordinates_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(arearegioncoordinates_items, str):
                        raise TypeError("arearegioncoordinates_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        arearegioncoordinates_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class KindOfArea(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"KindOfArea",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"kind of area", r"de": r"Arealart"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/kindofarea/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AreaName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AreaName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Area name", r"de": r"Arealname"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Name of the area or building", r"de": r"Name des Areals oder Gebäudes"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/areaname/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AreaId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AreaId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"area (ID)", r"de": r"Areal (ID)"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Identification of an area ", r"de": r"Ident einer Area "}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/areaid/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AreaDesciption(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"AreaDesciption",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"area description", r"de": r"Arealbeschreibung"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Description of an area", r"de": r"Beschreibung eines Areals"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/areadescription/1/0"),
                        "embedded_data_specifications": [
                            aas.EmbeddedDataSpecification(
                                data_specification=global_ref(
                                    r"http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/3/0"
                                ),
                                data_specification_content=aas.DataSpecificationIEC61360(
                                    preferred_name=aas.PreferredNameTypeIEC61360(
                                        dict_={r"en": r"Description of an area"}
                                    ),
                                    data_type=None,
                                    definition=None,
                                    short_name=None,
                                    unit=None,
                                    unit_id=None,
                                    source_of_definition=None,
                                    symbol=None,
                                    value_format=None,
                                    value_list=None,
                                    value=None,
                                    level_types=set(),
                                ),
                            )
                        ],
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AreaLayout(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"AreaLayout",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"area layout", r"de": r"Areallayout"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"File with a layout (map) of the area (e.g., hall plan)",
                                r"de": r"Datei mit einem Areallayout (z.B. Hallenplan)",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/file/arealayout/1/0"),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class BuildingLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BuildingLevel",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"building level", r"de": r"Stockwerk"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABJ094#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Areas (e.g., site, building, field warehouse) where an asset has been located or is located"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/visitedareasrecord/1/0"),
                }

            def __init__(
                self,
                areaId: Union[str, AreaId],
                coordinateSystemOfArea: Optional[Union[aas.Reference, CoordinateSystemOfArea]] = None,
                addressReferences: Optional[
                    Union[Iterable[Union[aas.Reference, AddressReferences.Addressreferences_item]], AddressReferences]
                ] = None,
                areaRegionCoordinates: Optional[
                    Union[Iterable[AreaRegionCoordinates.Arearegioncoordinates_item], AreaRegionCoordinates]
                ] = None,
                kindOfArea: Optional[Union[str, KindOfArea]] = None,
                areaName: Optional[Union[str, AreaName]] = None,
                areaDesciption: Optional[Union[aas.MultiLanguageTextType, AreaDesciption]] = None,
                areaLayout: Optional[AreaLayout] = None,
                buildingLevel: Optional[Union[str, BuildingLevel]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if coordinateSystemOfArea is not None and not isinstance(coordinateSystemOfArea, aas.SubmodelElement):
                    coordinateSystemOfArea = self.CoordinateSystemOfArea(coordinateSystemOfArea)

                # A str would be split into its characters
                if isinstance(addressReferences, str):
                    raise TypeError("addressReferences takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if addressReferences is not None and not isinstance(addressReferences, aas.SubmodelElement):
                    addressReferences = self.AddressReferences(addressReferences)

                # A str would be split into its characters
                if isinstance(areaRegionCoordinates, str):
                    raise TypeError("areaRegionCoordinates takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if areaRegionCoordinates is not None and not isinstance(areaRegionCoordinates, aas.SubmodelElement):
                    areaRegionCoordinates = self.AreaRegionCoordinates(areaRegionCoordinates)

                # Build a submodel element if a raw value was passed in the argument

                if kindOfArea is not None and not isinstance(kindOfArea, aas.SubmodelElement):
                    kindOfArea = self.KindOfArea(kindOfArea)

                # Build a submodel element if a raw value was passed in the argument

                if areaName is not None and not isinstance(areaName, aas.SubmodelElement):
                    areaName = self.AreaName(areaName)

                # Build a submodel element if a raw value was passed in the argument

                if areaId is not None and not isinstance(areaId, aas.SubmodelElement):
                    areaId = self.AreaId(areaId)

                # Build a submodel element if a raw value was passed in the argument

                if areaDesciption is not None and not isinstance(areaDesciption, aas.SubmodelElement):
                    areaDesciption = self.AreaDesciption(areaDesciption)

                # Build a submodel element if a raw value was passed in the argument

                if buildingLevel is not None and not isinstance(buildingLevel, aas.SubmodelElement):
                    buildingLevel = self.BuildingLevel(buildingLevel)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    coordinateSystemOfArea,
                    addressReferences,
                    areaRegionCoordinates,
                    kindOfArea,
                    areaName,
                    areaId,
                    areaDesciption,
                    areaLayout,
                    buildingLevel,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"VisitedAreas",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"https://admin-shell.io/idta/smc/visitedareasrecord/1/0"),
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"visited areas", r"de": r"besuchte Areale"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"List with areas (e.g., sites, buildings, field warehouses) where an asset has been located or is located",
                        r"de": r"Liste mit Arealen (z.B. Standort, Gebäude, Freilagerfläche) an denen sich ein Asset befunden hat oder sich befindet",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/visitedareas/1/0"),
            }

        def __init__(
            self, visitedareas_items: Iterable[Visitedareas_item], **kwargs: Unpack[SubmodelElementListMetadata]
        ):

            # A str would be split into its characters
            if isinstance(visitedareas_items, str):
                raise TypeError("visitedareas_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(visitedareas_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class AssetTraces(aas.SubmodelElementCollection):

        class AreaEventTimeSeriesData(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"AreaEventTimeSeriesData",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to an AAS time series data Submodel instance of the same AAS with AreaRecords",
                            r"de": r"Referenz zu einer AAS Submodel-Instanz der gleichen AAS mit Zeitreihendaten für AreaRecords",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ref/eventtimeseriesdata/1/0"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LocationEventTimeSeriesData(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"LocationEventTimeSeriesData",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to an AAS time series data Submodel instance of the same AAS with LocationRecords",
                            r"de": r"Referenz zu einer AAS Submodel-Instanz der gleichen AAS mit Zeitreihendaten für FenceRecords",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/ref/eventtimeseriesdata/1/0"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AreaRecords(GeneratedSubmodelElementList):

            class Arearecords_item(aas.SubmodelElementCollection):

                class AreaRef(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"AreaRef",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to the area where the event has been recorded for",
                                    r"de": r"Referenz auf das Areal, zu dem das Event erfasst wurde",
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/ref/areareference/1/0"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Time(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Time",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Time ", r"de": r"Zeitpunkt"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Time when the event occurred",
                                    r"de": r"Zeitpunkt an dem das Ereignis aufgetreten ist",
                                }
                            ),
                            "semantic_id": global_ref(r" 0173-1#02-ABF198#002"),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EventId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EventId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"event (ID)", r"de": r"Ereignis (ID)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Identification of an event", r"de": r"Ident eines events"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/eventid/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProviderId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ProviderId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"provider (ID)", r"de": r"Lieferant (ID)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Identifikation of the location provider which triggered the event ",
                                    r"de": r"Ident des Lieferenten der Positionsinformation, der das Event ausgelöst hat",
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/providerid/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EventType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EventType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"event type", r"de": r"Eventtyp"}),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/eventtype/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Record of an area localization event"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/arearecordsrecord/1/0"),
                    }

                def __init__(
                    self,
                    areaRef: Union[aas.Reference, AreaRef],
                    time: Union[xsd.DateTime, Time],
                    eventType: Union[str, EventType],
                    eventId: Optional[Union[str, EventId]] = None,
                    providerId: Optional[Union[str, ProviderId]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if areaRef is not None and not isinstance(areaRef, aas.SubmodelElement):
                        areaRef = self.AreaRef(areaRef)

                    # Build a submodel element if a raw value was passed in the argument

                    if time is not None and not isinstance(time, aas.SubmodelElement):
                        time = self.Time(time)

                    # Build a submodel element if a raw value was passed in the argument

                    if eventId is not None and not isinstance(eventId, aas.SubmodelElement):
                        eventId = self.EventId(eventId)

                    # Build a submodel element if a raw value was passed in the argument

                    if providerId is not None and not isinstance(providerId, aas.SubmodelElement):
                        providerId = self.ProviderId(providerId)

                    # Build a submodel element if a raw value was passed in the argument

                    if eventType is not None and not isinstance(eventType, aas.SubmodelElement):
                        eventType = self.EventType(eventType)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        areaRef, time, eventId, providerId, eventType
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"AreaRecords",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "semantic_id_list_element": global_ref(r"https://admin-shell.io/idta/smc/arearecordsrecord/1/0"),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List with records for area localization events",
                            r"de": r"Liste mit Datensätzen für Areallokalisierungsereignisse",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/arearecords/1/0"),
                }

            def __init__(
                self, arearecords_items: Iterable[Arearecords_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(arearecords_items, str):
                    raise TypeError("arearecords_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(arearecords_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LocationRecords(GeneratedSubmodelElementList):

            class Locationrecords_item(aas.SubmodelElementCollection):

                class CoordinateSystemReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"CoordinateSystemReference",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to a coordinate reference system for the position ",
                                    r"de": r"Referenz auf das Koordinatenreferenzsystem für die Position",
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/ref/coordinatesystemreference/1/0"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Position(aas.SubmodelElementCollection):

                    class X(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"X",
                                "value_type": xsd.Float,
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/x/1/0"),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Y(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Y",
                                "value_type": xsd.Float,
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/y/1/0"),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Z(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Z",
                                "value_type": xsd.Float,
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/z/1/0"),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Position",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"position", r"de": r"Position"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Position of the asset"}),
                            "semantic_id": global_ref(r"0173-1#02-ABI783#001"),
                        }

                    def __init__(
                        self,
                        x: Union[xsd.Float, X],
                        y: Union[xsd.Float, Y],
                        z: Union[xsd.Float, Z],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if x is not None and not isinstance(x, aas.SubmodelElement):
                            x = self.X(x)

                        # Build a submodel element if a raw value was passed in the argument

                        if y is not None and not isinstance(y, aas.SubmodelElement):
                            y = self.Y(y)

                        # Build a submodel element if a raw value was passed in the argument

                        if z is not None and not isinstance(z, aas.SubmodelElement):
                            z = self.Z(z)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(x, y, z)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ProviderId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ProviderId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"provider (ID)", r"de": r"Lieferant (ID)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Identifikation of the location provider which triggered the event ",
                                    r"de": r"Ident des Lieferenten der Positionsinformation, der das Event ausgelöst hat",
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/providerid/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProviderType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ProviderType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"provider type", r"de": r"Versorgertyp"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/providertype/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Accuracy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Accuracy",
                            "value_type": float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Accuracy", r"de": r"Genauigkeit"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/accuracy/1/0"),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MagneticHeading(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MagneticHeading",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"magnetic heading", r"de": r"magnetische Ausrichtung"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/magneticheading/1/0"),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TrueHeading(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TrueHeading",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"heading", r"de": r"Ausrichtung"}),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/trueheading/1/0"),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class HeadingAccuracy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"HeadingAccuracy",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"heading accuracy", r"de": r"Steuerkursgenauigkeit"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/headingaccuracy/1/0"),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Time(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Time",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time", r"de": r"Zeitpunkt"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The time (timestamp) when the location data was generated (e.g., by a RTLS) ",
                                    r"de": r"Der Zeitpunkt (Zeitstempel) zu dem die Lokalisierung erfolgt ist (z.B. durch ein RTLS)",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABF198#002"),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TransmissionTime(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TransmissionTime",
                            "value_type": xsd.DateTime,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"transmission time", r"de": r"Sendezeitpunkt"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Time (timestemp) when the location information has been updated",
                                    r"de": r"Zeitpunkt (Zeitstempel) an dem die Lokalisierungsinformation zuletzt geändert wurde",
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/transmissiontime/1/0"),
                        }

                    def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocationDescription(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"LocationDescription",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"location description", r"de": r"Ortsbeschreibung"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Location description (meta information for the position) , it is recommended to refer to the origin of the CRS",
                                    r"de": r"Beschreibung des Orts (Metainformationen zur Position); es wird empfohlen, auf den Ursprung des Koordinatenreferenzsystems Bezug zu nehmen",
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/locationdescription/1/0"),
                            "embedded_data_specifications": [
                                aas.EmbeddedDataSpecification(
                                    data_specification=global_ref(
                                        r"http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/3/0"
                                    ),
                                    data_specification_content=aas.DataSpecificationIEC61360(
                                        preferred_name=aas.PreferredNameTypeIEC61360(
                                            dict_={r"en": r"locationdescription"}
                                        ),
                                        data_type=None,
                                        definition=None,
                                        short_name=None,
                                        unit=None,
                                        unit_id=None,
                                        source_of_definition=None,
                                        symbol=None,
                                        value_format=None,
                                        value_list=None,
                                        value=None,
                                        level_types=set(),
                                    ),
                                )
                            ],
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Speed(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Speed",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"speed", r"de": r"Geschwindigkeit"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Speed of the asset at the time where the position was determined",
                                    r"de": r"Geschwindigkeit des Assets zum Zeitpunkt an dem die Position bestimmt wurde",
                                }
                            ),
                            "semantic_id": global_ref(r" 0173-1#02-AAV544#004"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Course(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Course",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"course", r"de": r"Kurs"}),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/course/1/0"),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReferencePointId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ReferencePointId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"reference point (ID)", r"de": r"Referenzpunkt (ID)"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/referencepointid/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Record of a location (position) localization event"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/locationrecordsrecord/1/0"),
                    }

                def __init__(
                    self,
                    coordinateSystemReference: Union[aas.Reference, CoordinateSystemReference],
                    position: Position,
                    time: Union[xsd.DateTime, Time],
                    providerId: Optional[Union[str, ProviderId]] = None,
                    providerType: Optional[Union[str, ProviderType]] = None,
                    accuracy: Optional[Union[float, Accuracy]] = None,
                    magneticHeading: Optional[Union[int, MagneticHeading]] = None,
                    trueHeading: Optional[Union[int, TrueHeading]] = None,
                    headingAccuracy: Optional[Union[int, HeadingAccuracy]] = None,
                    transmissionTime: Optional[Union[xsd.DateTime, TransmissionTime]] = None,
                    locationDescription: Optional[Union[aas.MultiLanguageTextType, LocationDescription]] = None,
                    speed: Optional[Union[xsd.Float, Speed]] = None,
                    course: Optional[Union[int, Course]] = None,
                    referencePointId: Optional[Union[str, ReferencePointId]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if coordinateSystemReference is not None and not isinstance(
                        coordinateSystemReference, aas.SubmodelElement
                    ):
                        coordinateSystemReference = self.CoordinateSystemReference(coordinateSystemReference)

                    # Build a submodel element if a raw value was passed in the argument

                    if providerId is not None and not isinstance(providerId, aas.SubmodelElement):
                        providerId = self.ProviderId(providerId)

                    # Build a submodel element if a raw value was passed in the argument

                    if providerType is not None and not isinstance(providerType, aas.SubmodelElement):
                        providerType = self.ProviderType(providerType)

                    # Build a submodel element if a raw value was passed in the argument

                    if accuracy is not None and not isinstance(accuracy, aas.SubmodelElement):
                        accuracy = self.Accuracy(accuracy)

                    # Build a submodel element if a raw value was passed in the argument

                    if magneticHeading is not None and not isinstance(magneticHeading, aas.SubmodelElement):
                        magneticHeading = self.MagneticHeading(magneticHeading)

                    # Build a submodel element if a raw value was passed in the argument

                    if trueHeading is not None and not isinstance(trueHeading, aas.SubmodelElement):
                        trueHeading = self.TrueHeading(trueHeading)

                    # Build a submodel element if a raw value was passed in the argument

                    if headingAccuracy is not None and not isinstance(headingAccuracy, aas.SubmodelElement):
                        headingAccuracy = self.HeadingAccuracy(headingAccuracy)

                    # Build a submodel element if a raw value was passed in the argument

                    if time is not None and not isinstance(time, aas.SubmodelElement):
                        time = self.Time(time)

                    # Build a submodel element if a raw value was passed in the argument

                    if transmissionTime is not None and not isinstance(transmissionTime, aas.SubmodelElement):
                        transmissionTime = self.TransmissionTime(transmissionTime)

                    # Build a submodel element if a raw value was passed in the argument

                    if locationDescription is not None and not isinstance(locationDescription, aas.SubmodelElement):
                        locationDescription = self.LocationDescription(locationDescription)

                    # Build a submodel element if a raw value was passed in the argument

                    if speed is not None and not isinstance(speed, aas.SubmodelElement):
                        speed = self.Speed(speed)

                    # Build a submodel element if a raw value was passed in the argument

                    if course is not None and not isinstance(course, aas.SubmodelElement):
                        course = self.Course(course)

                    # Build a submodel element if a raw value was passed in the argument

                    if referencePointId is not None and not isinstance(referencePointId, aas.SubmodelElement):
                        referencePointId = self.ReferencePointId(referencePointId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        coordinateSystemReference,
                        position,
                        providerId,
                        providerType,
                        accuracy,
                        magneticHeading,
                        trueHeading,
                        headingAccuracy,
                        time,
                        transmissionTime,
                        locationDescription,
                        speed,
                        course,
                        referencePointId,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"LocationRecords",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "semantic_id_list_element": global_ref(
                        r"https://admin-shell.io/idta/smc/locationrecordsrecord/1/0"
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List with records for location (position) localization events",
                            r"de": r"Liste mit Datensätzen für Ereignisse betreffend der Lokalisierung (Positionsbestimmung)",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/locationrecords/1/0"),
                }

            def __init__(
                self,
                locationrecords_items: Iterable[Locationrecords_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(locationrecords_items, str):
                    raise TypeError("locationrecords_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(locationrecords_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AssetTraces",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"asset traces", r"de": r"Assetverfolgung"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Collection of localization event records for sites, areas, fences and locations",
                        r"de": r"Sammlung von Lokalisierungsevents für Standorte, Areale, Schranken und Positionen",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/assettraces/1/0"),
            }

        def __init__(
            self,
            areaEventTimeSeriesData: Optional[Union[aas.Reference, AreaEventTimeSeriesData]] = None,
            locationEventTimeSeriesData: Optional[Union[aas.Reference, LocationEventTimeSeriesData]] = None,
            areaRecords: Optional[Union[Iterable[AreaRecords.Arearecords_item], AreaRecords]] = None,
            locationRecords: Optional[Union[Iterable[LocationRecords.Locationrecords_item], LocationRecords]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if areaEventTimeSeriesData is not None and not isinstance(areaEventTimeSeriesData, aas.SubmodelElement):
                areaEventTimeSeriesData = self.AreaEventTimeSeriesData(areaEventTimeSeriesData)

            # Build a submodel element if a raw value was passed in the argument

            if locationEventTimeSeriesData is not None and not isinstance(
                locationEventTimeSeriesData, aas.SubmodelElement
            ):
                locationEventTimeSeriesData = self.LocationEventTimeSeriesData(locationEventTimeSeriesData)

            # A str would be split into its characters
            if isinstance(areaRecords, str):
                raise TypeError("areaRecords takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if areaRecords is not None and not isinstance(areaRecords, aas.SubmodelElement):
                areaRecords = self.AreaRecords(areaRecords)

            # A str would be split into its characters
            if isinstance(locationRecords, str):
                raise TypeError("locationRecords takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if locationRecords is not None and not isinstance(locationRecords, aas.SubmodelElement):
                locationRecords = self.LocationRecords(locationRecords)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                areaEventTimeSeriesData, locationEventTimeSeriesData, areaRecords, locationRecords
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class AssetLocatingInformation(aas.SubmodelElementCollection):

        class Localizable(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Localizable",
                    "value_type": bool,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"localizable", r"de": r"lokalisierbar"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/localizable/1/0"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AssetLocationServiceRealTimeCapability(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"AssetLocationServiceRealTimeCapability",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Realtime capability description", r"de": r"Beschreibung der Echtzeitfähigkeit"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Description of the extend and conditions for real time applications of the AAS",
                            r"de": r"Beschreibung, inwieweit und unter welchen Bedingungen eine Echtzeitfähigkeit der AAS besteht",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/realtimecapabilityofaas/1/0"),
                    "embedded_data_specifications": [
                        aas.EmbeddedDataSpecification(
                            data_specification=global_ref(
                                r"http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/3/0"
                            ),
                            data_specification_content=aas.DataSpecificationIEC61360(
                                preferred_name=aas.PreferredNameTypeIEC61360(
                                    dict_={r"en": r"Realtime capability description"}
                                ),
                                data_type=None,
                                definition=None,
                                short_name=None,
                                unit=None,
                                unit_id=None,
                                source_of_definition=None,
                                symbol=None,
                                value_format=None,
                                value_list=None,
                                value=None,
                                level_types=set(),
                            ),
                        )
                    ],
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RealtimeLocationSourceType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RealtimeLocationSourceType",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"real time location source type",
                            r"de": r"Typ der Quelle für Echtzeitlokalisierung",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/realtimelocationsourcetype/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RealtimeLocationSource(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"RealtimeLocationSource",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Real time location source", r"de": r"Quelle für Echtzeitlokalisierung"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/realtimelocationsource/1/0"),
                    "embedded_data_specifications": [
                        aas.EmbeddedDataSpecification(
                            data_specification=global_ref(
                                r"http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/3/0"
                            ),
                            data_specification_content=aas.DataSpecificationIEC61360(
                                preferred_name=aas.PreferredNameTypeIEC61360(dict_={r"en": r"Course"}),
                                data_type=None,
                                definition=None,
                                short_name=None,
                                unit=None,
                                unit_id=None,
                                source_of_definition=None,
                                symbol=None,
                                value_format=None,
                                value_list=None,
                                value=None,
                                level_types=set(),
                            ),
                        )
                    ],
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AssetLocatingInformation",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Collection with additional information concerning the localization of an asset",
                        r"de": r"Sammlung mit zusätzlichen Informationen betreffend die Lokalisierung eines Assets",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/assetlocatinginformation/1/0"),
            }

        def __init__(
            self,
            localizable: Optional[Union[bool, Localizable]] = None,
            assetLocationServiceRealTimeCapability: Optional[
                Union[aas.MultiLanguageTextType, AssetLocationServiceRealTimeCapability]
            ] = None,
            realtimeLocationSourceType: Optional[Union[str, RealtimeLocationSourceType]] = None,
            realtimeLocationSource: Optional[Union[aas.MultiLanguageTextType, RealtimeLocationSource]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if localizable is not None and not isinstance(localizable, aas.SubmodelElement):
                localizable = self.Localizable(localizable)

            # Build a submodel element if a raw value was passed in the argument

            if assetLocationServiceRealTimeCapability is not None and not isinstance(
                assetLocationServiceRealTimeCapability, aas.SubmodelElement
            ):
                assetLocationServiceRealTimeCapability = self.AssetLocationServiceRealTimeCapability(
                    assetLocationServiceRealTimeCapability
                )

            # Build a submodel element if a raw value was passed in the argument

            if realtimeLocationSourceType is not None and not isinstance(
                realtimeLocationSourceType, aas.SubmodelElement
            ):
                realtimeLocationSourceType = self.RealtimeLocationSourceType(realtimeLocationSourceType)

            # Build a submodel element if a raw value was passed in the argument

            if realtimeLocationSource is not None and not isinstance(realtimeLocationSource, aas.SubmodelElement):
                realtimeLocationSource = self.RealtimeLocationSource(realtimeLocationSource)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                localizable, assetLocationServiceRealTimeCapability, realtimeLocationSourceType, realtimeLocationSource
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"AssetLocation",
            "display_name": aas.MultiLanguageNameType(
                dict_={r"en": r"Submodel asset location", r"de": r"Teilmodell Assetstandort"}
            ),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel for tracking & tracing of the location of an assets",
                    r"de": r"Teilmodell für das Tracking & Tracing des Standortes eines Assets",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=aas.ModelReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/smt/assetlocation/1/0"
                        ),
                    ),
                    type_=aas.Submodel,
                    referred_semantic_id=None,
                ),
                template_id=r"AssetLocation",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/smt/assetlocation/1/0"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        addresses: Optional[Union[Iterable[Addresses.Addresses_item], Addresses]] = None,
        coordinateSystems: Optional[
            Union[Iterable[CoordinateSystems.Coordinatesystems_item], CoordinateSystems]
        ] = None,
        visitedAreas: Optional[Union[Iterable[VisitedAreas.Visitedareas_item], VisitedAreas]] = None,
        assetTraces: Optional[AssetTraces] = None,
        assetLocatingInformation: Optional[AssetLocatingInformation] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(addresses, str):
            raise TypeError("addresses takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if addresses is not None and not isinstance(addresses, aas.SubmodelElement):
            addresses = self.Addresses(addresses)

        # A str would be split into its characters
        if isinstance(coordinateSystems, str):
            raise TypeError("coordinateSystems takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if coordinateSystems is not None and not isinstance(coordinateSystems, aas.SubmodelElement):
            coordinateSystems = self.CoordinateSystems(coordinateSystems)

        # A str would be split into its characters
        if isinstance(visitedAreas, str):
            raise TypeError("visitedAreas takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if visitedAreas is not None and not isinstance(visitedAreas, aas.SubmodelElement):
            visitedAreas = self.VisitedAreas(visitedAreas)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            addresses, coordinateSystems, visitedAreas, assetTraces, assetLocatingInformation
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
