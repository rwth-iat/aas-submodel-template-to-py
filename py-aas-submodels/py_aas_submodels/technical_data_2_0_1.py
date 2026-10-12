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


class TechnicalData(aas.Submodel):

    class GeneralInformation(aas.SubmodelElementCollection):

        class ManufacturerName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer name", r"de": r"Herstellername"}
                    ),
                    "category": r"PARAMETER",
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
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Company logo", r"de": r"Firmenlogo"}),
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
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer product designation", r"de": r"Herstellerproduktbezeichnung"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-AAW338#003"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAW338-003"),),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ManufacturerArticleNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerArticleNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer article number", r"de": r"Herstellerartikelnummer"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-AAO676#005"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO676-005"),),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ManufacturerOrderCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerOrderCode",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer order code", r"de": r"Bestellcode des Herstellers"}
                    ),
                    "category": r"PARAMETER",
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
                        return {
                            "id_short": r"ImageFile",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Product image", r"de": r"Bildname Sachaufnahme"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABK291#002"),
                        }

                    def __init__(
                        self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class ImageNote(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ImageNote",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Image note", r"de": r"Bildhinweis"}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-ABL423#001"),
                            "supplemental_semantic_id": (
                                global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABL423-001"),
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

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
                    imageNote: Optional[Union[aas.MultiLanguageTextType, ImageNote]] = None,
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
                "semantic_id": global_ref(r"0173-1#02-ABK161#002/0173-1#01-AHX838#002"),
                "supplemental_semantic_id": (
                    global_ref(r"https://api.eclass-cdp.com/ 0173-1-02-ABK161-002/0173-1-01-AHX838-002"),
                ),
            }

        def __init__(
            self,
            manufacturerName: Union[str, ManufacturerName],
            manufacturerProductDesignation: Union[aas.MultiLanguageTextType, ManufacturerProductDesignation],
            manufacturerArticleNumber: Union[str, ManufacturerArticleNumber],
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

            if manufacturerArticleNumber is not None and not isinstance(manufacturerArticleNumber, aas.SubmodelElement):
                manufacturerArticleNumber = self.ManufacturerArticleNumber(manufacturerArticleNumber)

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
                manufacturerArticleNumber,
                manufacturerOrderCode,
                productImages,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ProductClassifications(GeneratedSubmodelElementList):

        class Productclassifications_item(aas.SubmodelElementCollection):

            class ClassificationSystem(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ClassificationSystem",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Classification system", r"de": r"Klassifikationssystem"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABL424#001"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABL424-001"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ClassificationSystemVersion(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ClassificationSystemVersion",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Classification system version", r"de": r"Version der Klassifikationssystem"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-AAR710#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAR710-003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ClassificationSystemUrl(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ClassificationSystemUrl",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Classification system URL", r"de": r"URL des Klassifikationssystems"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/ProduktClassification/ClassificationSystemUrl/2/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProductClassId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProductClassId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Product class ID", r"de": r"Produktklassen ID"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABG776#003"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABG776-003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProductClassCodedName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProductClassCodedName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Product Class Coded Name", r"de": r"Produktklasse Coded Name"}
                        ),
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(r"0173-1#02-ABK128#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK128-002"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProductClassName(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ProductClassName",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Product class name", r"de": r"Produktklasse Name"}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABK273#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK273-002"),),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ReferenceToTechnicalPropertyArea(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"ReferenceToTechnicalPropertyArea",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Reference to technical property area",
                                r"de": r"Referenz auf einen technsichen Merkmalsbereich",
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABL358#002"),
                        "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABL358-002"),),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Produkt classification", r"de": r"Produktklassifikation"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABK162#002/0173-1#01-AHX839#002"),
                    "supplemental_semantic_id": (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABK162#002~0/0173-1#01-AHX839#002",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK162-002/0173-1-01-AHX839-002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                }

            def __init__(
                self,
                classificationSystem: Union[str, ClassificationSystem],
                productClassId: Union[str, ProductClassId],
                productClassCodedName: Union[str, ProductClassCodedName],
                classificationSystemVersion: Optional[Union[str, ClassificationSystemVersion]] = None,
                classificationSystemUrl: Optional[Union[str, ClassificationSystemUrl]] = None,
                productClassName: Optional[Union[aas.MultiLanguageTextType, ProductClassName]] = None,
                referenceToTechnicalPropertyArea: Optional[
                    Union[aas.Reference, ReferenceToTechnicalPropertyArea]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if classificationSystem is not None and not isinstance(classificationSystem, aas.SubmodelElement):
                    classificationSystem = self.ClassificationSystem(classificationSystem)

                # Build a submodel element if a raw value was passed in the argument

                if classificationSystemVersion is not None and not isinstance(
                    classificationSystemVersion, aas.SubmodelElement
                ):
                    classificationSystemVersion = self.ClassificationSystemVersion(classificationSystemVersion)

                # Build a submodel element if a raw value was passed in the argument

                if classificationSystemUrl is not None and not isinstance(classificationSystemUrl, aas.SubmodelElement):
                    classificationSystemUrl = self.ClassificationSystemUrl(classificationSystemUrl)

                # Build a submodel element if a raw value was passed in the argument

                if productClassId is not None and not isinstance(productClassId, aas.SubmodelElement):
                    productClassId = self.ProductClassId(productClassId)

                # Build a submodel element if a raw value was passed in the argument

                if productClassCodedName is not None and not isinstance(productClassCodedName, aas.SubmodelElement):
                    productClassCodedName = self.ProductClassCodedName(productClassCodedName)

                # Build a submodel element if a raw value was passed in the argument

                if productClassName is not None and not isinstance(productClassName, aas.SubmodelElement):
                    productClassName = self.ProductClassName(productClassName)

                # Build a submodel element if a raw value was passed in the argument

                if referenceToTechnicalPropertyArea is not None and not isinstance(
                    referenceToTechnicalPropertyArea, aas.SubmodelElement
                ):
                    referenceToTechnicalPropertyArea = self.ReferenceToTechnicalPropertyArea(
                        referenceToTechnicalPropertyArea
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    classificationSystem,
                    classificationSystemVersion,
                    classificationSystemUrl,
                    productClassId,
                    productClassCodedName,
                    productClassName,
                    referenceToTechnicalPropertyArea,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"ProductClassifications",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#02-ABK162#002/0173-1#01-AHX839#002"),
                "order_relevant": False,
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Product classifications", r"de": r"Produktklassifikationen"}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABK162#002"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK162-002"),),
            }

        def __init__(
            self,
            productclassifications_items: Iterable[Productclassifications_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(productclassifications_items, str):
                raise TypeError("productclassifications_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(productclassifications_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class TechnicalPropertyAreas(GeneratedSubmodelElementList):

        class Technicalpropertyareas_item(aas.SubmodelElementCollection):

            class Section(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Section",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ArbitrarySMC",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySML(GeneratedSubmodelElementList):

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ArbitrarySML",
                            "type_value_list_element": aas.SubmodelElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitraryProperty(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ArbitraryProperty",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ArbitraryMLP",
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryRange(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"ArbitraryRange",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Section",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: Using displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(
                    self,
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(section, str):
                        raise TypeError("section takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySMC, str):
                        raise TypeError("arbitrarySMC takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySML, str):
                        raise TypeError("arbitrarySML takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if arbitrarySML is not None and not isinstance(arbitrarySML, aas.SubmodelElement):
                        arbitrarySML = self.ArbitrarySML(arbitrarySML)

                    # A str would be split into its characters
                    if isinstance(arbitraryProperty, str):
                        raise TypeError("arbitraryProperty takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryProperty:
                        arbitraryProperty = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i)
                            for i in arbitraryProperty
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryMLP, str):
                        raise TypeError("arbitraryMLP takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryMLP:
                        arbitraryMLP = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryRange, str):
                        raise TypeError("arbitraryRange takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryRange:
                        arbitraryRange = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryRange(min=i[0], max=i[1])
                            for i in arbitraryRange
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        section, arbitrarySMC, arbitrarySML, arbitraryProperty, arbitraryMLP, arbitraryRange
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ArbitrarySMC(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Section",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ArbitrarySMC",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySML(GeneratedSubmodelElementList):

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ArbitrarySML",
                            "type_value_list_element": aas.SubmodelElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitraryProperty(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ArbitraryProperty",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ArbitraryMLP",
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryRange(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"ArbitraryRange",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ArbitrarySMC",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(
                    self,
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(section, str):
                        raise TypeError("section takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySMC, str):
                        raise TypeError("arbitrarySMC takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySML, str):
                        raise TypeError("arbitrarySML takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if arbitrarySML is not None and not isinstance(arbitrarySML, aas.SubmodelElement):
                        arbitrarySML = self.ArbitrarySML(arbitrarySML)

                    # A str would be split into its characters
                    if isinstance(arbitraryProperty, str):
                        raise TypeError("arbitraryProperty takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryProperty:
                        arbitraryProperty = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i)
                            for i in arbitraryProperty
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryMLP, str):
                        raise TypeError("arbitraryMLP takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryMLP:
                        arbitraryMLP = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryRange, str):
                        raise TypeError("arbitraryRange takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryRange:
                        arbitraryRange = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryRange(min=i[0], max=i[1])
                            for i in arbitraryRange
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        section, arbitrarySMC, arbitrarySML, arbitraryProperty, arbitraryMLP, arbitraryRange
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ArbitrarySML(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"ArbitrarySML",
                        "type_value_list_element": aas.SubmodelElement,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(
                    self,
                    arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(arbitrarysml_items, str):
                        raise TypeError("arbitrarysml_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(arbitrarysml_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ArbitraryProperty(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ArbitraryProperty",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ArbitraryMLP(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ArbitraryMLP",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ArbitraryRange(aas.Range):

                @staticmethod
                def template_defaults() -> RangeMetadata:
                    return {
                        "id_short": r"ArbitraryRange",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Technical property area", r"de": r"Technischer Merkmalsbereich"}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),
                    "supplemental_semantic_id": (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABL358#002~0/0173-1#01-AHX773#002",
                                ),
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABL358-002/0173-1-01-AHX773-002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                }

            def __init__(
                self,
                section: Optional[Iterable[Section]] = None,
                arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
                arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(section, str):
                    raise TypeError("section takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(arbitrarySMC, str):
                    raise TypeError("arbitrarySMC takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(arbitrarySML, str):
                    raise TypeError("arbitrarySML takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if arbitrarySML is not None and not isinstance(arbitrarySML, aas.SubmodelElement):
                    arbitrarySML = self.ArbitrarySML(arbitrarySML)

                # A str would be split into its characters
                if isinstance(arbitraryProperty, str):
                    raise TypeError("arbitraryProperty takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if arbitraryProperty:
                    arbitraryProperty = [
                        i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i)
                        for i in arbitraryProperty
                    ]

                # A str would be split into its characters
                if isinstance(arbitraryMLP, str):
                    raise TypeError("arbitraryMLP takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if arbitraryMLP:
                    arbitraryMLP = [
                        i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP
                    ]

                # A str would be split into its characters
                if isinstance(arbitraryRange, str):
                    raise TypeError("arbitraryRange takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if arbitraryRange:
                    arbitraryRange = [
                        i if isinstance(i, aas.SubmodelElement) else self.ArbitraryRange(min=i[0], max=i[1])
                        for i in arbitraryRange
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    section, arbitrarySMC, arbitrarySML, arbitraryProperty, arbitraryMLP, arbitraryRange
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"TechnicalPropertyAreas",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Technical property areas", r"de": r"Technsiche Merkmalsbereiche"}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABK163#002"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/ 0173-1-02-ABK163-002"),),
            }

        def __init__(
            self,
            technicalpropertyareas_items: Iterable[Technicalpropertyareas_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(technicalpropertyareas_items, str):
                raise TypeError("technicalpropertyareas_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(technicalpropertyareas_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FurtherInformation(aas.SubmodelElementCollection):

        class TextStatement(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"TextStatement",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Text statement", r"de": r"Anweisung im Text"}
                    ),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABK134#002"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK134-002"),),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ValidDate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ValidDate",
                    "value_type": xsd.Date,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Validity date", r"de": r"Verfallsdatum"}),
                    "category": r"PARAMETER",
                    "semantic_id": global_ref(r"0173-1#02-ABL775#001"),
                    "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1#02-ABL775#001"),),
                }

            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"FurtherInformation",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Further information", r"de": r"Weitere Informationen"}
                ),
                "semantic_id": global_ref(r"0173-1#02-ABK164#002"),
                "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK164-002"),),
            }

        def __init__(
            self,
            validDate: Union[xsd.Date, ValidDate],
            textStatement: Optional[Iterable[Union[aas.MultiLanguageTextType, TextStatement]]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(textStatement, str):
                raise TypeError("textStatement takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if textStatement:
                textStatement = [
                    i if isinstance(i, aas.SubmodelElement) else self.TextStatement(i) for i in textStatement
                ]

            # Build a submodel element if a raw value was passed in the argument

            if validDate is not None and not isinstance(validDate, aas.SubmodelElement):
                validDate = self.ValidDate(validDate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(textStatement, validDate)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SpecificDescriptions(GeneratedSubmodelElementList):

        class Specificdescriptions_item(aas.SubmodelElementCollection):

            class Section(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Section",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ArbitrarySMC",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySML(GeneratedSubmodelElementList):

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ArbitrarySML",
                            "type_value_list_element": aas.SubmodelElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitraryProperty(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ArbitraryProperty",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ArbitraryMLP",
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryRange(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"ArbitraryRange",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Section",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: Using displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(
                    self,
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(section, str):
                        raise TypeError("section takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySMC, str):
                        raise TypeError("arbitrarySMC takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySML, str):
                        raise TypeError("arbitrarySML takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if arbitrarySML is not None and not isinstance(arbitrarySML, aas.SubmodelElement):
                        arbitrarySML = self.ArbitrarySML(arbitrarySML)

                    # A str would be split into its characters
                    if isinstance(arbitraryProperty, str):
                        raise TypeError("arbitraryProperty takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryProperty:
                        arbitraryProperty = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i)
                            for i in arbitraryProperty
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryMLP, str):
                        raise TypeError("arbitraryMLP takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryMLP:
                        arbitraryMLP = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryRange, str):
                        raise TypeError("arbitraryRange takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryRange:
                        arbitraryRange = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryRange(min=i[0], max=i[1])
                            for i in arbitraryRange
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        section, arbitrarySMC, arbitrarySML, arbitraryProperty, arbitraryMLP, arbitraryRange
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ArbitrarySMC(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Section",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ArbitrarySMC",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements()

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitrarySML(GeneratedSubmodelElementList):

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ArbitrarySML",
                            "type_value_list_element": aas.SubmodelElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ArbitraryProperty(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ArbitraryProperty",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ArbitraryMLP",
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryRange(aas.Range):

                    @staticmethod
                    def template_defaults() -> RangeMetadata:
                        return {
                            "id_short": r"ArbitraryRange",
                            "value_type": str,
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Note: The use of a displayName is recommended."}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                        }

                    def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                        super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ArbitrarySMC",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(
                    self,
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(section, str):
                        raise TypeError("section takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySMC, str):
                        raise TypeError("arbitrarySMC takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitrarySML, str):
                        raise TypeError("arbitrarySML takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if arbitrarySML is not None and not isinstance(arbitrarySML, aas.SubmodelElement):
                        arbitrarySML = self.ArbitrarySML(arbitrarySML)

                    # A str would be split into its characters
                    if isinstance(arbitraryProperty, str):
                        raise TypeError("arbitraryProperty takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryProperty:
                        arbitraryProperty = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i)
                            for i in arbitraryProperty
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryMLP, str):
                        raise TypeError("arbitraryMLP takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryMLP:
                        arbitraryMLP = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryRange, str):
                        raise TypeError("arbitraryRange takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryRange:
                        arbitraryRange = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryRange(min=i[0], max=i[1])
                            for i in arbitraryRange
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        section, arbitrarySMC, arbitrarySML, arbitraryProperty, arbitraryMLP, arbitraryRange
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ArbitrarySML(GeneratedSubmodelElementList):

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"ArbitrarySML",
                        "type_value_list_element": aas.SubmodelElement,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(
                    self,
                    arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(arbitrarysml_items, str):
                        raise TypeError("arbitrarysml_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(arbitrarysml_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ArbitraryProperty(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ArbitraryProperty",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ArbitraryMLP(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ArbitraryMLP",
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ArbitraryRange(aas.Range):

                @staticmethod
                def template_defaults() -> RangeMetadata:
                    return {
                        "id_short": r"ArbitraryRange",
                        "value_type": str,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The use of a displayName is recommended."}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    }

                def __init__(self, min: str, max: str, **kwargs: Unpack[RangeMetadata]):

                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Specific description", r"de": r"Spezifische Beschreibung"}
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
                section: Optional[Iterable[Section]] = None,
                arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
                arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(section, str):
                    raise TypeError("section takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(arbitrarySMC, str):
                    raise TypeError("arbitrarySMC takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(arbitrarySML, str):
                    raise TypeError("arbitrarySML takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if arbitrarySML is not None and not isinstance(arbitrarySML, aas.SubmodelElement):
                    arbitrarySML = self.ArbitrarySML(arbitrarySML)

                # A str would be split into its characters
                if isinstance(arbitraryProperty, str):
                    raise TypeError("arbitraryProperty takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if arbitraryProperty:
                    arbitraryProperty = [
                        i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i)
                        for i in arbitraryProperty
                    ]

                # A str would be split into its characters
                if isinstance(arbitraryMLP, str):
                    raise TypeError("arbitraryMLP takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if arbitraryMLP:
                    arbitraryMLP = [
                        i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP
                    ]

                # A str would be split into its characters
                if isinstance(arbitraryRange, str):
                    raise TypeError("arbitraryRange takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if arbitraryRange:
                    arbitraryRange = [
                        i if isinstance(i, aas.SubmodelElement) else self.ArbitraryRange(min=i[0], max=i[1])
                        for i in arbitraryRange
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    section, arbitrarySMC, arbitrarySML, arbitraryProperty, arbitraryMLP, arbitraryRange
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"SpecificDescriptions",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id_list_element": global_ref(r"0173-1#02-ABM221#001/0173-1#01-AHY912#001"),
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Specific description", r"de": r"Spezifische Beschreibung"}
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
            "id_short": r"TechnicalData",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel containing technical data of the asset and associated product classificatons",
                    r"de": r"Teilmodell, das die technischen Daten des Assets und die zugehörigen Produktklassifizierungen enthält",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"2",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02003-2-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AHX837#002"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
            "supplemental_semantic_id": (global_ref(r"https://api.eclass-cdp.com/0173-1-01-AHX837-002"),),
        }

    def __init__(
        self,
        id_: str,
        generalInformation: GeneralInformation,
        productClassifications: Optional[
            Union[Iterable[ProductClassifications.Productclassifications_item], ProductClassifications]
        ] = None,
        technicalPropertyAreas: Optional[
            Union[Iterable[TechnicalPropertyAreas.Technicalpropertyareas_item], TechnicalPropertyAreas]
        ] = None,
        furtherInformation: Optional[FurtherInformation] = None,
        specificDescriptions: Optional[
            Union[Iterable[SpecificDescriptions.Specificdescriptions_item], SpecificDescriptions]
        ] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(productClassifications, str):
            raise TypeError("productClassifications takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if productClassifications is not None and not isinstance(productClassifications, aas.SubmodelElement):
            productClassifications = self.ProductClassifications(productClassifications)

        # A str would be split into its characters
        if isinstance(technicalPropertyAreas, str):
            raise TypeError("technicalPropertyAreas takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if technicalPropertyAreas is not None and not isinstance(technicalPropertyAreas, aas.SubmodelElement):
            technicalPropertyAreas = self.TechnicalPropertyAreas(technicalPropertyAreas)

        # A str would be split into its characters
        if isinstance(specificDescriptions, str):
            raise TypeError("specificDescriptions takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if specificDescriptions is not None and not isinstance(specificDescriptions, aas.SubmodelElement):
            specificDescriptions = self.SpecificDescriptions(specificDescriptions)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            generalInformation, productClassifications, technicalPropertyAreas, furtherInformation, specificDescriptions
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
