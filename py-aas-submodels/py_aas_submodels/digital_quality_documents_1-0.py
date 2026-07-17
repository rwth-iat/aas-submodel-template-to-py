from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class DigitalQualityDocuments(Submodel):

    class DocumentIds(SubmodelElementList):

        class Documentids_item(SubmodelElementCollection):

            class DocumentDomainId(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DocumentDomainId",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Document Domain Id"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identification of the domain in which the given DocumentId is unique. The domain ID can, e.g., be the name or acronym of the providing organisation"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH994#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH994-003",
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
                                semantic_id=None,
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

            class DocumentIdentifier(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DocumentIdentifier",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Document Identifier"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Alphanumeric character sequence uniquely identifying a document"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO099#004",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-AAO099-004",
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
                                semantic_id=None,
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

            class DocumentIsPrimary(Property):

                def __init__(
                    self,
                    value: bool,
                    id_short: Optional[str] = r"DocumentIsPrimary",
                    value_type: DataTypeDefXsd = bool,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Document Is Primary"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Flag indicating whether a DocumentId within a collection of at least two DocumentIds is the ‘primary’ identifier for the document. This is the preferred ID of the document (commonly from the point of view of the owner of the asset)"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH995#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH995-003",
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
                                semantic_id=None,
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
                documentDomainId: Union[str, DocumentDomainId],
                documentIdentifier: Union[str, DocumentIdentifier],
                documentIsPrimary: Optional[Union[bool, DocumentIsPrimary]] = None,
                id_short: Optional[str] = r"documentids_item",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Document Id"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"Information about a document identification entity"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI501#003/0173-1#01-AHF580#003",
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
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABI501-003",
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
                if documentDomainId and not isinstance(
                    documentDomainId, SubmodelElement
                ):
                    documentDomainId = self.DocumentDomainId(documentDomainId)

                # Build a submodel element if a raw value was passed in the argument
                if documentIdentifier and not isinstance(
                    documentIdentifier, SubmodelElement
                ):
                    documentIdentifier = self.DocumentIdentifier(documentIdentifier)

                # Build a submodel element if a raw value was passed in the argument
                if documentIsPrimary and not isinstance(
                    documentIsPrimary, SubmodelElement
                ):
                    documentIsPrimary = self.DocumentIsPrimary(documentIsPrimary)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [documentDomainId, documentIdentifier, documentIsPrimary]:
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
            documentids_items: Documentids_item,
            id_short: Optional[str] = r"DocumentIds",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"Document Ids"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Set of document identifiers for the document. One ID in this collection should be used as a preferred ID"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#02-ABI501#003"),
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
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI501-003",
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
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documentids_items]:
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

    class DocumentClassifications(SubmodelElementList):

        class Documentclassifications_item(SubmodelElementCollection):

            class ClassId(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ClassId",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Class Id"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Unique ID of the document class within a classficationsystem"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH996#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH996-003",
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
                                semantic_id=None,
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

            class ClassName(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"ClassName",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Class Name"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Name of the class in the classification system"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABJ219#002",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABJ219-002",
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
                                semantic_id=None,
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

            class ClassificationSystem(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ClassificationSystem",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Classification System"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Identification of the classification system "}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH997#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH997-003",
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
                                semantic_id=None,
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
                classId: Union[str, ClassId],
                className: Union[LangStringSet, ClassName],
                classificationSystem: Union[str, ClassificationSystem],
                id_short: Optional[str] = r"documentclassifications_item",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Document Classification"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Set of information for describing the classification of the Document according to a ClassificationSystem"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI502#003/0173-1#01-AHF581#003",
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
                if classId and not isinstance(classId, SubmodelElement):
                    classId = self.ClassId(classId)

                # Build a submodel element if a raw value was passed in the argument
                if className and not isinstance(className, SubmodelElement):
                    className = self.ClassName(className)

                # Build a submodel element if a raw value was passed in the argument
                if classificationSystem and not isinstance(
                    classificationSystem, SubmodelElement
                ):
                    classificationSystem = self.ClassificationSystem(
                        classificationSystem
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [classId, className, classificationSystem]:
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
            documentclassifications_items: Documentclassifications_item,
            id_short: Optional[str] = r"DocumentClassifications",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"Document Classifications"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Set of information for describing the classification of the Document according to ClassificationSystems"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#02-ABI502#003"),
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
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI502-003",
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
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documentclassifications_items]:
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

    class DocumentInstances(SubmodelElementList):

        class Documentinstances_item(SubmodelElementCollection):

            class Language(SubmodelElementList):

                class Language_item(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"language_item",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Language"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={r"en": r"Language of the document"}
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAN468#008",
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
                    language_items: Union[str, Language_item],
                    id_short: Optional[str] = r"Language",
                    type_value_list_element: SubmodelElement = Property,
                    semantic_id_list_element: Optional[Reference] = None,
                    value_type_list_element: Optional[DataTypeDefXsd] = str,
                    order_relevant: bool = True,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Language"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Language of the document instance."}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r" 0173-1#02-AAN468#008",
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
                    if language_items and not isinstance(
                        language_items, SubmodelElement
                    ):
                        language_items = self.Language_item(language_items)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [language_items]:
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

            class Version(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Version",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Version"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"Version of the document"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAP003#005",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-AAP003-005",
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
                                semantic_id=None,
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

            class Title(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Title",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Title"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(dict_={r"en": r"Name of the document"}),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG940#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABG940-003",
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
                                semantic_id=None,
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

            class Description(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Description",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Description"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Plain text characterizing the content of the document, e.g., the context of the quality document and its conformity statement."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAN466#004",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-AAN466-004",
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
                                semantic_id=None,
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

            class StatusSetDate(Property):

                def __init__(
                    self,
                    value: datetime,
                    id_short: Optional[str] = r"StatusSetDate",
                    value_type: DataTypeDefXsd = datetime,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Status Set Date"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Date when the document status was set. Usually, the date when the quality document was issued"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI000#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABI000-003",
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
                                semantic_id=None,
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

            class StatusValue(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"StatusValue",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Status Value"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Each document instance represents a point in time in the asset life cycle. This status value refers to the milestones in the asset life cycle. "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI001#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABI001-003",
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
                                semantic_id=None,
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

            class OrganizationShortName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OrganizationShortName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Organization Short Name"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Short name of the organization that issued the quality document instance"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABI002-003",
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
                                semantic_id=None,
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

            class OrganizationOfficialName(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OrganizationOfficialName",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(
                        dict_={r"en": r"Organization Official Name"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Official name of the organization that issued the document"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI004#003",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABI004-003",
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
                                semantic_id=None,
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

            class RefersToEntities(SubmodelElementList):

                class Referstoentities_item(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"referstoentities_item",
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Refers To Entity"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Forms a generic refers to-relationship to another document or document instance"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABK288#002",
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
                    referstoentities_items: Union[Reference, Referstoentities_item],
                    id_short: Optional[str] = r"RefersToEntities",
                    type_value_list_element: SubmodelElement = ReferenceElement,
                    semantic_id_list_element: Optional[Reference] = None,
                    value_type_list_element: Optional[DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Refers To Entities"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Forms a generic refers to-relationship to another document or document instance. "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK288#002",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK288-002",
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
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if referstoentities_items and not isinstance(
                        referstoentities_items, SubmodelElement
                    ):
                        referstoentities_items = self.Referstoentities_item(
                            referstoentities_items
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [referstoentities_items]:
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

            class BasedOnReferences(SubmodelElementList):

                class Basedonreferences_item(ReferenceElement):

                    def __init__(
                        self,
                        value: Reference,
                        id_short: Optional[str] = r"basedonreferences_item",
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Based On Reference"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(dict_={r"en": r"BasedOnReference"}),
                        semantic_id: Optional[Reference] = None,
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
                    basedonreferences_items: Union[Reference, Basedonreferences_item],
                    id_short: Optional[str] = r"BasedOnReferences",
                    type_value_list_element: SubmodelElement = ReferenceElement,
                    semantic_id_list_element: Optional[Reference] = None,
                    value_type_list_element: Optional[DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Based On References"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Forms a based on-relationship to another document or document instance"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK289#002",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK289-002",
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
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if basedonreferences_items and not isinstance(
                        basedonreferences_items, SubmodelElement
                    ):
                        basedonreferences_items = self.Basedonreferences_item(
                            basedonreferences_items
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [basedonreferences_items]:
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

            class DigitalFiles(SubmodelElementList):

                class Digitalfiles_item(File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"digitalfiles_item",
                        content_type: Optional[str] = r"text/xml",
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Digital File"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"MIME-Type, file name and file contents given by the file"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABK126#002",
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
                                    value=r"OneToMany",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
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

                def __init__(
                    self,
                    digitalfiles_items: Iterable[Digitalfiles_item],
                    id_short: Optional[str] = r"DigitalFiles",
                    type_value_list_element: SubmodelElement = File,
                    semantic_id_list_element: Optional[Reference] = None,
                    value_type_list_element: Optional[DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Digital Files"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"MIME-Type, file name and file contents given by the file SubmodelElement. This holds the actual quality document, e.g., the DCC XML file."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK126#002",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK126-002",
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
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [digitalfiles_items]:
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

            class PreviewFile(File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PreviewFile",
                    content_type: Optional[str] = r"application/pdf",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Preview File"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Provides a preview of the Document Instance, e.g., the human-readable PDF version of the XML file"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK127#002",
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
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK127-002",
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
                                semantic_id=None,
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

            class AdministrativeData(SubmodelElementCollection):

                class CoreData(SubmodelElementCollection):

                    class UniqueIdentifier(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"UniqueIdentifier",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Unique Identifier"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"A worldwide unique identifier for the DQD (e.g., calibration certificate number) "
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABI501#001/0173-1#01-AHF580#001*01",
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
                                        semantic_id=None,
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

                    class Identifications(SubmodelElementList):

                        class Identifications_item(SubmodelElementCollection):

                            class IdentificationName(MultiLanguageProperty):

                                def __init__(
                                    self,
                                    value: LangStringSet,
                                    id_short: Optional[str] = r"IdentificationName",
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Identification Name"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={r"en": r"Name of the identification"}
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName",
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
                                                semantic_id=None,
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

                            class IdentificationIssuer(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationIssuer",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Identification Issuer"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer",
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
                                                semantic_id=None,
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

                            class IdentificationValue(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationValue",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Identification Value"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue",
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
                                                semantic_id=None,
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

                            class ID(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ID",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(dict_={r"en": r"ID"}),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Attribute for which the value is unique within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID",
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
                                                semantic_id=None,
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

                            class RefID(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefID",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(dict_={r"en": r"Ref ID"}),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Reference to an existing ID within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID",
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
                                                semantic_id=None,
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

                            class RefType(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefType",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Ref Type"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType",
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
                                                semantic_id=None,
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
                                identificationName: Optional[
                                    Union[LangStringSet, IdentificationName]
                                ] = None,
                                identificationIssuer: Optional[
                                    Union[str, IdentificationIssuer]
                                ] = None,
                                identificationValue: Optional[
                                    Union[str, IdentificationValue]
                                ] = None,
                                iD: Optional[Union[str, ID]] = None,
                                refID: Optional[Iterable[Union[str, RefID]]] = None,
                                refType: Optional[Union[str, RefType]] = None,
                                id_short: Optional[str] = r"identifications_item",
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Identification"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={r"en": r"Identification"}
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
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
                                if identificationName and not isinstance(
                                    identificationName, SubmodelElement
                                ):
                                    identificationName = self.IdentificationName(
                                        identificationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if identificationIssuer and not isinstance(
                                    identificationIssuer, SubmodelElement
                                ):
                                    identificationIssuer = self.IdentificationIssuer(
                                        identificationIssuer
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if identificationValue and not isinstance(
                                    identificationValue, SubmodelElement
                                ):
                                    identificationValue = self.IdentificationValue(
                                        identificationValue
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if iD and not isinstance(iD, SubmodelElement):
                                    iD = self.ID(iD)

                                # Build a list of submodel elements if a raw values were passed in the argument
                                if refID and all([isinstance(i, str) for i in refID]):
                                    refID = [self.RefID(i) for i in refID]

                                # Build a submodel element if a raw value was passed in the argument
                                if refType and not isinstance(refType, SubmodelElement):
                                    refType = self.RefType(refType)

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    identificationName,
                                    identificationIssuer,
                                    identificationValue,
                                    iD,
                                    refID,
                                    refType,
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
                            identifications_items: Identifications_item,
                            id_short: Optional[str] = r"Identifications",
                            type_value_list_element: SubmodelElement = SubmodelElementCollection,
                            semantic_id_list_element: Optional[Reference] = None,
                            value_type_list_element: Optional[DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Identifications"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Identifications contains identifiers which exactly describe the content of the parent element"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications",
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
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [identifications_items]:
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

                    class IssueDate(Property):

                        def __init__(
                            self,
                            value: datetime,
                            id_short: Optional[str] = r"IssueDate",
                            value_type: DataTypeDefXsd = datetime,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(dict_={r"en": r"Issue Date"}),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Date when the document has been officially issued"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABI000#001",
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
                                        semantic_id=None,
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
                        uniqueIdentifier: Union[str, UniqueIdentifier],
                        identifications: Optional[Identifications] = None,
                        issueDate: Optional[Union[datetime, IssueDate]] = None,
                        id_short: Optional[str] = r"CoreData",
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Core Data"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains essential administrative information for the quality document"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData",
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
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument
                        if uniqueIdentifier and not isinstance(
                            uniqueIdentifier, SubmodelElement
                        ):
                            uniqueIdentifier = self.UniqueIdentifier(uniqueIdentifier)

                        # Build a submodel element if a raw value was passed in the argument
                        if issueDate and not isinstance(issueDate, SubmodelElement):
                            issueDate = self.IssueDate(issueDate)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [uniqueIdentifier, identifications, issueDate]:
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

                class Items(SubmodelElementCollection):

                    class Identifications(SubmodelElementList):

                        class Identifications_item(SubmodelElementCollection):

                            class IdentificationName(MultiLanguageProperty):

                                def __init__(
                                    self,
                                    value: LangStringSet,
                                    id_short: Optional[str] = r"IdentificationName",
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Identification Name"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={r"en": r"Name of the identification"}
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName",
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
                                                semantic_id=None,
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

                            class IdentificationIssuer(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationIssuer",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Identification Issuer"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer",
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
                                                semantic_id=None,
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

                            class IdentificationValue(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationValue",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Identification Value"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue",
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
                                                semantic_id=None,
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

                            class ID(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ID",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(dict_={r"en": r"ID"}),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Attribute for which the value is unique within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID",
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
                                                semantic_id=None,
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

                            class RefID(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefID",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(dict_={r"en": r"Ref ID"}),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Reference to an existing ID within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID",
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
                                                semantic_id=None,
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

                            class RefType(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefType",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Ref Type"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType",
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
                                                semantic_id=None,
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
                                identificationName: Optional[
                                    Union[LangStringSet, IdentificationName]
                                ] = None,
                                identificationIssuer: Optional[
                                    Union[str, IdentificationIssuer]
                                ] = None,
                                identificationValue: Optional[
                                    Union[str, IdentificationValue]
                                ] = None,
                                iD: Optional[Union[str, ID]] = None,
                                refID: Optional[Iterable[Union[str, RefID]]] = None,
                                refType: Optional[Union[str, RefType]] = None,
                                id_short: Optional[str] = r"identifications_item",
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Identification"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={r"en": r"Identification"}
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
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
                                if identificationName and not isinstance(
                                    identificationName, SubmodelElement
                                ):
                                    identificationName = self.IdentificationName(
                                        identificationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if identificationIssuer and not isinstance(
                                    identificationIssuer, SubmodelElement
                                ):
                                    identificationIssuer = self.IdentificationIssuer(
                                        identificationIssuer
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if identificationValue and not isinstance(
                                    identificationValue, SubmodelElement
                                ):
                                    identificationValue = self.IdentificationValue(
                                        identificationValue
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if iD and not isinstance(iD, SubmodelElement):
                                    iD = self.ID(iD)

                                # Build a list of submodel elements if a raw values were passed in the argument
                                if refID and all([isinstance(i, str) for i in refID]):
                                    refID = [self.RefID(i) for i in refID]

                                # Build a submodel element if a raw value was passed in the argument
                                if refType and not isinstance(refType, SubmodelElement):
                                    refType = self.RefType(refType)

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    identificationName,
                                    identificationIssuer,
                                    identificationValue,
                                    iD,
                                    refID,
                                    refType,
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
                            identifications_items: Identifications_item,
                            id_short: Optional[str] = r"Identifications",
                            type_value_list_element: SubmodelElement = SubmodelElementCollection,
                            semantic_id_list_element: Optional[Reference] = None,
                            value_type_list_element: Optional[DataTypeDefXsd] = str,
                            order_relevant: bool = True,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Identifications"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Identifications contains identifiers which exactly describe the content of the parent element."
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
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

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [identifications_items]:
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

                    class Item(SubmodelElementList):

                        class Item_item(SubmodelElementCollection):

                            class Identifications(SubmodelElementList):

                                class Identifications_item(SubmodelElementCollection):

                                    class IdentificationName(MultiLanguageProperty):

                                        def __init__(
                                            self,
                                            value: LangStringSet,
                                            id_short: Optional[
                                                str
                                            ] = r"IdentificationName",
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = MultiLanguageNameType(
                                                dict_={r"en": r"Identification Name"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Name of the identification"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[Qualifier] = None,
                                            extension: Iterable[Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                Reference
                                            ] = (),
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
                                                        semantic_id=None,
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

                                    class IdentificationIssuer(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"IdentificationIssuer",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = MultiLanguageNameType(
                                                dict_={r"en": r"Identification Issuer"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[Qualifier] = None,
                                            extension: Iterable[Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                Reference
                                            ] = (),
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
                                                        semantic_id=None,
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

                                    class IdentificationValue(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"IdentificationValue",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = MultiLanguageNameType(
                                                dict_={r"en": r"Identification Value"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[Qualifier] = None,
                                            extension: Iterable[Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                Reference
                                            ] = (),
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
                                                        semantic_id=None,
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

                                    class ID(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"ID",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = MultiLanguageNameType(
                                                dict_={r"en": r"ID"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Attribute for which the value is unique within the quality document"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[Qualifier] = None,
                                            extension: Iterable[Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                Reference
                                            ] = (),
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
                                                        semantic_id=None,
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

                                    class RefID(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"RefID",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = MultiLanguageNameType(
                                                dict_={r"en": r"Ref ID"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Reference to an existing ID within the quality document"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[Qualifier] = None,
                                            extension: Iterable[Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                Reference
                                            ] = (),
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
                                                        semantic_id=None,
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

                                    class RefType(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"RefType",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = MultiLanguageNameType(
                                                dict_={r"en": r"Ref Type"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = MultiLanguageTextType(
                                                dict_={
                                                    r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                                }
                                            ),
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[Qualifier] = None,
                                            extension: Iterable[Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                Reference
                                            ] = (),
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
                                                        semantic_id=None,
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
                                        identificationName: Optional[
                                            Union[LangStringSet, IdentificationName]
                                        ] = None,
                                        identificationIssuer: Optional[
                                            Union[str, IdentificationIssuer]
                                        ] = None,
                                        identificationValue: Optional[
                                            Union[str, IdentificationValue]
                                        ] = None,
                                        iD: Optional[Union[str, ID]] = None,
                                        refID: Optional[
                                            Iterable[Union[str, RefID]]
                                        ] = None,
                                        refType: Optional[Union[str, RefType]] = None,
                                        id_short: Optional[
                                            str
                                        ] = r"identifications_item",
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = MultiLanguageNameType(
                                            dict_={r"en": r"Identification"}
                                        ),
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = MultiLanguageTextType(
                                            dict_={r"en": r"Identification"}
                                        ),
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        qualifier: Iterable[Qualifier] = None,
                                        extension: Iterable[Extension] = (),
                                        supplemental_semantic_id: Iterable[
                                            Reference
                                        ] = (),
                                        embedded_data_specifications: Iterable[
                                            EmbeddedDataSpecification
                                        ] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument
                                        if identificationName and not isinstance(
                                            identificationName, SubmodelElement
                                        ):
                                            identificationName = (
                                                self.IdentificationName(
                                                    identificationName
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument
                                        if identificationIssuer and not isinstance(
                                            identificationIssuer, SubmodelElement
                                        ):
                                            identificationIssuer = (
                                                self.IdentificationIssuer(
                                                    identificationIssuer
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument
                                        if identificationValue and not isinstance(
                                            identificationValue, SubmodelElement
                                        ):
                                            identificationValue = (
                                                self.IdentificationValue(
                                                    identificationValue
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument
                                        if iD and not isinstance(iD, SubmodelElement):
                                            iD = self.ID(iD)

                                        # Build a list of submodel elements if a raw values were passed in the argument
                                        if refID and all(
                                            [isinstance(i, str) for i in refID]
                                        ):
                                            refID = [self.RefID(i) for i in refID]

                                        # Build a submodel element if a raw value was passed in the argument
                                        if refType and not isinstance(
                                            refType, SubmodelElement
                                        ):
                                            refType = self.RefType(refType)

                                        # Add all passed/initialized submodel elements to a single list
                                        embedded_submodel_elements = []
                                        for se_arg in [
                                            identificationName,
                                            identificationIssuer,
                                            identificationValue,
                                            iD,
                                            refID,
                                            refType,
                                        ]:
                                            if se_arg is None:
                                                continue
                                            elif isinstance(se_arg, SubmodelElement):
                                                embedded_submodel_elements.append(
                                                    se_arg
                                                )
                                            elif isinstance(se_arg, Iterable):
                                                for n, element in enumerate(se_arg):
                                                    element.id_short = (
                                                        f"{element.id_short}{n}"
                                                    )
                                                    embedded_submodel_elements.append(
                                                        element
                                                    )
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
                                    identifications_items: Identifications_item,
                                    id_short: Optional[str] = r"Identifications",
                                    type_value_list_element: SubmodelElement = SubmodelElementCollection,
                                    semantic_id_list_element: Optional[
                                        Reference
                                    ] = None,
                                    value_type_list_element: Optional[
                                        DataTypeDefXsd
                                    ] = None,
                                    order_relevant: bool = True,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = MultiLanguageNameType(
                                        dict_={r"en": r"Identifications"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        MultiLanguageTextType
                                    ] = MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Identifications contains identifiers which exactly describe the content of the parent element."
                                        }
                                    ),
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
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

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [identifications_items]:
                                        if se_arg is None:
                                            continue
                                        elif isinstance(se_arg, SubmodelElement):
                                            embedded_submodel_elements.append(se_arg)
                                        elif isinstance(se_arg, Iterable):
                                            for n, element in enumerate(se_arg):
                                                element.id_short = (
                                                    f"{element.id_short}{n}"
                                                )
                                                embedded_submodel_elements.append(
                                                    element
                                                )
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
                                    if not isinstance(
                                        new, self.type_value_list_element
                                    ):
                                        raise base.AASConstraintViolation(
                                            108,
                                            "All first level elements must be of the type specified in "
                                            f"type_value_list_element={self.type_value_list_element.__name__}, "
                                            f"got {new!r}",
                                        )

                                    if (
                                        self.semantic_id_list_element is not None
                                        and new.semantic_id is not None
                                        and new.semantic_id
                                        != self.semantic_id_list_element
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
                                        isinstance(
                                            self.type_value_list_element, Property
                                        )
                                        or isinstance(
                                            self.type_value_list_element, Range
                                        )
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
                                identifications: Identifications,
                                id_short: Optional[str] = r"item_item",
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(dict_={r"en": r"Item"}),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(dict_={r"en": r"Item"}),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://dccwiki.ptb.de/en/dccitems",
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

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [identifications]:
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
                            item_items: Item_item,
                            id_short: Optional[str] = r"Item",
                            type_value_list_element: SubmodelElement = SubmodelElementCollection,
                            semantic_id_list_element: Optional[Reference] = None,
                            value_type_list_element: Optional[DataTypeDefXsd] = None,
                            order_relevant: bool = True,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(dict_={r"en": r"Item"}),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Item of calibration, conformity assessment or other"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Items",
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
                                        value=r"OneToMany",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [item_items]:
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
                        identifications: Identifications,
                        item: Iterable[Item],
                        id_short: Optional[str] = r"Items",
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Items"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains unique identification, description and if applicable, conditions of the item"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/items",
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
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [identifications, item]:
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

                class Statements(SubmodelElementList):

                    class Statements_item(SubmodelElementCollection):

                        class DateOfStatement(Property):

                            def __init__(
                                self,
                                value: datetime,
                                id_short: Optional[str] = r"DateOfStatement",
                                value_type: DataTypeDefXsd = datetime,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Date Of Statement"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={r"en": r"Date of statement"}
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statements/Date",
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
                                            semantic_id=None,
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

                        class StatementReference(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"StatementReference",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Statement Reference"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Normative or other reference in accordance which the statement is made"
                                    }
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statement/StatementReference",
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
                                            semantic_id=None,
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

                        class Declaration(MultiLanguageProperty):

                            def __init__(
                                self,
                                value: LangStringSet,
                                id_short: Optional[str] = r"Declaration",
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Declaration"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Additional information providing context for the statement"
                                    }
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statement/Declaration",
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
                                            semantic_id=None,
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
                            dateOfStatement: Optional[
                                Union[datetime, DateOfStatement]
                            ] = None,
                            statementReference: Optional[
                                Union[str, StatementReference]
                            ] = None,
                            declaration: Optional[
                                Union[LangStringSet, Declaration]
                            ] = None,
                            id_short: Optional[str] = r"statements_item",
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(dict_={r"en": r"Statement"}),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"statement records regarding the quality assessment"
                                }
                            ),
                            semantic_id: Optional[Reference] = None,
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
                            if dateOfStatement and not isinstance(
                                dateOfStatement, SubmodelElement
                            ):
                                dateOfStatement = self.DateOfStatement(dateOfStatement)

                            # Build a submodel element if a raw value was passed in the argument
                            if statementReference and not isinstance(
                                statementReference, SubmodelElement
                            ):
                                statementReference = self.StatementReference(
                                    statementReference
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if declaration and not isinstance(
                                declaration, SubmodelElement
                            ):
                                declaration = self.Declaration(declaration)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                dateOfStatement,
                                statementReference,
                                declaration,
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
                        statements_items: Statements_item,
                        id_short: Optional[str] = r"Statements",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Statements"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains list of statement records regarding the quality assessment"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/statements",
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
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [statements_items]:
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
                    coreData: CoreData,
                    items: Optional[Items] = None,
                    statements: Optional[Statements] = None,
                    id_short: Optional[str] = r"AdministrativeData",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Administrative Data"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"This submodel element collection contains essential administrative information about the document."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData",
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
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [coreData, items, statements]:
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

            class DocumentSignature(SubmodelElementCollection):

                class SignedInfo(SubmodelElementCollection):

                    class CanonicalizationMethod(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"CanonicalizationMethod",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Canonicalization Method"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about the signature and the algorithms used"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/CanonicalizationMethod",
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
                                        semantic_id=None,
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

                    class SignatureMethod(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SignatureMethod",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Signature Method"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about the method used for creating the signature"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureMethod",
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
                                        semantic_id=None,
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

                    class SignatureReference(SubmodelElementCollection):

                        class Transforms(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Transforms",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(dict_={r"en": r"Transforms"}),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Contains the transformations applied to the resource prior to signing"
                                    }
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/Transforms",
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
                                            semantic_id=None,
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

                        class DigestMethod(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"DigestMethod",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Digest Method"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specifies the hash algorithm before applying the hash"
                                    }
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/DigestMethod",
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
                                            semantic_id=None,
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

                        class DigestValue(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"DigestValue",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[
                                    MultiLanguageNameType
                                ] = MultiLanguageNameType(
                                    dict_={r"en": r"Digest Value"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    MultiLanguageTextType
                                ] = MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Contains the Base64 encoded result of applying the hash algorithm to the transformed resource"
                                    }
                                ),
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/DigestValue",
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
                                            semantic_id=None,
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
                            transforms: Union[str, Transforms],
                            digestMethod: Union[str, DigestMethod],
                            digestValue: Union[str, DigestValue],
                            id_short: Optional[str] = r"SignatureReference",
                            display_name: Optional[
                                MultiLanguageNameType
                            ] = MultiLanguageNameType(
                                dict_={r"en": r"Signature Reference"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                MultiLanguageTextType
                            ] = MultiLanguageTextType(
                                dict_={
                                    r"en": r"Additional information for processing the signature"
                                }
                            ),
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference",
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
                                        value=r"OneToMany",
                                        value_id=None,
                                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument
                            if transforms and not isinstance(
                                transforms, SubmodelElement
                            ):
                                transforms = self.Transforms(transforms)

                            # Build a submodel element if a raw value was passed in the argument
                            if digestMethod and not isinstance(
                                digestMethod, SubmodelElement
                            ):
                                digestMethod = self.DigestMethod(digestMethod)

                            # Build a submodel element if a raw value was passed in the argument
                            if digestValue and not isinstance(
                                digestValue, SubmodelElement
                            ):
                                digestValue = self.DigestValue(digestValue)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [transforms, digestMethod, digestValue]:
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
                        canonicalizationMethod: Union[str, CanonicalizationMethod],
                        signatureMethod: Union[str, SignatureMethod],
                        signatureReference: Iterable[SignatureReference],
                        id_short: Optional[str] = r"SignedInfo",
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Signed Info"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about the signature and the algorithms used"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo",
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
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument
                        if canonicalizationMethod and not isinstance(
                            canonicalizationMethod, SubmodelElement
                        ):
                            canonicalizationMethod = self.CanonicalizationMethod(
                                canonicalizationMethod
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if signatureMethod and not isinstance(
                            signatureMethod, SubmodelElement
                        ):
                            signatureMethod = self.SignatureMethod(signatureMethod)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            canonicalizationMethod,
                            signatureMethod,
                            signatureReference,
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

                class SignatureValue(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"SignatureValue",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Signature Value"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains the Base64 encoded result of the hash algorithm, i.e., the signature generated with the parameters specified in the SignatureMethod defined in SignedInfo after applying the algorithm specified by the CanonicalizationMethod"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignatureValue",
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
                                    semantic_id=None,
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

                class KeyInfo(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"KeyInfo",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[
                            MultiLanguageNameType
                        ] = MultiLanguageNameType(dict_={r"en": r"Key Info"}),
                        category: Optional[str] = None,
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Information to allow the signer to provide recipients with the key that validates the signature, usually in the form of one or more X.509 digital certificates"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/KeyInfo",
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
                                    semantic_id=None,
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
                    signedInfo: SignedInfo,
                    signatureValue: Union[str, SignatureValue],
                    keyInfo: Union[str, KeyInfo],
                    id_short: Optional[str] = r"DocumentSignature",
                    display_name: Optional[
                        MultiLanguageNameType
                    ] = MultiLanguageNameType(dict_={r"en": r"Document Signature"}),
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Information about the electronic signature of the quality document. The semantic structure is based on the W3C schema xmldsig"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature",
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
                                    value=r"http://www.w3.org/TR/xmldsig-core1/",
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
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if signatureValue and not isinstance(
                        signatureValue, SubmodelElement
                    ):
                        signatureValue = self.SignatureValue(signatureValue)

                    # Build a submodel element if a raw value was passed in the argument
                    if keyInfo and not isinstance(keyInfo, SubmodelElement):
                        keyInfo = self.KeyInfo(keyInfo)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [signedInfo, signatureValue, keyInfo]:
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
                language: Union[Iterable[str], Language],
                version: Union[str, Version],
                title: Union[LangStringSet, Title],
                description_: Union[LangStringSet, Description],
                statusSetDate: Union[datetime, StatusSetDate],
                statusValue: Union[str, StatusValue],
                organizationShortName: Union[str, OrganizationShortName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFiles: DigitalFiles,
                administrativeData: AdministrativeData,
                refersToEntities: Optional[RefersToEntities] = None,
                basedOnReferences: Optional[BasedOnReferences] = None,
                previewFile: Optional[PreviewFile] = None,
                documentSignature: Optional[Iterable[DocumentSignature]] = None,
                id_short: Optional[str] = r"documentinstances_item",
                display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                    dict_={r"en": r"Document Instance"}
                ),
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Information about a document instance. This SMC inherits from “DocumentVersion” of IDTA 02004-2-0 “Handover Documentation”"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI503#003/0173-1#01-AHF582#003",
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
                if language and not isinstance(language, SubmodelElement):
                    language = self.Language(language)

                # Build a submodel element if a raw value was passed in the argument
                if version and not isinstance(version, SubmodelElement):
                    version = self.Version(version)

                # Build a submodel element if a raw value was passed in the argument
                if title and not isinstance(title, SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument
                if description_ and not isinstance(description_, SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument
                if statusSetDate and not isinstance(statusSetDate, SubmodelElement):
                    statusSetDate = self.StatusSetDate(statusSetDate)

                # Build a submodel element if a raw value was passed in the argument
                if statusValue and not isinstance(statusValue, SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument
                if organizationShortName and not isinstance(
                    organizationShortName, SubmodelElement
                ):
                    organizationShortName = self.OrganizationShortName(
                        organizationShortName
                    )

                # Build a submodel element if a raw value was passed in the argument
                if organizationOfficialName and not isinstance(
                    organizationOfficialName, SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(
                        organizationOfficialName
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    language,
                    version,
                    title,
                    description_,
                    statusSetDate,
                    statusValue,
                    organizationShortName,
                    organizationOfficialName,
                    refersToEntities,
                    basedOnReferences,
                    digitalFiles,
                    previewFile,
                    administrativeData,
                    documentSignature,
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
            documentinstances_items: Documentinstances_item,
            id_short: Optional[str] = r"DocumentInstances",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"Document Instances"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Information elements of individual document instances, which can be different versions of each other"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#02-ABI503#003"),
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
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI503-003",
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
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documentinstances_items]:
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
        documentIds: DocumentIds,
        documentClassifications: DocumentClassifications,
        documentInstances: DocumentInstances,
        id_short: Optional[str] = r"DigitalQualityDocuments",
        display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
            dict_={r"en": r"Digital Quality Documents"}
        ),
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={r"en": r"Template submodel for Digital Quality Documents."}
        ),
        administration: Optional[AdministrativeInformation] = None,
        semantic_id: Optional[Reference] = ExternalReference(
            key=(
                Key(
                    type_=KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/DigitalQualityDocument/1/0",
                ),
            ),
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
        for se_arg in [documentIds, documentClassifications, documentInstances]:
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
