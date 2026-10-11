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


class TechnicalDataAGV(aas.Submodel):

    class GeneralInformation(aas.SubmodelElementCollection):

        class ManufacturerName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerName",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging and labeling of a product in respect to its being brought into the market."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAO677#004"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO677-004"),),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CompanyLogo(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"CompanyLogo",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Imagefile for logo of manufacturer provided in common format (.png, .jpg)."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI776#002"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI776-002"),),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class ManufacturerProductDesignation(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"ManufacturerProductDesignation",
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Product designation as given by the mnaufacturer. Short description of the product, product group or function (short text) in common language."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAW338#003"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAW338-003"),),
                }

            def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductArticleNumberOfManufacturer(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProductArticleNumberOfManufacturer",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"unique product identifier of the manufacturer "}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAO054#003"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO054-003"),),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ManufacturerOrderCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerOrderCode",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"By manufactures issued unique combination of numbers and letters used to identify the device for ordering"
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAO227#004"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO227-004"),),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductImages(GeneratedSubmodelElementList):

            class Productimages_item(aas.SubmodelElementCollection):

                class ImageFile(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {"id_short": r"ImageFile", "semantic_id": global_ref(r"0173-1#02-ABK291#002")}

                    def __init__(
                        self, value: str, content_type: Optional[str] = r"image/jpeg", **kwargs: Unpack[FileMetadata]
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class ImageNote(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ImageNote",
                            "semantic_id": global_ref(r"0173-1#02-ABL423#001"),
                            "supplemental_semantic_id": (
                                global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABL423-001"),
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Product image", r"de": r"Produktbild"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABM220#001/0173-1#01-AHY911#001"),
                        "supplemental_semantic_id": (
                            aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABM220#001~0/0173-1#01-AHY911#001",
                                    ),
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://api.eclass-cdp.com/0173-1-02-ABM220-001/0173-1-01-AHY911-001",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                    }

                def __init__(
                    self,
                    imageFile: ImageFile,
                    imageNote: Optional[Union[aas.LangStringSet, ImageNote]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if imageNote is not None and not isinstance(imageNote, aas.SubmodelElement):
                        imageNote = self.ImageNote(imageNote)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(imageFile, imageNote)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"ProductImages",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "semantic_id_list_element": global_ref(r"0173-1#02-ABM220#001/0173-1#01-AHY911#001"),
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Product images", r"de": r"Produktbilder"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Image file for associated product provided in common format (.png, .jpg)"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABM220#001"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABM220-001"),),
                }

            def __init__(
                self, productimages_items: Iterable[Productimages_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(productimages_items, str):
                    raise TypeError("productimages_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(productimages_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"GeneralInformation",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"General information", r"de": r"Allgemeine Informationen"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"General information, for example ordering and manufacturer information."}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABK161#002/0173-1#01-AHX838#002"),
                "supplemental_semantic_id": (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK161-002/0173-1-01-AHX838-002"),
                ),
            }

        def __init__(
            self,
            manufacturerName: Union[str, ManufacturerName],
            manufacturerProductDesignation: Union[aas.LangStringSet, ManufacturerProductDesignation],
            productArticleNumberOfManufacturer: Union[str, ProductArticleNumberOfManufacturer],
            manufacturerOrderCode: Union[str, ManufacturerOrderCode],
            companyLogo: Optional[CompanyLogo] = None,
            productImages: Optional[Union[Iterable[ProductImages.Productimages_item], ProductImages]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                manufacturerName = self.ManufacturerName(manufacturerName)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerProductDesignation is not None and not isinstance(
                manufacturerProductDesignation, aas.SubmodelElement
            ):
                manufacturerProductDesignation = self.ManufacturerProductDesignation(manufacturerProductDesignation)

            # Build a submodel element if a raw value was passed in the argument

            if productArticleNumberOfManufacturer is not None and not isinstance(
                productArticleNumberOfManufacturer, aas.SubmodelElement
            ):
                productArticleNumberOfManufacturer = self.ProductArticleNumberOfManufacturer(
                    productArticleNumberOfManufacturer
                )

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerOrderCode is not None and not isinstance(manufacturerOrderCode, aas.SubmodelElement):
                manufacturerOrderCode = self.ManufacturerOrderCode(manufacturerOrderCode)

            # A str would be split into its characters
            if isinstance(productImages, str):
                raise TypeError("productImages takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if productImages is not None and not isinstance(productImages, aas.SubmodelElement):
                productImages = self.ProductImages(productImages)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                manufacturerName,
                companyLogo,
                manufacturerProductDesignation,
                productArticleNumberOfManufacturer,
                manufacturerOrderCode,
                productImages,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SpecificDescriptions(GeneratedSubmodelElementList):

        class Specificdescriptions_item(aas.SubmodelElementCollection):

            class DataSheet(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"DataSheet",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Product datasheet", r"de": r"Produktdatenblatt"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Document with technical product data of the AGV provided by the manufacturer",
                                r"de": r"Dokument mit technischen Produktdaten, das vom Hersteller bereitgestellt wird",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/datasheet/1/0"),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class TypeAndApplicationInformation(aas.SubmodelElementCollection):

                class AgvKinematic(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AgvKinematic",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Kinematic of the AGV", r"de": r"Kinematik des AGV"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Type of Kinematic of the AGV. The enumerations according VDA5050 "DIFF", "OMNI", "THREEWHEEL", "OTHER" can be used.'
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/agvkinematic/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AgvClass(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AgvClass",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Class of the AGV", r"de": r"Klasse des AGV"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Class of the AGV. The enumeration according VDA5050 with "FORKLIFT", "CONVEYER", "TUGGER", "CARRIER", "OTHER" can be used.'
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/agvclass/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TravelDirection(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TravelDirection",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Travel direction", r"de": r"Fahrtrichtung"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Direction of traveling of the AGV, the enumeration "FORWARD", "BACKWARD", "OMNI-DIRECTIONAL" can be used.'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/traveldirection/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TransportPrinciple(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TransportPrinciple",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Transportation principle", r"de": r"Transportprinzip"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Transportation pinciple of the AGV. The enumeration "LOADPULLING", "LOADCARRYING", "MIXED" can be used.'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/transportprinciple/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalizationType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalizationType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Type of localization", r"de": r"Lokalisierungsart"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Type of the localization the AGV is using. The enumeration according VDA5050 with "NATURAL", "REFLECTOR", "RFID", "DMC", "SPOT", "GRID", "OTHER" can be used.'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/localizationtype/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NavigationType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NavigationType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Type of navigation", r"de": r"Navigationsart"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Type of navigation the AGV uses. The enumeration according VDA5050 with "PHYSICAL_LINE_GUIDED", "VIRTUAL_LINE_GUIDED", "AUTONOMOUS" can be used.'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/navigationtype/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpecialApplications(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"SpecialApplications",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Special applications", r"de": r"Besondere Anwendungsbereiche"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Special applications and usage sectors of the AGV, e.g. EMC environment, chemical industry, mining, clean rooms, refrigerated rooms, areas with explosion risk"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/specialapplications/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpecialCapabilities(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"SpecialCapabilities",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Special capabilities", r"de": r"Besondere Fähigkeiten"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Special capabilities and functions of the AGV"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/specialcapabilities/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProtectionClassIP(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ProtectionClassIP",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"IP Protection Class", r"de": r"IP Schutzklasse"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Extent of protection provided by an enclosure against access to hazardous parts, against ingress of solid foreign objects and against ingress of water"
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAV695#003"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SuitableForOutdoorUse(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SuitableForOutdoorUse",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Indicates wether the AGV can be used outdoors (true) or not (false)",
                                    r"de": r"Gib an, ob das AGV im Außenbereich (Outdoor) genutzt werden kann (true) oder nicht (false)",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-BAD676#009"),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class RequiredEnvironmentalConditions(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"RequiredEnvironmentalConditions",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Required environmental conditions",
                                    r"de": r"Erforderliche Umweltbedingungen",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of required environmental conditions that have to be fulfilled to use the AGV, e.g., floor condition or ambient temperature (min./max.)"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/requiredenvironmentalconditions/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpecialQualificationDemand(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"SpecialQualificationDemand",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Special qualification demand",
                                    r"de": r"Besonderer Qualifikationsbedarf",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Demand for the special qualification required"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/specialqualificationdemand/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"TypeAndApplicationInformation",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Type and application information",
                                r"de": r"Typ- und Anwendungsinformationen",
                            }
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "Information about the AGV type and the vehicle's applications"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/technicaldataagv/typeandapplicationinformation/1/0"
                        ),
                    }

                def __init__(
                    self,
                    agvKinematic: Optional[Union[str, AgvKinematic]] = None,
                    agvClass: Optional[Union[str, AgvClass]] = None,
                    travelDirection: Optional[Union[str, TravelDirection]] = None,
                    transportPrinciple: Optional[Union[str, TransportPrinciple]] = None,
                    localizationType: Optional[Union[str, LocalizationType]] = None,
                    navigationType: Optional[Union[str, NavigationType]] = None,
                    specialApplications: Optional[Union[aas.LangStringSet, SpecialApplications]] = None,
                    specialCapabilities: Optional[Union[aas.LangStringSet, SpecialCapabilities]] = None,
                    protectionClassIP: Optional[Union[str, ProtectionClassIP]] = None,
                    suitableForOutdoorUse: Optional[Union[bool, SuitableForOutdoorUse]] = None,
                    requiredEnvironmentalConditions: Optional[
                        Union[aas.LangStringSet, RequiredEnvironmentalConditions]
                    ] = None,
                    specialQualificationDemand: Optional[Union[aas.LangStringSet, SpecialQualificationDemand]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if agvKinematic is not None and not isinstance(agvKinematic, aas.SubmodelElement):
                        agvKinematic = self.AgvKinematic(agvKinematic)

                    # Build a submodel element if a raw value was passed in the argument

                    if agvClass is not None and not isinstance(agvClass, aas.SubmodelElement):
                        agvClass = self.AgvClass(agvClass)

                    # Build a submodel element if a raw value was passed in the argument

                    if travelDirection is not None and not isinstance(travelDirection, aas.SubmodelElement):
                        travelDirection = self.TravelDirection(travelDirection)

                    # Build a submodel element if a raw value was passed in the argument

                    if transportPrinciple is not None and not isinstance(transportPrinciple, aas.SubmodelElement):
                        transportPrinciple = self.TransportPrinciple(transportPrinciple)

                    # Build a submodel element if a raw value was passed in the argument

                    if localizationType is not None and not isinstance(localizationType, aas.SubmodelElement):
                        localizationType = self.LocalizationType(localizationType)

                    # Build a submodel element if a raw value was passed in the argument

                    if navigationType is not None and not isinstance(navigationType, aas.SubmodelElement):
                        navigationType = self.NavigationType(navigationType)

                    # Build a submodel element if a raw value was passed in the argument

                    if specialApplications is not None and not isinstance(specialApplications, aas.SubmodelElement):
                        specialApplications = self.SpecialApplications(specialApplications)

                    # Build a submodel element if a raw value was passed in the argument

                    if specialCapabilities is not None and not isinstance(specialCapabilities, aas.SubmodelElement):
                        specialCapabilities = self.SpecialCapabilities(specialCapabilities)

                    # Build a submodel element if a raw value was passed in the argument

                    if protectionClassIP is not None and not isinstance(protectionClassIP, aas.SubmodelElement):
                        protectionClassIP = self.ProtectionClassIP(protectionClassIP)

                    # Build a submodel element if a raw value was passed in the argument

                    if suitableForOutdoorUse is not None and not isinstance(suitableForOutdoorUse, aas.SubmodelElement):
                        suitableForOutdoorUse = self.SuitableForOutdoorUse(suitableForOutdoorUse)

                    # Build a submodel element if a raw value was passed in the argument

                    if requiredEnvironmentalConditions is not None and not isinstance(
                        requiredEnvironmentalConditions, aas.SubmodelElement
                    ):
                        requiredEnvironmentalConditions = self.RequiredEnvironmentalConditions(
                            requiredEnvironmentalConditions
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if specialQualificationDemand is not None and not isinstance(
                        specialQualificationDemand, aas.SubmodelElement
                    ):
                        specialQualificationDemand = self.SpecialQualificationDemand(specialQualificationDemand)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        agvKinematic,
                        agvClass,
                        travelDirection,
                        transportPrinciple,
                        localizationType,
                        navigationType,
                        specialApplications,
                        specialCapabilities,
                        protectionClassIP,
                        suitableForOutdoorUse,
                        requiredEnvironmentalConditions,
                        specialQualificationDemand,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TechnicalParameters(aas.SubmodelElementCollection):

                class MaxLateralInclinationMaxLoad(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxLateralInclinationMaxLoad",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Lateral inclination (max.)", r"de": r"Querneigung (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximal lateral inclination of the AGV when loaded with the maximum weight",
                                    r"de": r"Maximale Querneigung des AGV bei Beladung mit maximaler Last",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/maxlateralinclination/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"with max. load",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaxLateralInclinationWithoutLoad(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxLateralInclinationWithoutLoad",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Lateral inclination (max.)", r"de": r"Querneigung (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximal lateral inclination of the AGV when unloaded",
                                    r"de": r"Maximale Querneigung des AGV wenn ohne Last",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/maxlateralinclination/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"without load",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaxClimbingInclinationMaxLoad(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxClimbingInclinationMaxLoad",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Climbing inclination (max.)", r"de": r"Längsneigung (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximal climbing inclination of the AGV when loaded with the maximum weight",
                                    r"de": r"Maximale Längsneigung des AGV bei maximaler Last",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/maxclimbinginclination/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"with max. load",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaxClimbingInclinationWithoutLoad(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxClimbingInclinationWithoutLoad",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Climbing inclination (max.)", r"de": r"Längsneigung (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximal climbing inclination of the AGV when unloaded",
                                    r"de": r"Maximale Längsneigung des AGV wenn ohne Last",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/maxclimbinginclination/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"without load",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalizationSensorDetails(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"LocalizationSensorDetails",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Localization sensor details",
                                    r"de": r"Details zur Lokalisierungssensorik",
                                }
                            ),
                            "category": r"CONSTANT",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Information about used localization sensors by the AGV"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/localizationsensordetails/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalizationAccuracy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalizationAccuracy",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Localization accuracy", r"de": r"Lokalisierungsgenauigkeit"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Accuracy of the determination of the current location of the AGV"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/localizationaccuracy/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PositioningAccuracy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PositioningAccuracy",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Positioning accuracy", r"de": r"Positionierungsgenauigkeit"}
                            ),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Positioning accuracy of the AGV"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/positioningaccuracy/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaxLoadMass(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxLoadMass",
                            "value_type": xsd.Float,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Maximal load on the AGV including attachments and load"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABJ258#001"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class InterfacesForAttachments(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"InterfacesForAttachments",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Interfaces for attachments", r"de": r"Schnittstellen für Anbauten"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the mechanical and electrical interfaces for load handling attachments and other attachments"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/interfacesforattachments/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SystemAvailability(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SystemAvailability",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"System availability", r"de": r"Systemverfügbarkeit"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"System availability of the AGV ",
                                    r"de": r"Systemverfügbarkeit des AGV ",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABA730#002"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaxRunTimeAsSpecified(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxRunTimeAsSpecified",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Run time (max.)", r"de": r"Run time (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Max runtime as stated in the specification sheet of the AGV",
                                    r"de": r"Maximale Laufzeit wie für das AGV vom Hersteller spezifiziert",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAJ479#004"),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"SPEC",
                                    value_id=global_ref(r"0112/2///61360_4#AAF579"),
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaxRunTimeAsOperated(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxRunTimeAsOperated",
                            "value_type": int,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Run time (max.)", r"de": r"Laufzeit (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Max runtime as the AGV is operated in the current environment",
                                    r"de": r"Maximale Laufzeit des AGV wie aktuell im Gesamtsystem implementiert",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAJ479#004"),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"OP",
                                    value_id=global_ref(r"0112/2///61360_4#AAF578"),
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpeedMin(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SpeedMin",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Speed (min.)", r"de": r"Geschwindigkeit (min.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Minimum controlled continuous speed"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/speedmin/1/0"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpeedMaxEmptyAsSpecified(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SpeedMaxEmptyAsSpecified",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Speed without load (max.)",
                                    r"de": r"Geschwindigkeit ohne Ladung (max.)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum speed without load as specified by the manufacturer",
                                    r"de": r"Maximale Geschwindigkeit ohne Beladung wie durch den Hersteller spezifiziert",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/speedmaxempty/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"SPEC",
                                    value_id=global_ref(r"0112/2///61360_4#AAF573"),
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpeedMaxEmptyAsOperated(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SpeedMaxEmptyAsOperated",
                            "value_type": xsd.Float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum speed without load as in the current system operated",
                                    r"de": r"Maximale Geschwindigkeit ohne Beladung wie im aktuellen System betrieben",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/speedmaxempty/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"OP",
                                    value_id=global_ref(r"0112/2///61360_4#AAF578"),
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpeedMaxWithMaxLoadAsSpecified(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SpeedMaxWithMaxLoadAsSpecified",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Speed with maximum load (max.)",
                                    r"de": r"Geschwindigkeit mit maximaler Ladung (max.)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum speed with maximal load as specified by the manufacturer",
                                    r"de": r"Maximale Geschwindigkeit bei maximal zulässiger Beladung wie durch den Hersteller vorgegeben",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/speedmaxwithmaxload/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"SPEC",
                                    value_id=global_ref(r"0112/2///61360_4#AAF579"),
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SpeedMaxWithMaxLoadAsOperated(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SpeedMaxWithMaxLoadAsOperated",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Speed with maximum load (max.)",
                                    r"de": r"Geschwindigkeit mit maximaler Ladung (max.)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum speed with maximal load as operated in the current system",
                                    r"de": r"Maximale Geschwindigkeit bei maximal zulässiger Beladung wie im aktuellen System betrieben",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/speedmaxwithmaxload/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"OP",
                                    value_id=global_ref(r"0112/2///61360_4#AAF579"),
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AccelerationMax(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AccelerationMax",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Acceleration (max.)", r"de": r"Beschleuniging (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum acceleration of the AGV with maximum load",
                                    r"de": r"Maximale Beschleunigung des AGV mit maximaler Last",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABG746#002"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DecelerationMax(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DecelerationMax",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Maximum deceleration", r"de": r"Maximale Verzögerung"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum deceleration of the AGV with maximum load",
                                    r"de": r"Maximale Verzögerung des AGV mit maximaler Last",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/decelerationmax/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VehicleHeightMax(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"VehicleHeightMax",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Vehicle height (max.)", r"de": r"Fahrzeughöhe (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum height of the AGV without attachments",
                                    r"de": r"Maximale Höhe des AGV ohne Anbauten",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-BAE355#006"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VehicleWidth(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"VehicleWidth",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Vehicle width (max.)", r"de": r"Fahrzeugbreite (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Maximum vehicle width", r"de": r"Maximale Fahrzeugbreite"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAG933#004"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VehicleLength(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"VehicleLength",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Vehicle length (max.)", r"de": r"Fahrzeuglänge (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum lengths of the AGV including outstanding components",
                                    r"de": r"Maximale Länge des AGV einschließlich überstehender Komponenten",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABE774#002"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VehicleWeight(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"VehicleWeight",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Vehicle weight (max.)", r"de": r"Fahrzeuggewicht (max.)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum weight of the AGV without necessary weights",
                                    r"de": r"Maximales Gewicht des AGV ohne Gegengewichte",
                                }
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABD800#002"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Emissions(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"Emissions",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"emissions", r"de": r"Emissionen"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of emissions of the AGV during operation, e.g. noise or exhaust"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/emissions/1/0"),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MapProcessingInformation(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"MapProcessingInformation",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Map processing information",
                                    r"de": r"Informationen zur Kartenverarbeitung",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about how the digital map is generated and processed by the AGV"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/mapprocessinginformation/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ManualControllerInformation(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ManualControllerInformation",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Manual controller information",
                                    r"de": r"Informationen zur manuellen Steuerung",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Information about the manual controllers of the AGV"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/manualcontrollerinformation/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DigitalAnalogInterfaces(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"DigitalAnalogInterfaces",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Digital and analog interfaces",
                                    r"de": r"Digitale und analoge Schnittstellen",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Information about digital and analog interfaces of the AGV"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/digitalanaloginterfaces/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"TechnicalParameters",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Technical parameters", r"de": r"Technische Parameter"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Technical parameters/properties of the AGV"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/technicaldataagv/technicalparameters/1/0"
                        ),
                    }

                def __init__(
                    self,
                    maxLateralInclinationMaxLoad: Optional[Union[int, MaxLateralInclinationMaxLoad]] = None,
                    maxLateralInclinationWithoutLoad: Optional[Union[int, MaxLateralInclinationWithoutLoad]] = None,
                    maxClimbingInclinationMaxLoad: Optional[Union[int, MaxClimbingInclinationMaxLoad]] = None,
                    maxClimbingInclinationWithoutLoad: Optional[Union[int, MaxClimbingInclinationWithoutLoad]] = None,
                    localizationSensorDetails: Optional[Union[aas.LangStringSet, LocalizationSensorDetails]] = None,
                    localizationAccuracy: Optional[Union[xsd.Float, LocalizationAccuracy]] = None,
                    positioningAccuracy: Optional[Union[xsd.Float, PositioningAccuracy]] = None,
                    maxLoadMass: Optional[Union[xsd.Float, MaxLoadMass]] = None,
                    interfacesForAttachments: Optional[Union[aas.LangStringSet, InterfacesForAttachments]] = None,
                    systemAvailability: Optional[Union[xsd.Float, SystemAvailability]] = None,
                    maxRunTimeAsSpecified: Optional[Union[int, MaxRunTimeAsSpecified]] = None,
                    maxRunTimeAsOperated: Optional[Union[int, MaxRunTimeAsOperated]] = None,
                    speedMin: Optional[Union[xsd.Float, SpeedMin]] = None,
                    speedMaxEmptyAsSpecified: Optional[Union[xsd.Float, SpeedMaxEmptyAsSpecified]] = None,
                    speedMaxEmptyAsOperated: Optional[Union[xsd.Float, SpeedMaxEmptyAsOperated]] = None,
                    speedMaxWithMaxLoadAsSpecified: Optional[Union[xsd.Float, SpeedMaxWithMaxLoadAsSpecified]] = None,
                    speedMaxWithMaxLoadAsOperated: Optional[Union[xsd.Float, SpeedMaxWithMaxLoadAsOperated]] = None,
                    accelerationMax: Optional[Union[xsd.Float, AccelerationMax]] = None,
                    decelerationMax: Optional[Union[xsd.Float, DecelerationMax]] = None,
                    vehicleHeightMax: Optional[Union[xsd.Float, VehicleHeightMax]] = None,
                    vehicleWidth: Optional[Union[str, VehicleWidth]] = None,
                    vehicleLength: Optional[Union[str, VehicleLength]] = None,
                    vehicleWeight: Optional[Union[str, VehicleWeight]] = None,
                    emissions: Optional[Union[aas.LangStringSet, Emissions]] = None,
                    mapProcessingInformation: Optional[Union[aas.LangStringSet, MapProcessingInformation]] = None,
                    manualControllerInformation: Optional[Union[aas.LangStringSet, ManualControllerInformation]] = None,
                    digitalAnalogInterfaces: Optional[Union[aas.LangStringSet, DigitalAnalogInterfaces]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if maxLateralInclinationMaxLoad is not None and not isinstance(
                        maxLateralInclinationMaxLoad, aas.SubmodelElement
                    ):
                        maxLateralInclinationMaxLoad = self.MaxLateralInclinationMaxLoad(maxLateralInclinationMaxLoad)

                    # Build a submodel element if a raw value was passed in the argument

                    if maxLateralInclinationWithoutLoad is not None and not isinstance(
                        maxLateralInclinationWithoutLoad, aas.SubmodelElement
                    ):
                        maxLateralInclinationWithoutLoad = self.MaxLateralInclinationWithoutLoad(
                            maxLateralInclinationWithoutLoad
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if maxClimbingInclinationMaxLoad is not None and not isinstance(
                        maxClimbingInclinationMaxLoad, aas.SubmodelElement
                    ):
                        maxClimbingInclinationMaxLoad = self.MaxClimbingInclinationMaxLoad(
                            maxClimbingInclinationMaxLoad
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if maxClimbingInclinationWithoutLoad is not None and not isinstance(
                        maxClimbingInclinationWithoutLoad, aas.SubmodelElement
                    ):
                        maxClimbingInclinationWithoutLoad = self.MaxClimbingInclinationWithoutLoad(
                            maxClimbingInclinationWithoutLoad
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if localizationSensorDetails is not None and not isinstance(
                        localizationSensorDetails, aas.SubmodelElement
                    ):
                        localizationSensorDetails = self.LocalizationSensorDetails(localizationSensorDetails)

                    # Build a submodel element if a raw value was passed in the argument

                    if localizationAccuracy is not None and not isinstance(localizationAccuracy, aas.SubmodelElement):
                        localizationAccuracy = self.LocalizationAccuracy(localizationAccuracy)

                    # Build a submodel element if a raw value was passed in the argument

                    if positioningAccuracy is not None and not isinstance(positioningAccuracy, aas.SubmodelElement):
                        positioningAccuracy = self.PositioningAccuracy(positioningAccuracy)

                    # Build a submodel element if a raw value was passed in the argument

                    if maxLoadMass is not None and not isinstance(maxLoadMass, aas.SubmodelElement):
                        maxLoadMass = self.MaxLoadMass(maxLoadMass)

                    # Build a submodel element if a raw value was passed in the argument

                    if interfacesForAttachments is not None and not isinstance(
                        interfacesForAttachments, aas.SubmodelElement
                    ):
                        interfacesForAttachments = self.InterfacesForAttachments(interfacesForAttachments)

                    # Build a submodel element if a raw value was passed in the argument

                    if systemAvailability is not None and not isinstance(systemAvailability, aas.SubmodelElement):
                        systemAvailability = self.SystemAvailability(systemAvailability)

                    # Build a submodel element if a raw value was passed in the argument

                    if maxRunTimeAsSpecified is not None and not isinstance(maxRunTimeAsSpecified, aas.SubmodelElement):
                        maxRunTimeAsSpecified = self.MaxRunTimeAsSpecified(maxRunTimeAsSpecified)

                    # Build a submodel element if a raw value was passed in the argument

                    if maxRunTimeAsOperated is not None and not isinstance(maxRunTimeAsOperated, aas.SubmodelElement):
                        maxRunTimeAsOperated = self.MaxRunTimeAsOperated(maxRunTimeAsOperated)

                    # Build a submodel element if a raw value was passed in the argument

                    if speedMin is not None and not isinstance(speedMin, aas.SubmodelElement):
                        speedMin = self.SpeedMin(speedMin)

                    # Build a submodel element if a raw value was passed in the argument

                    if speedMaxEmptyAsSpecified is not None and not isinstance(
                        speedMaxEmptyAsSpecified, aas.SubmodelElement
                    ):
                        speedMaxEmptyAsSpecified = self.SpeedMaxEmptyAsSpecified(speedMaxEmptyAsSpecified)

                    # Build a submodel element if a raw value was passed in the argument

                    if speedMaxEmptyAsOperated is not None and not isinstance(
                        speedMaxEmptyAsOperated, aas.SubmodelElement
                    ):
                        speedMaxEmptyAsOperated = self.SpeedMaxEmptyAsOperated(speedMaxEmptyAsOperated)

                    # Build a submodel element if a raw value was passed in the argument

                    if speedMaxWithMaxLoadAsSpecified is not None and not isinstance(
                        speedMaxWithMaxLoadAsSpecified, aas.SubmodelElement
                    ):
                        speedMaxWithMaxLoadAsSpecified = self.SpeedMaxWithMaxLoadAsSpecified(
                            speedMaxWithMaxLoadAsSpecified
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if speedMaxWithMaxLoadAsOperated is not None and not isinstance(
                        speedMaxWithMaxLoadAsOperated, aas.SubmodelElement
                    ):
                        speedMaxWithMaxLoadAsOperated = self.SpeedMaxWithMaxLoadAsOperated(
                            speedMaxWithMaxLoadAsOperated
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if accelerationMax is not None and not isinstance(accelerationMax, aas.SubmodelElement):
                        accelerationMax = self.AccelerationMax(accelerationMax)

                    # Build a submodel element if a raw value was passed in the argument

                    if decelerationMax is not None and not isinstance(decelerationMax, aas.SubmodelElement):
                        decelerationMax = self.DecelerationMax(decelerationMax)

                    # Build a submodel element if a raw value was passed in the argument

                    if vehicleHeightMax is not None and not isinstance(vehicleHeightMax, aas.SubmodelElement):
                        vehicleHeightMax = self.VehicleHeightMax(vehicleHeightMax)

                    # Build a submodel element if a raw value was passed in the argument

                    if vehicleWidth is not None and not isinstance(vehicleWidth, aas.SubmodelElement):
                        vehicleWidth = self.VehicleWidth(vehicleWidth)

                    # Build a submodel element if a raw value was passed in the argument

                    if vehicleLength is not None and not isinstance(vehicleLength, aas.SubmodelElement):
                        vehicleLength = self.VehicleLength(vehicleLength)

                    # Build a submodel element if a raw value was passed in the argument

                    if vehicleWeight is not None and not isinstance(vehicleWeight, aas.SubmodelElement):
                        vehicleWeight = self.VehicleWeight(vehicleWeight)

                    # Build a submodel element if a raw value was passed in the argument

                    if emissions is not None and not isinstance(emissions, aas.SubmodelElement):
                        emissions = self.Emissions(emissions)

                    # Build a submodel element if a raw value was passed in the argument

                    if mapProcessingInformation is not None and not isinstance(
                        mapProcessingInformation, aas.SubmodelElement
                    ):
                        mapProcessingInformation = self.MapProcessingInformation(mapProcessingInformation)

                    # Build a submodel element if a raw value was passed in the argument

                    if manualControllerInformation is not None and not isinstance(
                        manualControllerInformation, aas.SubmodelElement
                    ):
                        manualControllerInformation = self.ManualControllerInformation(manualControllerInformation)

                    # Build a submodel element if a raw value was passed in the argument

                    if digitalAnalogInterfaces is not None and not isinstance(
                        digitalAnalogInterfaces, aas.SubmodelElement
                    ):
                        digitalAnalogInterfaces = self.DigitalAnalogInterfaces(digitalAnalogInterfaces)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        maxLateralInclinationMaxLoad,
                        maxLateralInclinationWithoutLoad,
                        maxClimbingInclinationMaxLoad,
                        maxClimbingInclinationWithoutLoad,
                        localizationSensorDetails,
                        localizationAccuracy,
                        positioningAccuracy,
                        maxLoadMass,
                        interfacesForAttachments,
                        systemAvailability,
                        maxRunTimeAsSpecified,
                        maxRunTimeAsOperated,
                        speedMin,
                        speedMaxEmptyAsSpecified,
                        speedMaxEmptyAsOperated,
                        speedMaxWithMaxLoadAsSpecified,
                        speedMaxWithMaxLoadAsOperated,
                        accelerationMax,
                        decelerationMax,
                        vehicleHeightMax,
                        vehicleWidth,
                        vehicleLength,
                        vehicleWeight,
                        emissions,
                        mapProcessingInformation,
                        manualControllerInformation,
                        digitalAnalogInterfaces,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class VDA5050Factsheet(aas.SubmodelElementCollection):

                class TypeSpecification(aas.Blob):

                    @staticmethod
                    def template_defaults() -> BlobMetadata:
                        return {
                            "id_short": r"TypeSpecification",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"typeSpecification (JSON-object)",
                                    r"de": r"typeSpecification (JSON-Objekt)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'JSON-object "typeSpecification" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                    r"de": r'JSON-Objekt "typeSpecification" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/typespecification/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: Optional[bytes] = None,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[BlobMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class PhysicalParameters(aas.Blob):

                    @staticmethod
                    def template_defaults() -> BlobMetadata:
                        return {
                            "id_short": r"PhysicalParameters",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"physicalParameters (JSON-object)",
                                    r"de": r"physicalParameters (JSON-Objekt)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'JSON-object "physicalParameters" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                    r"de": r'JSON-Objekt "physicalParameters" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/pysicalparameters/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: Optional[bytes] = None,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[BlobMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class ProtocolLimits(aas.Blob):

                    @staticmethod
                    def template_defaults() -> BlobMetadata:
                        return {
                            "id_short": r"ProtocolLimits",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"protocolLimits (JSON-object)", r"de": r"protocolLimits (JSON-Objekt)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'JSON-object "protocolLimits" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                    r"de": r'JSON-Objekt "protocolLimits" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/protocollimits/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: Optional[bytes] = None,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[BlobMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class ProtocolFeatures(aas.Blob):

                    @staticmethod
                    def template_defaults() -> BlobMetadata:
                        return {
                            "id_short": r"ProtocolFeatures",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"protocolFeatures (JSON-object)",
                                    r"de": r"protocolFeatures (JSON-Objekt)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'JSON-object "protocolFeatures" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                    r"de": r'JSON-Objekt "protocolFeatures" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/protocolfeatures/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: Optional[bytes] = None,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[BlobMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class AgvGeometry(aas.Blob):

                    @staticmethod
                    def template_defaults() -> BlobMetadata:
                        return {
                            "id_short": r"AgvGeometry",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"agvGeometry (JSON-object)", r"de": r"agvGeometry (JSON-Objekt)"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'JSON-object "agvGeometry" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                    r"de": r'JSON-Objekt "agvGeometry" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/agvgeometry/1/0"),
                        }

                    def __init__(
                        self,
                        value: Optional[bytes] = None,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[BlobMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class LoadSpecification(aas.Blob):

                    @staticmethod
                    def template_defaults() -> BlobMetadata:
                        return {
                            "id_short": r"LoadSpecification",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"loadSpecification (JSON-object)",
                                    r"de": r"loadSpecification (JSON-Objekt)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'JSON-object "loadSpecification" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                    r"de": r'JSON-Objekt "loadSpecification" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/loadspecification/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: Optional[bytes] = None,
                        content_type: Optional[str] = r"application/json",
                        **kwargs: Unpack[BlobMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class LocalizationParameters(aas.Blob):

                    @staticmethod
                    def template_defaults() -> BlobMetadata:
                        return {
                            "id_short": r"LocalizationParameters",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"localizationParameters (JSON-object)",
                                    r"de": r"localizationParameters (JSON-Objekt)",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'JSON-object "localizationParameters" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                    r"de": r'JSON-Objekt "localizationParameters" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/localizationparameters/1/0"
                            ),
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
                        "id_short": r"VDA5050Factsheet",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Factsheet data according VDA 5050 MQTT communication protocol"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/vda5050factsheet/1/0"),
                    }

                def __init__(
                    self,
                    typeSpecification: Optional[TypeSpecification] = None,
                    physicalParameters: Optional[PhysicalParameters] = None,
                    protocolLimits: Optional[ProtocolLimits] = None,
                    protocolFeatures: Optional[ProtocolFeatures] = None,
                    agvGeometry: Optional[AgvGeometry] = None,
                    loadSpecification: Optional[LoadSpecification] = None,
                    localizationParameters: Optional[LocalizationParameters] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        typeSpecification,
                        physicalParameters,
                        protocolLimits,
                        protocolFeatures,
                        agvGeometry,
                        loadSpecification,
                        localizationParameters,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Energy(aas.SubmodelElementCollection):

                class EnergySource(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EnergySource",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Energy source", r"de": r"Energiequelle"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Type of auxiliary energy the AGV is consuming, the enumeration "POWER", "DIESEL", "GAS", "HYDROGEN", "HYBRID", "SOLAR", "OTHER" can be used'
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/energysource/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EnergyAbsorption(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EnergyAbsorption",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Energy absorption", r"de": r"Energieaufnahme"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Way to absorb auxiliary energy. The enumeration "INDUCTION", "CONDUCTORRAIL", "FLEXIBLECABLE", "CHARGINGCABLE", "FILLER", "OTHER" can be used'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/energyabsorption/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EnergyStorage(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EnergyStorage",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Energy storage", r"de": r"Energiespeicher"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Type of storage the AGV is using. The enumeration "BATTERY", "TANK", "CARTRIDGE", "CAPACITOR", "OTHER" can be used.'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/energystorage/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Battery(aas.SubmodelElementCollection):

                    class ChargingDeviceRequirements(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"ChargingDeviceRequirements",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Charging device requirements",
                                        r"de": r"Anforderungen an die Ladestation",
                                    }
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Requirements of the AGV for the charging station and infrastructure, e.g., voltage range or max. current"
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/technicaldataagv/chargingdevicerequirements/1/0"
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class BatteryInformation(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"BatteryInformation",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Battery information", r"de": r"Informationen zur Batterie"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Information about the used battery of the AGV, for example type of battery (e.g., NiCd), capacity and max. charge cycles"
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/technicaldataagv/batteryinformation/1/0"
                                ),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ChargingTimeAsSpecified(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ChargingTimeAsSpecified",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Charging time", r"de": r"Ladedauer"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Charging time of the AGV from empty to full capacity as specified by the manufacturer",
                                        r"de": r"Ladedauer des AGV von leer nach voll wie vom Hersteller spezifiziert",
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAF391#006"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"LifeCycleQual",
                                        value_type=str,
                                        value=r"SPEC",
                                        value_id=global_ref(r"0112/2///61360_4#AAF579"),
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ChargingTimeAsOperated(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ChargingTimeAsOperated",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Charging time", r"de": r"Ladedauer"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Charging time of the AGV from empty to full capacity as implemented in the current system",
                                        r"de": r"Ladedauer des AGV von leer nach voll, wie im aktuellen System implementiert",
                                    }
                                ),
                                "semantic_id": global_ref(r"0173-1#02-AAF391#006"),
                                "qualifier": (
                                    aas.Qualifier(
                                        type_=r"LifeCycleQual",
                                        value_type=str,
                                        value=r"OP",
                                        value_id=global_ref(r"0112/2///61360_4#AAF579"),
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=global_ref(r"0112/2///61360_4#AAF575"),
                                        supplemental_semantic_id=(),
                                    ),
                                ),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class RemainingChargeCycles(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"RemainingChargeCycles",
                                "value_type": int,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Remaining charge cycles", r"de": r"Verbleibende Ladezyklen"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Assumed remaining charge cycles of the battery"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/technicaldataagv/remainingchargecycles/1/0"
                                ),
                            }

                        def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Battery",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Information about the battery of the AGV"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/battery/1/0"),
                        }

                    def __init__(
                        self,
                        chargingDeviceRequirements: Optional[
                            Union[aas.LangStringSet, ChargingDeviceRequirements]
                        ] = None,
                        batteryInformation: Optional[Union[aas.LangStringSet, BatteryInformation]] = None,
                        chargingTimeAsSpecified: Optional[Union[xsd.Float, ChargingTimeAsSpecified]] = None,
                        chargingTimeAsOperated: Optional[Union[xsd.Float, ChargingTimeAsOperated]] = None,
                        remainingChargeCycles: Optional[Union[int, RemainingChargeCycles]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if chargingDeviceRequirements is not None and not isinstance(
                            chargingDeviceRequirements, aas.SubmodelElement
                        ):
                            chargingDeviceRequirements = self.ChargingDeviceRequirements(chargingDeviceRequirements)

                        # Build a submodel element if a raw value was passed in the argument

                        if batteryInformation is not None and not isinstance(batteryInformation, aas.SubmodelElement):
                            batteryInformation = self.BatteryInformation(batteryInformation)

                        # Build a submodel element if a raw value was passed in the argument

                        if chargingTimeAsSpecified is not None and not isinstance(
                            chargingTimeAsSpecified, aas.SubmodelElement
                        ):
                            chargingTimeAsSpecified = self.ChargingTimeAsSpecified(chargingTimeAsSpecified)

                        # Build a submodel element if a raw value was passed in the argument

                        if chargingTimeAsOperated is not None and not isinstance(
                            chargingTimeAsOperated, aas.SubmodelElement
                        ):
                            chargingTimeAsOperated = self.ChargingTimeAsOperated(chargingTimeAsOperated)

                        # Build a submodel element if a raw value was passed in the argument

                        if remainingChargeCycles is not None and not isinstance(
                            remainingChargeCycles, aas.SubmodelElement
                        ):
                            remainingChargeCycles = self.RemainingChargeCycles(remainingChargeCycles)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            chargingDeviceRequirements,
                            batteryInformation,
                            chargingTimeAsSpecified,
                            chargingTimeAsOperated,
                            remainingChargeCycles,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class PowerTransmissionToExternal(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"PowerTransmissionToExternal",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Power transmission to external",
                                    r"de": r"Energieübertragung nach extern",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about mechanical or electrical power transmission capabilities from the AGV to external devices"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/powertransmissionexternal/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Energy",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Technical properties related to the energy supply of the AGV"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/energy/1/0"),
                    }

                def __init__(
                    self,
                    battery: Battery,
                    energySource: Optional[Union[str, EnergySource]] = None,
                    energyAbsorption: Optional[Union[str, EnergyAbsorption]] = None,
                    energyStorage: Optional[Union[str, EnergyStorage]] = None,
                    powerTransmissionToExternal: Optional[Union[aas.LangStringSet, PowerTransmissionToExternal]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if energySource is not None and not isinstance(energySource, aas.SubmodelElement):
                        energySource = self.EnergySource(energySource)

                    # Build a submodel element if a raw value was passed in the argument

                    if energyAbsorption is not None and not isinstance(energyAbsorption, aas.SubmodelElement):
                        energyAbsorption = self.EnergyAbsorption(energyAbsorption)

                    # Build a submodel element if a raw value was passed in the argument

                    if energyStorage is not None and not isinstance(energyStorage, aas.SubmodelElement):
                        energyStorage = self.EnergyStorage(energyStorage)

                    # Build a submodel element if a raw value was passed in the argument

                    if powerTransmissionToExternal is not None and not isinstance(
                        powerTransmissionToExternal, aas.SubmodelElement
                    ):
                        powerTransmissionToExternal = self.PowerTransmissionToExternal(powerTransmissionToExternal)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        energySource, energyAbsorption, energyStorage, battery, powerTransmissionToExternal
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class CommunicationAndControl(aas.SubmodelElementCollection):

                class CommunicationProtocol(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"CommunicationProtocol",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Communication protocol", r"de": r"Kommunikationsprotokoll"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information regarding the supported communication protocols, like MQTT, HTTP, OPC UA or ROS2"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/communicationprotocol/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class CommunicationNetwork(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"CommunicationNetwork",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Communication network", r"de": r"Kommunikationsnetzwerk"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information regarding the supported communication networks, like WLAN, 5G or IrDA"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/communicationnetwork/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VDA5050InterfaceDescription(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"VDA5050InterfaceDescription",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"VDA5050 Interface Description",
                                    r"de": r"VDA5050 Schnittstellenbeschreibung",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Information about the MQTT communication according VDA 5050"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/vda5050interfacedescription/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AutomationInterface(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"AutomationInterface",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Automation interface", r"de": r"Automatisierungsschnittstellen"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about the supported automation interfaces and standards, like ROS1, ROS2, IO-Link or OPC UA"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/automationinterface/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ControlSystemInformation(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ControlSystemInformation",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Control system information", r"de": r"Informationen zur Steuerung"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information regarding the used control system for the vehicle, e.g., SPS"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/controlsysteminformation/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"CommunicationAndControl",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Technical properties related to the communication and control of the AGV"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/technicaldataagv/communicationandcontrol/1/0"
                        ),
                    }

                def __init__(
                    self,
                    communicationProtocol: Optional[Union[aas.LangStringSet, CommunicationProtocol]] = None,
                    communicationNetwork: Optional[Union[aas.LangStringSet, CommunicationNetwork]] = None,
                    vDA5050InterfaceDescription: Optional[Union[aas.LangStringSet, VDA5050InterfaceDescription]] = None,
                    automationInterface: Optional[Union[aas.LangStringSet, AutomationInterface]] = None,
                    controlSystemInformation: Optional[Union[aas.LangStringSet, ControlSystemInformation]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if communicationProtocol is not None and not isinstance(communicationProtocol, aas.SubmodelElement):
                        communicationProtocol = self.CommunicationProtocol(communicationProtocol)

                    # Build a submodel element if a raw value was passed in the argument

                    if communicationNetwork is not None and not isinstance(communicationNetwork, aas.SubmodelElement):
                        communicationNetwork = self.CommunicationNetwork(communicationNetwork)

                    # Build a submodel element if a raw value was passed in the argument

                    if vDA5050InterfaceDescription is not None and not isinstance(
                        vDA5050InterfaceDescription, aas.SubmodelElement
                    ):
                        vDA5050InterfaceDescription = self.VDA5050InterfaceDescription(vDA5050InterfaceDescription)

                    # Build a submodel element if a raw value was passed in the argument

                    if automationInterface is not None and not isinstance(automationInterface, aas.SubmodelElement):
                        automationInterface = self.AutomationInterface(automationInterface)

                    # Build a submodel element if a raw value was passed in the argument

                    if controlSystemInformation is not None and not isinstance(
                        controlSystemInformation, aas.SubmodelElement
                    ):
                        controlSystemInformation = self.ControlSystemInformation(controlSystemInformation)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        communicationProtocol,
                        communicationNetwork,
                        vDA5050InterfaceDescription,
                        automationInterface,
                        controlSystemInformation,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Safety(aas.SubmodelElementCollection):

                class ConformityToSafetyStandards(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ConformityToSafetyStandards",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Conformity to safety standards",
                                    r"de": r"Konformität zu Sicherheitsstandards",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information regarding the safety standards that are met by the vehicle and certifications"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/conformitytosafetystandards/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ManualControlInformation(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ManualControlInformation",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Manual control information",
                                    r"de": r"Informationen zur manuellen Steuerung",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Safety information for manual control of the vehicle"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/manualcontrolinformation/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SafetySensorTechnology(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"SafetySensorTechnology",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Safety sensor technology", r"de": r"Sicherheitssensorik"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about the sensor technology implemented to ensure vehicle safety"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/safetysensortechnology/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SafetyMechanics(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"SafetyMechanics",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Safety mechanics", r"de": r"Mechanische Sicherheitseinrichtungen"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Information regarding implemented mechanical measures to ensure safety"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/safetymechanics/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Safety",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Technical properties related to the safety of the AGV"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/safety/1/0"),
                    }

                def __init__(
                    self,
                    conformityToSafetyStandards: Optional[Union[aas.LangStringSet, ConformityToSafetyStandards]] = None,
                    manualControlInformation: Optional[Union[aas.LangStringSet, ManualControlInformation]] = None,
                    safetySensorTechnology: Optional[Union[aas.LangStringSet, SafetySensorTechnology]] = None,
                    safetyMechanics: Optional[Union[aas.LangStringSet, SafetyMechanics]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if conformityToSafetyStandards is not None and not isinstance(
                        conformityToSafetyStandards, aas.SubmodelElement
                    ):
                        conformityToSafetyStandards = self.ConformityToSafetyStandards(conformityToSafetyStandards)

                    # Build a submodel element if a raw value was passed in the argument

                    if manualControlInformation is not None and not isinstance(
                        manualControlInformation, aas.SubmodelElement
                    ):
                        manualControlInformation = self.ManualControlInformation(manualControlInformation)

                    # Build a submodel element if a raw value was passed in the argument

                    if safetySensorTechnology is not None and not isinstance(
                        safetySensorTechnology, aas.SubmodelElement
                    ):
                        safetySensorTechnology = self.SafetySensorTechnology(safetySensorTechnology)

                    # Build a submodel element if a raw value was passed in the argument

                    if safetyMechanics is not None and not isinstance(safetyMechanics, aas.SubmodelElement):
                        safetyMechanics = self.SafetyMechanics(safetyMechanics)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        conformityToSafetyStandards, manualControlInformation, safetySensorTechnology, safetyMechanics
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TemporaryTechnicalData(aas.SubmodelElementCollection):

                class CurrentWorkingSetupName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"CurrentWorkingSetupName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Current working setup ", r"de": r"Aktuelle Arbeitskonfiguration"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Name of the current working setup"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/currentworkingsetup/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ActiveLoading(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ActiveLoading",
                            "value_type": bool,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Active loading", r"de": r"Aktive Beladung"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Describes whether the AGV is currently able to load itself (true)"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/activeloading/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LoadingType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LoadingType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Loading type", r"de": r"Beladungsart"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Way of loading of the AGV, the enumeration acc. VDI 2510 can be used"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/technicaldataagv/loadingtype/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LoadingRequirements(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"LoadingRequirements",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Loading requirements", r"de": r"Beladungsanforderungen"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Requirements and instructions when loading with the current setup, e.g., load floor to floor vs. height difference"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/loadingrequirements/1/0"
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class CurrentAttachments(GeneratedSubmodelElementList):

                    class Currentattachments_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Attachment (ID)", r"de": r"Anbau (ID)"}
                                ),
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Order not relevant"}),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/technicaldataagv/attachmentid/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"CurrentAttachments",
                            "type_value_list_element": aas.Property,
                            "semantic_id_list_element": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/attachmentid/1/0"
                            ),
                            "value_type_list_element": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Current attachments", r"de": r"Aktuelle Anbauten "}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List with the identification of current attachments on the AGV, e.g., for load handling",
                                    r"de": r"Liste mit Idents der aktuellen Anbauten am AGV, z.B. für die Ladungshandhabung",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/currentattachments/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        currentattachments_items: Optional[Iterable[Union[str, Currentattachments_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(currentattachments_items, str):
                            raise TypeError("currentattachments_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if currentattachments_items:
                            currentattachments_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Currentattachments_item(i)
                                for i in currentattachments_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            currentattachments_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ProprietaryConfigurationOptions(GeneratedSubmodelElementList):

                    class Proprietaryconfigurationoptions_item(aas.SubmodelElementCollection):

                        class OptionName(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"OptionName",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Option name", r"de": r"Optionsname"}
                                    ),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Name of the proprietary configuration option"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/technicaldataagv/optionname/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class OptionValue(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"OptionValue",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(
                                        dict_={r"en": r"Option value", r"de": r"Optionswert"}
                                    ),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"Value of the proprietary option"}
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/technicaldataagv/optionvalue/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Configuration option", r"de": r"Konfigurationsoption"}
                                ),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Proprietary vehicle configuration setting"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/technicaldataagv/proprietaryconfigurationoptionsrecord/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            optionName: Union[str, OptionName],
                            optionValue: Union[str, OptionValue],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if optionName is not None and not isinstance(optionName, aas.SubmodelElement):
                                optionName = self.OptionName(optionName)

                            # Build a submodel element if a raw value was passed in the argument

                            if optionValue is not None and not isinstance(optionValue, aas.SubmodelElement):
                                optionValue = self.OptionValue(optionValue)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(optionName, optionValue)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ProprietaryConfigurationOptions",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id_list_element": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/proprietaryconfigurationoptionsrecord/1/0"
                            ),
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Proprietary configuration options",
                                    r"de": r"Herstellerspezifische Konfigurationsoptionen",
                                }
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List with proprietary vehicle configuration settings",
                                    r"de": r"Liste der herstellerspezifischen Konfigurationseinstellungen des Fahrzeugs",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/technicaldataagv/proprietaryconfigurationoptions/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        proprietaryconfigurationoptions_items: Optional[
                            Iterable[Proprietaryconfigurationoptions_item]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(proprietaryconfigurationoptions_items, str):
                            raise TypeError("proprietaryconfigurationoptions_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            proprietaryconfigurationoptions_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"TemporaryTechnicalData",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Temporary technical data depending on the implementation at the operator and current configuration"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/technicaldataagv/temporarytechnicaldata/1/0"
                        ),
                    }

                def __init__(
                    self,
                    currentWorkingSetupName: Optional[Union[str, CurrentWorkingSetupName]] = None,
                    activeLoading: Optional[Union[bool, ActiveLoading]] = None,
                    loadingType: Optional[Union[str, LoadingType]] = None,
                    loadingRequirements: Optional[Union[aas.LangStringSet, LoadingRequirements]] = None,
                    currentAttachments: Optional[
                        Union[Iterable[Union[str, CurrentAttachments.Currentattachments_item]], CurrentAttachments]
                    ] = None,
                    proprietaryConfigurationOptions: Optional[
                        Union[
                            Iterable[ProprietaryConfigurationOptions.Proprietaryconfigurationoptions_item],
                            ProprietaryConfigurationOptions,
                        ]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if currentWorkingSetupName is not None and not isinstance(
                        currentWorkingSetupName, aas.SubmodelElement
                    ):
                        currentWorkingSetupName = self.CurrentWorkingSetupName(currentWorkingSetupName)

                    # Build a submodel element if a raw value was passed in the argument

                    if activeLoading is not None and not isinstance(activeLoading, aas.SubmodelElement):
                        activeLoading = self.ActiveLoading(activeLoading)

                    # Build a submodel element if a raw value was passed in the argument

                    if loadingType is not None and not isinstance(loadingType, aas.SubmodelElement):
                        loadingType = self.LoadingType(loadingType)

                    # Build a submodel element if a raw value was passed in the argument

                    if loadingRequirements is not None and not isinstance(loadingRequirements, aas.SubmodelElement):
                        loadingRequirements = self.LoadingRequirements(loadingRequirements)

                    # A str would be split into its characters
                    if isinstance(currentAttachments, str):
                        raise TypeError("currentAttachments takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if currentAttachments is not None and not isinstance(currentAttachments, aas.SubmodelElement):
                        currentAttachments = self.CurrentAttachments(currentAttachments)

                    # A str would be split into its characters
                    if isinstance(proprietaryConfigurationOptions, str):
                        raise TypeError("proprietaryConfigurationOptions takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if proprietaryConfigurationOptions is not None and not isinstance(
                        proprietaryConfigurationOptions, aas.SubmodelElement
                    ):
                        proprietaryConfigurationOptions = self.ProprietaryConfigurationOptions(
                            proprietaryConfigurationOptions
                        )

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        currentWorkingSetupName,
                        activeLoading,
                        loadingType,
                        loadingRequirements,
                        currentAttachments,
                        proprietaryConfigurationOptions,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Specific description for a use case or area of ​​application",
                            r"de": r"Spezifische Beschreibung für einen Anwendungsfall oder ein Einsatzgebiet",
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABM221#001/0173-1#01-AHY912#001"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"Naming",
                            value_type=str,
                            value=r"Name of SMC is use case or application",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(r"https://admin-shell.io/SubmodelTemplates/Naming/1/0"),
                            supplemental_semantic_id=(),
                        ),
                    ),
                    "supplemental_semantic_id": (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABM221#001~0/0173-1#01-AHY912#001",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABM221-001/0173-1-01-AHY912-001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                }

            def __init__(
                self,
                dataSheet: Optional[DataSheet] = None,
                typeAndApplicationInformation: Optional[TypeAndApplicationInformation] = None,
                technicalParameters: Optional[TechnicalParameters] = None,
                vDA5050Factsheet: Optional[VDA5050Factsheet] = None,
                energy: Optional[Energy] = None,
                communicationAndControl: Optional[CommunicationAndControl] = None,
                safety: Optional[Safety] = None,
                temporaryTechnicalData: Optional[TemporaryTechnicalData] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    dataSheet,
                    typeAndApplicationInformation,
                    technicalParameters,
                    vDA5050Factsheet,
                    energy,
                    communicationAndControl,
                    safety,
                    temporaryTechnicalData,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"SpecificDescriptions",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#02-ABM221#001/0173-1#01-AHY912#001"),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Specific description for a use case or area of application"}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABM221#001"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABM221-001"),),
            }

        def __init__(
            self,
            specificdescriptions_items: Iterable[Specificdescriptions_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(specificdescriptions_items, str):
                raise TypeError("specificdescriptions_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(specificdescriptions_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"TechnicalDataAGV",
            "display_name": aas.MultiLanguageNameType(
                dict_={
                    r"en": r"Technical Data for AGV in Intralogistics",
                    r"de": r"Technische Daten für AGV in der Intralogistik",
                }
            ),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel containing technical data for AGV in intralogistcis",
                    r"de": r"Teilmodell, das die technischen Daten von AGV (Fahrerlose Transportfahrzeuge) enthält",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02047-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/technicaldataagv/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        generalInformation: GeneralInformation,
        specificDescriptions: Optional[
            Union[Iterable[SpecificDescriptions.Specificdescriptions_item], SpecificDescriptions]
        ] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(specificDescriptions, str):
            raise TypeError("specificDescriptions takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if specificDescriptions is not None and not isinstance(specificDescriptions, aas.SubmodelElement):
            specificDescriptions = self.SpecificDescriptions(specificDescriptions)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(generalInformation, specificDescriptions)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
