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


class DppMetadata(aas.Submodel):

    class DigitalProductPassportId(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"digitalProductPassportId",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Unique Product Passport Identifier (DPP ID)"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Unique identifier of an instance of the digital product"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/digitalProductPassportId/1"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class UniqueProductIdentifier(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"uniqueProductIdentifier",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unique Product Identifier"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Unique string of characters for the identification of a product, that also enables a web link to the digital product passport."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/uniqueProductIdentifier/1"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Granularity(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"granularity",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Granularity"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The granularity of the Product. There are three values: ‘Model‘, ‘Item‘ and ‘Batch‘."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/granularity/1"),
                "supplemental_semantic_id": (global_ref(r"https://admin-shell.io/aas/3/2/AssetKind"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class DppSchemaVersion(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"dppSchemaVersion",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"DPP Schema Version"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Reference standard the DPP instance schema refers to."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/dppSchemaVersion/1"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class DppStatus(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"dppStatus",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"DPP Status"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Status of the DPP instance as digital resource."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/dppStatus/1"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class LastUpdate(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"lastUpdate",
                "value_type": xsd.DateTime,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Last Update"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Date and time of the latest update to the DPP instance."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/lastUpdate/1"),
                "supplemental_semantic_id": (
                    global_ref(r"<https://admin-shell.io/aas/3/2/AdministrativeInformation/updatedAt"),
                ),
            }

        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class EconomicOperatorId(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"economicOperatorId",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Economic Operator ID"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Unique string of characters for the identification of an actor involved in a product’s life cycle."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/economicOperatorId/1"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class FacilityId(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"facilityId",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Facility ID"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Unique string of characters for the identification of locations or buildings involved in a product’s value chain or used by actors involved in a product’s life cycle."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/facilityId/1"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ContentSpecificationIds(GeneratedSubmodelElementList):

        class Contentspecificationids_item(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": None,
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Content Specification ID"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/contentSpecificationId/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"contentSpecificationIds",
                "type_value_list_element": aas.Property,
                "value_type_list_element": str,
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Content Specification IDs"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference to horizontal or product-type related content specifications for the DPP."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/contentSpecificationIds/1"),
            }

        def __init__(
            self,
            contentspecificationids_items: Iterable[Union[str, Contentspecificationids_item]],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(contentspecificationids_items, str):
                raise TypeError("contentspecificationids_items takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if contentspecificationids_items:
                contentspecificationids_items = [
                    i if isinstance(i, aas.SubmodelElement) else self.Contentspecificationids_item(i)
                    for i in contentspecificationids_items
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(contentspecificationids_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"DppMetadata",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": "\n   Digital record of product characteristics throughout its life cycle.\n   \n   SOURCE: FprEN 18223:2026(en)   \n   "
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/cds/dppMetadata/1"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        digitalProductPassportId: Union[str, DigitalProductPassportId],
        uniqueProductIdentifier: Union[str, UniqueProductIdentifier],
        granularity: Union[str, Granularity],
        dppSchemaVersion: Union[str, DppSchemaVersion],
        dppStatus: Union[str, DppStatus],
        lastUpdate: Union[xsd.DateTime, LastUpdate],
        economicOperatorId: Union[str, EconomicOperatorId],
        facilityId: Optional[Union[str, FacilityId]] = None,
        contentSpecificationIds: Optional[
            Union[Iterable[Union[str, ContentSpecificationIds.Contentspecificationids_item]], ContentSpecificationIds]
        ] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if digitalProductPassportId is not None and not isinstance(digitalProductPassportId, aas.SubmodelElement):
            digitalProductPassportId = self.DigitalProductPassportId(digitalProductPassportId)

        # Build a submodel element if a raw value was passed in the argument

        if uniqueProductIdentifier is not None and not isinstance(uniqueProductIdentifier, aas.SubmodelElement):
            uniqueProductIdentifier = self.UniqueProductIdentifier(uniqueProductIdentifier)

        # Build a submodel element if a raw value was passed in the argument

        if granularity is not None and not isinstance(granularity, aas.SubmodelElement):
            granularity = self.Granularity(granularity)

        # Build a submodel element if a raw value was passed in the argument

        if dppSchemaVersion is not None and not isinstance(dppSchemaVersion, aas.SubmodelElement):
            dppSchemaVersion = self.DppSchemaVersion(dppSchemaVersion)

        # Build a submodel element if a raw value was passed in the argument

        if dppStatus is not None and not isinstance(dppStatus, aas.SubmodelElement):
            dppStatus = self.DppStatus(dppStatus)

        # Build a submodel element if a raw value was passed in the argument

        if lastUpdate is not None and not isinstance(lastUpdate, aas.SubmodelElement):
            lastUpdate = self.LastUpdate(lastUpdate)

        # Build a submodel element if a raw value was passed in the argument

        if economicOperatorId is not None and not isinstance(economicOperatorId, aas.SubmodelElement):
            economicOperatorId = self.EconomicOperatorId(economicOperatorId)

        # Build a submodel element if a raw value was passed in the argument

        if facilityId is not None and not isinstance(facilityId, aas.SubmodelElement):
            facilityId = self.FacilityId(facilityId)

        # A str would be split into its characters
        if isinstance(contentSpecificationIds, str):
            raise TypeError("contentSpecificationIds takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if contentSpecificationIds is not None and not isinstance(contentSpecificationIds, aas.SubmodelElement):
            contentSpecificationIds = self.ContentSpecificationIds(contentSpecificationIds)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            digitalProductPassportId,
            uniqueProductIdentifier,
            granularity,
            dppSchemaVersion,
            dppStatus,
            lastUpdate,
            economicOperatorId,
            facilityId,
            contentSpecificationIds,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
