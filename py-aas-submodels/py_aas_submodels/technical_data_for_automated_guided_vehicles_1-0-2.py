from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class TechnicalDataAGV(Submodel):

    class GeneralInformation(SubmodelElementCollection):

        class ManufacturerName(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ManufacturerName",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging and labeling of a product in respect to its being brought into the market."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAO677#004",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (
                    ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-AAO677-004",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

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

        class CompanyLogo(File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CompanyLogo",
                content_type: Optional[str] = r"image/png",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Imagefile for logo of manufacturer provided in common format (.png, .jpg)."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI776#002",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (
                    ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABI776-002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

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

        class ManufacturerProductDesignation(MultiLanguageProperty):

            def __init__(
                self,
                value: LangStringSet,
                id_short: Optional[str] = r"ManufacturerProductDesignation",
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Product designation as given by the mnaufacturer. Short description of the product, product group or function (short text) in common language."
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAW338#003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (
                    ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-AAW338-003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

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

        class ProductArticleNumberOfManufacturer(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ProductArticleNumberOfManufacturer",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"unique product identifier of the manufacturer "}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAO054#003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (
                    ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-AAO054-003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

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

        class ManufacturerOrderCode(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ManufacturerOrderCode",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"By manufactures issued unique combination of numbers and letters used to identify the device for ordering"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAO227#004",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (
                    ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-AAO227-004",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

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

        class ProductImages(SubmodelElementList):

            class Productimages_item(SubmodelElementCollection):

                class ImageFile(File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ImageFile",
                        content_type: Optional[str] = r"image/jpeg",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABK291#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class ImageNote(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"ImageNote",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABL423#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (
                            ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://api.eclass-cdp.com/0173-1-02-ABL423-001",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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
                    imageNote: Optional[Union[LangStringSet, ImageNote]] = None,
                    id_short: Optional[str] = r"productimages_item",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Product image", r"de": r"Produktbild"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABM220#001/0173-1#01-AHY911#001",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (
                        ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABM220#001~0/0173-1#01-AHY911#001",
                                ),
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABM220-001/0173-1-01-AHY911-001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if imageNote and not isinstance(imageNote, SubmodelElement):
                        imageNote = self.ImageNote(imageNote)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [imageFile, imageNote]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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
                productimages_items: Productimages_item,
                id_short: Optional[str] = r"ProductImages",
                type_value_list_element: SubmodelElement = SubmodelElementCollection,
                semantic_id_list_element: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABM220#001/0173-1#01-AHY911#001",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                value_type_list_element: Optional[DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Product images", r"de": r"Produktbilder"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Image file for associated product provided in common format (.png, .jpg)"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABM220#001",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (
                    ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABM220-001",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [productimages_items]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

            def _check_constraints(self, new, existing) -> None:
                # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                saved_id_short = new.id_short
                new.id_short = None

                # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                if not isinstance(new, self.type_value_list_element):
                    raise base.AASConstraintViolation(
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
                    raise base.AASConstraintViolation(
                        107,
                        f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                        "is specified all first level children must have the same "
                        f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                    )

                # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                # is either Property or Range. Thus, `new` must have the value_type property.
                # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                if (
                    isinstance(self.type_value_list_element, Property)
                    or isinstance(self.type_value_list_element, Range)
                    and not isinstance(new.value_type, self.value_type_list_element)
                ):  # type: ignore
                    raise base.AASConstraintViolation(
                        109,
                        "All first level elements must have the value_type "  # type: ignore
                        "specified by value_type_list_element="
                        f"{self.value_type_list_element.__name__}, got "  # type: ignore
                        f"{new!r} with value_type={new.value_type.__name__}",
                    )  # type: ignore

                # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                if (
                    new.semantic_id is not None
                    and self.semantic_id_list_element is None
                ):
                    for item in existing:
                        if (
                            item.semantic_id is not None
                            and new.semantic_id != item.semantic_id
                        ):
                            raise base.AASConstraintViolation(
                                114,
                                f"Element to be added {new!r} has semantic_id "
                                f"{new.semantic_id!r}, while already contained element "
                                f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                "aren't equal.",
                            )

                # Re-assign id_short
                new.id_short = saved_id_short

        def __init__(
            self,
            manufacturerName: Union[str, ManufacturerName],
            manufacturerProductDesignation: Union[
                LangStringSet, ManufacturerProductDesignation
            ],
            productArticleNumberOfManufacturer: Union[
                str, ProductArticleNumberOfManufacturer
            ],
            manufacturerOrderCode: Union[str, ManufacturerOrderCode],
            companyLogo: Optional[CompanyLogo] = None,
            productImages: Optional[Iterable[ProductImages]] = None,
            id_short: Optional[str] = r"GeneralInformation",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={
                    r"en": r"General information",
                    r"de": r"Allgemeine Informationen",
                }
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"General information, for example ordering and manufacturer information."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABK161#002/0173-1#01-AHX838#002",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (
                ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABK161-002/0173-1-01-AHX838-002",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument
            if manufacturerName and not isinstance(manufacturerName, SubmodelElement):
                manufacturerName = self.ManufacturerName(manufacturerName)

            # Build a submodel element if a raw value was passed in the argument
            if manufacturerProductDesignation and not isinstance(
                manufacturerProductDesignation, SubmodelElement
            ):
                manufacturerProductDesignation = self.ManufacturerProductDesignation(
                    manufacturerProductDesignation
                )

            # Build a submodel element if a raw value was passed in the argument
            if productArticleNumberOfManufacturer and not isinstance(
                productArticleNumberOfManufacturer, SubmodelElement
            ):
                productArticleNumberOfManufacturer = (
                    self.ProductArticleNumberOfManufacturer(
                        productArticleNumberOfManufacturer
                    )
                )

            # Build a submodel element if a raw value was passed in the argument
            if manufacturerOrderCode and not isinstance(
                manufacturerOrderCode, SubmodelElement
            ):
                manufacturerOrderCode = self.ManufacturerOrderCode(
                    manufacturerOrderCode
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                manufacturerName,
                companyLogo,
                manufacturerProductDesignation,
                productArticleNumberOfManufacturer,
                manufacturerOrderCode,
                productImages,
            ]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

    class SpecificDescriptions(SubmodelElementList):

        class Specificdescriptions_item(SubmodelElementCollection):

            class DataSheet(File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DataSheet",
                    content_type: Optional[str] = r"application/pdf",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Product datasheet", r"de": r"Produktdatenblatt"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Document with technical product data of the AGV provided by the manufacturer",
                            r"de": r"Dokument mit technischen Produktdaten, das vom Hersteller bereitgestellt wird",
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/datasheet/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class TypeAndApplicationInformation(SubmodelElementCollection):

                class AgvKinematic(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AgvKinematic",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Kinematic of the AGV",
                                r"de": r"Kinematik des AGV",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Type of Kinematic of the AGV. The enumerations according VDA5050 "DIFF", "OMNI", "THREEWHEEL", "OTHER" can be used.'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/agvkinematic/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class AgvClass(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AgvClass",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Class of the AGV", r"de": r"Klasse des AGV"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Class of the AGV. The enumeration according VDA5050 with "FORKLIFT", "CONVEYER", "TUGGER", "CARRIER", "OTHER" can be used.'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/agvclass/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class TravelDirection(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TravelDirection",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Travel direction", r"de": r"Fahrtrichtung"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Direction of traveling of the AGV, the enumeration "FORWARD", "BACKWARD", "OMNI-DIRECTIONAL" can be used.'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/traveldirection/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class TransportPrinciple(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TransportPrinciple",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Transportation principle",
                                r"de": r"Transportprinzip",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Transportation pinciple of the AGV. The enumeration "LOADPULLING", "LOADCARRYING", "MIXED" can be used.'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/transportprinciple/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class LocalizationType(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"LocalizationType",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Type of localization",
                                r"de": r"Lokalisierungsart",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Type of the localization the AGV is using. The enumeration according VDA5050 with "NATURAL", "REFLECTOR", "RFID", "DMC", "SPOT", "GRID", "OTHER" can be used.'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/localizationtype/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class NavigationType(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"NavigationType",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Type of navigation",
                                r"de": r"Navigationsart",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Type of navigation the AGV uses. The enumeration according VDA5050 with "PHYSICAL_LINE_GUIDED", "VIRTUAL_LINE_GUIDED", "AUTONOMOUS" can be used.'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/navigationtype/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpecialApplications(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"SpecialApplications",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Special applications",
                                r"de": r"Besondere Anwendungsbereiche",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Special applications and usage sectors of the AGV, e.g. EMC environment, chemical industry, mining, clean rooms, refrigerated rooms, areas with explosion risk"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/specialapplications/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpecialCapabilities(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"SpecialCapabilities",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Special capabilities",
                                r"de": r"Besondere Fähigkeiten",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Special capabilities and functions of the AGV"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/specialcapabilities/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class ProtectionClassIP(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ProtectionClassIP",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"IP Protection Class",
                                r"de": r"IP Schutzklasse",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Extent of protection provided by an enclosure against access to hazardous parts, against ingress of solid foreign objects and against ingress of water"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAV695#003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SuitableForOutdoorUse(Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"SuitableForOutdoorUse",
                        value_type: DataTypeDefXsd = bool,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Indicates wether the AGV can be used outdoors (true) or not (false)",
                                r"de": r"Gib an, ob das AGV im Außenbereich (Outdoor) genutzt werden kann (true) oder nicht (false)",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-BAD676#009",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class RequiredEnvironmentalConditions(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"RequiredEnvironmentalConditions",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Required environmental conditions",
                                r"de": r"Erforderliche Umweltbedingungen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Description of required environmental conditions that have to be fulfilled to use the AGV, e.g., floor condition or ambient temperature (min./max.)"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/requiredenvironmentalconditions/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpecialQualificationDemand(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"SpecialQualificationDemand",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Special qualification demand",
                                r"de": r"Besonderer Qualifikationsbedarf",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Demand for the special qualification required"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/specialqualificationdemand/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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
                    agvKinematic: Optional[Union[str, AgvKinematic]] = None,
                    agvClass: Optional[Union[str, AgvClass]] = None,
                    travelDirection: Optional[Union[str, TravelDirection]] = None,
                    transportPrinciple: Optional[Union[str, TransportPrinciple]] = None,
                    localizationType: Optional[Union[str, LocalizationType]] = None,
                    navigationType: Optional[Union[str, NavigationType]] = None,
                    specialApplications: Optional[
                        Union[LangStringSet, SpecialApplications]
                    ] = None,
                    specialCapabilities: Optional[
                        Union[LangStringSet, SpecialCapabilities]
                    ] = None,
                    protectionClassIP: Optional[Union[str, ProtectionClassIP]] = None,
                    suitableForOutdoorUse: Optional[
                        Union[bool, SuitableForOutdoorUse]
                    ] = None,
                    requiredEnvironmentalConditions: Optional[
                        Union[LangStringSet, RequiredEnvironmentalConditions]
                    ] = None,
                    specialQualificationDemand: Optional[
                        Union[LangStringSet, SpecialQualificationDemand]
                    ] = None,
                    id_short: Optional[str] = r"TypeAndApplicationInformation",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Type and application information",
                            r"de": r"Typ- und Anwendungsinformationen",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "Information about the AGV type and the vehicle's applications"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/typeandapplicationinformation/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if agvKinematic and not isinstance(agvKinematic, SubmodelElement):
                        agvKinematic = self.AgvKinematic(agvKinematic)

                    # Build a submodel element if a raw value was passed in the argument
                    if agvClass and not isinstance(agvClass, SubmodelElement):
                        agvClass = self.AgvClass(agvClass)

                    # Build a submodel element if a raw value was passed in the argument
                    if travelDirection and not isinstance(
                        travelDirection, SubmodelElement
                    ):
                        travelDirection = self.TravelDirection(travelDirection)

                    # Build a submodel element if a raw value was passed in the argument
                    if transportPrinciple and not isinstance(
                        transportPrinciple, SubmodelElement
                    ):
                        transportPrinciple = self.TransportPrinciple(transportPrinciple)

                    # Build a submodel element if a raw value was passed in the argument
                    if localizationType and not isinstance(
                        localizationType, SubmodelElement
                    ):
                        localizationType = self.LocalizationType(localizationType)

                    # Build a submodel element if a raw value was passed in the argument
                    if navigationType and not isinstance(
                        navigationType, SubmodelElement
                    ):
                        navigationType = self.NavigationType(navigationType)

                    # Build a submodel element if a raw value was passed in the argument
                    if specialApplications and not isinstance(
                        specialApplications, SubmodelElement
                    ):
                        specialApplications = self.SpecialApplications(
                            specialApplications
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if specialCapabilities and not isinstance(
                        specialCapabilities, SubmodelElement
                    ):
                        specialCapabilities = self.SpecialCapabilities(
                            specialCapabilities
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if protectionClassIP and not isinstance(
                        protectionClassIP, SubmodelElement
                    ):
                        protectionClassIP = self.ProtectionClassIP(protectionClassIP)

                    # Build a submodel element if a raw value was passed in the argument
                    if suitableForOutdoorUse and not isinstance(
                        suitableForOutdoorUse, SubmodelElement
                    ):
                        suitableForOutdoorUse = self.SuitableForOutdoorUse(
                            suitableForOutdoorUse
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if requiredEnvironmentalConditions and not isinstance(
                        requiredEnvironmentalConditions, SubmodelElement
                    ):
                        requiredEnvironmentalConditions = (
                            self.RequiredEnvironmentalConditions(
                                requiredEnvironmentalConditions
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if specialQualificationDemand and not isinstance(
                        specialQualificationDemand, SubmodelElement
                    ):
                        specialQualificationDemand = self.SpecialQualificationDemand(
                            specialQualificationDemand
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
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
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

            class TechnicalParameters(SubmodelElementCollection):

                class MaxLateralInclinationMaxLoad(Property):

                    def __init__(
                        self,
                        value: int,
                        id_short: Optional[str] = r"MaxLateralInclinationMaxLoad",
                        value_type: DataTypeDefXsd = int,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Lateral inclination (max.)",
                                r"de": r"Querneigung (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximal lateral inclination of the AGV when loaded with the maximum weight",
                                r"de": r"Maximale Querneigung des AGV bei Beladung mit maximaler Last",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/maxlateralinclination/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"with max. load",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class MaxLateralInclinationWithoutLoad(Property):

                    def __init__(
                        self,
                        value: int,
                        id_short: Optional[str] = r"MaxLateralInclinationWithoutLoad",
                        value_type: DataTypeDefXsd = int,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Lateral inclination (max.)",
                                r"de": r"Querneigung (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximal lateral inclination of the AGV when unloaded",
                                r"de": r"Maximale Querneigung des AGV wenn ohne Last",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/maxlateralinclination/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"without load",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class MaxClimbingInclinationMaxLoad(Property):

                    def __init__(
                        self,
                        value: int,
                        id_short: Optional[str] = r"MaxClimbingInclinationMaxLoad",
                        value_type: DataTypeDefXsd = int,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Climbing inclination (max.)",
                                r"de": r"Längsneigung (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximal climbing inclination of the AGV when loaded with the maximum weight",
                                r"de": r"Maximale Längsneigung des AGV bei maximaler Last",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/maxclimbinginclination/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"with max. load",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class MaxClimbingInclinationWithoutLoad(Property):

                    def __init__(
                        self,
                        value: int,
                        id_short: Optional[str] = r"MaxClimbingInclinationWithoutLoad",
                        value_type: DataTypeDefXsd = int,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Climbing inclination (max.)",
                                r"de": r"Längsneigung (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximal climbing inclination of the AGV when unloaded",
                                r"de": r"Maximale Längsneigung des AGV wenn ohne Last",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/maxclimbinginclination/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LoadStatus",
                                    value_type=str,
                                    value=r"without load",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class LocalizationSensorDetails(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"LocalizationSensorDetails",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Localization sensor details",
                                r"de": r"Details zur Lokalisierungssensorik",
                            }
                        ),
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about used localization sensors by the AGV"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/localizationsensordetails/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class LocalizationAccuracy(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"LocalizationAccuracy",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Localization accuracy",
                                r"de": r"Lokalisierungsgenauigkeit",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Accuracy of the determination of the current location of the AGV"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/localizationaccuracy/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class PositioningAccuracy(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"PositioningAccuracy",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Positioning accuracy",
                                r"de": r"Positionierungsgenauigkeit",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={r"en": r"Positioning accuracy of the AGV"}
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/positioningaccuracy/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class MaxLoadMass(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"MaxLoadMass",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximal load on the AGV including attachments and load"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABJ258#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class InterfacesForAttachments(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"InterfacesForAttachments",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Interfaces for attachments",
                                r"de": r"Schnittstellen für Anbauten",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Description of the mechanical and electrical interfaces for load handling attachments and other attachments"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/interfacesforattachments/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SystemAvailability(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"SystemAvailability",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"System availability",
                                r"de": r"Systemverfügbarkeit",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"System availability of the AGV ",
                                r"de": r"Systemverfügbarkeit des AGV ",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABA730#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class MaxRunTimeAsSpecified(Property):

                    def __init__(
                        self,
                        value: int,
                        id_short: Optional[str] = r"MaxRunTimeAsSpecified",
                        value_type: DataTypeDefXsd = int,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Run time (max.)", r"de": r"Run time (max.)"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Max runtime as stated in the specification sheet of the AGV",
                                r"de": r"Maximale Laufzeit wie für das AGV vom Hersteller spezifiziert",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAJ479#004",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"SPEC",
                                    value_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF579",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF575",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class MaxRunTimeAsOperated(Property):

                    def __init__(
                        self,
                        value: int,
                        id_short: Optional[str] = r"MaxRunTimeAsOperated",
                        value_type: DataTypeDefXsd = int,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Run time (max.)", r"de": r"Laufzeit (max.)"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Max runtime as the AGV is operated in the current environment",
                                r"de": r"Maximale Laufzeit des AGV wie aktuell im Gesamtsystem implementiert",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAJ479#004",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"OP",
                                    value_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF578",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF575",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpeedMin(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"SpeedMin",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Speed (min.)",
                                r"de": r"Geschwindigkeit (min.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={r"en": r"Minimum controlled continuous speed"}
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/speedmin/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpeedMaxEmptyAsSpecified(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"SpeedMaxEmptyAsSpecified",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Speed without load (max.)",
                                r"de": r"Geschwindigkeit ohne Ladung (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum speed without load as specified by the manufacturer",
                                r"de": r"Maximale Geschwindigkeit ohne Beladung wie durch den Hersteller spezifiziert",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/speedmaxempty/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"SPEC",
                                    value_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF573",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF575",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpeedMaxEmptyAsOperated(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"SpeedMaxEmptyAsOperated",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum speed without load as in the current system operated",
                                r"de": r"Maximale Geschwindigkeit ohne Beladung wie im aktuellen System betrieben",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/speedmaxempty/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"OP",
                                    value_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF578",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF575",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpeedMaxWithMaxLoadAsSpecified(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"SpeedMaxWithMaxLoadAsSpecified",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Speed with maximum load (max.)",
                                r"de": r"Geschwindigkeit mit maximaler Ladung (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum speed with maximal load as specified by the manufacturer",
                                r"de": r"Maximale Geschwindigkeit bei maximal zulässiger Beladung wie durch den Hersteller vorgegeben",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/speedmaxwithmaxload/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"SPEC",
                                    value_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF579",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF575",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SpeedMaxWithMaxLoadAsOperated(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"SpeedMaxWithMaxLoadAsOperated",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Speed with maximum load (max.)",
                                r"de": r"Geschwindigkeit mit maximaler Ladung (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum speed with maximal load as operated in the current system",
                                r"de": r"Maximale Geschwindigkeit bei maximal zulässiger Beladung wie im aktuellen System betrieben",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/speedmaxwithmaxload/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"LifeCycleQual",
                                    value_type=str,
                                    value=r"OP",
                                    value_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF579",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"0112/2///61360_4#AAF575",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class AccelerationMax(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"AccelerationMax",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Acceleration (max.)",
                                r"de": r"Beschleuniging (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum acceleration of the AGV with maximum load",
                                r"de": r"Maximale Beschleunigung des AGV mit maximaler Last",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABG746#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class DecelerationMax(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"DecelerationMax",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Maximum deceleration",
                                r"de": r"Maximale Verzögerung",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum deceleration of the AGV with maximum load",
                                r"de": r"Maximale Verzögerung des AGV mit maximaler Last",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/decelerationmax/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class VehicleHeightMax(Property):

                    def __init__(
                        self,
                        value: Float,
                        id_short: Optional[str] = r"VehicleHeightMax",
                        value_type: DataTypeDefXsd = Float,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Vehicle height (max.)",
                                r"de": r"Fahrzeughöhe (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum height of the AGV without attachments",
                                r"de": r"Maximale Höhe des AGV ohne Anbauten",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-BAE355#006",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class VehicleWidth(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"VehicleWidth",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Vehicle width (max.)",
                                r"de": r"Fahrzeugbreite (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum vehicle width",
                                r"de": r"Maximale Fahrzeugbreite",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAG933#004",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class VehicleLength(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"VehicleLength",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Vehicle length (max.)",
                                r"de": r"Fahrzeuglänge (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum lengths of the AGV including outstanding components",
                                r"de": r"Maximale Länge des AGV einschließlich überstehender Komponenten",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABE774#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class VehicleWeight(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"VehicleWeight",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Vehicle weight (max.)",
                                r"de": r"Fahrzeuggewicht (max.)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Maximum weight of the AGV without necessary weights",
                                r"de": r"Maximales Gewicht des AGV ohne Gegengewichte",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABD800#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class Emissions(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"Emissions",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"emissions", r"de": r"Emissionen"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Description of emissions of the AGV during operation, e.g. noise or exhaust"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/emissions/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class MapProcessingInformation(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"MapProcessingInformation",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Map processing information",
                                r"de": r"Informationen zur Kartenverarbeitung",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about how the digital map is generated and processed by the AGV"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/mapprocessinginformation/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class ManualControllerInformation(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"ManualControllerInformation",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Manual controller information",
                                r"de": r"Informationen zur manuellen Steuerung",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about the manual controllers of the AGV"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/manualcontrollerinformation/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class DigitalAnalogInterfaces(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"DigitalAnalogInterfaces",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Digital and analog interfaces",
                                r"de": r"Digitale und analoge Schnittstellen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about digital and analog interfaces of the AGV"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/digitalanaloginterfaces/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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
                    maxLateralInclinationMaxLoad: Optional[
                        Union[int, MaxLateralInclinationMaxLoad]
                    ] = None,
                    maxLateralInclinationWithoutLoad: Optional[
                        Union[int, MaxLateralInclinationWithoutLoad]
                    ] = None,
                    maxClimbingInclinationMaxLoad: Optional[
                        Union[int, MaxClimbingInclinationMaxLoad]
                    ] = None,
                    maxClimbingInclinationWithoutLoad: Optional[
                        Union[int, MaxClimbingInclinationWithoutLoad]
                    ] = None,
                    localizationSensorDetails: Optional[
                        Union[LangStringSet, LocalizationSensorDetails]
                    ] = None,
                    localizationAccuracy: Optional[
                        Union[Float, LocalizationAccuracy]
                    ] = None,
                    positioningAccuracy: Optional[
                        Union[Float, PositioningAccuracy]
                    ] = None,
                    maxLoadMass: Optional[Union[Float, MaxLoadMass]] = None,
                    interfacesForAttachments: Optional[
                        Union[LangStringSet, InterfacesForAttachments]
                    ] = None,
                    systemAvailability: Optional[
                        Union[Float, SystemAvailability]
                    ] = None,
                    maxRunTimeAsSpecified: Optional[
                        Union[int, MaxRunTimeAsSpecified]
                    ] = None,
                    maxRunTimeAsOperated: Optional[
                        Union[int, MaxRunTimeAsOperated]
                    ] = None,
                    speedMin: Optional[Union[Float, SpeedMin]] = None,
                    speedMaxEmptyAsSpecified: Optional[
                        Union[Float, SpeedMaxEmptyAsSpecified]
                    ] = None,
                    speedMaxEmptyAsOperated: Optional[
                        Union[Float, SpeedMaxEmptyAsOperated]
                    ] = None,
                    speedMaxWithMaxLoadAsSpecified: Optional[
                        Union[Float, SpeedMaxWithMaxLoadAsSpecified]
                    ] = None,
                    speedMaxWithMaxLoadAsOperated: Optional[
                        Union[Float, SpeedMaxWithMaxLoadAsOperated]
                    ] = None,
                    accelerationMax: Optional[Union[Float, AccelerationMax]] = None,
                    decelerationMax: Optional[Union[Float, DecelerationMax]] = None,
                    vehicleHeightMax: Optional[Union[Float, VehicleHeightMax]] = None,
                    vehicleWidth: Optional[Union[str, VehicleWidth]] = None,
                    vehicleLength: Optional[Union[str, VehicleLength]] = None,
                    vehicleWeight: Optional[Union[str, VehicleWeight]] = None,
                    emissions: Optional[Union[LangStringSet, Emissions]] = None,
                    mapProcessingInformation: Optional[
                        Union[LangStringSet, MapProcessingInformation]
                    ] = None,
                    manualControllerInformation: Optional[
                        Union[LangStringSet, ManualControllerInformation]
                    ] = None,
                    digitalAnalogInterfaces: Optional[
                        Union[LangStringSet, DigitalAnalogInterfaces]
                    ] = None,
                    id_short: Optional[str] = r"TechnicalParameters",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Technical parameters",
                            r"de": r"Technische Parameter",
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Technical parameters/properties of the AGV"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/technicalparameters/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if maxLateralInclinationMaxLoad and not isinstance(
                        maxLateralInclinationMaxLoad, SubmodelElement
                    ):
                        maxLateralInclinationMaxLoad = (
                            self.MaxLateralInclinationMaxLoad(
                                maxLateralInclinationMaxLoad
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if maxLateralInclinationWithoutLoad and not isinstance(
                        maxLateralInclinationWithoutLoad, SubmodelElement
                    ):
                        maxLateralInclinationWithoutLoad = (
                            self.MaxLateralInclinationWithoutLoad(
                                maxLateralInclinationWithoutLoad
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if maxClimbingInclinationMaxLoad and not isinstance(
                        maxClimbingInclinationMaxLoad, SubmodelElement
                    ):
                        maxClimbingInclinationMaxLoad = (
                            self.MaxClimbingInclinationMaxLoad(
                                maxClimbingInclinationMaxLoad
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if maxClimbingInclinationWithoutLoad and not isinstance(
                        maxClimbingInclinationWithoutLoad, SubmodelElement
                    ):
                        maxClimbingInclinationWithoutLoad = (
                            self.MaxClimbingInclinationWithoutLoad(
                                maxClimbingInclinationWithoutLoad
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if localizationSensorDetails and not isinstance(
                        localizationSensorDetails, SubmodelElement
                    ):
                        localizationSensorDetails = self.LocalizationSensorDetails(
                            localizationSensorDetails
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if localizationAccuracy and not isinstance(
                        localizationAccuracy, SubmodelElement
                    ):
                        localizationAccuracy = self.LocalizationAccuracy(
                            localizationAccuracy
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if positioningAccuracy and not isinstance(
                        positioningAccuracy, SubmodelElement
                    ):
                        positioningAccuracy = self.PositioningAccuracy(
                            positioningAccuracy
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if maxLoadMass and not isinstance(maxLoadMass, SubmodelElement):
                        maxLoadMass = self.MaxLoadMass(maxLoadMass)

                    # Build a submodel element if a raw value was passed in the argument
                    if interfacesForAttachments and not isinstance(
                        interfacesForAttachments, SubmodelElement
                    ):
                        interfacesForAttachments = self.InterfacesForAttachments(
                            interfacesForAttachments
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if systemAvailability and not isinstance(
                        systemAvailability, SubmodelElement
                    ):
                        systemAvailability = self.SystemAvailability(systemAvailability)

                    # Build a submodel element if a raw value was passed in the argument
                    if maxRunTimeAsSpecified and not isinstance(
                        maxRunTimeAsSpecified, SubmodelElement
                    ):
                        maxRunTimeAsSpecified = self.MaxRunTimeAsSpecified(
                            maxRunTimeAsSpecified
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if maxRunTimeAsOperated and not isinstance(
                        maxRunTimeAsOperated, SubmodelElement
                    ):
                        maxRunTimeAsOperated = self.MaxRunTimeAsOperated(
                            maxRunTimeAsOperated
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if speedMin and not isinstance(speedMin, SubmodelElement):
                        speedMin = self.SpeedMin(speedMin)

                    # Build a submodel element if a raw value was passed in the argument
                    if speedMaxEmptyAsSpecified and not isinstance(
                        speedMaxEmptyAsSpecified, SubmodelElement
                    ):
                        speedMaxEmptyAsSpecified = self.SpeedMaxEmptyAsSpecified(
                            speedMaxEmptyAsSpecified
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if speedMaxEmptyAsOperated and not isinstance(
                        speedMaxEmptyAsOperated, SubmodelElement
                    ):
                        speedMaxEmptyAsOperated = self.SpeedMaxEmptyAsOperated(
                            speedMaxEmptyAsOperated
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if speedMaxWithMaxLoadAsSpecified and not isinstance(
                        speedMaxWithMaxLoadAsSpecified, SubmodelElement
                    ):
                        speedMaxWithMaxLoadAsSpecified = (
                            self.SpeedMaxWithMaxLoadAsSpecified(
                                speedMaxWithMaxLoadAsSpecified
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if speedMaxWithMaxLoadAsOperated and not isinstance(
                        speedMaxWithMaxLoadAsOperated, SubmodelElement
                    ):
                        speedMaxWithMaxLoadAsOperated = (
                            self.SpeedMaxWithMaxLoadAsOperated(
                                speedMaxWithMaxLoadAsOperated
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if accelerationMax and not isinstance(
                        accelerationMax, SubmodelElement
                    ):
                        accelerationMax = self.AccelerationMax(accelerationMax)

                    # Build a submodel element if a raw value was passed in the argument
                    if decelerationMax and not isinstance(
                        decelerationMax, SubmodelElement
                    ):
                        decelerationMax = self.DecelerationMax(decelerationMax)

                    # Build a submodel element if a raw value was passed in the argument
                    if vehicleHeightMax and not isinstance(
                        vehicleHeightMax, SubmodelElement
                    ):
                        vehicleHeightMax = self.VehicleHeightMax(vehicleHeightMax)

                    # Build a submodel element if a raw value was passed in the argument
                    if vehicleWidth and not isinstance(vehicleWidth, SubmodelElement):
                        vehicleWidth = self.VehicleWidth(vehicleWidth)

                    # Build a submodel element if a raw value was passed in the argument
                    if vehicleLength and not isinstance(vehicleLength, SubmodelElement):
                        vehicleLength = self.VehicleLength(vehicleLength)

                    # Build a submodel element if a raw value was passed in the argument
                    if vehicleWeight and not isinstance(vehicleWeight, SubmodelElement):
                        vehicleWeight = self.VehicleWeight(vehicleWeight)

                    # Build a submodel element if a raw value was passed in the argument
                    if emissions and not isinstance(emissions, SubmodelElement):
                        emissions = self.Emissions(emissions)

                    # Build a submodel element if a raw value was passed in the argument
                    if mapProcessingInformation and not isinstance(
                        mapProcessingInformation, SubmodelElement
                    ):
                        mapProcessingInformation = self.MapProcessingInformation(
                            mapProcessingInformation
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if manualControllerInformation and not isinstance(
                        manualControllerInformation, SubmodelElement
                    ):
                        manualControllerInformation = self.ManualControllerInformation(
                            manualControllerInformation
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if digitalAnalogInterfaces and not isinstance(
                        digitalAnalogInterfaces, SubmodelElement
                    ):
                        digitalAnalogInterfaces = self.DigitalAnalogInterfaces(
                            digitalAnalogInterfaces
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
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
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

            class VDA5050Factsheet(SubmodelElementCollection):

                class TypeSpecification(Blob):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"TypeSpecification",
                        content_type: Optional[str] = r"application/json",
                        value: Optional[bytes] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"typeSpecification (JSON-object)",
                                r"de": r"typeSpecification (JSON-Objekt)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'JSON-object "typeSpecification" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                r"de": r'JSON-Objekt "typeSpecification" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/typespecification/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            id_short=id_short,
                            content_type=content_type,
                            value=value,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class PhysicalParameters(Blob):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"PhysicalParameters",
                        content_type: Optional[str] = r"application/json",
                        value: Optional[bytes] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"physicalParameters (JSON-object)",
                                r"de": r"physicalParameters (JSON-Objekt)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'JSON-object "physicalParameters" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                r"de": r'JSON-Objekt "physicalParameters" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/pysicalparameters/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            id_short=id_short,
                            content_type=content_type,
                            value=value,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ProtocolLimits(Blob):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"ProtocolLimits",
                        content_type: Optional[str] = r"application/json",
                        value: Optional[bytes] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"protocolLimits (JSON-object)",
                                r"de": r"protocolLimits (JSON-Objekt)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'JSON-object "protocolLimits" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                r"de": r'JSON-Objekt "protocolLimits" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/protocollimits/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            id_short=id_short,
                            content_type=content_type,
                            value=value,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ProtocolFeatures(Blob):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"ProtocolFeatures",
                        content_type: Optional[str] = r"application/json",
                        value: Optional[bytes] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"protocolFeatures (JSON-object)",
                                r"de": r"protocolFeatures (JSON-Objekt)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'JSON-object "protocolFeatures" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                r"de": r'JSON-Objekt "protocolFeatures" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/protocolfeatures/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            id_short=id_short,
                            content_type=content_type,
                            value=value,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class AgvGeometry(Blob):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"AgvGeometry",
                        content_type: Optional[str] = r"application/json",
                        value: Optional[bytes] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"agvGeometry (JSON-object)",
                                r"de": r"agvGeometry (JSON-Objekt)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'JSON-object "agvGeometry" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                r"de": r'JSON-Objekt "agvGeometry" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/agvgeometry/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            id_short=id_short,
                            content_type=content_type,
                            value=value,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class LoadSpecification(Blob):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"LoadSpecification",
                        content_type: Optional[str] = r"application/json",
                        value: Optional[bytes] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"loadSpecification (JSON-object)",
                                r"de": r"loadSpecification (JSON-Objekt)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'JSON-object "loadSpecification" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                r"de": r'JSON-Objekt "loadSpecification" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/loadspecification/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            id_short=id_short,
                            content_type=content_type,
                            value=value,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class LocalizationParameters(Blob):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"LocalizationParameters",
                        content_type: Optional[str] = r"application/json",
                        value: Optional[bytes] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"localizationParameters (JSON-object)",
                                r"de": r"localizationParameters (JSON-Objekt)",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'JSON-object "localizationParameters" according VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                                r"de": r'JSON-Objekt "localizationParameters" entsprechend VDA5050 Factsheet, Version 2.0.0, January 2022 ',
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/localizationparameters/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            id_short=id_short,
                            content_type=content_type,
                            value=value,
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
                    typeSpecification: Optional[TypeSpecification] = None,
                    physicalParameters: Optional[PhysicalParameters] = None,
                    protocolLimits: Optional[ProtocolLimits] = None,
                    protocolFeatures: Optional[ProtocolFeatures] = None,
                    agvGeometry: Optional[AgvGeometry] = None,
                    loadSpecification: Optional[LoadSpecification] = None,
                    localizationParameters: Optional[LocalizationParameters] = None,
                    id_short: Optional[str] = r"VDA5050Factsheet",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Factsheet data according VDA 5050 MQTT communication protocol"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/vda5050factsheet/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        typeSpecification,
                        physicalParameters,
                        protocolLimits,
                        protocolFeatures,
                        agvGeometry,
                        loadSpecification,
                        localizationParameters,
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

            class Energy(SubmodelElementCollection):

                class EnergySource(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"EnergySource",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Energy source", r"de": r"Energiequelle"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Type of auxiliary energy the AGV is consuming, the enumeration "POWER", "DIESEL", "GAS", "HYDROGEN", "HYBRID", "SOLAR", "OTHER" can be used'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/energysource/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class EnergyAbsorption(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"EnergyAbsorption",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Energy absorption",
                                r"de": r"Energieaufnahme",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Way to absorb auxiliary energy. The enumeration "INDUCTION", "CONDUCTORRAIL", "FLEXIBLECABLE", "CHARGINGCABLE", "FILLER", "OTHER" can be used'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/energyabsorption/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class EnergyStorage(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"EnergyStorage",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Energy storage", r"de": r"Energiespeicher"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r'Type of storage the AGV is using. The enumeration "BATTERY", "TANK", "CARTRIDGE", "CAPACITOR", "OTHER" can be used.'
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/energystorage/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class Battery(SubmodelElementCollection):

                    class ChargingDeviceRequirements(MultiLanguageProperty):

                        def __init__(
                            self,
                            value: LangStringSet,
                            id_short: Optional[str] = r"ChargingDeviceRequirements",
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={
                                    r"en": r"Charging device requirements",
                                    r"de": r"Anforderungen an die Ladestation",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Requirements of the AGV for the charging station and infrastructure, e.g., voltage range or max. current"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/technicaldataagv/chargingdevicerequirements/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[Qualifier] = None,
                            extension: Iterable[Extension] = (),
                            supplemental_semantic_id: Iterable[Reference] = (),
                            embedded_data_specifications: Iterable[
                                EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

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

                    class BatteryInformation(MultiLanguageProperty):

                        def __init__(
                            self,
                            value: LangStringSet,
                            id_short: Optional[str] = r"BatteryInformation",
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={
                                    r"en": r"Battery information",
                                    r"de": r"Informationen zur Batterie",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about the used battery of the AGV, for example type of battery (e.g., NiCd), capacity and max. charge cycles"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/technicaldataagv/batteryinformation/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[Qualifier] = None,
                            extension: Iterable[Extension] = (),
                            supplemental_semantic_id: Iterable[Reference] = (),
                            embedded_data_specifications: Iterable[
                                EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

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

                    class ChargingTimeAsSpecified(Property):

                        def __init__(
                            self,
                            value: Float,
                            id_short: Optional[str] = r"ChargingTimeAsSpecified",
                            value_type: DataTypeDefXsd = Float,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Charging time", r"de": r"Ladedauer"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Charging time of the AGV from empty to full capacity as specified by the manufacturer",
                                    r"de": r"Ladedauer des AGV von leer nach voll wie vom Hersteller spezifiziert",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAF391#006",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[Qualifier] = None,
                            extension: Iterable[Extension] = (),
                            supplemental_semantic_id: Iterable[Reference] = (),
                            embedded_data_specifications: Iterable[
                                EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    Qualifier(
                                        type_=r"LifeCycleQual",
                                        value_type=str,
                                        value=r"SPEC",
                                        value_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"0112/2///61360_4#AAF579",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"0112/2///61360_4#AAF575",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

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

                    class ChargingTimeAsOperated(Property):

                        def __init__(
                            self,
                            value: Float,
                            id_short: Optional[str] = r"ChargingTimeAsOperated",
                            value_type: DataTypeDefXsd = Float,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Charging time", r"de": r"Ladedauer"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Charging time of the AGV from empty to full capacity as implemented in the current system",
                                    r"de": r"Ladedauer des AGV von leer nach voll, wie im aktuellen System implementiert",
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-AAF391#006",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[Qualifier] = None,
                            extension: Iterable[Extension] = (),
                            supplemental_semantic_id: Iterable[Reference] = (),
                            embedded_data_specifications: Iterable[
                                EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    Qualifier(
                                        type_=r"LifeCycleQual",
                                        value_type=str,
                                        value=r"OP",
                                        value_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"0112/2///61360_4#AAF579",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"0112/2///61360_4#AAF575",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

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

                    class RemainingChargeCycles(Property):

                        def __init__(
                            self,
                            value: int,
                            id_short: Optional[str] = r"RemainingChargeCycles",
                            value_type: DataTypeDefXsd = int,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={
                                    r"en": r"Remaining charge cycles",
                                    r"de": r"Verbleibende Ladezyklen",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Assumed remaining charge cycles of the battery"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/technicaldataagv/remainingchargecycles/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[Qualifier] = None,
                            extension: Iterable[Extension] = (),
                            supplemental_semantic_id: Iterable[Reference] = (),
                            embedded_data_specifications: Iterable[
                                EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

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
                        chargingDeviceRequirements: Optional[
                            Union[LangStringSet, ChargingDeviceRequirements]
                        ] = None,
                        batteryInformation: Optional[
                            Union[LangStringSet, BatteryInformation]
                        ] = None,
                        chargingTimeAsSpecified: Optional[
                            Union[Float, ChargingTimeAsSpecified]
                        ] = None,
                        chargingTimeAsOperated: Optional[
                            Union[Float, ChargingTimeAsOperated]
                        ] = None,
                        remainingChargeCycles: Optional[
                            Union[int, RemainingChargeCycles]
                        ] = None,
                        id_short: Optional[str] = r"Battery",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={r"en": r"Information about the battery of the AGV"}
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/battery/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument
                        if chargingDeviceRequirements and not isinstance(
                            chargingDeviceRequirements, SubmodelElement
                        ):
                            chargingDeviceRequirements = (
                                self.ChargingDeviceRequirements(
                                    chargingDeviceRequirements
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if batteryInformation and not isinstance(
                            batteryInformation, SubmodelElement
                        ):
                            batteryInformation = self.BatteryInformation(
                                batteryInformation
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if chargingTimeAsSpecified and not isinstance(
                            chargingTimeAsSpecified, SubmodelElement
                        ):
                            chargingTimeAsSpecified = self.ChargingTimeAsSpecified(
                                chargingTimeAsSpecified
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if chargingTimeAsOperated and not isinstance(
                            chargingTimeAsOperated, SubmodelElement
                        ):
                            chargingTimeAsOperated = self.ChargingTimeAsOperated(
                                chargingTimeAsOperated
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if remainingChargeCycles and not isinstance(
                            remainingChargeCycles, SubmodelElement
                        ):
                            remainingChargeCycles = self.RemainingChargeCycles(
                                remainingChargeCycles
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            chargingDeviceRequirements,
                            batteryInformation,
                            chargingTimeAsSpecified,
                            chargingTimeAsOperated,
                            remainingChargeCycles,
                        ]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

                class PowerTransmissionToExternal(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"PowerTransmissionToExternal",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Power transmission to external",
                                r"de": r"Energieübertragung nach extern",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about mechanical or electrical power transmission capabilities from the AGV to external devices"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/powertransmissionexternal/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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
                    battery: Battery,
                    energySource: Optional[Union[str, EnergySource]] = None,
                    energyAbsorption: Optional[Union[str, EnergyAbsorption]] = None,
                    energyStorage: Optional[Union[str, EnergyStorage]] = None,
                    powerTransmissionToExternal: Optional[
                        Union[LangStringSet, PowerTransmissionToExternal]
                    ] = None,
                    id_short: Optional[str] = r"Energy",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Technical properties related to the energy supply of the AGV"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/energy/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if energySource and not isinstance(energySource, SubmodelElement):
                        energySource = self.EnergySource(energySource)

                    # Build a submodel element if a raw value was passed in the argument
                    if energyAbsorption and not isinstance(
                        energyAbsorption, SubmodelElement
                    ):
                        energyAbsorption = self.EnergyAbsorption(energyAbsorption)

                    # Build a submodel element if a raw value was passed in the argument
                    if energyStorage and not isinstance(energyStorage, SubmodelElement):
                        energyStorage = self.EnergyStorage(energyStorage)

                    # Build a submodel element if a raw value was passed in the argument
                    if powerTransmissionToExternal and not isinstance(
                        powerTransmissionToExternal, SubmodelElement
                    ):
                        powerTransmissionToExternal = self.PowerTransmissionToExternal(
                            powerTransmissionToExternal
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        energySource,
                        energyAbsorption,
                        energyStorage,
                        battery,
                        powerTransmissionToExternal,
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

            class CommunicationAndControl(SubmodelElementCollection):

                class CommunicationProtocol(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"CommunicationProtocol",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Communication protocol",
                                r"de": r"Kommunikationsprotokoll",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information regarding the supported communication protocols, like MQTT, HTTP, OPC UA or ROS2"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/communicationprotocol/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class CommunicationNetwork(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"CommunicationNetwork",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Communication network",
                                r"de": r"Kommunikationsnetzwerk",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information regarding the supported communication networks, like WLAN, 5G or IrDA"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/communicationnetwork/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class VDA5050InterfaceDescription(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"VDA5050InterfaceDescription",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"VDA5050 Interface Description",
                                r"de": r"VDA5050 Schnittstellenbeschreibung",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about the MQTT communication according VDA 5050"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/vda5050interfacedescription/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class AutomationInterface(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"AutomationInterface",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Automation interface",
                                r"de": r"Automatisierungsschnittstellen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about the supported automation interfaces and standards, like ROS1, ROS2, IO-Link or OPC UA"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/automationinterface/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class ControlSystemInformation(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"ControlSystemInformation",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Control system information",
                                r"de": r"Informationen zur Steuerung",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information regarding the used control system for the vehicle, e.g., SPS"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/controlsysteminformation/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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
                    communicationProtocol: Optional[
                        Union[LangStringSet, CommunicationProtocol]
                    ] = None,
                    communicationNetwork: Optional[
                        Union[LangStringSet, CommunicationNetwork]
                    ] = None,
                    vDA5050InterfaceDescription: Optional[
                        Union[LangStringSet, VDA5050InterfaceDescription]
                    ] = None,
                    automationInterface: Optional[
                        Union[LangStringSet, AutomationInterface]
                    ] = None,
                    controlSystemInformation: Optional[
                        Union[LangStringSet, ControlSystemInformation]
                    ] = None,
                    id_short: Optional[str] = r"CommunicationAndControl",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Technical properties related to the communication and control of the AGV"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/communicationandcontrol/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if communicationProtocol and not isinstance(
                        communicationProtocol, SubmodelElement
                    ):
                        communicationProtocol = self.CommunicationProtocol(
                            communicationProtocol
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if communicationNetwork and not isinstance(
                        communicationNetwork, SubmodelElement
                    ):
                        communicationNetwork = self.CommunicationNetwork(
                            communicationNetwork
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if vDA5050InterfaceDescription and not isinstance(
                        vDA5050InterfaceDescription, SubmodelElement
                    ):
                        vDA5050InterfaceDescription = self.VDA5050InterfaceDescription(
                            vDA5050InterfaceDescription
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if automationInterface and not isinstance(
                        automationInterface, SubmodelElement
                    ):
                        automationInterface = self.AutomationInterface(
                            automationInterface
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if controlSystemInformation and not isinstance(
                        controlSystemInformation, SubmodelElement
                    ):
                        controlSystemInformation = self.ControlSystemInformation(
                            controlSystemInformation
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        communicationProtocol,
                        communicationNetwork,
                        vDA5050InterfaceDescription,
                        automationInterface,
                        controlSystemInformation,
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

            class Safety(SubmodelElementCollection):

                class ConformityToSafetyStandards(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"ConformityToSafetyStandards",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Conformity to safety standards",
                                r"de": r"Konformität zu Sicherheitsstandards",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information regarding the safety standards that are met by the vehicle and certifications"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/conformitytosafetystandards/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class ManualControlInformation(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"ManualControlInformation",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Manual control information",
                                r"de": r"Informationen zur manuellen Steuerung",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Safety information for manual control of the vehicle"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/manualcontrolinformation/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SafetySensorTechnology(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"SafetySensorTechnology",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Safety sensor technology",
                                r"de": r"Sicherheitssensorik",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about the sensor technology implemented to ensure vehicle safety"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/safetysensortechnology/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class SafetyMechanics(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"SafetyMechanics",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Safety mechanics",
                                r"de": r"Mechanische Sicherheitseinrichtungen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information regarding implemented mechanical measures to ensure safety"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/safetymechanics/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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
                    conformityToSafetyStandards: Optional[
                        Union[LangStringSet, ConformityToSafetyStandards]
                    ] = None,
                    manualControlInformation: Optional[
                        Union[LangStringSet, ManualControlInformation]
                    ] = None,
                    safetySensorTechnology: Optional[
                        Union[LangStringSet, SafetySensorTechnology]
                    ] = None,
                    safetyMechanics: Optional[
                        Union[LangStringSet, SafetyMechanics]
                    ] = None,
                    id_short: Optional[str] = r"Safety",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Technical properties related to the safety of the AGV"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/safety/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if conformityToSafetyStandards and not isinstance(
                        conformityToSafetyStandards, SubmodelElement
                    ):
                        conformityToSafetyStandards = self.ConformityToSafetyStandards(
                            conformityToSafetyStandards
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if manualControlInformation and not isinstance(
                        manualControlInformation, SubmodelElement
                    ):
                        manualControlInformation = self.ManualControlInformation(
                            manualControlInformation
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if safetySensorTechnology and not isinstance(
                        safetySensorTechnology, SubmodelElement
                    ):
                        safetySensorTechnology = self.SafetySensorTechnology(
                            safetySensorTechnology
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if safetyMechanics and not isinstance(
                        safetyMechanics, SubmodelElement
                    ):
                        safetyMechanics = self.SafetyMechanics(safetyMechanics)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        conformityToSafetyStandards,
                        manualControlInformation,
                        safetySensorTechnology,
                        safetyMechanics,
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

            class TemporaryTechnicalData(SubmodelElementCollection):

                class CurrentWorkingSetupName(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"CurrentWorkingSetupName",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Current working setup ",
                                r"de": r"Aktuelle Arbeitskonfiguration",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={r"en": r"Name of the current working setup"}
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/currentworkingsetup/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class ActiveLoading(Property):

                    def __init__(
                        self,
                        value: bool,
                        id_short: Optional[str] = r"ActiveLoading",
                        value_type: DataTypeDefXsd = bool,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Active loading", r"de": r"Aktive Beladung"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Describes whether the AGV is currently able to load itself (true)"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/activeloading/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class LoadingType(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"LoadingType",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={r"en": r"Loading type", r"de": r"Beladungsart"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Way of loading of the AGV, the enumeration acc. VDI 2510 can be used"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/loadingtype/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class LoadingRequirements(MultiLanguageProperty):

                    def __init__(
                        self,
                        value: LangStringSet,
                        id_short: Optional[str] = r"LoadingRequirements",
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Loading requirements",
                                r"de": r"Beladungsanforderungen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Requirements and instructions when loading with the current setup, e.g., load floor to floor vs. height difference"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/loadingrequirements/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class CurrentAttachments(SubmodelElementList):

                    class Currentattachments_item(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"currentattachments_item",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Attachment (ID)", r"de": r"Anbau (ID)"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={r"en": r"Order not relevant"}
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/technicaldataagv/attachmentid/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[Qualifier] = None,
                            extension: Iterable[Extension] = (),
                            supplemental_semantic_id: Iterable[Reference] = (),
                            embedded_data_specifications: Iterable[
                                EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

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
                        currentattachments_items: Optional[
                            Iterable[Union[str, Currentattachments_item]]
                        ] = None,
                        id_short: Optional[str] = r"CurrentAttachments",
                        type_value_list_element: SubmodelElement = Property,
                        semantic_id_list_element: Optional[
                            Reference
                        ] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/attachmentid/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        value_type_list_element: Optional[DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Current attachments",
                                r"de": r"Aktuelle Anbauten ",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"List with the identification of current attachments on the AGV, e.g., for load handling",
                                r"de": r"Liste mit Idents der aktuellen Anbauten am AGV, z.B. für die Ladungshandhabung",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/currentattachments/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a list of submodel elements if a raw values were passed in the argument
                        if currentattachments_items and all(
                            [isinstance(i, str) for i in currentattachments_items]
                        ):
                            currentattachments_items = [
                                self.Currentattachments_item(i)
                                for i in currentattachments_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [currentattachments_items]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

                    def _check_constraints(self, new, existing) -> None:
                        # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                        # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                        saved_id_short = new.id_short
                        new.id_short = None

                        # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                        if not isinstance(new, self.type_value_list_element):
                            raise base.AASConstraintViolation(
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
                            raise base.AASConstraintViolation(
                                107,
                                f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                                "is specified all first level children must have the same "
                                f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                            )

                        # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                        # is either Property or Range. Thus, `new` must have the value_type property.
                        # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                        if (
                            isinstance(self.type_value_list_element, Property)
                            or isinstance(self.type_value_list_element, Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
                        ):  # type: ignore
                            raise base.AASConstraintViolation(
                                109,
                                "All first level elements must have the value_type "  # type: ignore
                                "specified by value_type_list_element="
                                f"{self.value_type_list_element.__name__}, got "  # type: ignore
                                f"{new!r} with value_type={new.value_type.__name__}",
                            )  # type: ignore

                        # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                        # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                        if (
                            new.semantic_id is not None
                            and self.semantic_id_list_element is None
                        ):
                            for item in existing:
                                if (
                                    item.semantic_id is not None
                                    and new.semantic_id != item.semantic_id
                                ):
                                    raise base.AASConstraintViolation(
                                        114,
                                        f"Element to be added {new!r} has semantic_id "
                                        f"{new.semantic_id!r}, while already contained element "
                                        f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                        "aren't equal.",
                                    )

                        # Re-assign id_short
                        new.id_short = saved_id_short

                class ProprietaryConfigurationOptions(SubmodelElementList):

                    class Proprietaryconfigurationoptions_item(
                        SubmodelElementCollection
                    ):

                        class OptionName(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"OptionName",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Option name", r"de": r"Optionsname"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Name of the proprietary configuration option"
                                    }
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/technicaldataagv/optionname/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[Qualifier] = None,
                                extension: Iterable[Extension] = (),
                                supplemental_semantic_id: Iterable[Reference] = (),
                                embedded_data_specifications: Iterable[
                                    EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                                            semantic_id=ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                    )

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

                        class OptionValue(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"OptionValue",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Option value",
                                        r"de": r"Optionswert",
                                    }
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={r"en": r"Value of the proprietary option"}
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/technicaldataagv/optionvalue/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[Qualifier] = None,
                                extension: Iterable[Extension] = (),
                                supplemental_semantic_id: Iterable[Reference] = (),
                                embedded_data_specifications: Iterable[
                                    EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                                            semantic_id=ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                    )

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
                            optionName: Union[str, OptionName],
                            optionValue: Union[str, OptionValue],
                            id_short: Optional[
                                str
                            ] = r"proprietaryconfigurationoptions_item",
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={
                                    r"en": r"Configuration option",
                                    r"de": r"Konfigurationsoption",
                                }
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Proprietary vehicle configuration setting"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/technicaldataagv/proprietaryconfigurationoptionsrecord/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[Qualifier] = None,
                            extension: Iterable[Extension] = (),
                            supplemental_semantic_id: Iterable[Reference] = (),
                            embedded_data_specifications: Iterable[
                                EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument
                            if optionName and not isinstance(
                                optionName, SubmodelElement
                            ):
                                optionName = self.OptionName(optionName)

                            # Build a submodel element if a raw value was passed in the argument
                            if optionValue and not isinstance(
                                optionValue, SubmodelElement
                            ):
                                optionValue = self.OptionValue(optionValue)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [optionName, optionValue]:
                                if se_arg is None:
                                    continue
                                elif isinstance(se_arg, SubmodelElement):
                                    embedded_submodel_elements.append(se_arg)
                                elif isinstance(se_arg, Iterable):
                                    for n, element in enumerate(se_arg):
                                        element.id_short = f"{element.id_short}{n}"
                                        embedded_submodel_elements.append(element)
                                else:
                                    raise TypeError(
                                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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
                        proprietaryconfigurationoptions_items: Optional[
                            Iterable[Proprietaryconfigurationoptions_item]
                        ] = None,
                        id_short: Optional[str] = r"ProprietaryConfigurationOptions",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[
                            Reference
                        ] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/proprietaryconfigurationoptionsrecord/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(
                            dict_={
                                r"en": r"Proprietary configuration options",
                                r"de": r"Herstellerspezifische Konfigurationsoptionen",
                            }
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"List with proprietary vehicle configuration settings",
                                r"de": r"Liste der herstellerspezifischen Konfigurationseinstellungen des Fahrzeugs",
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/technicaldataagv/proprietaryconfigurationoptions/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [proprietaryconfigurationoptions_items]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

                    def _check_constraints(self, new, existing) -> None:
                        # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                        # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                        saved_id_short = new.id_short
                        new.id_short = None

                        # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                        if not isinstance(new, self.type_value_list_element):
                            raise base.AASConstraintViolation(
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
                            raise base.AASConstraintViolation(
                                107,
                                f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                                "is specified all first level children must have the same "
                                f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                            )

                        # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                        # is either Property or Range. Thus, `new` must have the value_type property.
                        # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                        if (
                            isinstance(self.type_value_list_element, Property)
                            or isinstance(self.type_value_list_element, Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
                        ):  # type: ignore
                            raise base.AASConstraintViolation(
                                109,
                                "All first level elements must have the value_type "  # type: ignore
                                "specified by value_type_list_element="
                                f"{self.value_type_list_element.__name__}, got "  # type: ignore
                                f"{new!r} with value_type={new.value_type.__name__}",
                            )  # type: ignore

                        # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                        # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                        if (
                            new.semantic_id is not None
                            and self.semantic_id_list_element is None
                        ):
                            for item in existing:
                                if (
                                    item.semantic_id is not None
                                    and new.semantic_id != item.semantic_id
                                ):
                                    raise base.AASConstraintViolation(
                                        114,
                                        f"Element to be added {new!r} has semantic_id "
                                        f"{new.semantic_id!r}, while already contained element "
                                        f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                        "aren't equal.",
                                    )

                        # Re-assign id_short
                        new.id_short = saved_id_short

                def __init__(
                    self,
                    currentWorkingSetupName: Optional[
                        Union[str, CurrentWorkingSetupName]
                    ] = None,
                    activeLoading: Optional[Union[bool, ActiveLoading]] = None,
                    loadingType: Optional[Union[str, LoadingType]] = None,
                    loadingRequirements: Optional[
                        Union[LangStringSet, LoadingRequirements]
                    ] = None,
                    currentAttachments: Optional[
                        Union[Iterable[str], CurrentAttachments]
                    ] = None,
                    proprietaryConfigurationOptions: Optional[
                        ProprietaryConfigurationOptions
                    ] = None,
                    id_short: Optional[str] = r"TemporaryTechnicalData",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={
                            r"en": r"Temporary technical data depending on the implementation at the operator and current configuration"
                        }
                    ),
                    category: Optional[str] = None,
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/technicaldataagv/temporarytechnicaldata/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if currentWorkingSetupName and not isinstance(
                        currentWorkingSetupName, SubmodelElement
                    ):
                        currentWorkingSetupName = self.CurrentWorkingSetupName(
                            currentWorkingSetupName
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if activeLoading and not isinstance(activeLoading, SubmodelElement):
                        activeLoading = self.ActiveLoading(activeLoading)

                    # Build a submodel element if a raw value was passed in the argument
                    if loadingType and not isinstance(loadingType, SubmodelElement):
                        loadingType = self.LoadingType(loadingType)

                    # Build a submodel element if a raw value was passed in the argument
                    if loadingRequirements and not isinstance(
                        loadingRequirements, SubmodelElement
                    ):
                        loadingRequirements = self.LoadingRequirements(
                            loadingRequirements
                        )

                    # Build a submodel element if a raw value was passed in the argument
                    if currentAttachments and not isinstance(
                        currentAttachments, SubmodelElement
                    ):
                        currentAttachments = self.CurrentAttachments(currentAttachments)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        currentWorkingSetupName,
                        activeLoading,
                        loadingType,
                        loadingRequirements,
                        currentAttachments,
                        proprietaryConfigurationOptions,
                    ]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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
                dataSheet: Optional[DataSheet] = None,
                typeAndApplicationInformation: Optional[
                    TypeAndApplicationInformation
                ] = None,
                technicalParameters: Optional[TechnicalParameters] = None,
                vDA5050Factsheet: Optional[VDA5050Factsheet] = None,
                energy: Optional[Energy] = None,
                communicationAndControl: Optional[CommunicationAndControl] = None,
                safety: Optional[Safety] = None,
                temporaryTechnicalData: Optional[TemporaryTechnicalData] = None,
                id_short: Optional[str] = r"specificdescriptions_item",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={
                        r"en": r"Specific description for a use case or area of ​​application",
                        r"de": r"Spezifische Beschreibung für einen Anwendungsfall oder ein Einsatzgebiet",
                    }
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABM221#001/0173-1#01-AHY912#001",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (
                    ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABM221#001~0/0173-1#01-AHY912#001",
                            ),
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABM221-001/0173-1-01-AHY912-001",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"Naming",
                            value_type=str,
                            value=r"Name of SMC is use case or application",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Naming/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    dataSheet,
                    typeAndApplicationInformation,
                    technicalParameters,
                    vDA5050Factsheet,
                    energy,
                    communicationAndControl,
                    safety,
                    temporaryTechnicalData,
                ]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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
            specificdescriptions_items: Specificdescriptions_item,
            id_short: Optional[str] = r"SpecificDescriptions",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABM221#001/0173-1#01-AHY912#001",
                    ),
                ),
                referred_semantic_id=None,
            ),
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Specific description for a use case or area of application"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#02-ABM221#001"),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (
                ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABM221-001",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToMany",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [specificdescriptions_items]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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

        def _check_constraints(self, new, existing) -> None:
            # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
            # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
            saved_id_short = new.id_short
            new.id_short = None

            # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
            if not isinstance(new, self.type_value_list_element):
                raise base.AASConstraintViolation(
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
                raise base.AASConstraintViolation(
                    107,
                    f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                    "is specified all first level children must have the same "
                    f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
                )

            # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
            # is either Property or Range. Thus, `new` must have the value_type property.
            # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
            if (
                isinstance(self.type_value_list_element, Property)
                or isinstance(self.type_value_list_element, Range)
                and not isinstance(new.value_type, self.value_type_list_element)
            ):  # type: ignore
                raise base.AASConstraintViolation(
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise base.AASConstraintViolation(
                            114,
                            f"Element to be added {new!r} has semantic_id "
                            f"{new.semantic_id!r}, while already contained element "
                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                            "aren't equal.",
                        )

            # Re-assign id_short
            new.id_short = saved_id_short

    def __init__(
        self,
        id_: str,
        generalInformation: GeneralInformation,
        specificDescriptions: Optional[Iterable[SpecificDescriptions]] = None,
        id_short: Optional[str] = r"TechnicalDataAGV",
        display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
            dict_={
                r"en": r"Technical Data for AGV in Intralogistics",
                r"de": r"Technische Daten für AGV in der Intralogistik",
            }
        ),
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"Submodel containing technical data for AGV in intralogistcis",
                r"de": r"Teilmodell, das die technischen Daten von AGV (Fahrerlose Transportfahrzeuge) enthält",
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/idta-02047-1-0",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(
                Key(
                    type_=KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/technicaldataagv/1/0",
                ),
            ),
            type_=Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[Qualifier] = None,
        kind: ModellingKind = ModellingKind.TEMPLATE,
        extension: Iterable[Extension] = (),
        supplemental_semantic_id: Iterable[Reference] = (),
        embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
    ):

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [generalInformation, specificDescriptions]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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
