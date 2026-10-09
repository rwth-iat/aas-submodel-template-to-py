from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class DigitalQualityDocuments(aas.Submodel):

    class DocumentIds(aas.SubmodelElementList):

        class Documentids_item(aas.SubmodelElementCollection):

            class DocumentDomainId(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DocumentDomainId",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Document Domain Id"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Identification of the domain in which the given DocumentId is unique. The domain ID can, e.g., be the name or acronym of the providing organisation"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH994#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH994-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class DocumentIdentifier(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DocumentIdentifier",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Document Identifier"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Alphanumeric character sequence uniquely identifying a document"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO099#004",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-AAO099-004",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class DocumentIsPrimary(aas.Property):

                def __init__(
                    self,
                    value: bool,
                    id_short: Optional[str] = r"DocumentIsPrimary",
                    value_type: aas.DataTypeDefXsd = bool,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Document Is Primary"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Flag indicating whether a DocumentId within a collection of at least two DocumentIds is the ‘primary’ identifier for the document. This is the preferred ID of the document (commonly from the point of view of the owner of the asset)"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH995#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH995-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                id_short: Optional[str] = None,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(dict_={r"en": r"Document Id"}),
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={r"en": r"Information about a document identification entity"}
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI501#003/0173-1#01-AHF580#003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABI501-003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if documentDomainId is not None and not isinstance(
                    documentDomainId, aas.SubmodelElement
                ):
                    documentDomainId = self.DocumentDomainId(documentDomainId)

                # Build a submodel element if a raw value was passed in the argument

                if documentIdentifier is not None and not isinstance(
                    documentIdentifier, aas.SubmodelElement
                ):
                    documentIdentifier = self.DocumentIdentifier(documentIdentifier)

                # Build a submodel element if a raw value was passed in the argument

                if documentIsPrimary is not None and not isinstance(
                    documentIsPrimary, aas.SubmodelElement
                ):
                    documentIsPrimary = self.DocumentIsPrimary(documentIsPrimary)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [documentDomainId, documentIdentifier, documentIsPrimary]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, aas.SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
            documentids_items: Iterable[Documentids_item],
            id_short: Optional[str] = r"DocumentIds",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[
                aas.MultiLanguageNameType
            ] = aas.MultiLanguageNameType(dict_={r"en": r"Document Ids"}),
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Set of document identifiers for the document. One ID in this collection should be used as a preferred ID"
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABI501#003",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI501-003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(documentids_items, str):
                raise TypeError("documentids_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documentids_items]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    embedded_submodel_elements.extend(se_arg)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise aas.AASConstraintViolation(
                            114,
                            f"Element to be added {new!r} has semantic_id "
                            f"{new.semantic_id!r}, while already contained element "
                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                            "aren't equal.",
                        )

            # Re-assign id_short
            new.id_short = saved_id_short

    class DocumentClassifications(aas.SubmodelElementList):

        class Documentclassifications_item(aas.SubmodelElementCollection):

            class ClassId(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ClassId",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Class Id"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Unique ID of the document class within a classficationsystem"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH996#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH996-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class ClassName(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"ClassName",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Class Name"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={r"en": r"Name of the class in the classification system"}
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABJ219#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABJ219-002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class ClassificationSystem(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ClassificationSystem",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Classification System"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={r"en": r"Identification of the classification system "}
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABH997#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABH997-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                className: Union[aas.LangStringSet, ClassName],
                classificationSystem: Union[str, ClassificationSystem],
                id_short: Optional[str] = None,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(
                    dict_={r"en": r"Document Classification"}
                ),
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Set of information for describing the classification of the Document according to a ClassificationSystem"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI502#003/0173-1#01-AHF581#003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if classId is not None and not isinstance(classId, aas.SubmodelElement):
                    classId = self.ClassId(classId)

                # Build a submodel element if a raw value was passed in the argument

                if className is not None and not isinstance(
                    className, aas.SubmodelElement
                ):
                    className = self.ClassName(className)

                # Build a submodel element if a raw value was passed in the argument

                if classificationSystem is not None and not isinstance(
                    classificationSystem, aas.SubmodelElement
                ):
                    classificationSystem = self.ClassificationSystem(
                        classificationSystem
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [classId, className, classificationSystem]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, aas.SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
            documentclassifications_items: Iterable[Documentclassifications_item],
            id_short: Optional[str] = r"DocumentClassifications",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[
                aas.MultiLanguageNameType
            ] = aas.MultiLanguageNameType(dict_={r"en": r"Document Classifications"}),
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Set of information for describing the classification of the Document according to ClassificationSystems"
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABI502#003",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI502-003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(documentclassifications_items, str):
                raise TypeError(
                    "documentclassifications_items takes several elements, got a str"
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documentclassifications_items]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    embedded_submodel_elements.extend(se_arg)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise aas.AASConstraintViolation(
                            114,
                            f"Element to be added {new!r} has semantic_id "
                            f"{new.semantic_id!r}, while already contained element "
                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                            "aren't equal.",
                        )

            # Re-assign id_short
            new.id_short = saved_id_short

    class DocumentInstances(aas.SubmodelElementList):

        class Documentinstances_item(aas.SubmodelElementCollection):

            class Language(aas.SubmodelElementList):

                class Language_item(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = None,
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(dict_={r"en": r"Language"}),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={r"en": r"Language of the document"}
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAN468#008",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
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
                    language_items: Iterable[Union[str, Language_item]],
                    id_short: Optional[str] = r"Language",
                    type_value_list_element: aas.SubmodelElement = aas.Property,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                    order_relevant: bool = True,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Language"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={r"en": r"Language of the document instance."}
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r" 0173-1#02-AAN468#008",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(language_items, str):
                        raise TypeError(
                            "language_items takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if language_items:
                        language_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.Language_item(i)
                            )
                            for i in language_items
                        ]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [language_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            embedded_submodel_elements.extend(se_arg)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise aas.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            class Version(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Version",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Version"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={r"en": r"Version of the document"}
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAP003#005",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-AAP003-005",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class Title(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Title",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Title"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={r"en": r"Name of the document"}
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABG940#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABG940-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class Description(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"Description",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Description"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Plain text characterizing the content of the document, e.g., the context of the quality document and its conformity statement."
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAN466#004",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-AAN466-004",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class StatusSetDate(aas.Property):

                def __init__(
                    self,
                    value: xsd.DateTime,
                    id_short: Optional[str] = r"StatusSetDate",
                    value_type: aas.DataTypeDefXsd = xsd.DateTime,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Status Set Date"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Date when the document status was set. Usually, the date when the quality document was issued"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI000#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABI000-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class StatusValue(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"StatusValue",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Status Value"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Each document instance represents a point in time in the asset life cycle. This status value refers to the milestones in the asset life cycle. "
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI001#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABI001-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class OrganizationShortName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OrganizationShortName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Organization Short Name"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Short name of the organization that issued the quality document instance"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABI002-003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class OrganizationOfficialName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OrganizationOfficialName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Organization Official Name"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Official name of the organization that issued the document"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI004#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABI004-003",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class RefersToEntities(aas.SubmodelElementList):

                class Referstoentities_item(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={r"en": r"Refers To Entity"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Forms a generic refers to-relationship to another document or document instance"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABK288#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
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
                    referstoentities_items: Iterable[
                        Union[aas.Reference, Referstoentities_item]
                    ],
                    id_short: Optional[str] = r"RefersToEntities",
                    type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Refers To Entities"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Forms a generic refers to-relationship to another document or document instance. "
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK288#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK288-002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(referstoentities_items, str):
                        raise TypeError(
                            "referstoentities_items takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if referstoentities_items:
                        referstoentities_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.Referstoentities_item(i)
                            )
                            for i in referstoentities_items
                        ]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [referstoentities_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            embedded_submodel_elements.extend(se_arg)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise aas.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            class BasedOnReferences(aas.SubmodelElementList):

                class Basedonreferences_item(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={r"en": r"Based On Reference"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={r"en": r"BasedOnReference"}
                        ),
                        semantic_id: Optional[aas.Reference] = None,
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
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
                    basedonreferences_items: Iterable[
                        Union[aas.Reference, Basedonreferences_item]
                    ],
                    id_short: Optional[str] = r"BasedOnReferences",
                    type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Based On References"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Forms a based on-relationship to another document or document instance"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK289#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK289-002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(basedonreferences_items, str):
                        raise TypeError(
                            "basedonreferences_items takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if basedonreferences_items:
                        basedonreferences_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.Basedonreferences_item(i)
                            )
                            for i in basedonreferences_items
                        ]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [basedonreferences_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            embedded_submodel_elements.extend(se_arg)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise aas.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            class DigitalFiles(aas.SubmodelElementList):

                class Digitalfiles_item(aas.File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = None,
                        content_type: Optional[str] = r"text/xml",
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(dict_={r"en": r"Digital File"}),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"MIME-Type, file name and file contents given by the file"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABK126#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"OneToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                    type_value_list_element: aas.SubmodelElement = aas.File,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Digital Files"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"MIME-Type, file name and file contents given by the file SubmodelElement. This holds the actual quality document, e.g., the DCC XML file."
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK126#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK126-002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(digitalfiles_items, str):
                        raise TypeError(
                            "digitalfiles_items takes several elements, got a str"
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [digitalfiles_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            embedded_submodel_elements.extend(se_arg)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise aas.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            class PreviewFile(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PreviewFile",
                    content_type: Optional[str] = r"application/pdf",
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Preview File"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Provides a preview of the Document Instance, e.g., the human-readable PDF version of the XML file"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABK127#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://api.eclass-cdp.com/0173-1-02-ABK127-002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

            class AdministrativeData(aas.SubmodelElementCollection):

                class CoreData(aas.SubmodelElementCollection):

                    class UniqueIdentifier(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"UniqueIdentifier",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Unique Identifier"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"A worldwide unique identifier for the DQD (e.g., calibration certificate number) "
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABI501#001/0173-1#01-AHF580#001*01",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                    class Identifications(aas.SubmodelElementList):

                        class Identifications_item(aas.SubmodelElementCollection):

                            class IdentificationName(aas.MultiLanguageProperty):

                                def __init__(
                                    self,
                                    value: aas.LangStringSet,
                                    id_short: Optional[str] = r"IdentificationName",
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Identification Name"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={r"en": r"Name of the identification"}
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class IdentificationIssuer(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationIssuer",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Identification Issuer"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class IdentificationValue(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationValue",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Identification Value"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class ID(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ID",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(dict_={r"en": r"ID"}),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Attribute for which the value is unique within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class RefID(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefID",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Ref ID"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Reference to an existing ID within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToMany",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class RefType(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefType",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Ref Type"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                                    Union[aas.LangStringSet, IdentificationName]
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
                                id_short: Optional[str] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Identification"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Identification"}
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationName is not None and not isinstance(
                                    identificationName, aas.SubmodelElement
                                ):
                                    identificationName = self.IdentificationName(
                                        identificationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationIssuer is not None and not isinstance(
                                    identificationIssuer, aas.SubmodelElement
                                ):
                                    identificationIssuer = self.IdentificationIssuer(
                                        identificationIssuer
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationValue is not None and not isinstance(
                                    identificationValue, aas.SubmodelElement
                                ):
                                    identificationValue = self.IdentificationValue(
                                        identificationValue
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if iD is not None and not isinstance(
                                    iD, aas.SubmodelElement
                                ):
                                    iD = self.ID(iD)

                                # A str would be split into its characters
                                if isinstance(refID, str):
                                    raise TypeError(
                                        "refID takes several elements, got a str"
                                    )

                                # Build submodel elements from raw values passed in the argument
                                if refID:
                                    refID = [
                                        (
                                            i
                                            if isinstance(i, aas.SubmodelElement)
                                            else self.RefID(i)
                                        )
                                        for i in refID
                                    ]

                                # Build a submodel element if a raw value was passed in the argument

                                if refType is not None and not isinstance(
                                    refType, aas.SubmodelElement
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
                                    elif isinstance(se_arg, aas.SubmodelElement):
                                        embedded_submodel_elements.append(se_arg)
                                    elif isinstance(se_arg, Iterable):
                                        for n, element in enumerate(se_arg):
                                            element.id_short = f"{element.id_short}{n}"
                                            embedded_submodel_elements.append(element)
                                    else:
                                        raise TypeError(
                                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                            identifications_items: Iterable[Identifications_item],
                            id_short: Optional[str] = r"Identifications",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                            semantic_id_list_element: Optional[aas.Reference] = None,
                            value_type_list_element: Optional[
                                aas.DataTypeDefXsd
                            ] = None,
                            order_relevant: bool = True,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Identifications"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Identifications contains identifiers which exactly describe the content of the parent element"
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(identifications_items, str):
                                raise TypeError(
                                    "identifications_items takes several elements, got a str"
                                )

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [identifications_items]:
                                if se_arg is None:
                                    continue
                                elif isinstance(se_arg, aas.SubmodelElement):
                                    embedded_submodel_elements.append(se_arg)
                                elif isinstance(se_arg, Iterable):
                                    embedded_submodel_elements.extend(se_arg)
                                else:
                                    raise TypeError(
                                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                                self.type_value_list_element
                                in (aas.Property, aas.Range)
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
                            if (
                                new.semantic_id is not None
                                and self.semantic_id_list_element is None
                            ):
                                for item in existing:
                                    if (
                                        item.semantic_id is not None
                                        and new.semantic_id != item.semantic_id
                                    ):
                                        raise aas.AASConstraintViolation(
                                            114,
                                            f"Element to be added {new!r} has semantic_id "
                                            f"{new.semantic_id!r}, while already contained element "
                                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                            "aren't equal.",
                                        )

                            # Re-assign id_short
                            new.id_short = saved_id_short

                    class IssueDate(aas.Property):

                        def __init__(
                            self,
                            value: xsd.DateTime,
                            id_short: Optional[str] = r"IssueDate",
                            value_type: aas.DataTypeDefXsd = xsd.DateTime,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(dict_={r"en": r"Issue Date"}),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Date when the document has been officially issued"
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABI000#001",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                        identifications: Optional[
                            Union[
                                Iterable[Identifications.Identifications_item],
                                Identifications,
                            ]
                        ] = None,
                        issueDate: Optional[Union[xsd.DateTime, IssueDate]] = None,
                        id_short: Optional[str] = r"CoreData",
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(dict_={r"en": r"Core Data"}),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains essential administrative information for the quality document"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if uniqueIdentifier is not None and not isinstance(
                            uniqueIdentifier, aas.SubmodelElement
                        ):
                            uniqueIdentifier = self.UniqueIdentifier(uniqueIdentifier)

                        # A str would be split into its characters
                        if isinstance(identifications, str):
                            raise TypeError(
                                "identifications takes several elements, got a str"
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if identifications is not None and not isinstance(
                            identifications, aas.SubmodelElement
                        ):
                            identifications = self.Identifications(identifications)

                        # Build a submodel element if a raw value was passed in the argument

                        if issueDate is not None and not isinstance(
                            issueDate, aas.SubmodelElement
                        ):
                            issueDate = self.IssueDate(issueDate)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [uniqueIdentifier, identifications, issueDate]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, aas.SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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

                class Items(aas.SubmodelElementCollection):

                    class Identifications(aas.SubmodelElementList):

                        class Identifications_item(aas.SubmodelElementCollection):

                            class IdentificationName(aas.MultiLanguageProperty):

                                def __init__(
                                    self,
                                    value: aas.LangStringSet,
                                    id_short: Optional[str] = r"IdentificationName",
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Identification Name"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={r"en": r"Name of the identification"}
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class IdentificationIssuer(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationIssuer",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Identification Issuer"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class IdentificationValue(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"IdentificationValue",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Identification Value"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class ID(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ID",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(dict_={r"en": r"ID"}),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Attribute for which the value is unique within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class RefID(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefID",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Ref ID"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Reference to an existing ID within the quality document"
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToMany",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                            class RefType(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"RefType",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Ref Type"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = (
                                            aas.Qualifier(
                                                type_=r"SMT/Cardinality",
                                                value_type=str,
                                                value=r"ZeroToOne",
                                                value_id=None,
                                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                                    Union[aas.LangStringSet, IdentificationName]
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
                                id_short: Optional[str] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Identification"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Identification"}
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationName is not None and not isinstance(
                                    identificationName, aas.SubmodelElement
                                ):
                                    identificationName = self.IdentificationName(
                                        identificationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationIssuer is not None and not isinstance(
                                    identificationIssuer, aas.SubmodelElement
                                ):
                                    identificationIssuer = self.IdentificationIssuer(
                                        identificationIssuer
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if identificationValue is not None and not isinstance(
                                    identificationValue, aas.SubmodelElement
                                ):
                                    identificationValue = self.IdentificationValue(
                                        identificationValue
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if iD is not None and not isinstance(
                                    iD, aas.SubmodelElement
                                ):
                                    iD = self.ID(iD)

                                # A str would be split into its characters
                                if isinstance(refID, str):
                                    raise TypeError(
                                        "refID takes several elements, got a str"
                                    )

                                # Build submodel elements from raw values passed in the argument
                                if refID:
                                    refID = [
                                        (
                                            i
                                            if isinstance(i, aas.SubmodelElement)
                                            else self.RefID(i)
                                        )
                                        for i in refID
                                    ]

                                # Build a submodel element if a raw value was passed in the argument

                                if refType is not None and not isinstance(
                                    refType, aas.SubmodelElement
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
                                    elif isinstance(se_arg, aas.SubmodelElement):
                                        embedded_submodel_elements.append(se_arg)
                                    elif isinstance(se_arg, Iterable):
                                        for n, element in enumerate(se_arg):
                                            element.id_short = f"{element.id_short}{n}"
                                            embedded_submodel_elements.append(element)
                                    else:
                                        raise TypeError(
                                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                            identifications_items: Iterable[Identifications_item],
                            id_short: Optional[str] = r"Identifications",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                            semantic_id_list_element: Optional[aas.Reference] = None,
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                            order_relevant: bool = True,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Identifications"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Identifications contains identifiers which exactly describe the content of the parent element."
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(identifications_items, str):
                                raise TypeError(
                                    "identifications_items takes several elements, got a str"
                                )

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [identifications_items]:
                                if se_arg is None:
                                    continue
                                elif isinstance(se_arg, aas.SubmodelElement):
                                    embedded_submodel_elements.append(se_arg)
                                elif isinstance(se_arg, Iterable):
                                    embedded_submodel_elements.extend(se_arg)
                                else:
                                    raise TypeError(
                                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                                self.type_value_list_element
                                in (aas.Property, aas.Range)
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
                            if (
                                new.semantic_id is not None
                                and self.semantic_id_list_element is None
                            ):
                                for item in existing:
                                    if (
                                        item.semantic_id is not None
                                        and new.semantic_id != item.semantic_id
                                    ):
                                        raise aas.AASConstraintViolation(
                                            114,
                                            f"Element to be added {new!r} has semantic_id "
                                            f"{new.semantic_id!r}, while already contained element "
                                            f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                            "aren't equal.",
                                        )

                            # Re-assign id_short
                            new.id_short = saved_id_short

                    class Item(aas.SubmodelElementList):

                        class Item_item(aas.SubmodelElementCollection):

                            class Identifications(aas.SubmodelElementList):

                                class Identifications_item(
                                    aas.SubmodelElementCollection
                                ):

                                    class IdentificationName(aas.MultiLanguageProperty):

                                        def __init__(
                                            self,
                                            value: aas.LangStringSet,
                                            id_short: Optional[
                                                str
                                            ] = r"IdentificationName",
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = aas.MultiLanguageNameType(
                                                dict_={r"en": r"Identification Name"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = aas.MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Name of the identification"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationName",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[aas.Qualifier] = None,
                                            extension: Iterable[aas.Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                aas.Reference
                                            ] = (),
                                            embedded_data_specifications: Iterable[
                                                aas.EmbeddedDataSpecification
                                            ] = None,
                                        ):

                                            if qualifier is None:
                                                qualifier = (
                                                    aas.Qualifier(
                                                        type_=r"SMT/Cardinality",
                                                        value_type=str,
                                                        value=r"ZeroToOne",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                                    class IdentificationIssuer(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"IdentificationIssuer",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = aas.MultiLanguageNameType(
                                                dict_={r"en": r"Identification Issuer"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = aas.MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Issuer of the identification to distinguish various categories of quality document"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationIssuer",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[aas.Qualifier] = None,
                                            extension: Iterable[aas.Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                aas.Reference
                                            ] = (),
                                            embedded_data_specifications: Iterable[
                                                aas.EmbeddedDataSpecification
                                            ] = None,
                                        ):

                                            if qualifier is None:
                                                qualifier = (
                                                    aas.Qualifier(
                                                        type_=r"SMT/Cardinality",
                                                        value_type=str,
                                                        value=r"ZeroToOne",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                                    class IdentificationValue(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"IdentificationValue",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = aas.MultiLanguageNameType(
                                                dict_={r"en": r"Identification Value"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = aas.MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Placeholder for the actual identification (e.g., serial number)"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/IdentificationValue",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[aas.Qualifier] = None,
                                            extension: Iterable[aas.Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                aas.Reference
                                            ] = (),
                                            embedded_data_specifications: Iterable[
                                                aas.EmbeddedDataSpecification
                                            ] = None,
                                        ):

                                            if qualifier is None:
                                                qualifier = (
                                                    aas.Qualifier(
                                                        type_=r"SMT/Cardinality",
                                                        value_type=str,
                                                        value=r"ZeroToOne",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                                    class ID(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"ID",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = aas.MultiLanguageNameType(
                                                dict_={r"en": r"ID"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = aas.MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Attribute for which the value is unique within the quality document"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/ID",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[aas.Qualifier] = None,
                                            extension: Iterable[aas.Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                aas.Reference
                                            ] = (),
                                            embedded_data_specifications: Iterable[
                                                aas.EmbeddedDataSpecification
                                            ] = None,
                                        ):

                                            if qualifier is None:
                                                qualifier = (
                                                    aas.Qualifier(
                                                        type_=r"SMT/Cardinality",
                                                        value_type=str,
                                                        value=r"ZeroToOne",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                                    class RefID(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"RefID",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = aas.MultiLanguageNameType(
                                                dict_={r"en": r"Ref ID"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = aas.MultiLanguageTextType(
                                                dict_={
                                                    r"en": r"Reference to an existing ID within the quality document"
                                                }
                                            ),
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refID",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[aas.Qualifier] = None,
                                            extension: Iterable[aas.Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                aas.Reference
                                            ] = (),
                                            embedded_data_specifications: Iterable[
                                                aas.EmbeddedDataSpecification
                                            ] = None,
                                        ):

                                            if qualifier is None:
                                                qualifier = (
                                                    aas.Qualifier(
                                                        type_=r"SMT/Cardinality",
                                                        value_type=str,
                                                        value=r"ZeroToMany",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                                    class RefType(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"RefType",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = aas.MultiLanguageNameType(
                                                dict_={r"en": r"Ref Type"}
                                            ),
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = aas.MultiLanguageTextType(
                                                dict_={
                                                    r"en": r'Specification of a context defining identification. For instance, the temperature measurement can have as context "ambientTemperature"'
                                                }
                                            ),
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identificationshttps://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identifications/refType",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            qualifier: Iterable[aas.Qualifier] = None,
                                            extension: Iterable[aas.Extension] = (),
                                            supplemental_semantic_id: Iterable[
                                                aas.Reference
                                            ] = (),
                                            embedded_data_specifications: Iterable[
                                                aas.EmbeddedDataSpecification
                                            ] = None,
                                        ):

                                            if qualifier is None:
                                                qualifier = (
                                                    aas.Qualifier(
                                                        type_=r"SMT/Cardinality",
                                                        value_type=str,
                                                        value=r"ZeroToOne",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                                            Union[aas.LangStringSet, IdentificationName]
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
                                        id_short: Optional[str] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = aas.MultiLanguageNameType(
                                            dict_={r"en": r"Identification"}
                                        ),
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = aas.MultiLanguageTextType(
                                            dict_={r"en": r"Identification"}
                                        ),
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        qualifier: Iterable[aas.Qualifier] = None,
                                        extension: Iterable[aas.Extension] = (),
                                        supplemental_semantic_id: Iterable[
                                            aas.Reference
                                        ] = (),
                                        embedded_data_specifications: Iterable[
                                            aas.EmbeddedDataSpecification
                                        ] = None,
                                    ):

                                        if qualifier is None:
                                            qualifier = ()

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument

                                        if (
                                            identificationName is not None
                                            and not isinstance(
                                                identificationName, aas.SubmodelElement
                                            )
                                        ):
                                            identificationName = (
                                                self.IdentificationName(
                                                    identificationName
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument

                                        if (
                                            identificationIssuer is not None
                                            and not isinstance(
                                                identificationIssuer,
                                                aas.SubmodelElement,
                                            )
                                        ):
                                            identificationIssuer = (
                                                self.IdentificationIssuer(
                                                    identificationIssuer
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument

                                        if (
                                            identificationValue is not None
                                            and not isinstance(
                                                identificationValue, aas.SubmodelElement
                                            )
                                        ):
                                            identificationValue = (
                                                self.IdentificationValue(
                                                    identificationValue
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument

                                        if iD is not None and not isinstance(
                                            iD, aas.SubmodelElement
                                        ):
                                            iD = self.ID(iD)

                                        # A str would be split into its characters
                                        if isinstance(refID, str):
                                            raise TypeError(
                                                "refID takes several elements, got a str"
                                            )

                                        # Build submodel elements from raw values passed in the argument
                                        if refID:
                                            refID = [
                                                (
                                                    i
                                                    if isinstance(
                                                        i, aas.SubmodelElement
                                                    )
                                                    else self.RefID(i)
                                                )
                                                for i in refID
                                            ]

                                        # Build a submodel element if a raw value was passed in the argument

                                        if refType is not None and not isinstance(
                                            refType, aas.SubmodelElement
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
                                            elif isinstance(
                                                se_arg, aas.SubmodelElement
                                            ):
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
                                                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                                    identifications_items: Iterable[
                                        Identifications_item
                                    ],
                                    id_short: Optional[str] = r"Identifications",
                                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                                    semantic_id_list_element: Optional[
                                        aas.Reference
                                    ] = None,
                                    value_type_list_element: Optional[
                                        aas.DataTypeDefXsd
                                    ] = None,
                                    order_relevant: bool = True,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Identifications"}
                                    ),
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Identifications contains identifiers which exactly describe the content of the parent element."
                                        }
                                    ),
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Identification",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    qualifier: Iterable[aas.Qualifier] = None,
                                    extension: Iterable[aas.Extension] = (),
                                    supplemental_semantic_id: Iterable[
                                        aas.Reference
                                    ] = (),
                                    embedded_data_specifications: Iterable[
                                        aas.EmbeddedDataSpecification
                                    ] = None,
                                ):

                                    if qualifier is None:
                                        qualifier = ()

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # A str would be split into its characters
                                    if isinstance(identifications_items, str):
                                        raise TypeError(
                                            "identifications_items takes several elements, got a str"
                                        )

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [identifications_items]:
                                        if se_arg is None:
                                            continue
                                        elif isinstance(se_arg, aas.SubmodelElement):
                                            embedded_submodel_elements.append(se_arg)
                                        elif isinstance(se_arg, Iterable):
                                            embedded_submodel_elements.extend(se_arg)
                                        else:
                                            raise TypeError(
                                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                                        raise aas.AASConstraintViolation(
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
                                        self.type_value_list_element
                                        in (aas.Property, aas.Range)
                                        and new.value_type
                                        is not self.value_type_list_element
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
                                    if (
                                        new.semantic_id is not None
                                        and self.semantic_id_list_element is None
                                    ):
                                        for item in existing:
                                            if (
                                                item.semantic_id is not None
                                                and new.semantic_id != item.semantic_id
                                            ):
                                                raise aas.AASConstraintViolation(
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
                                identifications: Union[
                                    Iterable[Identifications.Identifications_item],
                                    Identifications,
                                ],
                                id_short: Optional[str] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(dict_={r"en": r"Item"}),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(dict_={r"en": r"Item"}),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://dccwiki.ptb.de/en/dccitems",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = ()

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(identifications, str):
                                    raise TypeError(
                                        "identifications takes several elements, got a str"
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if identifications is not None and not isinstance(
                                    identifications, aas.SubmodelElement
                                ):
                                    identifications = self.Identifications(
                                        identifications
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [identifications]:
                                    if se_arg is None:
                                        continue
                                    elif isinstance(se_arg, aas.SubmodelElement):
                                        embedded_submodel_elements.append(se_arg)
                                    elif isinstance(se_arg, Iterable):
                                        for n, element in enumerate(se_arg):
                                            element.id_short = f"{element.id_short}{n}"
                                            embedded_submodel_elements.append(element)
                                    else:
                                        raise TypeError(
                                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                            item_items: Iterable[Item_item],
                            id_short: Optional[str] = r"Item",
                            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                            semantic_id_list_element: Optional[aas.Reference] = None,
                            value_type_list_element: Optional[
                                aas.DataTypeDefXsd
                            ] = None,
                            order_relevant: bool = True,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(dict_={r"en": r"Item"}),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Item of calibration, conformity assessment or other"
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/coreData/Items",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"OneToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(item_items, str):
                                raise TypeError(
                                    "item_items takes several elements, got a str"
                                )

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [item_items]:
                                if se_arg is None:
                                    continue
                                elif isinstance(se_arg, aas.SubmodelElement):
                                    embedded_submodel_elements.append(se_arg)
                                elif isinstance(se_arg, Iterable):
                                    embedded_submodel_elements.extend(se_arg)
                                else:
                                    raise TypeError(
                                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                                self.type_value_list_element
                                in (aas.Property, aas.Range)
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
                            if (
                                new.semantic_id is not None
                                and self.semantic_id_list_element is None
                            ):
                                for item in existing:
                                    if (
                                        item.semantic_id is not None
                                        and new.semantic_id != item.semantic_id
                                    ):
                                        raise aas.AASConstraintViolation(
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
                        identifications: Union[
                            Iterable[Identifications.Identifications_item],
                            Identifications,
                        ],
                        item: Union[Iterable[Item.Item_item], Item],
                        id_short: Optional[str] = r"Items",
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(dict_={r"en": r"Items"}),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains unique identification, description and if applicable, conditions of the item"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/items",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(identifications, str):
                            raise TypeError(
                                "identifications takes several elements, got a str"
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if identifications is not None and not isinstance(
                            identifications, aas.SubmodelElement
                        ):
                            identifications = self.Identifications(identifications)

                        # A str would be split into its characters
                        if isinstance(item, str):
                            raise TypeError("item takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if item is not None and not isinstance(
                            item, aas.SubmodelElement
                        ):
                            item = self.Item(item)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [identifications, item]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, aas.SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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

                class Statements(aas.SubmodelElementList):

                    class Statements_item(aas.SubmodelElementCollection):

                        class DateOfStatement(aas.Property):

                            def __init__(
                                self,
                                value: xsd.DateTime,
                                id_short: Optional[str] = r"DateOfStatement",
                                value_type: aas.DataTypeDefXsd = xsd.DateTime,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Date Of Statement"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Date of statement"}
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statements/Date",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                        class StatementReference(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"StatementReference",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Statement Reference"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Normative or other reference in accordance which the statement is made"
                                    }
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statement/StatementReference",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                        class Declaration(aas.MultiLanguageProperty):

                            def __init__(
                                self,
                                value: aas.LangStringSet,
                                id_short: Optional[str] = r"Declaration",
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Declaration"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Additional information providing context for the statement"
                                    }
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData/Statement/Declaration",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"ZeroToOne",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                                Union[xsd.DateTime, DateOfStatement]
                            ] = None,
                            statementReference: Optional[
                                Union[str, StatementReference]
                            ] = None,
                            declaration: Optional[
                                Union[aas.LangStringSet, Declaration]
                            ] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(dict_={r"en": r"Statement"}),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"statement records regarding the quality assessment"
                                }
                            ),
                            semantic_id: Optional[aas.Reference] = None,
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if dateOfStatement is not None and not isinstance(
                                dateOfStatement, aas.SubmodelElement
                            ):
                                dateOfStatement = self.DateOfStatement(dateOfStatement)

                            # Build a submodel element if a raw value was passed in the argument

                            if statementReference is not None and not isinstance(
                                statementReference, aas.SubmodelElement
                            ):
                                statementReference = self.StatementReference(
                                    statementReference
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if declaration is not None and not isinstance(
                                declaration, aas.SubmodelElement
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
                                elif isinstance(se_arg, aas.SubmodelElement):
                                    embedded_submodel_elements.append(se_arg)
                                elif isinstance(se_arg, Iterable):
                                    for n, element in enumerate(se_arg):
                                        element.id_short = f"{element.id_short}{n}"
                                        embedded_submodel_elements.append(element)
                                else:
                                    raise TypeError(
                                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                        statements_items: Iterable[Statements_item],
                        id_short: Optional[str] = r"Statements",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(dict_={r"en": r"Statements"}),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains list of statement records regarding the quality assessment"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/administrativeData/statements",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(statements_items, str):
                            raise TypeError(
                                "statements_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [statements_items]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, aas.SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                embedded_submodel_elements.extend(se_arg)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                        if (
                            new.semantic_id is not None
                            and self.semantic_id_list_element is None
                        ):
                            for item in existing:
                                if (
                                    item.semantic_id is not None
                                    and new.semantic_id != item.semantic_id
                                ):
                                    raise aas.AASConstraintViolation(
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
                    statements: Optional[
                        Union[Iterable[Statements.Statements_item], Statements]
                    ] = None,
                    id_short: Optional[str] = r"AdministrativeData",
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"Administrative Data"}
                    ),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"This submodel element collection contains essential administrative information about the document."
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/AdministrativeData",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(statements, str):
                        raise TypeError("statements takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if statements is not None and not isinstance(
                        statements, aas.SubmodelElement
                    ):
                        statements = self.Statements(statements)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [coreData, items, statements]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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

            class DocumentSignature(aas.SubmodelElementCollection):

                class SignedInfo(aas.SubmodelElementCollection):

                    class CanonicalizationMethod(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"CanonicalizationMethod",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Canonicalization Method"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about the signature and the algorithms used"
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/CanonicalizationMethod",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                    class SignatureMethod(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SignatureMethod",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Signature Method"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about the method used for creating the signature"
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureMethod",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                    class SignatureReference(aas.SubmodelElementCollection):

                        class Transforms(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Transforms",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Transforms"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Contains the transformations applied to the resource prior to signing"
                                    }
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/Transforms",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                        class DigestMethod(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"DigestMethod",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Digest Method"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specifies the hash algorithm before applying the hash"
                                    }
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/DigestMethod",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                        class DigestValue(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"DigestValue",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Digest Value"}
                                ),
                                category: Optional[str] = None,
                                description: Optional[
                                    aas.MultiLanguageTextType
                                ] = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Contains the Base64 encoded result of applying the hash algorithm to the transformed resource"
                                    }
                                ),
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference/DigestValue",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[
                                    aas.EmbeddedDataSpecification
                                ] = None,
                            ):

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"One",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                                aas.MultiLanguageNameType
                            ] = aas.MultiLanguageNameType(
                                dict_={r"en": r"Signature Reference"}
                            ),
                            category: Optional[str] = None,
                            description: Optional[
                                aas.MultiLanguageTextType
                            ] = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Additional information for processing the signature"
                                }
                            ),
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo/SignatureReference",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"OneToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if transforms is not None and not isinstance(
                                transforms, aas.SubmodelElement
                            ):
                                transforms = self.Transforms(transforms)

                            # Build a submodel element if a raw value was passed in the argument

                            if digestMethod is not None and not isinstance(
                                digestMethod, aas.SubmodelElement
                            ):
                                digestMethod = self.DigestMethod(digestMethod)

                            # Build a submodel element if a raw value was passed in the argument

                            if digestValue is not None and not isinstance(
                                digestValue, aas.SubmodelElement
                            ):
                                digestValue = self.DigestValue(digestValue)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [transforms, digestMethod, digestValue]:
                                if se_arg is None:
                                    continue
                                elif isinstance(se_arg, aas.SubmodelElement):
                                    embedded_submodel_elements.append(se_arg)
                                elif isinstance(se_arg, Iterable):
                                    for n, element in enumerate(se_arg):
                                        element.id_short = f"{element.id_short}{n}"
                                        embedded_submodel_elements.append(element)
                                else:
                                    raise TypeError(
                                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(dict_={r"en": r"Signed Info"}),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about the signature and the algorithms used"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignedInfo",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if canonicalizationMethod is not None and not isinstance(
                            canonicalizationMethod, aas.SubmodelElement
                        ):
                            canonicalizationMethod = self.CanonicalizationMethod(
                                canonicalizationMethod
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if signatureMethod is not None and not isinstance(
                            signatureMethod, aas.SubmodelElement
                        ):
                            signatureMethod = self.SignatureMethod(signatureMethod)

                        # A str would be split into its characters
                        if isinstance(signatureReference, str):
                            raise TypeError(
                                "signatureReference takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            canonicalizationMethod,
                            signatureMethod,
                            signatureReference,
                        ]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, aas.SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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

                class SignatureValue(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"SignatureValue",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(
                            dict_={r"en": r"Signature Value"}
                        ),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Contains the Base64 encoded result of the hash algorithm, i.e., the signature generated with the parameters specified in the SignatureMethod defined in SignedInfo after applying the algorithm specified by the CanonicalizationMethod"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/SignatureValue",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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

                class KeyInfo(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"KeyInfo",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[
                            aas.MultiLanguageNameType
                        ] = aas.MultiLanguageNameType(dict_={r"en": r"Key Info"}),
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Information to allow the signer to provide recipients with the key that validates the signature, usually in the form of one or more X.509 digital certificates"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature/KeyInfo",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
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
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(dict_={r"en": r"Document Signature"}),
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Information about the electronic signature of the quality document. The semantic structure is based on the W3C schema xmldsig"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/DigitalQualityDocument/1/0/DocumentSignature",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"http://www.w3.org/TR/xmldsig-core1/",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if signatureValue is not None and not isinstance(
                        signatureValue, aas.SubmodelElement
                    ):
                        signatureValue = self.SignatureValue(signatureValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if keyInfo is not None and not isinstance(
                        keyInfo, aas.SubmodelElement
                    ):
                        keyInfo = self.KeyInfo(keyInfo)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [signedInfo, signatureValue, keyInfo]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                language: Union[Iterable[Union[str, Language.Language_item]], Language],
                version: Union[str, Version],
                title: Union[aas.LangStringSet, Title],
                description_: Union[aas.LangStringSet, Description],
                statusSetDate: Union[xsd.DateTime, StatusSetDate],
                statusValue: Union[str, StatusValue],
                organizationShortName: Union[str, OrganizationShortName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFiles: Union[
                    Iterable[DigitalFiles.Digitalfiles_item], DigitalFiles
                ],
                administrativeData: AdministrativeData,
                refersToEntities: Optional[
                    Union[
                        Iterable[
                            Union[aas.Reference, RefersToEntities.Referstoentities_item]
                        ],
                        RefersToEntities,
                    ]
                ] = None,
                basedOnReferences: Optional[
                    Union[
                        Iterable[
                            Union[
                                aas.Reference, BasedOnReferences.Basedonreferences_item
                            ]
                        ],
                        BasedOnReferences,
                    ]
                ] = None,
                previewFile: Optional[PreviewFile] = None,
                documentSignature: Optional[Iterable[DocumentSignature]] = None,
                id_short: Optional[str] = None,
                display_name: Optional[
                    aas.MultiLanguageNameType
                ] = aas.MultiLanguageNameType(dict_={r"en": r"Document Instance"}),
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Information about a document instance. This SMC inherits from “DocumentVersion” of IDTA 02004-2-0 “Handover Documentation”"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI503#003/0173-1#01-AHF582#003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if language is not None and not isinstance(
                    language, aas.SubmodelElement
                ):
                    language = self.Language(language)

                # Build a submodel element if a raw value was passed in the argument

                if version is not None and not isinstance(version, aas.SubmodelElement):
                    version = self.Version(version)

                # Build a submodel element if a raw value was passed in the argument

                if title is not None and not isinstance(title, aas.SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(
                    description_, aas.SubmodelElement
                ):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if statusSetDate is not None and not isinstance(
                    statusSetDate, aas.SubmodelElement
                ):
                    statusSetDate = self.StatusSetDate(statusSetDate)

                # Build a submodel element if a raw value was passed in the argument

                if statusValue is not None and not isinstance(
                    statusValue, aas.SubmodelElement
                ):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument

                if organizationShortName is not None and not isinstance(
                    organizationShortName, aas.SubmodelElement
                ):
                    organizationShortName = self.OrganizationShortName(
                        organizationShortName
                    )

                # Build a submodel element if a raw value was passed in the argument

                if organizationOfficialName is not None and not isinstance(
                    organizationOfficialName, aas.SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(
                        organizationOfficialName
                    )

                # A str would be split into its characters
                if isinstance(refersToEntities, str):
                    raise TypeError(
                        "refersToEntities takes several elements, got a str"
                    )

                # Build a submodel element if a raw value was passed in the argument

                if refersToEntities is not None and not isinstance(
                    refersToEntities, aas.SubmodelElement
                ):
                    refersToEntities = self.RefersToEntities(refersToEntities)

                # A str would be split into its characters
                if isinstance(basedOnReferences, str):
                    raise TypeError(
                        "basedOnReferences takes several elements, got a str"
                    )

                # Build a submodel element if a raw value was passed in the argument

                if basedOnReferences is not None and not isinstance(
                    basedOnReferences, aas.SubmodelElement
                ):
                    basedOnReferences = self.BasedOnReferences(basedOnReferences)

                # A str would be split into its characters
                if isinstance(digitalFiles, str):
                    raise TypeError("digitalFiles takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if digitalFiles is not None and not isinstance(
                    digitalFiles, aas.SubmodelElement
                ):
                    digitalFiles = self.DigitalFiles(digitalFiles)

                # A str would be split into its characters
                if isinstance(documentSignature, str):
                    raise TypeError(
                        "documentSignature takes several elements, got a str"
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
                    elif isinstance(se_arg, aas.SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
            documentinstances_items: Iterable[Documentinstances_item],
            id_short: Optional[str] = r"DocumentInstances",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[
                aas.MultiLanguageNameType
            ] = aas.MultiLanguageNameType(dict_={r"en": r"Document Instances"}),
            category: Optional[str] = None,
            description: Optional[
                aas.MultiLanguageTextType
            ] = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Information elements of individual document instances, which can be different versions of each other"
                }
            ),
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABI503#003",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI503-003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(documentinstances_items, str):
                raise TypeError(
                    "documentinstances_items takes several elements, got a str"
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documentinstances_items]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    embedded_submodel_elements.extend(se_arg)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
                    if (
                        item.semantic_id is not None
                        and new.semantic_id != item.semantic_id
                    ):
                        raise aas.AASConstraintViolation(
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
        documentIds: Union[Iterable[DocumentIds.Documentids_item], DocumentIds],
        documentClassifications: Union[
            Iterable[DocumentClassifications.Documentclassifications_item],
            DocumentClassifications,
        ],
        documentInstances: Union[
            Iterable[DocumentInstances.Documentinstances_item], DocumentInstances
        ],
        id_short: Optional[str] = r"DigitalQualityDocuments",
        display_name: Optional[aas.MultiLanguageNameType] = aas.MultiLanguageNameType(
            dict_={r"en": r"Digital Quality Documents"}
        ),
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = aas.MultiLanguageTextType(
            dict_={r"en": r"Template submodel for Digital Quality Documents."}
        ),
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/DigitalQualityDocument/1/0",
                ),
            ),
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.TEMPLATE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # A str would be split into its characters
        if isinstance(documentIds, str):
            raise TypeError("documentIds takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documentIds is not None and not isinstance(documentIds, aas.SubmodelElement):
            documentIds = self.DocumentIds(documentIds)

        # A str would be split into its characters
        if isinstance(documentClassifications, str):
            raise TypeError("documentClassifications takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documentClassifications is not None and not isinstance(
            documentClassifications, aas.SubmodelElement
        ):
            documentClassifications = self.DocumentClassifications(
                documentClassifications
            )

        # A str would be split into its characters
        if isinstance(documentInstances, str):
            raise TypeError("documentInstances takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documentInstances is not None and not isinstance(
            documentInstances, aas.SubmodelElement
        ):
            documentInstances = self.DocumentInstances(documentInstances)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [documentIds, documentClassifications, documentInstances]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, aas.SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
