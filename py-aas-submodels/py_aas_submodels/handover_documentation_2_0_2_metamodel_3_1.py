from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class HandoverDocumentation(aas.Submodel):

    class Documents(aas.SubmodelElementList):

        class Documents_item(aas.SubmodelElementCollection):

            class DocumentIds(aas.SubmodelElementList):

                class Documentids_item(aas.SubmodelElementCollection):

                    class DocumentDomainId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"DocumentDomainId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"document domain identificator",
                                        r"de": r"Document Domain Identifikator",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"https://domain.com/...",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class DocumentIdentifier(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"DocumentIdentifier",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document Identifyer",
                                        r"de": r"Dokumentennummer",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"XF90-884",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class DocumentIsPrimary(aas.Property):

                        def __init__(
                            self,
                            value: bool,
                            id_short: Optional[str] = r"DocumentIsPrimary",
                            value_type: aas.DataTypeDefXsd = bool,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document is primary",
                                        r"de": r"Dokument ist primär",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"true",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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
                        documentDomainId: Union[str, DocumentDomainId],
                        documentIdentifier: Union[str, DocumentIdentifier],
                        documentIsPrimary: Optional[
                            Union[bool, DocumentIsPrimary]
                        ] = None,
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
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
                                        value=r"0173-1#02-ABI501#003~0/0173-1#01-AHF580#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://api.eclass-cdp.com/0173-1-02-ABI501-003/0173-1-01-AHF580-003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Document identificator",
                                    r"de": r"Dokumentidentifikator",
                                }
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"This SubmodelElementCollection holds the information for a VDI 2770 Document entity"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"OneToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
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

                        if documentDomainId is not None and not isinstance(
                            documentDomainId, aas.SubmodelElement
                        ):
                            documentDomainId = self.DocumentDomainId(documentDomainId)

                        # Build a submodel element if a raw value was passed in the argument

                        if documentIdentifier is not None and not isinstance(
                            documentIdentifier, aas.SubmodelElement
                        ):
                            documentIdentifier = self.DocumentIdentifier(
                                documentIdentifier
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if documentIsPrimary is not None and not isinstance(
                            documentIsPrimary, aas.SubmodelElement
                        ):
                            documentIsPrimary = self.DocumentIsPrimary(
                                documentIsPrimary
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            documentDomainId,
                            documentIdentifier,
                            documentIsPrimary,
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
                    documentids_items: Iterable[Documentids_item],
                    id_short: Optional[str] = r"DocumentIds",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                    semantic_id_list_element: Optional[
                        aas.Reference
                    ] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI501#003/0173-1#01-AHF580#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Document identifiers",
                                r"de": r"Dokumentidentifikatoren",
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(documentids_items, str):
                        raise TypeError(
                            "documentids_items takes several elements, got a str"
                        )

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

            class DocumentClassifications(aas.SubmodelElementList):

                class Documentclassifications_item(aas.SubmodelElementCollection):

                    class ClassId(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"ClassId",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Class identificator",
                                        r"de": r"Klassenidentifikator",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"03-02",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class ClassName(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"ClassName",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Class Name", r"de": r"Klassenname"}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Operation@en",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Classification system",
                                        r"de": r"Klassifizierungssystem",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"VDI 2770 Blatt 1:2020",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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
                        classId: Union[str, ClassId],
                        className: Union[aas.LangStringSet, ClassName],
                        classificationSystem: Union[str, ClassificationSystem],
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
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
                        supplemental_semantic_id: Iterable[aas.Reference] = (
                            aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABI502#003~0/0173-1#01-AHF581#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://api.eclass-cdp.com/0173-1-02-ABI502-003/0173-1-01-AHF581-003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Document classification",
                                    r"de": r"Dokumentklassifikation",
                                }
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Set of information for describing the classification of the Document according to a ClassificationSystem"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"OneToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
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

                        if classId is not None and not isinstance(
                            classId, aas.SubmodelElement
                        ):
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
                    documentclassifications_items: Iterable[
                        Documentclassifications_item
                    ],
                    id_short: Optional[str] = r"DocumentClassifications",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                    semantic_id_list_element: Optional[
                        aas.Reference
                    ] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI502#003/0173-1#01-AHF581#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Document classifications",
                                r"de": r"Dokumentklassifikationen",
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class DocumentVersions(aas.SubmodelElementList):

                class Documentversions_item(aas.SubmodelElementCollection):

                    class Language(aas.SubmodelElementList):

                        class Language_item(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = None,
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"0173-1#07-AAS045#003",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
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

                                if display_name is None:
                                    display_name = aas.MultiLanguageNameType(
                                        dict_={
                                            r"en": r"en (English)",
                                            r"de": r"en (Englisch)",
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"OneToMany",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"ExampleValue",
                                            value_type=str,
                                            value=r"en",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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
                            language_items: Iterable[Union[str, Language_item]],
                            id_short: Optional[str] = r"Language",
                            type_value_list_element: aas.SubmodelElement = aas.Property,
                            semantic_id_list_element: Optional[aas.Reference] = None,
                            value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://api.eclass-cdp.com/0173-1-02-AAN468-008",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Language", r"de": r"Sprache"}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

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

                    class Version(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Version",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document version",
                                        r"de": r"Dokumentenversion",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"V1.2",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class Title(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"Title",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document title",
                                        r"de": r"Dokumententitel",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Examplary title@en",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class Subtitle(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"Subtitle",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABH998#003",
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
                                            value=r"https://api.eclass-cdp.com/0173-1-02-ABH998-003",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Subtitle", r"de": r"Untertitel"}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Examplary subtitle@en",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class Description(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"Description",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document description",
                                        r"de": r"Dokumentenbeschreibung",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Abstract@en",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class KeyWords(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"KeyWords",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABH999#003",
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
                                            value=r"https://api.eclass-cdp.com/0173-1-02-ABH999-003",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Keywords", r"de": r"Stichworte"}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Examplary keywords@en",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class StatusSetDate(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Date,
                            id_short: Optional[str] = r"StatusSetDate",
                            value_type: aas.DataTypeDefXsd = xsd.Date,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document status set date",
                                        r"de": r"Datum der Einstellung des Dokumentenstatus",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"2020-02-06",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class StatusValue(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"StatusValue",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Document status",
                                        r"de": r"Dokumentstatus",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Released",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class OrganizationShortName(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"OrganizationShortName",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Organization short name",
                                        r"de": r"Kurzname der Organisation",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Example company",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class OrganizationOfficialName(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"OrganizationOfficialName",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Organization official name",
                                        r"de": r"Offizieller Name der Organisation",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"Example company Ltd.",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
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

                    class RefersToEntities(aas.SubmodelElementList):

                        class Referstoentities_item(aas.ReferenceElement):

                            def __init__(
                                self,
                                value: aas.Reference,
                                id_short: Optional[str] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
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
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"OneToMany",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"AllowedIdShort",
                                            value_type=str,
                                            value=r"RefersTo[\d{2,3}]",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
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
                            value_type_list_element: Optional[
                                aas.DataTypeDefXsd
                            ] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Reference to other documents",
                                        r"de": r"Referenz zu anderen Dokumenten",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
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

                    class BasedOnReferences(aas.SubmodelElementList):

                        class Basedonreferences_item(aas.ReferenceElement):

                            def __init__(
                                self,
                                value: aas.Reference,
                                id_short: Optional[str] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
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
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"AllowedIdShort",
                                            value_type=str,
                                            value=r"BasedOn[\d{2,3}]",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
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
                            value_type_list_element: Optional[
                                aas.DataTypeDefXsd
                            ] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Based on other documents",
                                        r"de": r"Basiert auf anderen Dokumenten",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
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

                    class TranslationOfEntities(aas.SubmodelElementList):

                        class Translationofentities_item(aas.ReferenceElement):

                            def __init__(
                                self,
                                value: aas.Reference,
                                id_short: Optional[str] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"0173-1#02-ABK290#002",
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

                                if display_name is None:
                                    display_name = aas.MultiLanguageNameType(
                                        dict_={
                                            r"en": r"Translation of documents",
                                            r"de": r"Übersetzung von anderen Elementen",
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"OneToMany",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"AllowedIdShort",
                                            value_type=str,
                                            value=r"TranslationOf[\d{2,3}]",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
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
                            translationofentities_items: Iterable[
                                Union[aas.Reference, Translationofentities_item]
                            ],
                            id_short: Optional[str] = r"TranslationOfEntities",
                            type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                            semantic_id_list_element: Optional[aas.Reference] = None,
                            value_type_list_element: Optional[
                                aas.DataTypeDefXsd
                            ] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABK290#002",
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
                                            value=r"https://api.eclass-cdp.com/0173-1-02-ABK290-002",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Translation of other documents",
                                        r"de": r"Übersetzung von anderen Elementen",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(translationofentities_items, str):
                                raise TypeError(
                                    "translationofentities_items takes several elements, got a str"
                                )

                            # Build submodel elements from raw values passed in the argument
                            if translationofentities_items:
                                translationofentities_items = [
                                    (
                                        i
                                        if isinstance(i, aas.SubmodelElement)
                                        else self.Translationofentities_item(i)
                                    )
                                    for i in translationofentities_items
                                ]

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [translationofentities_items]:
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

                    class DigitalFiles(aas.SubmodelElementList):

                        class Digitalfiles_item(aas.File):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = None,
                                content_type: Optional[str] = r"application/pdf",
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
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

                                if display_name is None:
                                    display_name = aas.MultiLanguageNameType(
                                        dict_={
                                            r"en": r"Name of the specific digital file@en",
                                            r"de": r"Name der spezifischen digitalen Datei@de",
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"SMT/Cardinality",
                                            value_type=str,
                                            value=r"OneToMany",
                                            value_id=None,
                                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"ExampleValue",
                                            value_type=str,
                                            value=r"docu_cecc_fullmanual_DE.PDF",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                                    ),
                                                ),
                                                referred_semantic_id=None,
                                            ),
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"AllowedIdShort",
                                            value_type=str,
                                            value=r"DigitalFile[\d{2,3}]",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
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

                        def __init__(
                            self,
                            digitalfiles_items: Iterable[Digitalfiles_item],
                            id_short: Optional[str] = r"DigitalFiles",
                            type_value_list_element: aas.SubmodelElement = aas.File,
                            semantic_id_list_element: Optional[aas.Reference] = None,
                            value_type_list_element: Optional[
                                aas.DataTypeDefXsd
                            ] = None,
                            order_relevant: bool = True,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Digital files",
                                        r"de": r"Digitale Dateien",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
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

                    class PreviewFile(aas.File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"PreviewFile",
                            content_type: Optional[str] = r"image/jpeg",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Preview file",
                                        r"de": r"Vorschaudatei",
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"ExampleValue",
                                        value_type=str,
                                        value=r"docu_cecc_fullmanual_DE.jpg",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"AllowedIdShort",
                                        value_type=str,
                                        value=r"PreviewFile[\d{2,3}]",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
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

                    def __init__(
                        self,
                        language: Union[
                            Iterable[Union[str, Language.Language_item]], Language
                        ],
                        version: Union[str, Version],
                        title: Union[aas.LangStringSet, Title],
                        description_: Union[aas.LangStringSet, Description],
                        statusSetDate: Union[xsd.Date, StatusSetDate],
                        statusValue: Union[str, StatusValue],
                        organizationShortName: Union[str, OrganizationShortName],
                        organizationOfficialName: Union[str, OrganizationOfficialName],
                        digitalFiles: Union[
                            Iterable[DigitalFiles.Digitalfiles_item], DigitalFiles
                        ],
                        subtitle: Optional[Union[aas.LangStringSet, Subtitle]] = None,
                        keyWords: Optional[Union[aas.LangStringSet, KeyWords]] = None,
                        refersToEntities: Optional[
                            Union[
                                Iterable[
                                    Union[
                                        aas.Reference,
                                        RefersToEntities.Referstoentities_item,
                                    ]
                                ],
                                RefersToEntities,
                            ]
                        ] = None,
                        basedOnReferences: Optional[
                            Union[
                                Iterable[
                                    Union[
                                        aas.Reference,
                                        BasedOnReferences.Basedonreferences_item,
                                    ]
                                ],
                                BasedOnReferences,
                            ]
                        ] = None,
                        translationOfEntities: Optional[
                            Union[
                                Iterable[
                                    Union[
                                        aas.Reference,
                                        TranslationOfEntities.Translationofentities_item,
                                    ]
                                ],
                                TranslationOfEntities,
                            ]
                        ] = None,
                        previewFile: Optional[PreviewFile] = None,
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
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
                        supplemental_semantic_id: Iterable[aas.Reference] = (
                            aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"0173-1#02-ABI503#003~0/0173-1#01-AHF582#003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://api.eclass-cdp.com/0173-1-02-ABI503-003/0173-1-01-AHF582-003",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                        ),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Document version",
                                    r"de": r"Document version",
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"OneToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(language, str):
                            raise TypeError(
                                "language takes several elements, got a str"
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if language is not None and not isinstance(
                            language, aas.SubmodelElement
                        ):
                            language = self.Language(language)

                        # Build a submodel element if a raw value was passed in the argument

                        if version is not None and not isinstance(
                            version, aas.SubmodelElement
                        ):
                            version = self.Version(version)

                        # Build a submodel element if a raw value was passed in the argument

                        if title is not None and not isinstance(
                            title, aas.SubmodelElement
                        ):
                            title = self.Title(title)

                        # Build a submodel element if a raw value was passed in the argument

                        if subtitle is not None and not isinstance(
                            subtitle, aas.SubmodelElement
                        ):
                            subtitle = self.Subtitle(subtitle)

                        # Build a submodel element if a raw value was passed in the argument

                        if description_ is not None and not isinstance(
                            description_, aas.SubmodelElement
                        ):
                            description_ = self.Description(description_)

                        # Build a submodel element if a raw value was passed in the argument

                        if keyWords is not None and not isinstance(
                            keyWords, aas.SubmodelElement
                        ):
                            keyWords = self.KeyWords(keyWords)

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
                            basedOnReferences = self.BasedOnReferences(
                                basedOnReferences
                            )

                        # A str would be split into its characters
                        if isinstance(translationOfEntities, str):
                            raise TypeError(
                                "translationOfEntities takes several elements, got a str"
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if translationOfEntities is not None and not isinstance(
                            translationOfEntities, aas.SubmodelElement
                        ):
                            translationOfEntities = self.TranslationOfEntities(
                                translationOfEntities
                            )

                        # A str would be split into its characters
                        if isinstance(digitalFiles, str):
                            raise TypeError(
                                "digitalFiles takes several elements, got a str"
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if digitalFiles is not None and not isinstance(
                            digitalFiles, aas.SubmodelElement
                        ):
                            digitalFiles = self.DigitalFiles(digitalFiles)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            language,
                            version,
                            title,
                            subtitle,
                            description_,
                            keyWords,
                            statusSetDate,
                            statusValue,
                            organizationShortName,
                            organizationOfficialName,
                            refersToEntities,
                            basedOnReferences,
                            translationOfEntities,
                            digitalFiles,
                            previewFile,
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
                    documentversions_items: Iterable[Documentversions_item],
                    id_short: Optional[str] = r"DocumentVersions",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                    semantic_id_list_element: Optional[
                        aas.Reference
                    ] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABI503#003/0173-1#01-AHF582#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Document versions",
                                r"de": r"Dokumentenversionen",
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(documentversions_items, str):
                        raise TypeError(
                            "documentversions_items takes several elements, got a str"
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [documentversions_items]:
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

            class DocumentedEntities(aas.SubmodelElementList):

                class Documentedentities_item(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity",
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
                                    semantic_id=aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
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
                    documentedentities_items: Iterable[
                        Union[aas.Reference, Documentedentities_item]
                    ],
                    id_short: Optional[str] = r"DocumentedEntities",
                    type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                    semantic_id_list_element: Optional[aas.Reference] = None,
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities",
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
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(documentedentities_items, str):
                        raise TypeError(
                            "documentedentities_items takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if documentedentities_items:
                        documentedentities_items = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.Documentedentities_item(i)
                            )
                            for i in documentedentities_items
                        ]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [documentedentities_items]:
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
                documentIds: Union[Iterable[DocumentIds.Documentids_item], DocumentIds],
                documentClassifications: Union[
                    Iterable[DocumentClassifications.Documentclassifications_item],
                    DocumentClassifications,
                ],
                documentVersions: Union[
                    Iterable[DocumentVersions.Documentversions_item], DocumentVersions
                ],
                documentedEntities: Optional[
                    Union[
                        Iterable[
                            Union[
                                aas.Reference,
                                DocumentedEntities.Documentedentities_item,
                            ]
                        ],
                        DocumentedEntities,
                    ]
                ] = None,
                id_short: Optional[str] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI500#003/0173-1#01-AHF579#003",
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
                                value=r"0173-1#02-ABI500#003~0/0173-1#01-AHF579#003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABI500-003/0173-1-01-AHF579-003",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"This SubmodelElementCollection holds the information for a VDI 2770 Document entity"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(documentIds, str):
                    raise TypeError("documentIds takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if documentIds is not None and not isinstance(
                    documentIds, aas.SubmodelElement
                ):
                    documentIds = self.DocumentIds(documentIds)

                # A str would be split into its characters
                if isinstance(documentClassifications, str):
                    raise TypeError(
                        "documentClassifications takes several elements, got a str"
                    )

                # Build a submodel element if a raw value was passed in the argument

                if documentClassifications is not None and not isinstance(
                    documentClassifications, aas.SubmodelElement
                ):
                    documentClassifications = self.DocumentClassifications(
                        documentClassifications
                    )

                # A str would be split into its characters
                if isinstance(documentVersions, str):
                    raise TypeError(
                        "documentVersions takes several elements, got a str"
                    )

                # Build a submodel element if a raw value was passed in the argument

                if documentVersions is not None and not isinstance(
                    documentVersions, aas.SubmodelElement
                ):
                    documentVersions = self.DocumentVersions(documentVersions)

                # A str would be split into its characters
                if isinstance(documentedEntities, str):
                    raise TypeError(
                        "documentedEntities takes several elements, got a str"
                    )

                # Build a submodel element if a raw value was passed in the argument

                if documentedEntities is not None and not isinstance(
                    documentedEntities, aas.SubmodelElement
                ):
                    documentedEntities = self.DocumentedEntities(documentedEntities)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    documentIds,
                    documentClassifications,
                    documentVersions,
                    documentedEntities,
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
            documents_items: Iterable[Documents_item],
            id_short: Optional[str] = r"Documents",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
            semantic_id_list_element: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABI500#003/0173-1#01-AHF579#003",
                    ),
                ),
                referred_semantic_id=None,
            ),
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABI500#003",
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
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABI500-003",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={
                        r"en": r"Documents (handover documentation)",
                        r"de": r"Dokumente (Übergabedokumentation)",
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(documents_items, str):
                raise TypeError("documents_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [documents_items]:
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

    class Entities(aas.SubmodelElementList):

        class Entities_item(aas.Entity):

            def __init__(
                self,
                id_short: Optional[str] = None,
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.CO_MANAGED_ENTITY,
                statement: Iterable[aas.SubmodelElement] = (),
                global_asset_id: Optional[str] = None,
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation",
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
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
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
                    entity_type=entity_type,
                    statement=statement,
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

        def __init__(
            self,
            entities_items: Iterable[Entities_item],
            id_short: Optional[str] = r"Entities",
            type_value_list_element: aas.SubmodelElement = aas.Entity,
            semantic_id_list_element: Optional[aas.Reference] = None,
            value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/vdi/2770/1/0/EntitiesForDocumentation",
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
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(entities_items, str):
                raise TypeError("entities_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [entities_items]:
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
        documents: Union[Iterable[Documents.Documents_item], Documents],
        entities: Optional[Union[Iterable[Entities.Entities_item], Entities]] = None,
        id_short: Optional[str] = r"HandoverDocumentation",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AHF578#003"),),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.TEMPLATE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (
            aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://api.eclass-cdp.com/0173-1-01-AHF578-003",
                    ),
                ),
                referred_semantic_id=None,
            ),
        ),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel defines a set meta data for the handover of documentation from the manufacturer to the operator for industrial equipment"
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"2",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02004-2-0",
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # A str would be split into its characters
        if isinstance(documents, str):
            raise TypeError("documents takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if documents is not None and not isinstance(documents, aas.SubmodelElement):
            documents = self.Documents(documents)

        # A str would be split into its characters
        if isinstance(entities, str):
            raise TypeError("entities takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if entities is not None and not isinstance(entities, aas.SubmodelElement):
            entities = self.Entities(entities)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [documents, entities]:
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
