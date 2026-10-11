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


class TechnicalData(aas.Submodel):

    class GeneralInformation(aas.SubmodelElementCollection):

        class ManufacturerName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ManufacturerName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAO677#004"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO677-004"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer name", r"de": r"Herstellername"}
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

        class CompanyLogo(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CompanyLogo",
                content_type: Optional[str] = r"image/png",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABI776#002"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI776-002"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Company logo", r"de": r"Firmenlogo"})

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

        class ManufacturerProductDesignation(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"ManufacturerProductDesignation",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAW338#003"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAW338-003"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer product designation", r"de": r"Herstellerproduktbezeichnung"}
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

        class ManufacturerArticleNumber(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ManufacturerArticleNumber",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAO676#005"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO676-005"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer article number", r"de": r"Herstellerartikelnummer"}
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

        class ManufacturerOrderCode(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ManufacturerOrderCode",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAO227#004"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO227-004"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Manufacturer order code", r"de": r"Bestellcode des Herstellers"}
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

        class ProductImages(GeneratedSubmodelElementList):

            class Productimages_item(aas.SubmodelElementCollection):

                class ImageFile(aas.File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ImageFile",
                        content_type: Optional[str] = r"image/png",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK291#002"),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Product image", r"de": r"Bildname Sachaufnahme"}
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

                class ImageNote(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ImageNote",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABL423#001"),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (
                            global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABL423-001"),
                        ),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Image note", r"de": r"Bildhinweis"}
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
                    imageFile: ImageFile,
                    imageNote: Optional[Union[aas.LangStringSet, ImageNote]] = None,
                    id_short: Optional[str] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABM220#001/0173-1#01-AHY911#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
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
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(dict_={r"en": r"Product image", r"de": r"Produktbild"})

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if imageNote is not None and not isinstance(imageNote, aas.SubmodelElement):
                        imageNote = self.ImageNote(imageNote)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(imageFile, imageNote)

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
                productimages_items: Iterable[Productimages_item],
                id_short: Optional[str] = r"ProductImages",
                type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                semantic_id_list_element: Optional[aas.Reference] = global_ref(
                    r"0173-1#02-ABM220#001/0173-1#01-AHY911#001"
                ),
                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABM220#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABM220-001"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Product images", r"de": r"Produktbilder"})

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(productimages_items, str):
                    raise TypeError("productimages_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(productimages_items, number_repeated=False)

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    type_value_list_element=type_value_list_element,
                    semantic_id_list_element=semantic_id_list_element,
                    value_type_list_element=value_type_list_element,
                    order_relevant=order_relevant,
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
            manufacturerName: Union[str, ManufacturerName],
            manufacturerProductDesignation: Union[aas.LangStringSet, ManufacturerProductDesignation],
            manufacturerArticleNumber: Union[str, ManufacturerArticleNumber],
            manufacturerOrderCode: Union[str, ManufacturerOrderCode],
            companyLogo: Optional[CompanyLogo] = None,
            productImages: Optional[Union[Iterable[ProductImages.Productimages_item], ProductImages]] = None,
            id_short: Optional[str] = r"GeneralInformation",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK161#002/0173-1#01-AHX838#002"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK161-002/0173-1-01-AHX838-002"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"General information", r"de": r"Allgemeine Informationen"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

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

    class ProductClassifications(GeneratedSubmodelElementList):

        class Productclassifications_item(aas.SubmodelElementCollection):

            class ClassificationSystem(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ClassificationSystem",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABL424#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABL424-001"),
                    ),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Classification system", r"de": r"Klassifikationssystem"}
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

            class ClassificationSystemVersion(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ClassificationSystemVersion",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAR710#003"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAR710-003"),
                    ),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Classification system version", r"de": r"Version der Klassifikationssystem"}
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

            class ClassificationSystemUrl(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ClassificationSystemUrl",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/ProduktClassification/ClassificationSystemUrl/2/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Classification system URL", r"de": r"URL des Klassifikationssystems"}
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

            class ProductClassId(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ProductClassId",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABG776#003"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABG776-003"),
                    ),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Product class ID", r"de": r"Produktklassen ID"}
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

            class ProductClassCodedName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ProductClassCodedName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK128#002"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK128-002"),
                    ),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Product Class Coded Name", r"de": r"Produktklasse Coded Name"}
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

            class ProductClassName(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"ProductClassName",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK273#002"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK273-002"),
                    ),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Product class name", r"de": r"Produktklasse Name"}
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

            class ReferenceToTechnicalPropertyArea(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"ReferenceToTechnicalPropertyArea",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABL358#002"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABL358-002"),
                    ),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Reference to technical property area",
                                r"de": r"Referenz auf einen technsichen Merkmalsbereich",
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
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
                classificationSystem: Union[str, ClassificationSystem],
                productClassId: Union[str, ProductClassId],
                productClassCodedName: Union[str, ProductClassCodedName],
                classificationSystemVersion: Optional[Union[str, ClassificationSystemVersion]] = None,
                classificationSystemUrl: Optional[Union[str, ClassificationSystemUrl]] = None,
                productClassName: Optional[Union[aas.LangStringSet, ProductClassName]] = None,
                referenceToTechnicalPropertyArea: Optional[
                    Union[aas.Reference, ReferenceToTechnicalPropertyArea]
                ] = None,
                id_short: Optional[str] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK162#002/0173-1#01-AHX839#002"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
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
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Produkt classification", r"de": r"Produktklassifikation"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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
            productclassifications_items: Iterable[Productclassifications_item],
            id_short: Optional[str] = r"ProductClassifications",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                r"0173-1#02-ABK162#002/0173-1#01-AHX839#002"
            ),
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = False,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK162#002"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK162-002"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Product classifications", r"de": r"Produktklassifikationen"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(productclassifications_items, str):
                raise TypeError("productclassifications_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(productclassifications_items, number_repeated=False)

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                type_value_list_element=type_value_list_element,
                semantic_id_list_element=semantic_id_list_element,
                value_type_list_element=value_type_list_element,
                order_relevant=order_relevant,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class TechnicalPropertyAreas(GeneratedSubmodelElementList):

        class Technicalpropertyareas_item(aas.SubmodelElementCollection):

            class Section(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"Section",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

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

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"ArbitrarySMC",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitrarySML(GeneratedSubmodelElementList):

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        id_short: Optional[str] = r"ArbitrarySML",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            type_value_list_element=type_value_list_element,
                            semantic_id_list_element=semantic_id_list_element,
                            value_type_list_element=value_type_list_element,
                            order_relevant=order_relevant,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ArbitraryProperty(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ArbitraryProperty",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
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

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ArbitraryMLP",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
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

                class ArbitraryRange(aas.Range):

                    def __init__(
                        self,
                        min: str,
                        max: str,
                        id_short: Optional[str] = r"ArbitraryRange",
                        value_type: aas.DataTypeDefXsd = str,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
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
                            min=min,
                            max=max,
                            id_short=id_short,
                            value_type=value_type,
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
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.LangStringSet, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    id_short: Optional[str] = r"Section",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The idShort is arbitrary. Note: Using displayName is recommended."}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

            class ArbitrarySMC(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"Section",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

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

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"ArbitrarySMC",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitrarySML(GeneratedSubmodelElementList):

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        id_short: Optional[str] = r"ArbitrarySML",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            type_value_list_element=type_value_list_element,
                            semantic_id_list_element=semantic_id_list_element,
                            value_type_list_element=value_type_list_element,
                            order_relevant=order_relevant,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ArbitraryProperty(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ArbitraryProperty",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
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

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ArbitraryMLP",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
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

                class ArbitraryRange(aas.Range):

                    def __init__(
                        self,
                        min: str,
                        max: str,
                        id_short: Optional[str] = r"ArbitraryRange",
                        value_type: aas.DataTypeDefXsd = str,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
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
                            min=min,
                            max=max,
                            id_short=id_short,
                            value_type=value_type,
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
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.LangStringSet, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    id_short: Optional[str] = r"ArbitrarySMC",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

            class ArbitrarySML(GeneratedSubmodelElementList):

                def __init__(
                    self,
                    arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                    id_short: Optional[str] = r"ArbitrarySML",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every SML with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(arbitrarysml_items, str):
                        raise TypeError("arbitrarysml_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(arbitrarysml_items, number_repeated=False)

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ArbitraryProperty(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ArbitraryProperty",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
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

            class ArbitraryMLP(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"ArbitraryMLP",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every multilanguage property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

            class ArbitraryRange(aas.Range):

                def __init__(
                    self,
                    min: str,
                    max: str,
                    id_short: Optional[str] = r"ArbitraryRange",
                    value_type: aas.DataTypeDefXsd = str,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every range property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        min=min,
                        max=max,
                        id_short=id_short,
                        value_type=value_type,
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
                section: Optional[Iterable[Section]] = None,
                arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                arbitraryMLP: Optional[Iterable[Union[aas.LangStringSet, ArbitraryMLP]]] = None,
                arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                id_short: Optional[str] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
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
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Technical property area", r"de": r"Technischer Merkmalsbereich"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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
            technicalpropertyareas_items: Iterable[Technicalpropertyareas_item],
            id_short: Optional[str] = r"TechnicalPropertyAreas",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"
            ),
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK163#002"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK163-002"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Technical property areas", r"de": r"Technsiche Merkmalsbereiche"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(technicalpropertyareas_items, str):
                raise TypeError("technicalpropertyareas_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(technicalpropertyareas_items, number_repeated=False)

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                type_value_list_element=type_value_list_element,
                semantic_id_list_element=semantic_id_list_element,
                value_type_list_element=value_type_list_element,
                order_relevant=order_relevant,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class FurtherInformation(aas.SubmodelElementCollection):

        class TextStatement(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"TextStatement",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK134#002"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK134-002"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Text statement", r"de": r"Anweisung im Text"}
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

        class ValidDate(aas.Property):

            def __init__(
                self,
                value: xsd.Date,
                id_short: Optional[str] = r"ValidDate",
                value_type: aas.DataTypeDefXsd = xsd.Date,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABL775#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    global_ref(r"https://api.eclass-cdp.com/0173-1#02-ABL775#001"),
                ),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Validity date", r"de": r"Verfallsdatum"})

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

        def __init__(
            self,
            validDate: Union[xsd.Date, ValidDate],
            textStatement: Optional[Iterable[Union[aas.LangStringSet, TextStatement]]] = None,
            id_short: Optional[str] = r"FurtherInformation",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABK164#002"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK164-002"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Further information", r"de": r"Weitere Informationen"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

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

    class SpecificDescriptions(GeneratedSubmodelElementList):

        class Specificdescriptions_item(aas.SubmodelElementCollection):

            class Section(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"Section",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"ArbitrarySMC",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitrarySML(GeneratedSubmodelElementList):

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        id_short: Optional[str] = r"ArbitrarySML",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            type_value_list_element=type_value_list_element,
                            semantic_id_list_element=semantic_id_list_element,
                            value_type_list_element=value_type_list_element,
                            order_relevant=order_relevant,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ArbitraryProperty(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ArbitraryProperty",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
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

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ArbitraryMLP",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every multilanguage property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitraryRange(aas.Range):

                    def __init__(
                        self,
                        min: str,
                        max: str,
                        id_short: Optional[str] = r"ArbitraryRange",
                        value_type: aas.DataTypeDefXsd = str,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every range property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            min=min,
                            max=max,
                            id_short=id_short,
                            value_type=value_type,
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
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.LangStringSet, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    id_short: Optional[str] = r"Section",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Note: The idShort is arbitrary. Note: Using displayName is recommended."}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

            class ArbitrarySMC(aas.SubmodelElementCollection):

                class Section(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"Section",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitrarySMC(aas.SubmodelElementCollection):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"ArbitrarySMC",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitrarySML(GeneratedSubmodelElementList):

                    def __init__(
                        self,
                        arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                        id_short: Optional[str] = r"ArbitrarySML",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(arbitrarysml_items, str):
                            raise TypeError("arbitrarysml_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            arbitrarysml_items, number_repeated=False
                        )

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            type_value_list_element=type_value_list_element,
                            semantic_id_list_element=semantic_id_list_element,
                            value_type_list_element=value_type_list_element,
                            order_relevant=order_relevant,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ArbitraryProperty(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ArbitraryProperty",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
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

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ArbitraryMLP",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every multilanguage property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

                class ArbitraryRange(aas.Range):

                    def __init__(
                        self,
                        min: str,
                        max: str,
                        id_short: Optional[str] = r"ArbitraryRange",
                        value_type: aas.DataTypeDefXsd = str,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/SMT/General/Arbitrary"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every range property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            min=min,
                            max=max,
                            id_short=id_short,
                            value_type=value_type,
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
                    section: Optional[Iterable[Section]] = None,
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                    arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.LangStringSet, ArbitraryMLP]]] = None,
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                    id_short: Optional[str] = r"ArbitrarySMC",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every SMC with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

            class ArbitrarySML(GeneratedSubmodelElementList):

                def __init__(
                    self,
                    arbitrarysml_items: Optional[Iterable[aas.SubmodelElement]] = None,
                    id_short: Optional[str] = r"ArbitrarySML",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElement,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every SML with a specific semanticId can serve as a section. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(arbitrarysml_items, str):
                        raise TypeError("arbitrarysml_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(arbitrarysml_items, number_repeated=False)

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class ArbitraryProperty(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ArbitraryProperty",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
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

            class ArbitraryMLP(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"ArbitraryMLP",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every multilanguage property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
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

            class ArbitraryRange(aas.Range):

                def __init__(
                    self,
                    min: str,
                    max: str,
                    id_short: Optional[str] = r"ArbitraryRange",
                    value_type: aas.DataTypeDefXsd = str,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/SMT/General/Arbitrary"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Every range property can be used. Note: The idShort is arbitrary. Note: The use of a displayName is recommended."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        min=min,
                        max=max,
                        id_short=id_short,
                        value_type=value_type,
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
                section: Optional[Iterable[Section]] = None,
                arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                arbitrarySML: Optional[Union[Iterable[aas.SubmodelElement], ArbitrarySML]] = None,
                arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                arbitraryMLP: Optional[Iterable[Union[aas.LangStringSet, ArbitraryMLP]]] = None,
                arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                id_short: Optional[str] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABM221#001/0173-1#01-AHY912#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
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
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Specific description", r"de": r"Spezifische Beschreibung"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Naming",
                            value_type=str,
                            value=r"Name of SMC is use case or application",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(r"https://admin-shell.io/SubmodelTemplates/Naming/1/0"),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

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
            specificdescriptions_items: Iterable[Specificdescriptions_item],
            id_short: Optional[str] = r"SpecificDescriptions",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = global_ref(
                r"0173-1#02-ABM221#001/0173-1#01-AHY912#001"
            ),
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-ABM221#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABM221-001"),
            ),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Specific description", r"de": r"Spezifische Beschreibung"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(specificdescriptions_items, str):
                raise TypeError("specificdescriptions_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(specificdescriptions_items, number_repeated=False)

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                type_value_list_element=type_value_list_element,
                semantic_id_list_element=semantic_id_list_element,
                value_type_list_element=value_type_list_element,
                order_relevant=order_relevant,
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
        id_short: Optional[str] = r"TechnicalData",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AHX837#002"),),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (
            global_ref(r"https://api.eclass-cdp.com/0173-1-01-AHX837-002"),
        ),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel containing technical data of the asset and associated product classificatons",
                    r"de": r"Teilmodell, das die technischen Daten des Assets und die zugehörigen Produktklassifizierungen enthält",
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"2",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02003-2-0",
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

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
